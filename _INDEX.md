---
title: docs-tech-ol — Root Index
tags: [system, index]
type: index
updated: 2026-04-08
sensitivity: public
---

# docs-tech-ol Technical Knowledge Base

Oracle Linux / UEK / system administration knowledge base with Qdrant hybrid search (dense semantic + BM25 keyword RRF fusion).

## Directory Structure

| Folder | Contents | Count |
|--------|----------|-------|
| 00_System/ | Ingestion, search, and fetch scripts | 3 scripts |
| 01_Markdown/oracle/ | Oracle Linux official docs (OL8/9/10, UEK, OLAM, OLCNE, OLM210, shared) | ~197 |

## Search

```bash
# Default hybrid search
python3 00_System/tech_qdrant_search.py "query"

# Keyword mode (error codes / CVE / package names)
python3 00_System/tech_qdrant_search.py "ORA-12154" --mode keyword

# Filter by OL version
python3 00_System/tech_qdrant_search.py "firewall" --filter ol_version=ol9
```

## Document Organization

Oracle docs are organized by product/version:

| Subfolder | Content |
|-----------|---------|
| `ol8/`, `ol9/`, `ol10/` | Oracle Linux per-version docs |
| `uek/` | Unbreakable Enterprise Kernel release notes |
| `shared/` | Cross-version docs (openssh, selinux, podman, ksplice, etc.) |
| `olam/` | Oracle Linux Automation Manager 2.3 |
| `olcne/` | Oracle Cloud Native Environment |
| `olm210/` | Oracle Linux Manager 2.10 |
| `pdf/` | Downloaded PDFs and their Markdown conversions |
