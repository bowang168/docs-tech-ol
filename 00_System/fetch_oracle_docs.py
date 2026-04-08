#!/usr/bin/env python3
"""
docs-tech-ol — Oracle Docs Fetcher
从 docs-urls.md 提取所有 URL，抓取 HTML 并转为 Markdown 保存到本地

Usage:
    python fetch_oracle_docs.py                          # fetch all (skip existing)
    python fetch_oracle_docs.py --force                  # re-fetch all
    python fetch_oracle_docs.py --dry-run                # show what would be fetched
    python fetch_oracle_docs.py --limit 5                # fetch first N only (for testing)
    python fetch_oracle_docs.py --filter ol9             # only fetch URLs matching pattern

Only fetches URLs explicitly listed in docs-urls.md. No URL expansion.
"""

import os
import re
import sys
import time
import argparse
import hashlib
import json
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin

try:
    from markdownify import markdownify as md
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Run: pip3 install markdownify beautifulsoup4 requests")
    sys.exit(1)

# --- Configuration ---
BASE_DIR = Path(__file__).resolve().parent.parent
ORACLE_URLS_FILE = BASE_DIR / "docs-urls.md"
ORACLE_DIR = BASE_DIR / "01_Markdown" / "oracle"
FETCH_LOG = BASE_DIR / "00_System" / ".fetch_log.json"

# Request settings
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) TechnicalAIBrain/1.0",
    "Accept": "text/html,application/xhtml+xml",
}
TIMEOUT = 30
DELAY_BETWEEN_REQUESTS = 1.5  # seconds, be polite to Oracle servers
CRAWL_DELAY = 0.5  # seconds between sub-page requests


def extract_urls_from_markdown(filepath: Path) -> list[dict]:
    """Extract all markdown links from docs-urls.md.
    Returns list of {url, title, context} dicts.
    """
    text = filepath.read_text(encoding="utf-8")
    # Match markdown links: [title](url)
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')

    urls = []
    seen = set()

    for match in link_pattern.finditer(text):
        title = match.group(1).strip()
        url = match.group(2).strip().rstrip('/')
        if url in seen:
            continue
        seen.add(url)

        urls.append({
            "title": title,
            "url": url,
            "subfolder": classify_url(url),
        })

    # Also extract bare URLs (not in markdown link format)
    bare_url_pattern = re.compile(r'(?<!\()(?<!")(https?://docs\.oracle\.com[^\s\)>]+)')
    for match in bare_url_pattern.finditer(text):
        url = match.group(1).strip().rstrip('/')
        if url in seen:
            continue
        seen.add(url)
        urls.append({
            "title": Path(urlparse(url).path).name or "untitled",
            "url": url,
            "subfolder": classify_url(url),
        })

    return urls


def classify_url(url: str) -> str:
    """Determine which subfolder a URL belongs to based on its path."""
    path = urlparse(url).path.lower()

    # UEK release notes
    if "/uek/" in path:
        return "uek"

    # Oracle Linux Manager 2.10
    if "/oracle-linux-manager" in path:
        return "olm210"

    # Oracle Linux Automation Manager
    if "automation-manager" in path or "/olam/" in path:
        return "olam"

    # Oracle Cloud Native Environment
    if "/olcne/" in path:
        return "olcne"

    # Version-specific Oracle Linux docs
    if "/oracle-linux/10/" in path:
        return "ol10"
    if "/oracle-linux/9/" in path:
        return "ol9"
    if "/oracle-linux/8/" in path:
        return "ol8"

    # Learning / tutorials
    learn_patterns = [
        "/learn", "/tutorials", "/developer.html",
    ]
    for pat in learn_patterns:
        if pat in path:
            return "shared/learn"

    # Shared docs (cross-version: openssh, selinux, podman, etc.)
    shared_patterns = [
        "/openssh/", "/selinux/", "/podman/", "/software-management/",
        "/uln/", "/ksplice-", "/cockpit/", "/certmanage/", "/vpn/",
        "/mptcp/", "/kvm-virtio/", "/asmlib/", "/dtrace-", "/nbde/",
        "/backup/", "/product-lifecycle/", "/limits/", "/notice-",
        "/gluster-storage/",
    ]
    for pat in shared_patterns:
        if pat in path:
            return "shared"

    # Docs under oracle-linux but not version-specific
    if "/oracle-linux/" in path:
        return "shared"

    # Everything else from docs.oracle.com
    if "docs.oracle.com" in url:
        return "shared"

    # Non-docs URLs (downloads, training, etc.) — skip or put in shared
    return "shared"


