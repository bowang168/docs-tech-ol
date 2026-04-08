# Claude Code Instructions for docs-tech-ol

## Overview

This is an Oracle Linux technical knowledge base with Qdrant hybrid search. When answering questions about Oracle Linux, UEK, Ksplice, or related topics, search the local knowledge base first.

## Architecture

- **Qdrant Local Mode** — embedded database in `qdrant_local_db/`, no Docker, no network ports
- **Embedding** — Ollama `qwen3-embedding:0.6b` (1024-dim)
- **BM25** — jieba Chinese/English tokenizer for keyword matching
- **Search** — hybrid mode (dense + BM25 via RRF fusion) by default
- **Portable** — clone, install dependencies, `--rebuild`, and search

## Search Commands

```bash
# Default hybrid mode (best for most queries)
python3 00_System/tech_qdrant_search.py "query" --limit 5

# With filters
python3 00_System/tech_qdrant_search.py "firewall" --filter ol_version=ol9
python3 00_System/tech_qdrant_search.py "ksplice" --filter product=uek

# Keyword mode: error codes, CVE, command names, package names
python3 00_System/tech_qdrant_search.py "CVE-2024-26704" --mode keyword

# Semantic mode: conceptual/fuzzy queries
python3 00_System/tech_qdrant_search.py "how to troubleshoot boot issues" --mode semantic

# List available filter values
python3 00_System/tech_qdrant_search.py --filters

# Collection stats
python3 00_System/tech_qdrant_search.py --stats
```

## Search Mode Selection

| Mode | When to use |
|------|-------------|
| hybrid (default) | Most queries |
| keyword | Error codes, CVE IDs, package names, exact commands |
| semantic | Conceptual questions ("how does X work") |

## Available Filters

| Filter | Values | Usage |
|--------|--------|-------|
| `ol_version` | ol8, ol9, ol10 | OS version |
| `product` | oracle-linux, uek, olam, olcne, olm210 | Product line |
| `topic` | security, networking, storage, patching, etc. | Technical subject |
| `source` | oracle | Content origin |
| `type` | oracle-doc, pdf-converted, index | Document type |

## Ingestion

```bash
# Incremental sync (only changed files)
python3 00_System/tech_qdrant_ingest.py

# Full rebuild
python3 00_System/tech_qdrant_ingest.py --rebuild
```
