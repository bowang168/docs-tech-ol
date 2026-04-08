#!/usr/bin/env python3
"""
docs-tech-ol → Qdrant Ingestion Pipeline (Local Mode + BM25 Hybrid)
技术知识库向量数据库导入管道 — 本地无 Docker

Usage:
    python tech_qdrant_ingest.py                                # incremental
    python tech_qdrant_ingest.py --force                        # re-embed all
    python tech_qdrant_ingest.py --rebuild                      # hot-swap rebuild (zero downtime)
    python tech_qdrant_ingest.py --dry-run                      # parse only, no upload
    python tech_qdrant_ingest.py --filter oracle                # only process files under oracle/

Local: QdrantClient(path=...) — no Docker, no network port

Author: Bo Wang
Created: 2026-03-26
Updated: 2026-04-08  — Local-only mode, removed cloud target
"""

import os
import re
import sys
import csv
import yaml
import json
import hashlib
import argparse
import requests
import uuid
import time
from pathlib import Path
from typing import Optional

from qdrant_client import QdrantClient, models

# --- Configuration ---
QDRANT_LOCAL_PATH = str(Path(__file__).resolve().parent.parent / "qdrant_local_db")
OLLAMA_URL = "http://localhost:11434/api/embed"
EMBEDDING_MODEL = "qwen3-embedding:0.6b"
ALIAS_NAME = "docs_tech_ol"
COLLECTION_PREFIX = "docs_tech_ol_v"
VECTOR_SIZE = 1024
MAX_CHUNK_CHARS = 1500   # larger chunks for tech docs
BATCH_SIZE = 100
EMBED_BATCH_SIZE = 32
HASH_CACHE_FILE = ".tech_hash_cache.json"
BM25_MODEL_FILE = ".tech_bm25_model.json"

BASE_DIR = Path(__file__).resolve().parent.parent

PAYLOAD_INDEXES = ["tags", "source_file", "source_url", "ol_version",
                   "product", "topic", "type", "file_type", "source"]

SKIP_PATTERNS = [".DS_Store", ".claude", ".obsidian", "__pycache__",
                 ".tech_hash_cache", ".fetch_log", "00_System",
                 "-SKIP-OCR", "-SKIP-"]
SUPPORTED_EXTENSIONS = {".md", ".csv"}


# ============================================================
# Multi-target client management
# ============================================================

class QdrantTarget:
    """Wraps a QdrantClient with a name for logging."""
    def __init__(self, name: str, client: QdrantClient):
        self.name = name
        self.client = client


def init_targets() -> list[QdrantTarget]:
    """Initialize local Qdrant client."""
    os.makedirs(QDRANT_LOCAL_PATH, mode=0o700, exist_ok=True)
    local_client = QdrantClient(path=QDRANT_LOCAL_PATH)
    targets = [QdrantTarget("local", local_client)]
    print(f"Target:    local ({QDRANT_LOCAL_PATH})")
    return targets


# ============================================================
# Alias & collection management (SDK-based)
# ============================================================

def resolve_alias(tgt: QdrantTarget) -> Optional[str]:
    try:
        aliases = tgt.client.get_aliases().aliases
        for a in aliases:
            if a.alias_name == ALIAS_NAME:
                return a.collection_name
    except Exception:
        pass
    return None


def get_real_collection(tgt: QdrantTarget) -> Optional[str]:
    target = resolve_alias(tgt)
    if target:
        return target
    try:
        collections = [c.name for c in tgt.client.get_collections().collections]
        if ALIAS_NAME in collections:
            return ALIAS_NAME
    except Exception:
        pass
    return None


