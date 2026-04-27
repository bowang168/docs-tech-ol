# Claude Code Instructions for docs-tech-ol

## Overview

This is an Oracle Linux technical knowledge base with Qdrant hybrid search. When answering questions about Oracle Linux, UEK, Ksplice, or related topics, search the local knowledge base first.

## Directory Structure

```
00_System/           — scripts: ingest, search, fetch, BM25 tokenizer
01_Markdown/oracle/  — source docs by OL version (ol8/, ol9/, ol10/)
qdrant_local_db/     — embedded Qdrant storage (gitignored)
```

## Architecture

- **Qdrant Local Mode** — embedded database in `qdrant_local_db/`, no Docker, no network ports
- **Embedding** — Ollama `qwen3-embedding:0.6b` (1024-dim)
- **BM25** — `bm25_tokenizer.py` (local copy, jieba Chinese/English tokenizer)
- **Search** — hybrid mode (dense + BM25 via RRF fusion) by default
- **Portable** — clone, install dependencies, `--rebuild`, and search

## Claude Code Integration

This knowledge base is wrapped by the `/techdb` skill (`~/.claude/skills/techdb/SKILL.md`). Cascade:

1. **Qdrant local** (this repo) — covers OL7/8/9/10
2. **Context7 MCP** — fallback for OL10/RHEL10/OCI latest docs (**opt-in**)
3. **WebSearch + WebFetch** — last resort

**Context7 launch requirement**: Context7 only loads when Claude Code is started via the `claude-techdb` alias (defined in `~/.shell_common`):

```bash
alias claude-techdb='claude --mcp-config ~/.claude/mcp-techdb.json'
```

The MCP config file `~/.claude/mcp-techdb.json` declares the `@upstash/context7-mcp` server. Default `claude` does NOT load Context7 — `/techdb` cascade falls through directly to WebSearch in that case. Use `claude-techdb` whenever you expect to query OL10 / RHEL10 / OCI latest docs.

## Prerequisites

- Python 3.10+, `pip install qdrant-client requests jieba`
- **Ollama must be running** before search or ingest (`ollama serve`)
- Model pulled: `ollama pull qwen3-embedding:0.6b`

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

## Fetching Upstream Docs

```bash
# Download/update Oracle Linux docs → 01_Markdown/
python3 00_System/fetch_oracle_docs.py
```

## Ingestion

```bash
# Incremental sync (only changed files)
python3 00_System/tech_qdrant_ingest.py

# Full rebuild
python3 00_System/tech_qdrant_ingest.py --rebuild
```