def url_to_filename(url: str, title: str) -> str:
    """Generate a clean filename from URL and title."""
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.strip("/").split("/") if p]

    # Use last 2-3 meaningful path segments
    if len(path_parts) >= 2:
        name = "_".join(path_parts[-2:])
    elif path_parts:
        name = path_parts[-1]
    else:
        name = hashlib.md5(url.encode()).hexdigest()[:12]

    # Clean up
    name = re.sub(r'[^\w\-.]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')

    # Ensure .md extension
    if not name.endswith('.md'):
        name += '.md'

    return name


def fetch_html(url: str) -> tuple[str, str, str]:
    """Fetch URL, return (html, content_type, final_url).
    final_url reflects any redirects (e.g. added trailing slash).
    Returns ("", "", url) on failure.
    """
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        resp.raise_for_status()
        return resp.text, resp.headers.get("Content-Type", ""), resp.url
    except requests.RequestException:
        return "", "", url


def html_to_markdown(html: str) -> str:
    """Convert HTML to clean markdown, stripping Oracle chrome."""
    soup = BeautifulSoup(html, "html.parser")

    # Try to extract main content area (Oracle docs structure)
    main_content = (
        soup.find("div", {"id": "content"})
        or soup.find("div", {"class": "book-body"})
        or soup.find("div", {"class": "chapter"})
        or soup.find("div", {"class": "article"})
        or soup.find("article")
        or soup.find("main")
        or soup.find("div", {"class": "content"})
        or soup.find("body")
    )

    if main_content is None:
        main_content = soup

    # Remove noise elements
    for tag in main_content.find_all(["nav", "header", "footer", "aside",
                                       "script", "style", "noscript"]):
        tag.decompose()
    for selector in [".breadcrumbs", ".breadcrumb", ".sidebar", ".toc", "#toc",
                     "#sidebar", ".header-nav", ".footer-nav", ".cookie-banner",
                     ".feedback-section", ".feedback", "#feedback", ".copyright",
                     ".book-nav", ".navigation", ".nav-bar"]:
        for el in main_content.select(selector):
            el.decompose()

    # Convert to markdown
    markdown = md(
        str(main_content),
        heading_style="ATX",
        bullets="-",
        strip=["img", "svg", "input", "button", "form", "iframe"],
    )

    markdown = re.sub(r'\n{4,}', '\n\n\n', markdown)
    return markdown.strip()


# Global set tracking ALL sub-page URLs fetched across all documents
# Prevents duplicate content when different entry URLs share sub-pages
_global_fetched_pages: set[str] = set()