def create_collection(name: str, tgt: QdrantTarget, defer_indexing: bool = False):
    print(f"[CREATE][{tgt.name}] Creating collection '{name}' (dense + BM25 sparse)...")
    try:
        optimizers = None
        if defer_indexing:
            optimizers = models.OptimizersConfigDiff(indexing_threshold=0)

        tgt.client.create_collection(
            collection_name=name,
            vectors_config={
                "dense": models.VectorParams(
                    size=VECTOR_SIZE,
                    distance=models.Distance.COSINE,
                ),
            },
            sparse_vectors_config={
                "bm25": models.SparseVectorParams(),
            },
            on_disk_payload=True,
            optimizers_config=optimizers,
        )
        print(f"[CREATE][{tgt.name}] Done")
        return True
    except Exception as e:
        print(f"[FATAL][{tgt.name}] Create failed: {e}")
        return False


def drop_collection(name: str, tgt: QdrantTarget):
    try:
        tgt.client.delete_collection(name)
        return True
    except Exception as e:
        print(f"[WARN][{tgt.name}] Drop '{name}' failed: {e}")
        return False


def swap_alias(new_collection: str, tgt: QdrantTarget, old_collection: Optional[str] = None):
    print(f"[SWAP][{tgt.name}] Alias '{ALIAS_NAME}' → '{new_collection}'...")
    try:
        actions = []
        if old_collection and old_collection != ALIAS_NAME:
            actions.append(
                models.DeleteAliasOperation(
                    delete_alias=models.DeleteAlias(alias_name=ALIAS_NAME)
                )
            )
        actions.append(
            models.CreateAliasOperation(
                create_alias=models.CreateAlias(
                    alias_name=ALIAS_NAME,
                    collection_name=new_collection,
                )
            )
        )
        tgt.client.update_collection_aliases(change_aliases_operations=actions)
        print(f"[SWAP][{tgt.name}] Done")
        return True
    except Exception as e:
        print(f"[ERROR][{tgt.name}] Alias swap failed: {e}")
        return False


def enable_indexing(collection: str, tgt: QdrantTarget):
    print(f"[INDEX][{tgt.name}] Enabling HNSW indexing on '{collection}'...")
    try:
        tgt.client.update_collection(
            collection_name=collection,
            optimizers_config=models.OptimizersConfigDiff(indexing_threshold=100),
        )
        print(f"[INDEX][{tgt.name}] Done")
    except Exception as e:
        print(f"[WARN][{tgt.name}] Could not enable indexing: {e}")


def delete_file_points(collection: str, source_file: str, tgt: QdrantTarget):
    try:
        tgt.client.delete(
            collection_name=collection,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[models.FieldCondition(
                        key="source_file",
                        match=models.MatchValue(value=source_file),
                    )]
                )
            ),
        )
    except Exception:
        pass


# ============================================================
# Parsing & chunking
# ============================================================

def parse_yaml_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', text, re.DOTALL)
    if match:
        try:
            fm = yaml.safe_load(match.group(1)) or {}
            return fm, match.group(2)
        except (yaml.YAMLError, ValueError):
            return {}, text
    return {}, text


