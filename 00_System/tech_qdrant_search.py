#!/usr/bin/env python3
"""
docs-tech-ol — Qdrant Hybrid Search (Local Mode + BM25)
技术知识库搜索工具 — 语义 + BM25 关键词混合搜索

Usage:
    python tech_qdrant_search.py "kernel panic after upgrade"
    python tech_qdrant_search.py "systemd service failed" --filter ol_version=ol9
    python tech_qdrant_search.py "firewall" --filter topic=security
    python tech_qdrant_search.py "ORA-12345" --mode keyword          # BM25 keyword only
    python tech_qdrant_search.py "ksplice" --mode hybrid             # default: dense + BM25
    python tech_qdrant_search.py --stats
    python tech_qdrant_search.py --filters

Search modes:
    hybrid (default): Dense semantic + BM25 keyword via RRF fusion
    semantic:         Dense vector only
    keyword:          BM25 sparse vector only

Local: QdrantClient(path=...) — no Docker, no network port

Queries the alias 'technical_ai_brain'.
"""

import os
import sys
import json
import argparse
import requests
import re
from pathlib import Path

from qdrant_client import QdrantClient, models

# --- Configuration ---
QDRANT_LOCAL_PATH = str(Path(__file__).resolve().parent.parent / "qdrant_local_db")

OLLAMA_URL = "http://localhost:11434/api/embed"
EMBEDDING_MODEL = "qwen3-embedding:0.6b"
COLLECTION = "docs_tech_ol"
BM25_MODEL_FILE = ".tech_bm25_model.json"

BASE_DIR = Path(__file__).resolve().parent.parent


def get_client() -> QdrantClient:
    """Get local Qdrant client."""
    return QdrantClient(path=QDRANT_LOCAL_PATH)


