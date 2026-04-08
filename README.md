# docs-tech-ol

Oracle Linux technical knowledge base with Qdrant hybrid search (dense semantic + BM25 keyword RRF fusion).

**Portable**: all docs and scripts live inside the repo — clone, install dependencies, build the index, and search.

## How It Works

```
docs-urls.md          ->  fetch_oracle_docs.py  ->  01_Markdown/oracle/*.md
                                                            |
                                                            v
                                                Ollama (qwen3-embedding:0.6b)
                                                            |
                                                 tech_qdrant_ingest.py
                                              (dense vectors + BM25 model)
                                                            |
                                                 Qdrant Local Mode
                                                (qdrant_local_db/ in repo)
                                              No Docker. No network port.
                                                            |
                                       ┌────────────────────┴────────────────────┐
                                       v                                         v
                              Dense vector index                        BM25 sparse index
                                 (semantic)                        (jieba tokenizer)
                                       └────────────────────┬────────────────────┘
                                                            v
                                                 RRF fusion (hybrid)
                                                            |
                                                 tech_qdrant_search.py
```

1. `docs-urls.md` — Oracle documentation URL list (single source of truth)
2. `fetch_oracle_docs.py` — Fetch URLs and save as Markdown
3. `tech_qdrant_ingest.py` — Chunk, embed, build BM25 model, write to Qdrant
4. `tech_qdrant_search.py` — Hybrid search (dense + BM25 via RRF)

## Directory Structure

```
docs-tech-ol/
├── docs-urls.md                    # URL list (edit this to add/remove docs)
├── 00_System/                      # Scripts and tools
│   ├── fetch_oracle_docs.py        # Fetch Oracle docs
│   ├── tech_qdrant_ingest.py       # Chunk, embed, index
│   └── tech_qdrant_search.py       # Hybrid search
├── 01_Markdown/                    # All technical documents
│   └── oracle/                     # Oracle official docs
│       ├── ol10/                   # Oracle Linux 10
│       ├── ol9/                    # Oracle Linux 9
│       ├── ol8/                    # Oracle Linux 8
│       ├── uek/                    # Unbreakable Enterprise Kernel
│       ├── shared/                 # Cross-version docs (openssh, selinux, podman...)
│       ├── olam/                   # Oracle Linux Automation Manager 2.3
│       ├── olm210/                 # Oracle Linux Manager 2.10
│       ├── olcne/                  # Oracle Cloud Native Environment
│       └── pdf/                    # Downloaded PDFs + converted .pdf.md
├── qdrant_local_db/                # Qdrant vector database (git-ignored, rebuild locally)
├── .tech_bm25_model.json           # BM25 model (git-ignored, rebuilt during ingest)
├── CLAUDE.md                       # Claude Code project instructions
└── README.md                       # This file
```

## Prerequisites

- **Python 3.10+**: `requests`, `beautifulsoup4`, `markdownify`, `pyyaml`, `qdrant-client`, `jieba`
- **Ollama**: `qwen3-embedding:0.6b` model

```bash
pip3 install requests beautifulsoup4 markdownify pyyaml qdrant-client jieba
ollama pull qwen3-embedding:0.6b
```

## Quick Start

### First-time setup after clone

```bash
# 1. Fetch all Oracle docs
python3 00_System/fetch_oracle_docs.py

# 2. Build search index (dense + BM25), writes to qdrant_local_db/
python3 00_System/tech_qdrant_ingest.py --rebuild
```

### Search

```bash
# Hybrid search (default, recommended)
python3 00_System/tech_qdrant_search.py "kernel panic after upgrade"

# Filter by OL version
python3 00_System/tech_qdrant_search.py "networking bond" --filter ol_version=ol9

# Filter by topic
python3 00_System/tech_qdrant_search.py "firewall zone" --filter topic=security

# Filter by product
python3 00_System/tech_qdrant_search.py "ksplice" --filter product=uek

# Keyword mode — error codes, CVE, package names
python3 00_System/tech_qdrant_search.py "ORA-12345" --mode keyword

# Semantic mode — conceptual queries
python3 00_System/tech_qdrant_search.py "how to troubleshoot boot issues" --mode semantic

# Index stats
python3 00_System/tech_qdrant_search.py --stats

# Available filters
python3 00_System/tech_qdrant_search.py --filters
```

**Search mode selection:**

| Mode | Best for |
|------|----------|
| `hybrid` (default) | Most queries |
| `keyword` | Error codes, CVE IDs, package names, command names |
| `semantic` | Conceptual questions ("how does X work") |

**Available filters:**

| Filter | Values | Example |
|--------|--------|---------|
| `ol_version` | ol8, ol9, ol10 | `--filter ol_version=ol9` |
| `product` | oracle-linux, uek, olam, olcne, olm210 | `--filter product=uek` |
| `topic` | security, networking, storage, patching, ... | `--filter topic=security` |
| `source` | oracle | `--filter source=oracle` |
| `type` | oracle-doc, pdf-converted, index | `--filter type=oracle-doc` |

### Update docs (after editing docs-urls.md)

```bash
# 1. Preview changes
python3 00_System/fetch_oracle_docs.py --sync --dry-run

# 2. Execute sync
python3 00_System/fetch_oracle_docs.py --sync

# 3. Rebuild index
python3 00_System/tech_qdrant_ingest.py --rebuild
```

## Command Reference

| Command | When to use |
|---------|-------------|
| `fetch_oracle_docs.py` | First-time fetch / after Oracle publishes new docs |
| `fetch_oracle_docs.py --sync` | After editing docs-urls.md |
| `fetch_oracle_docs.py --force` | Force re-fetch all docs |
| `tech_qdrant_ingest.py --rebuild` | Full index rebuild |
| `tech_qdrant_ingest.py` | Incremental update (changed files only) |
| `tech_qdrant_search.py "query"` | Search the knowledge base |
| `tech_qdrant_search.py --stats` | View index statistics |
| `tech_qdrant_search.py --filters` | View available filter values |

## License

The scripts in this repo are provided as-is. Oracle Linux documentation content is sourced from [Oracle's public documentation](https://docs.oracle.com/en/operating-systems/oracle-linux/) and is subject to Oracle's terms of use.
