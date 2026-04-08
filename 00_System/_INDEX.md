---
title: System — Index
tags: [system, index]
type: index
updated: 2026-04-05
sensitivity: public
---

# 00_System 系统工具

脚本、模板和工具。

## 脚本

| 文件 | 用途 |
|------|------|
| tech_qdrant_ingest.py | 文档分块、embedding、BM25 建模、写入 Qdrant Local |
| tech_qdrant_search.py | Hybrid 搜索（dense + BM25 via RRF）|
| fetch_oracle_docs.py | 从 docs-urls.md 抓取 Oracle 官方文档 |
| pdf2md_check.py | 检查 PDF 是否已转 MD，支持 Claude API 自动转换 |

## 模板

| 文件夹/文件 | 用途 |
|-------------|------|
| ZZ-Obsidian笔记模板/00-模板-每日笔记.md | Obsidian 每日笔记模板 |
| ZZ-Obsidian笔记模板/09-Oracle技术支持沟通模板-Github.md | Oracle 技术支持邮件模板（公开版）|

## 生成文件（git-ignored）

| 文件 | 说明 |
|------|------|
| .tech_hash_cache.json | 增量 ingest 缓存（记录已处理文件 hash）|
| .tech_bm25_model.json | BM25 模型（ingest 时自动构建，search 时加载）|