def load_bm25():
    """Load BM25 tokenizer from saved model."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from bm25_tokenizer import BM25Tokenizer

    model_path = os.path.join(str(BASE_DIR), BM25_MODEL_FILE)
    if not os.path.exists(model_path):
        print(f"[WARN] BM25 model not found. Run ingest first.", file=sys.stderr)
        return None
    return BM25Tokenizer.load(model_path)


def embed(text: str) -> list[float]:
    resp = requests.post(OLLAMA_URL, json={"model": EMBEDDING_MODEL, "input": text}, timeout=30)
    resp.raise_for_status()
    return resp.json()["embeddings"][0]


def build_filter(filters: dict) -> models.Filter:
    must = []
    for k, v in filters.items():
        must.append(models.FieldCondition(key=k, match=models.MatchValue(value=v)))
    return models.Filter(must=must)


def search_hybrid(client: QdrantClient, query: str, limit: int = 5,
                   filters: dict = None, mode: str = "hybrid", bm25=None) -> list[dict]:
    """Search with dense, BM25, or hybrid (RRF fusion)."""

    qdrant_filter = build_filter(filters) if filters else None

    if mode == "keyword":
        if bm25 is None:
            print("[WARN] BM25 not loaded, falling back to semantic", file=sys.stderr)
            mode = "semantic"
        else:
            sparse_vec = bm25.encode(query)
            try:
                results = client.query_points(
                    collection_name=COLLECTION,
                    query=sparse_vec,
                    using="bm25",
                    query_filter=qdrant_filter,
                    limit=limit,
                    with_payload=True,
                )
                return [{"score": p.score, "payload": p.payload} for p in results.points]
            except Exception as e:
                print(f"[WARN] BM25 search failed: {e}", file=sys.stderr)
                return []

    if mode == "semantic":
        try:
            vector = embed(query)
        except Exception as e:
            print(f"[WARN] Embedding failed: {e}", file=sys.stderr)
            return []
        try:
            results = client.query_points(
                collection_name=COLLECTION,
                query=vector,
                using="dense",
                query_filter=qdrant_filter,
                limit=limit,
                with_payload=True,
            )
            return [{"score": p.score, "payload": p.payload} for p in results.points]
        except Exception as e:
            print(f"[WARN] Search failed: {e}", file=sys.stderr)
            return []

    # --- Hybrid: dense + BM25 with RRF ---
    try:
        vector = embed(query)
    except Exception as e:
        print(f"[WARN] Embedding failed: {e}", file=sys.stderr)
        return []

    prefetch_list = [
        models.Prefetch(
            query=vector,
            using="dense",
            limit=limit * 3,
            filter=qdrant_filter,
        ),
    ]

    fusion_query = None
    if bm25 is not None:
        sparse_vec = bm25.encode(query)
        if sparse_vec.indices:
            prefetch_list.append(
                models.Prefetch(
                    query=sparse_vec,
                    using="bm25",
                    limit=limit * 3,
                    filter=qdrant_filter,
                ),
            )
            fusion_query = models.FusionQuery(fusion=models.Fusion.RRF)

    try:
        if fusion_query and len(prefetch_list) > 1:
            results = client.query_points(
                collection_name=COLLECTION,
                prefetch=prefetch_list,
                query=fusion_query,
                limit=limit,
                with_payload=True,
            )
        else:
            results = client.query_points(
                collection_name=COLLECTION,
                query=vector,
                using="dense",
                query_filter=qdrant_filter,
                limit=limit,
                with_payload=True,
            )
        return [{"score": p.score, "payload": p.payload} for p in results.points]
    except Exception as e:
        print(f"[WARN] Hybrid search failed: {e}", file=sys.stderr)
        return []


def list_filters(client: QdrantClient):
    """List all available filter keys and their distinct values."""
    try:
        info = client.get_collection(COLLECTION)
        total_points = info.points_count
    except Exception as e:
        print(f"Collection '{COLLECTION}' not found: {e}")
        return

    filter_fields = ["ol_version", "product", "topic", "source", "tags", "type", "source_url"]
    print(f"Scanning {total_points} points for filter values...\n")

    # Scroll through all points
    payloads = []
    offset = None
    while True:
        results = client.scroll(
            collection_name=COLLECTION,
            limit=100,
            offset=offset,
            with_payload=filter_fields,
            with_vectors=False,
        )
        points, next_offset = results
        for p in points:
            payloads.append(p.payload)
        if next_offset is None:
            break
        offset = next_offset

    print(f"Available filter keys and values:")
    print(f"{'='*60}")

    for field in filter_fields:
        values = set()
        for p in payloads:
            val = p.get(field)
            if val is None:
                continue
            if isinstance(val, list):
                values.update(str(v) for v in val)
            else:
                values.add(str(val))

        if not values:
            continue

        sorted_vals = sorted(values)
        print(f"\n  {field} ({len(sorted_vals)} values):")
        if field == "source_url" and len(sorted_vals) > 10:
            for v in sorted_vals[:5]:
                print(f"    - {v}")
            print(f"    ... and {len(sorted_vals) - 5} more")
        else:
            for v in sorted_vals:
                print(f"    - {v}")

    print(f"\nUsage: tech_qdrant_search.py \"query\" --filter key=value")


def stats(client: QdrantClient):
    try:
        info = client.get_collection(COLLECTION)
        print(f"Collection: {COLLECTION}")
        print(f"Points:     {info.points_count}")
        print(f"Status:     {info.status}")
        print(f"Storage:    {QDRANT_LOCAL_PATH}")

        try:
            aliases = client.get_aliases().aliases
            for a in aliases:
                if a.alias_name == COLLECTION:
                    print(f"Alias →     {a.collection_name}")
                    break
        except Exception:
            pass

        # BM25 info
        model_path = os.path.join(str(BASE_DIR), BM25_MODEL_FILE)
        if os.path.exists(model_path):
            bm25 = load_bm25()
            if bm25:
                print(f"BM25 vocab: {bm25.vocab_size} tokens")
        else:
            print(f"BM25 model: not found (run ingest to build)")

        md_count = sum(1 for _ in BASE_DIR.rglob("*.md") if "00_System" not in str(_))
        print(f"\nLocal files: {md_count} markdown files")

    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Search docs-tech-ol (hybrid)")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--limit", "-n", type=int, default=5, help="Number of results")
    parser.add_argument("--filter", "-f", action="append", help="Filter as key=value")
    parser.add_argument("--mode", "-m", choices=["hybrid", "semantic", "keyword"],
                        default="hybrid", help="Search mode (default: hybrid)")
    parser.add_argument("--stats", action="store_true", help="Show collection stats")
    parser.add_argument("--filters", action="store_true", help="List available filter values")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    try:
        client = get_client()
    except Exception as e:
        print(f"[FATAL] Cannot connect to Qdrant: {e}", file=sys.stderr)
        sys.exit(1)

    if args.filters:
        list_filters(client)
        client.close()
        return

    if args.stats:
        stats(client)
        client.close()
        return

    if not args.query:
        parser.print_help()
        client.close()
        return

    filters = {}
    if args.filter:
        for f in args.filter:
            k, v = f.split("=", 1)
            filters[k] = v

    # Auto-detect: error codes/commands → hybrid
    if args.mode == "hybrid":
        if re.match(r'^(ORA-\d+|CVE-\d+|rpm|yum|dnf|systemctl|journalctl)\b', args.query, re.IGNORECASE):
            pass  # already hybrid, good

    # Load BM25
    bm25 = load_bm25() if args.mode in ("hybrid", "keyword") else None

    results = search_hybrid(client, args.query, args.limit, filters if filters else None,
                            mode=args.mode, bm25=bm25)

    if args.json:
        output = [{
            "score": round(r["score"], 4),
            "source_file": r["payload"]["source_file"],
            "title": r["payload"].get("title", ""),
            "tags": r["payload"].get("tags", []),
            "ol_version": r["payload"].get("ol_version", ""),
            "source_url": r["payload"].get("source_url", ""),
            "text": (r["payload"].get("chunk_text") or "")[:300],
            "target": "local",
        } for r in results]
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        if not results:
            print(f"Query: {args.query} (mode: {args.mode})")
            print("No results found.")
            client.close()
            return
        print(f"Query: {args.query} (mode: {args.mode})")
        print(f"Results: {len(results)}\n")
        for i, r in enumerate(results):
            p = r["payload"]
            print(f"[{i+1}] Score: {r['score']:.4f}")
            print(f"    File: {p['source_file']}")
            print(f"    Title: {p.get('title', 'N/A')}")
            ol = p.get('ol_version', '')
            if ol:
                print(f"    OL Version: {ol}")
            tags = p.get('tags', [])
            if tags:
                print(f"    Tags: {tags}")
            url = p.get('source_url', '')
            if url:
                print(f"    URL: {url}")
            text = (p.get("chunk_text") or "").replace("\n", " ")[:200]
            print(f"    Text: {text}...")
            print()

    client.close()


if __name__ == "__main__":
    main()