def discover_and_fetch_sub_pages(start_url: str, first_html: str) -> list[tuple[str, str]]:
    """Follow <link rel="next"> chain to discover and fetch all pages in a multi-page doc.
    Oracle docs use rel="next" in HTML <head> to link pages sequentially.
    e.g. index.html -> network-Preface.html -> network-Overview.html -> ...
    Returns list of (url, html) tuples. First entry is (start_url, first_html).
    Skips pages already fetched by other documents (global dedup).
    """
    global _global_fetched_pages

    start_clean = start_url.rstrip("/")
    pages = [(start_url, first_html)]
    seen = {start_clean}
    _global_fetched_pages.add(start_clean)
    current_url = start_url
    current_html = first_html

    # Base directory for scope checking (e.g. /en/operating-systems/oracle-linux/9/network/)
    base_dir = urlparse(start_url).path.rstrip("/") + "/"

    max_pages = 100  # safety limit

    while len(pages) < max_pages:
        soup = BeautifulSoup(current_html, "html.parser")
        next_link = soup.find("link", rel="next")
        if not next_link or not next_link.get("href"):
            break

        next_url = urljoin(current_url, next_link["href"])
        # Strip fragment
        parsed = urlparse(next_url)
        next_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        clean = next_url.rstrip("/")

        # Avoid loops within this document
        if clean in seen:
            break
        # Skip if already fetched by another document (global dedup)
        if clean in _global_fetched_pages:
            print(f"           [DEDUP] Skipping already-fetched sub-page: {clean}")
            break
        # Must stay under same base directory
        if not parsed.path.startswith(base_dir):
            break

        time.sleep(CRAWL_DELAY)
        pg_html, _, pg_final_url = fetch_html(next_url)
        if not pg_html:
            break

        pages.append((next_url, pg_html))
        seen.add(clean)
        _global_fetched_pages.add(clean)
        current_url = next_url
        current_html = pg_html

    return pages


def fetch_and_convert(url: str, title: str) -> tuple[str, bool, int]:
    """Fetch URL (and all sub-pages via rel=next) and convert to markdown.
    Returns (markdown_content, success, page_count).
    """
    html, content_type, final_url = fetch_html(url)
    if not html and not content_type:
        return f"# Fetch Error\n\nURL: {url}\nError: fetch failed\n", False, 0

    # PDF — download binary to oracle/pdf/ and save placeholder .md
    if "pdf" in content_type.lower() or url.lower().endswith(".pdf"):
        pdf_dir = ORACLE_DIR / "pdf"
        pdf_dir.mkdir(parents=True, exist_ok=True)
        pdf_filename = Path(urlparse(url).path).name
        if not pdf_filename.endswith(".pdf"):
            pdf_filename += ".pdf"
        pdf_path = pdf_dir / pdf_filename

        # Download actual PDF binary
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
            resp.raise_for_status()
            pdf_path.write_bytes(resp.content)
            pdf_size_kb = len(resp.content) / 1024
            print(f"           PDF saved: oracle/pdf/{pdf_filename} ({pdf_size_kb:.0f} KB)")
        except requests.RequestException as e:
            print(f"           PDF download failed: {e}")

        local_note = f"Local copy: oracle/pdf/{pdf_filename}" if pdf_path.exists() else ""
        md_content = f"# {title}\n\n> PDF document — download from: {url}\n"
        if local_note:
            md_content += f"> {local_note}\n"
        return md_content, True, 1

    # Discover and fetch all sub-pages via <link rel="next"> chain
    # Use final_url (after redirect) so urljoin resolves relative hrefs correctly
    all_pages = discover_and_fetch_sub_pages(final_url, html)

    # Convert all pages to markdown
    markdown_parts = []
    for page_url, page_html in all_pages:
        page_md = html_to_markdown(page_html)
        if page_md and len(page_md) > 30:
            if len(markdown_parts) > 0:
                markdown_parts.append(f"\n\n---\n<!-- page: {page_url} -->\n\n{page_md}")
            else:
                markdown_parts.append(page_md)

    page_count = len(all_pages)

    markdown = "\n".join(markdown_parts)
    markdown = re.sub(r'\n{4,}', '\n\n\n', markdown).strip()

    if len(markdown) < 50:
        return f"# {title}\n\n> Content too short after conversion. Visit: {url}\n", False, page_count

    return markdown, True, page_count