def heading_aware_chunk(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Split markdown by headings, prepend heading breadcrumb for context."""
    sections = re.split(r'(?=^#{1,6}\s)', text, flags=re.MULTILINE)
    heading_stack = {}

    def _heading_level(line: str) -> int:
        m = re.match(r'^(#{1,6})\s', line)
        return len(m.group(1)) if m else 0

    def _breadcrumb() -> str:
        if not heading_stack:
            return ""
        return " > ".join(heading_stack[lvl] for lvl in sorted(heading_stack))

    def _prepend_context(chunk_text: str, breadcrumb: str) -> str:
        if not breadcrumb:
            return chunk_text
        first_line = chunk_text.split('\n', 1)[0].strip().lstrip('#').strip()
        if first_line and first_line in breadcrumb:
            return chunk_text
        return f"[{breadcrumb}]\n{chunk_text}"

    chunks = []
    current = ""
    current_breadcrumb = ""

    for section in sections:
        section = section.strip()
        if not section:
            continue

        first_line = section.split('\n', 1)[0]
        level = _heading_level(first_line)
        if level > 0:
            heading_text = first_line.lstrip('#').strip()
            heading_stack[level] = heading_text
            for lvl in list(heading_stack):
                if lvl > level:
                    del heading_stack[lvl]

        breadcrumb = _breadcrumb()

        if len(section) > max_chars:
            if current:
                chunks.append(_prepend_context(current.strip(), current_breadcrumb))
                current = ""
            lines = section.split('\n')
            sub = ""
            for line in lines:
                if len(sub) + len(line) > max_chars and sub:
                    chunks.append(_prepend_context(sub.strip(), breadcrumb))
                    sub = ""
                sub += line + "\n"
            if sub.strip():
                chunks.append(_prepend_context(sub.strip(), breadcrumb))
        elif len(current) + len(section) > max_chars:
            if current:
                chunks.append(_prepend_context(current.strip(), current_breadcrumb))
            current = section + "\n\n"
            current_breadcrumb = breadcrumb
        else:
            if not current:
                current_breadcrumb = breadcrumb
            current += section + "\n\n"

    if current.strip():
        chunks.append(_prepend_context(current.strip(), current_breadcrumb))

    return chunks if chunks else [text.strip()] if text.strip() else []


def infer_ol_version(filepath: str) -> str:
    """Infer Oracle Linux OS version. Only ol8/ol9/ol10 — not products or kernel types."""
    parts = filepath.lower()
    if "/ol10/" in parts or "oracle-linux/10" in parts:
        return "ol10"
    if "/ol9/" in parts or "oracle-linux/9" in parts:
        return "ol9"
    if "/ol8/" in parts or "oracle-linux/8" in parts:
        return "ol8"
    return ""


def infer_product(filepath: str) -> str:
    """Infer product line from path. Separate from OS version."""
    parts = filepath.lower()
    if "/olam/" in parts:
        return "olam"
    if "/olcne/" in parts:
        return "olcne"
    if "/olm210/" in parts:
        return "olm210"
    if "/uek/" in parts:
        return "uek"
    if "/ol8/" in parts or "/ol9/" in parts or "/ol10/" in parts:
        return "oracle-linux"
    if "/shared/" in parts:
        return "oracle-linux"
    return ""


def infer_source(filepath: str) -> str:
    lower = filepath.lower()
    if "/oracle/" in lower:
        return "oracle"
    if "/personal_tech_input/" in lower:
        return "personal_tech_input"
    if "oracle运维" in filepath:
        return "personal_ops"
    return "other"


def generate_uuid(source_file: str, chunk_index: int) -> str:
    key = f"tech::{source_file}::chunk_{chunk_index}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, key))


# ============================================================
# Hash cache
# ============================================================

def load_hash_cache(base_path: str) -> dict:
    cache_path = os.path.join(base_path, HASH_CACHE_FILE)
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_hash_cache(base_path: str, cache: dict):
    cache_path = os.path.join(base_path, HASH_CACHE_FILE)
    with open(cache_path, 'w') as f:
        json.dump(cache, f, indent=2)


def file_content_hash(filepath: str) -> str:
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


# ============================================================
# Embedding
# ============================================================

def embed_batch(texts: list[str], retries: int = 2) -> list[Optional[list[float]]]:
    for attempt in range(retries + 1):
        try:
            resp = requests.post(OLLAMA_URL, json={
                "model": EMBEDDING_MODEL, "input": texts
            }, timeout=180)
            resp.raise_for_status()
            embeddings = resp.json().get("embeddings", [])
            if len(embeddings) == len(texts):
                return [emb if len(emb) == VECTOR_SIZE else None for emb in embeddings]
            return [None] * len(texts)
        except Exception as e:
            if attempt < retries:
                time.sleep(1)
            else:
                print(f"  [ERROR] Batch embedding failed: {e}")
                return [None] * len(texts)


# ============================================================
# File processing
# ============================================================

def process_markdown(filepath: str, base_path: str) -> list[dict]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        return []

    fm, body = parse_yaml_frontmatter(text)
    rel_path = os.path.relpath(filepath, base_path)

    if not body.strip():
        return []

    chunks = heading_aware_chunk(body)
    results = []
    ol_version = infer_ol_version(rel_path)
    product = infer_product(rel_path)
    source = infer_source(rel_path)

    # Tags that are not meaningful as topic (product names, version labels, meta tags)
    # Tags that should NOT be used as topic (too generic, or product/meta labels)
    NON_TOPIC_TAGS = frozenset({
        "oracle-linux", "ol8", "ol9", "ol10", "uek",
        "olam", "olcne", "olm210", "clippings", "technical",
        "index", "oracle", "system", "operations", "linux",
        "knowledge", "career", "oracle-vm",
    })

    for i, chunk in enumerate(chunks):
        payload = {
            "source_file": rel_path,
            "chunk_index": i,
            "chunk_text": chunk,
            "title": fm.get("title", Path(filepath).stem),
            "source": source,
            "file_type": "markdown",
        }

        if fm.get("source_url"):
            payload["source_url"] = fm["source_url"]
        if fm.get("type"):
            payload["type"] = fm["type"]

        tags = fm.get("tags", [])
        if tags:
            payload["tags"] = [str(t) for t in tags]

        if ol_version:
            payload["ol_version"] = ol_version

        if product:
            payload["product"] = product

        topic = fm.get("topic", "")
        if not topic and tags:
            for t in tags:
                if str(t) not in NON_TOPIC_TAGS:
                    topic = str(t)
                    break
        if topic and topic not in NON_TOPIC_TAGS:
            payload["topic"] = topic

        results.append({
            "id": generate_uuid(rel_path, i),
            "payload": payload,
            "chunk_text": chunk,
        })

    return results


def scan_vault(base_path: str, filter_pattern: str = "") -> list[str]:
    files = []
    for root, dirs, filenames in os.walk(base_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fname in filenames:
            if any(skip in fname or skip in root for skip in SKIP_PATTERNS):
                continue
            filepath = os.path.join(root, fname)
            ext = os.path.splitext(fname)[1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                if filter_pattern and filter_pattern.lower() not in filepath.lower():
                    continue
                files.append(filepath)
    files.sort()
    return files


def format_eta(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.0f}s"
    m, s = divmod(int(seconds), 60)
    return f"{m}m{s:02d}s"


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Ingest docs-tech-ol into Qdrant (Local Mode)")
    parser.add_argument("--dry-run", action="store_true", help="Parse only, no embedding/upload")
    parser.add_argument("--force", action="store_true", help="Re-embed all files")
    parser.add_argument("--rebuild", action="store_true", help="Hot-swap rebuild")
    parser.add_argument("--filter", type=str, default="", help="Only process files matching pattern")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    base_path = str(BASE_DIR)
    is_rebuild = args.rebuild

    print(f"=== docs-tech-ol → Qdrant Ingestion (Local Mode + BM25) ===")
    print(f"Base:      {base_path}")
    print(f"Storage:   {QDRANT_LOCAL_PATH} (local)")
    print(f"Alias:     {ALIAS_NAME}")
    print(f"Embedding: {EMBEDDING_MODEL} ({VECTOR_SIZE}d)")
    print(f"BM25:      jieba + Chinese/English tokenizer")
    print(f"Chunk:     max {MAX_CHUNK_CHARS} chars")
    print(f"Mode:      {'REBUILD' if is_rebuild else 'FORCE' if args.force else 'incremental'}")
    if args.filter:
        print(f"Filter:    {args.filter}")

    if not args.dry_run:
        targets = init_targets()
    else:
        targets = []

    print()

    # --- Determine target collection per Qdrant target ---
    target_info = {}  # tgt_name -> {"old": str|None, "new": str, "tgt": QdrantTarget}
    ts = time.strftime("%Y%m%d_%H%M%S")

    for tgt in targets:
        old_col = get_real_collection(tgt)
        if is_rebuild:
            new_col = f"{COLLECTION_PREFIX}{ts}"
            if not create_collection(new_col, tgt, defer_indexing=True):
                print(f"[FATAL][{tgt.name}] Cannot create collection, skipping")
                continue
            if old_col:
                print(f"[HOT-SWAP][{tgt.name}] Old: '{old_col}' → New: '{new_col}'")
        else:
            if old_col:
                new_col = old_col
            else:
                new_col = f"{COLLECTION_PREFIX}{ts}"
                if not create_collection(new_col, tgt):
                    print(f"[FATAL][{tgt.name}] Cannot create collection, skipping")
                    continue
                swap_alias(new_col, tgt)
        target_info[tgt.name] = {"old": old_col, "new": new_col, "tgt": tgt}

    if is_rebuild and not args.dry_run:
        cache_path = os.path.join(base_path, HASH_CACHE_FILE)
        if os.path.exists(cache_path):
            os.remove(cache_path)

    if not target_info and not args.dry_run:
        print("[FATAL] No targets available")
        sys.exit(1)

    for name, info in target_info.items():
        print(f"Target:    [{name}] {info['new']}")

    # --- Check Ollama ---
    if not args.dry_run:
        try:
            r = requests.post(OLLAMA_URL, json={"model": EMBEDDING_MODEL, "input": "warmup"}, timeout=120)
            r.raise_for_status()
            print(f"[OK] Ollama ready")
        except Exception as e:
            print(f"[FATAL] Ollama not reachable: {e}")
            sys.exit(1)

    # --- Scan and filter files ---
    skip_cache = args.force or is_rebuild
    hash_cache = {} if skip_cache else load_hash_cache(base_path)
    new_cache = {}

    files = scan_vault(base_path, args.filter)
    print(f"\nFound {len(files)} files")

    changed_files = []
    skipped = 0
    for filepath in files:
        rel_path = os.path.relpath(filepath, base_path)
        current_hash = file_content_hash(filepath)
        new_cache[rel_path] = current_hash
        if hash_cache.get(rel_path) == current_hash and not skip_cache:
            skipped += 1
        else:
            changed_files.append(filepath)

    if skipped:
        print(f"Skipped {skipped} unchanged files")
    print(f"Processing {len(changed_files)} files\n")

    # --- Parse all chunks first (needed for BM25 fit) ---
    print("[PARSE] Extracting chunks from all changed files...")
    all_file_chunks = []
    total_chunks = 0
    for filepath in changed_files:
        chunks = process_markdown(filepath, base_path)
        all_file_chunks.append((filepath, chunks))
        total_chunks += len(chunks)
    print(f"[PARSE] {total_chunks} chunks from {len(changed_files)} files")

    if not changed_files:
        print("Nothing to do.")
        save_hash_cache(base_path, new_cache)
        return

    # --- Build BM25 model ---
    bm25 = None
    if not args.dry_run:
        print("[BM25] Building BM25 model from corpus...")
        # Import from Personal_AI_Brain's shared module
        bm25_module_path = os.path.expanduser("~/d/Personal_AI_Brain/00_System")
        sys.path.insert(0, bm25_module_path)
        from bm25_tokenizer import BM25Tokenizer

        all_texts = []
        for _, chunks in all_file_chunks:
            for c in chunks:
                all_texts.append(c["chunk_text"])

        bm25 = BM25Tokenizer()
        bm25.fit(all_texts)
        print(f"[BM25] Vocab size: {bm25.vocab_size}, corpus: {len(all_texts)} chunks")

    # --- Embed and upsert ---
    total_embedded = 0
    total_failed = 0
    upsert_buffers = {name: [] for name in target_info}
    t_start = time.time()

    for fi, (filepath, chunks) in enumerate(all_file_chunks):
        rel_path = os.path.relpath(filepath, base_path)

        if args.dry_run:
            tags = chunks[0]["payload"].get("tags", []) if chunks else []
            ol = chunks[0]["payload"].get("ol_version", "") if chunks else ""
            print(f"  [{fi+1}/{len(changed_files)}] {rel_path}: {len(chunks)} chunks, ol={ol}, tags={tags}")
            continue

        if not chunks:
            continue

        # Delete old points (incremental mode)
        if not is_rebuild:
            for name, info in target_info.items():
                delete_file_points(info['new'], rel_path, info['tgt'])

        # Embed once, upsert to all targets
        for batch_start in range(0, len(chunks), EMBED_BATCH_SIZE):
            batch_chunks = chunks[batch_start:batch_start + EMBED_BATCH_SIZE]
            texts = [c["chunk_text"] for c in batch_chunks]
            vectors = embed_batch(texts)

            for chunk_data, vector in zip(batch_chunks, vectors):
                if vector:
                    # Generate BM25 sparse vector
                    sparse_vec = bm25.encode(chunk_data["chunk_text"])

                    point = models.PointStruct(
                        id=chunk_data["id"],
                        vector={
                            "dense": vector,
                            "bm25": sparse_vec,
                        },
                        payload=chunk_data["payload"],
                    )
                    total_embedded += 1

                    for name in target_info:
                        upsert_buffers[name].append(point)
                        if len(upsert_buffers[name]) >= BATCH_SIZE:
                            tgt = target_info[name]['tgt']
                            tgt.client.upsert(
                                collection_name=target_info[name]['new'],
                                points=upsert_buffers[name],
                            )
                            upsert_buffers[name] = []
                else:
                    total_failed += 1

        elapsed = time.time() - t_start
        rate = (fi + 1) / elapsed if elapsed > 0 else 0
        remaining = (len(changed_files) - fi - 1) / rate if rate > 0 else 0
        print(f"  [{fi+1}/{len(changed_files)}] {rel_path}: {len(chunks)} chunks  "
              f"[{format_eta(elapsed)} elapsed, ~{format_eta(remaining)} left]")

    # Flush remaining buffers
    if not args.dry_run:
        for name, buf in upsert_buffers.items():
            if buf:
                tgt = target_info[name]['tgt']
                tgt.client.upsert(
                    collection_name=target_info[name]['new'],
                    points=buf,
                )

    elapsed = time.time() - t_start

    # --- Save BM25 model ---
    if not args.dry_run and bm25:
        bm25_path = os.path.join(base_path, BM25_MODEL_FILE)
        bm25.save(bm25_path)
        print(f"[BM25] Model saved to {BM25_MODEL_FILE} (vocab={bm25.vocab_size})")

    # --- Post-processing per target ---
    if not args.dry_run:
        for name, info in target_info.items():
            tgt = info['tgt']
            new_col = info['new']
            old_col = info['old']

            if is_rebuild:
                enable_indexing(new_col, tgt)

            if is_rebuild:
                if old_col and old_col != ALIAS_NAME:
                    swap_alias(new_col, tgt, old_col)
                    drop_collection(old_col, tgt)
                elif old_col == ALIAS_NAME:
                    drop_collection(ALIAS_NAME, tgt)
                    swap_alias(new_col, tgt)
                else:
                    swap_alias(new_col, tgt)

    save_hash_cache(base_path, new_cache)

    # --- Summary ---
    print(f"\n{'='*50}")
    print(f"Files:     {len(changed_files)} / {len(files)}")
    print(f"Chunks:    {total_chunks}")
    print(f"Time:      {format_eta(elapsed)}")
    if not args.dry_run:
        print(f"Embedded:  {total_embedded}")
        print(f"Failed:    {total_failed}")
        if total_embedded > 0:
            print(f"Speed:     {elapsed/total_embedded*1000:.0f}ms/chunk")
        if bm25:
            print(f"BM25:      {bm25.vocab_size} tokens")
        for name, info in target_info.items():
            print(f"\n--- {name} ---")
            print(f"Alias:     {ALIAS_NAME} → {info['new']}")
            try:
                col_info = info['tgt'].client.get_collection(info['new'])
                print(f"Points:    {col_info.points_count}, status={col_info.status}")
            except Exception:
                pass

    # Lock down storage permissions (owner only)
    if not args.dry_run:
        for root, dirs, files in os.walk(QDRANT_LOCAL_PATH):
            os.chmod(root, 0o700)
            for f in files:
                os.chmod(os.path.join(root, f), 0o600)

    # Close clients
    if not args.dry_run:
        for tgt in targets:
            tgt.client.close()


if __name__ == "__main__":
    main()