def build_frontmatter(title: str, url: str, subfolder: str) -> str:
    """Build YAML frontmatter for the saved document.

    Metadata design:
      - ol_version: only ol8/ol9/ol10 (OS version)
      - product: oracle-linux/uek/olam/olcne/olm210 (product line, inferred by ingest from path)
      - topic: technical subject (from URL inference)
      - tags: includes product identifiers + topic for searchability
    """
    today = time.strftime("%Y-%m-%d")

    tags = ["oracle-linux"]

    # OL version tags (OS version only)
    if subfolder in ("ol8", "ol9", "ol10"):
        tags.append(subfolder)

    # Product tags (keep short, consistent names)
    if subfolder == "uek":
        tags.append("uek")
    elif subfolder == "olam":
        tags.append("olam")
    elif subfolder == "olcne":
        tags.append("olcne")
    elif subfolder == "olm210":
        tags.append("olm210")

    # Determine topic from URL
    topic = infer_topic(url)
    if topic:
        tags.append(topic)

    tags_yaml = "\n".join(f'  - "{t}"' for t in tags)
    return f"""---
title: "{title}"
source_url: "{url}"
fetched: {today}
tags:
{tags_yaml}
type: "oracle-doc"
---

"""


def infer_topic(url: str) -> str:
    """Infer topic category from URL path."""
    path = urlparse(url).path.lower()
    topic_map = {
        "install": "installation",
        "leapp": "upgrade",
        "boot": "system-management",
        "systemd": "system-management",
        "udev": "system-management",
        "hugepages": "system-management",
        "cron": "system-management",
        "security": "security",
        "userauth": "security",
        "firewall": "security",
        "oscap": "security",
        "selinux": "security",
        "openssh": "security",
        "fapolicyd": "security",
        "secure-boot": "security",
        "certmanage": "security",
        "stordev": "storage",
        "fsadmin": "storage",
        "xfs": "storage",
        "btrfs": "storage",
        "ext": "storage",
        "nfs": "storage",
        "ocfs2": "storage",
        "samba": "storage",
        "nbde": "storage",
        "gluster": "storage",
        "network": "networking",
        "balancing": "networking",
        "vpn": "networking",
        "mptcp": "networking",
        "dhcp": "networking",
        "bind": "networking",
        "chrony": "networking",
        "kvm": "virtualization",
        "podman": "containers",
        "olcne": "containers",
        "monitoring": "monitoring",
        "tuned": "performance",
        "pcp": "monitoring",
        "sos": "debugging",
        "auditing": "monitoring",
        "dtrace": "tracing",
        "gprofng": "performance",
        "python": "development",
        "drgn": "debugging",
        "corelens": "debugging",
        "relnotes": "release-notes",
        "ibldr": "image-builder",
        "ksplice": "patching",
        "software-management": "package-management",
        "uln": "package-management",
        "cockpit": "system-management",
        "asmlib": "database",
        "availability": "high-availability",
        "backup": "backup",
        "accessibility": "accessibility",
    }
    for key, topic in topic_map.items():
        if key in path:
            return topic
    return ""


def load_fetch_log() -> dict:
    """Load fetch log to track what's been fetched."""
    if FETCH_LOG.exists():
        try:
            return json.loads(FETCH_LOG.read_text())
        except Exception:
            pass
    return {}


def save_fetch_log(log: dict):
    FETCH_LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False))


def get_expected_files(all_urls: list[dict]) -> dict[str, str]:
    """Build mapping of expected file paths -> source URLs from URL list."""
    expected = {}
    for u in all_urls:
        subfolder = u["subfolder"]
        filename = url_to_filename(u["url"], u["title"])
        rel_path = str(Path("01_Markdown") / "oracle" / subfolder / filename)
        expected[rel_path] = u["url"]
    return expected


def find_orphaned_files(expected_files: dict[str, str], fetch_log: dict) -> list[tuple[str, str]]:
    """Find local oracle/ markdown files that are NOT in the current docs-urls.md.
    Returns list of (rel_path, source_url_or_empty).
    """
    orphans = []

    # All files tracked in fetch_log
    log_files = {}
    for url, info in fetch_log.items():
        if info.get("file"):
            log_files[info["file"]] = url

    # Scan oracle/ directory for all .md files
    for md_file in ORACLE_DIR.rglob("*.md"):
        rel_path = str(md_file.relative_to(BASE_DIR))
        if rel_path not in expected_files:
            source_url = log_files.get(rel_path, "")
            orphans.append((rel_path, source_url))

    return orphans


def cmd_sync(args, all_urls: list[dict]):
    """Sync mode: fetch new URLs, detect orphaned files, optionally delete + reindex."""
    fetch_log = load_fetch_log()
    expected_files = get_expected_files(all_urls)
    current_urls = {u["url"] for u in all_urls}

    # --- 1. Detect new URLs (in docs-urls.md but not yet fetched) ---
    new_urls = [u for u in all_urls if u["url"] not in fetch_log
                or not (BASE_DIR / expected_files.get(
                    str(Path("oracle") / u["subfolder"] / url_to_filename(u["url"], u["title"])), "x"
                )).exists()]
    # Simpler: just check fetch_log + file existence
    new_urls = []
    for u in all_urls:
        subfolder = u["subfolder"]
        filename = url_to_filename(u["url"], u["title"])
        dest_path = ORACLE_DIR / subfolder / filename
        if u["url"] not in fetch_log or not dest_path.exists():
            new_urls.append(u)

    # --- 2. Detect orphaned files (local files whose URL was removed from docs-urls.md) ---
    orphans = find_orphaned_files(expected_files, fetch_log)

    # --- 3. Detect stale log entries (URLs in fetch_log but removed from docs-urls.md) ---
    stale_log_urls = [url for url in fetch_log if url not in current_urls]

    # --- Report ---
    print(f"\n{'='*50}")
    print(f"SYNC REPORT")
    print(f"{'='*50}")
    print(f"URLs in docs-urls.md:  {len(all_urls)}")
    print(f"URLs in fetch log:       {len(fetch_log)}")
    print(f"New (to fetch):          {len(new_urls)}")
    print(f"Orphaned files:          {len(orphans)}")
    print(f"Stale log entries:       {len(stale_log_urls)}")

    if new_urls:
        print(f"\n--- New URLs to fetch ({len(new_urls)}) ---")
        for u in new_urls:
            print(f"  [NEW] {u['subfolder']}/{url_to_filename(u['url'], u['title'])} <- {u['url']}")

    if orphans:
        print(f"\n--- Orphaned files to delete ({len(orphans)}) ---")
        for rel_path, source_url in orphans:
            note = f" (was: {source_url})" if source_url else ""
            print(f"  [ORPHAN] {rel_path}{note}")

    if stale_log_urls:
        print(f"\n--- Stale log entries to clean ({len(stale_log_urls)}) ---")
        for url in stale_log_urls:
            info = fetch_log[url]
            print(f"  [STALE] {info.get('file', '?')} <- {url}")

    if not new_urls and not orphans and not stale_log_urls:
        print(f"\nEverything is in sync. Nothing to do.")
        return

    # --- Dry run stops here ---
    if args.dry_run:
        print(f"\n[DRY RUN] No changes made. Run without --dry-run to apply.")
        return

    # --- Confirm ---
    changes = []
    if new_urls:
        changes.append(f"fetch {len(new_urls)} new")
    if orphans:
        changes.append(f"delete {len(orphans)} orphaned")
    if stale_log_urls:
        changes.append(f"clean {len(stale_log_urls)} stale log entries")

    print(f"\nWill: {', '.join(changes)}")
    confirm = input("Proceed? [y/N] ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        return

    # --- Apply: delete orphans ---
    deleted = 0
    if orphans:
        for rel_path, source_url in orphans:
            full_path = BASE_DIR / rel_path
            if full_path.exists():
                full_path.unlink()
                deleted += 1
                print(f"  [DELETED] {rel_path}")
        # Clean empty directories
        for d in sorted(ORACLE_DIR.rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
                print(f"  [RMDIR] {d.relative_to(BASE_DIR)}")

    # --- Apply: clean stale log entries ---
    cleaned = 0
    for url in stale_log_urls:
        # Also delete the file if it still exists
        info = fetch_log[url]
        file_path = BASE_DIR / info.get("file", "")
        if file_path.exists():
            file_path.unlink()
            deleted += 1
            print(f"  [DELETED] {info['file']}")
        del fetch_log[url]
        cleaned += 1
    if cleaned:
        save_fetch_log(fetch_log)

    # --- Apply: fetch new URLs ---
    fetched = 0
    failed = 0
    if new_urls:
        global _global_fetched_pages
        _global_fetched_pages = set()

        print(f"\nFetching {len(new_urls)} new URLs...")
        for i, entry in enumerate(new_urls):
            url = entry["url"]
            title = entry["title"]
            subfolder = entry["subfolder"]
            filename = url_to_filename(url, title)
            dest_dir = ORACLE_DIR / subfolder
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / filename

            print(f"  [{i+1}/{len(new_urls)}] Fetching: {title[:60]}...")
            print(f"           URL: {url}")

            content, success, page_count = fetch_and_convert(url, title)

            if success:
                frontmatter = build_frontmatter(title, url, subfolder)
                dest_path.write_text(frontmatter + content, encoding="utf-8")
                fetch_log[url] = {
                    "file": str(dest_path.relative_to(BASE_DIR)),
                    "fetched": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "title": title,
                    "pages": page_count,
                    "success": True,
                }
                fetched += 1
                pages_note = f" ({page_count} pages)" if page_count > 1 else ""
                print(f"           Saved: {dest_path.relative_to(BASE_DIR)} ({len(content)} chars){pages_note}")
            else:
                fetch_log[url] = {
                    "file": str(dest_path.relative_to(BASE_DIR)),
                    "fetched": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "title": title,
                    "success": False,
                }
                failed += 1
                print(f"           FAILED")

            if (i + 1) % 10 == 0:
                save_fetch_log(fetch_log)
            time.sleep(DELAY_BETWEEN_REQUESTS)

        save_fetch_log(fetch_log)

    # --- Summary ---
    print(f"\n{'='*50}")
    print(f"SYNC COMPLETE")
    print(f"{'='*50}")
    if fetched or failed:
        print(f"Fetched:          {fetched}")
        print(f"Fetch failed:     {failed}")
    if deleted:
        print(f"Files deleted:    {deleted}")
    if cleaned:
        print(f"Log entries cleaned: {cleaned}")

    needs_reindex = fetched > 0 or deleted > 0
    if needs_reindex:
        print(f"\n[TIP] Local files changed. Rebuild Qdrant index:")
        print(f"  python3 {Path(__file__).parent / 'tech_qdrant_ingest.py'} --rebuild")


def main():
    parser = argparse.ArgumentParser(description="Fetch Oracle docs from docs-urls.md")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be fetched/deleted")
    parser.add_argument("--force", action="store_true", help="Re-fetch all, overwrite existing")
    parser.add_argument("--sync", action="store_true",
                        help="Sync mode: fetch new, delete orphaned, clean stale log entries")
    parser.add_argument("--limit", type=int, default=0, help="Fetch only first N URLs")
    parser.add_argument("--filter", type=str, default="", help="Only fetch URLs matching pattern")
    parser.add_argument("--skip-non-docs", action="store_true", default=True,
                        help="Skip non-docs.oracle.com URLs (default: true)")
    args = parser.parse_args()

    if not ORACLE_URLS_FILE.exists():
        print(f"[FATAL] {ORACLE_URLS_FILE} not found")
        sys.exit(1)

    # Extract URLs
    all_urls = extract_urls_from_markdown(ORACLE_URLS_FILE)
    print(f"Found {len(all_urls)} unique URLs in docs-urls.md")

    # Filter
    if args.filter:
        all_urls = [u for u in all_urls if args.filter.lower() in u["url"].lower()
                    or args.filter.lower() in u["subfolder"].lower()]
        print(f"After filter '{args.filter}': {len(all_urls)} URLs")

    if args.skip_non_docs:
        fetchable = [u for u in all_urls if "docs.oracle.com" in u["url"]
                     or u["url"].endswith(".pdf")]
        skipped_non_docs = len(all_urls) - len(fetchable)
        if skipped_non_docs:
            print(f"Skipping {skipped_non_docs} non-docs URLs (training, downloads, etc.)")
        all_urls = fetchable

    # --- Sync mode ---
    if args.sync:
        cmd_sync(args, all_urls)
        return

    if args.limit > 0:
        all_urls = all_urls[:args.limit]
        print(f"Limited to first {args.limit} URLs")

    # Reset global sub-page dedup tracker
    global _global_fetched_pages
    _global_fetched_pages = set()

    # Load fetch log
    fetch_log = load_fetch_log()

    # Summary by subfolder
    by_folder = {}
    for u in all_urls:
        by_folder.setdefault(u["subfolder"], []).append(u)
    print(f"\nURL distribution:")
    for folder, urls in sorted(by_folder.items()):
        print(f"  {folder}: {len(urls)}")

    if args.dry_run:
        print(f"\n--- Dry run: would fetch {len(all_urls)} URLs ---")
        for u in all_urls:
            status = "EXISTS" if u["url"] in fetch_log else "NEW"
            print(f"  [{status}] {u['subfolder']}/{url_to_filename(u['url'], u['title'])} <- {u['url']}")
        return

    # Fetch
    print(f"\nFetching {len(all_urls)} URLs...")
    fetched = 0
    skipped = 0
    failed = 0
    t_start = time.time()

    for i, entry in enumerate(all_urls):
        url = entry["url"]
        title = entry["title"]
        subfolder = entry["subfolder"]
        filename = url_to_filename(url, title)
        dest_dir = ORACLE_DIR / subfolder
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path = dest_dir / filename

        # Skip if already fetched (unless --force)
        if not args.force and url in fetch_log and dest_path.exists():
            skipped += 1
            continue

        print(f"  [{i+1}/{len(all_urls)}] Fetching: {title[:60]}...")
        print(f"           URL: {url}")

        content, success, page_count = fetch_and_convert(url, title)

        if success:
            frontmatter = build_frontmatter(title, url, subfolder)
            dest_path.write_text(frontmatter + content, encoding="utf-8")
            fetch_log[url] = {
                "file": str(dest_path.relative_to(BASE_DIR)),
                "fetched": time.strftime("%Y-%m-%d %H:%M:%S"),
                "title": title,
                "pages": page_count,
                "success": True,
            }
            fetched += 1
            pages_note = f" ({page_count} pages)" if page_count > 1 else ""
            print(f"           Saved: {dest_path.relative_to(BASE_DIR)} ({len(content)} chars){pages_note}")
        else:
            fetch_log[url] = {
                "file": str(dest_path.relative_to(BASE_DIR)),
                "fetched": time.strftime("%Y-%m-%d %H:%M:%S"),
                "title": title,
                "success": False,
            }
            failed += 1
            print(f"           FAILED")

        # Save log periodically
        if (i + 1) % 10 == 0:
            save_fetch_log(fetch_log)

        # Rate limiting
        time.sleep(DELAY_BETWEEN_REQUESTS)

    save_fetch_log(fetch_log)

    elapsed = time.time() - t_start
    print(f"\n{'='*50}")
    print(f"Fetched:  {fetched}")
    print(f"Skipped:  {skipped} (already exists)")
    print(f"Failed:   {failed}")
    print(f"Sub-pages fetched (global): {len(_global_fetched_pages)}")
    print(f"Time:     {elapsed:.0f}s")


if __name__ == "__main__":
    main()
