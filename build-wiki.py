#!/usr/bin/env python3
"""
Static HTML wiki generator for gb-wiki.
Converts markdown wiki pages into a Wikipedia-style static HTML site.
No external dependencies beyond Python stdlib + PyYAML.
"""

import os
import re
import yaml
import html
import shutil
from datetime import datetime
from pathlib import Path

WIKI_DIR = Path(__file__).parent / "wiki"
OUTPUT_DIR = Path(__file__).parent / "outputs" / "exports" / "html-wiki"
SITE_TITLE = "GB-Wiki"
SITE_SUBTITLE = "AI & Data Engineering Knowledge Base"


# ---------------------------------------------------------------------------
# Markdown-to-HTML converter (no external deps)
# ---------------------------------------------------------------------------

_current_page_prefix = ""

def md_to_html(text, page_prefix=""):
    global _current_page_prefix
    _current_page_prefix = page_prefix
    lines = text.split("\n")
    out = []
    in_ul = False
    in_ol = False
    in_code = False
    code_buf = []
    in_table = False
    table_buf = []
    in_blockquote = False
    bq_buf = []
    i = 0

    def flush_list(out, in_ul, in_ol):
        if in_ul:
            out.append("</ul>")
        if in_ol:
            out.append("</ol>")
        return False, False

    def flush_table(out, table_buf):
        if not table_buf:
            return
        out.append('<table class="wiki-table">')
        for ri, row in enumerate(table_buf):
            out.append("<tr>")
            tag = "th" if ri == 0 else "td"
            for cell in row:
                out.append(f"<{tag}>{inline(cell.strip())}</{tag}>")
            out.append("</tr>")
        out.append("</table>")

    def flush_bq(out, bq_buf):
        if bq_buf:
            out.append('<blockquote class="wiki-quote">')
            out.append(md_to_html("\n".join(bq_buf)))
            out.append("</blockquote>")

    while i < len(lines):
        line = lines[i]

        # Fenced code blocks
        if line.strip().startswith("```"):
            if in_code:
                out.append(html.escape("\n".join(code_buf)))
                out.append("</code></pre>")
                code_buf = []
                in_code = False
                i += 1
                continue
            else:
                if in_ul or in_ol:
                    in_ul, in_ol = flush_list(out, in_ul, in_ol)
                if in_table:
                    flush_table(out, table_buf)
                    table_buf = []
                    in_table = False
                lang = line.strip()[3:].strip()
                cls = f' class="language-{html.escape(lang)}"' if lang else ""
                out.append(f"<pre><code{cls}>")
                in_code = True
                i += 1
                continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Blockquotes
        if line.startswith("> ") or line == ">":
            if not in_blockquote:
                if in_ul or in_ol:
                    in_ul, in_ol = flush_list(out, in_ul, in_ol)
                if in_table:
                    flush_table(out, table_buf)
                    table_buf = []
                    in_table = False
                in_blockquote = True
            bq_buf.append(line[2:] if line.startswith("> ") else "")
            i += 1
            continue
        elif in_blockquote:
            flush_bq(out, bq_buf)
            bq_buf = []
            in_blockquote = False

        # Tables
        if "|" in line and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.match(r"^[-:]+$", c) for c in cells):
                i += 1
                continue
            if not in_table:
                if in_ul or in_ol:
                    in_ul, in_ol = flush_list(out, in_ul, in_ol)
                in_table = True
            table_buf.append(cells)
            i += 1
            continue
        elif in_table:
            flush_table(out, table_buf)
            table_buf = []
            in_table = False

        # Blank line
        if line.strip() == "":
            if in_ul or in_ol:
                in_ul, in_ol = flush_list(out, in_ul, in_ol)
            i += 1
            continue

        # Headings
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            if in_ul or in_ol:
                in_ul, in_ol = flush_list(out, in_ul, in_ol)
            level = len(m.group(1))
            text = inline(m.group(2))
            slug = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
            out.append(f'<h{level} id="{slug}">{text}</h{level}>')
            i += 1
            continue

        # Unordered list
        m = re.match(r"^(\s*)[-*]\s+(.*)", line)
        if m:
            if in_ol:
                in_ul, in_ol = flush_list(out, in_ul, in_ol)
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(m.group(2))}</li>")
            i += 1
            continue

        # Ordered list
        m = re.match(r"^(\s*)\d+\.\s+(.*)", line)
        if m:
            if in_ul:
                in_ul, in_ol = flush_list(out, in_ul, in_ol)
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline(m.group(2))}</li>")
            i += 1
            continue

        # Close lists if we hit non-list content
        if in_ul or in_ol:
            in_ul, in_ol = flush_list(out, in_ul, in_ol)

        # Horizontal rule
        if re.match(r"^[-*_]{3,}\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # Paragraph
        out.append(f"<p>{inline(line)}</p>")
        i += 1

    # Flush remaining state
    if in_ul or in_ol:
        flush_list(out, in_ul, in_ol)
    if in_code:
        out.append(html.escape("\n".join(code_buf)))
        out.append("</code></pre>")
    if in_table:
        flush_table(out, table_buf)
    if in_blockquote:
        flush_bq(out, bq_buf)

    return "\n".join(out)


def inline(text):
    t = html.escape(text)
    # Code spans
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    # Bold + italic
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", t)
    # Bold
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    # Italic
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    # Wikilinks with display text [[target|display]]
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", wikilink_replace, t)
    # Wikilinks [[target]]
    t = re.sub(r"\[\[([^\]]+)\]\]", wikilink_replace, t)
    # Standard markdown links [text](url)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def wikilink_replace(m):
    if m.lastindex == 2:
        target = m.group(1)
        display = m.group(2)
    else:
        target = m.group(1)
        parts = target.split("/")
        display = parts[-1].replace("-", " ").title()
    href = target.rstrip("/")
    if not href.endswith(".html"):
        href = href + ".html"
    href = _current_page_prefix + href
    return f'<a href="{href}" class="wikilink">{display}</a>'


# ---------------------------------------------------------------------------
# Page parsing
# ---------------------------------------------------------------------------

def parse_page(filepath):
    text = filepath.read_text(encoding="utf-8")
    fm = {}
    body = text

    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                fm = {}
            body = parts[2].strip()

    # Strip the H1 title if it duplicates frontmatter title
    body = re.sub(r"^#\s+.*\n?", "", body, count=1)

    rel = filepath.relative_to(WIKI_DIR)
    key = str(rel.with_suffix(""))  # e.g. "concepts/rag"

    return {
        "key": key,
        "path": filepath,
        "frontmatter": fm,
        "body": body,
        "title": fm.get("title", key.split("/")[-1].replace("-", " ").title()),
        "type": fm.get("type", "unknown"),
        "tags": fm.get("tags", []),
        "category": fm.get("category", ""),
        "sources": fm.get("sources", []),
        "last_updated": str(fm.get("last_updated", "")),
    }


# ---------------------------------------------------------------------------
# HTML templates
# ---------------------------------------------------------------------------

def css():
    return """
:root {
    --bg: #f6f6f6;
    --sidebar-bg: #f0f0f0;
    --sidebar-border: #c8ccd1;
    --content-bg: #ffffff;
    --header-bg: #ffffff;
    --header-border: #a7d7f9;
    --link: #0645ad;
    --link-visited: #0b0080;
    --text: #202122;
    --text-muted: #54595d;
    --accent: #3366cc;
    --border: #a2a9b1;
    --section-bg: #f8f9fa;
    --tag-bg: #eaf3ff;
    --tag-border: #a7d7f9;
    --featured-bg: #f6fff6;
    --featured-border: #69a569;
    --recent-bg: #f0f6ff;
    --recent-border: #a7c1f2;
    --code-bg: #f8f9fa;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: "Linux Libertine", "Georgia", "Times", serif;
    font-size: 14px;
    line-height: 1.6;
    color: var(--text);
    background: var(--bg);
}

a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }
a:visited { color: var(--link-visited); }

.site-header {
    background: var(--header-bg);
    border-bottom: 3px solid var(--header-border);
    padding: 8px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.site-header .logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.site-header .logo-icon {
    width: 40px;
    height: 40px;
    background: #e0e0e0;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: bold;
    color: #555;
    font-family: sans-serif;
}

.site-header h1 {
    font-size: 18px;
    font-weight: normal;
    font-variant: small-caps;
    letter-spacing: 1px;
}

.site-header .subtitle {
    font-size: 11px;
    color: var(--text-muted);
}

.search-box {
    display: flex;
    gap: 4px;
}

.search-box input {
    padding: 4px 8px;
    border: 1px solid var(--border);
    border-radius: 2px;
    font-size: 13px;
    width: 220px;
    font-family: sans-serif;
}

.search-box button {
    padding: 4px 12px;
    background: #f8f9fa;
    border: 1px solid var(--border);
    border-radius: 2px;
    cursor: pointer;
    font-size: 13px;
    font-family: sans-serif;
}

.tabs {
    background: var(--content-bg);
    border-bottom: 1px solid var(--border);
    padding: 0 20px;
    display: flex;
    gap: 0;
}

.tabs a {
    display: inline-block;
    padding: 6px 16px;
    font-size: 13px;
    border: 1px solid transparent;
    border-bottom: none;
    color: var(--link);
    font-family: sans-serif;
}

.tabs a.active {
    background: var(--content-bg);
    border-color: var(--border);
    border-bottom: 1px solid var(--content-bg);
    margin-bottom: -1px;
    font-weight: bold;
    color: var(--text);
}

.layout {
    display: flex;
    max-width: 1400px;
    margin: 0 auto;
}

.sidebar {
    width: 220px;
    min-width: 220px;
    background: var(--sidebar-bg);
    border-right: 1px solid var(--sidebar-border);
    padding: 12px;
    font-size: 12.5px;
    font-family: sans-serif;
    overflow-y: auto;
    max-height: calc(100vh - 80px);
    position: sticky;
    top: 0;
}

.sidebar h3 {
    font-size: 12px;
    text-transform: uppercase;
    color: var(--text-muted);
    border-bottom: 1px solid var(--sidebar-border);
    padding-bottom: 4px;
    margin-top: 14px;
    margin-bottom: 6px;
    letter-spacing: 0.5px;
}

.sidebar h3:first-child { margin-top: 0; }

.sidebar ul {
    list-style: none;
    margin-bottom: 4px;
}

.sidebar li {
    padding: 1px 0;
}

.sidebar a {
    color: var(--link);
    font-size: 12.5px;
}

.main-content {
    flex: 1;
    min-width: 0;
    background: var(--content-bg);
    padding: 20px 24px;
    border-right: 1px solid var(--sidebar-border);
}

.right-sidebar {
    width: 260px;
    min-width: 260px;
    padding: 12px;
    font-size: 12.5px;
    font-family: sans-serif;
}

.right-sidebar .box {
    background: var(--section-bg);
    border: 1px solid var(--border);
    margin-bottom: 12px;
    border-radius: 2px;
}

.right-sidebar .box h3 {
    background: #dde;
    padding: 6px 10px;
    font-size: 13px;
    border-bottom: 1px solid var(--border);
}

.right-sidebar .box-content {
    padding: 8px 10px;
}

.right-sidebar .box-content ul {
    list-style: none;
}

.right-sidebar .box-content li {
    padding: 2px 0;
}

.right-sidebar .box-content li::before {
    content: "\\2022 ";
    color: var(--text-muted);
}

/* Article styles */
.article h1 {
    font-size: 28px;
    font-weight: normal;
    border-bottom: 1px solid var(--border);
    padding-bottom: 4px;
    margin-bottom: 16px;
}

.article h2 {
    font-size: 22px;
    font-weight: normal;
    border-bottom: 1px solid var(--border);
    padding-bottom: 2px;
    margin-top: 24px;
    margin-bottom: 10px;
}

.article h3 {
    font-size: 17px;
    margin-top: 18px;
    margin-bottom: 6px;
}

.article h4 {
    font-size: 15px;
    margin-top: 14px;
    margin-bottom: 4px;
}

.article p { margin-bottom: 10px; }

.article ul, .article ol {
    margin: 8px 0 8px 24px;
}

.article li { margin-bottom: 4px; }

.article pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    padding: 12px;
    overflow-x: auto;
    font-size: 13px;
    margin: 10px 0;
    border-radius: 2px;
}

.article code {
    font-family: "Menlo", "Consolas", monospace;
    font-size: 13px;
}

.article p code, .article li code {
    background: var(--code-bg);
    padding: 1px 4px;
    border-radius: 2px;
}

.article .wiki-table {
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 13px;
    width: 100%;
}

.article .wiki-table th, .article .wiki-table td {
    border: 1px solid var(--border);
    padding: 6px 10px;
    text-align: left;
}

.article .wiki-table th {
    background: var(--section-bg);
    font-weight: bold;
}

.article blockquote {
    border-left: 3px solid var(--border);
    padding: 4px 12px;
    margin: 10px 0;
    color: var(--text-muted);
}

.article hr {
    border: none;
    border-top: 1px solid var(--border);
    margin: 20px 0;
}

.page-meta {
    background: var(--section-bg);
    border: 1px solid var(--border);
    padding: 10px 14px;
    margin-bottom: 16px;
    font-size: 12.5px;
    font-family: sans-serif;
    border-radius: 2px;
}

.page-meta .meta-type {
    font-weight: bold;
    text-transform: capitalize;
    color: var(--accent);
}

.page-meta .tags {
    margin-top: 4px;
}

.tag {
    display: inline-block;
    background: var(--tag-bg);
    border: 1px solid var(--tag-border);
    padding: 1px 8px;
    border-radius: 10px;
    font-size: 11px;
    margin: 2px 2px;
    color: var(--accent);
    font-family: sans-serif;
}

/* Home page specific */
.welcome-banner {
    text-align: center;
    padding: 20px 0 16px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 20px;
}

.welcome-banner h1 {
    border: none;
    font-size: 28px;
    margin-bottom: 4px;
}

.welcome-banner .stats {
    color: var(--text-muted);
    font-size: 14px;
    font-family: sans-serif;
}

.featured-box {
    background: var(--featured-bg);
    border: 1px solid var(--featured-border);
    padding: 16px;
    margin-bottom: 20px;
    border-radius: 2px;
}

.featured-box h2 {
    font-size: 18px;
    border-bottom: 1px solid var(--featured-border);
    padding-bottom: 4px;
    margin-bottom: 10px;
    margin-top: 0;
}

.browse-section {
    background: var(--section-bg);
    border: 1px solid var(--border);
    padding: 16px;
    margin-bottom: 20px;
    border-radius: 2px;
}

.browse-section h2 {
    font-size: 18px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 4px;
    margin-bottom: 12px;
    margin-top: 0;
}

.browse-section h3 {
    font-size: 15px;
    margin-top: 14px;
    margin-bottom: 6px;
}

.browse-section ul { list-style: disc; margin-left: 20px; }
.browse-section li { margin-bottom: 3px; font-size: 13px; font-family: sans-serif; }

.search-results {
    display: none;
    background: white;
    border: 1px solid var(--border);
    max-height: 400px;
    overflow-y: auto;
    position: absolute;
    width: 300px;
    z-index: 100;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.search-results a {
    display: block;
    padding: 6px 10px;
    border-bottom: 1px solid #eee;
    font-size: 13px;
    font-family: sans-serif;
}

.search-results a:hover { background: var(--tag-bg); }

.search-container { position: relative; }

@media (max-width: 1000px) {
    .right-sidebar { display: none; }
}

@media (max-width: 750px) {
    .sidebar { display: none; }
    .layout { flex-direction: column; }
}
"""


def search_js(pages):
    items = []
    for p in pages:
        items.append({
            "t": p["title"],
            "k": p["key"],
            "type": p["type"],
            "tags": " ".join(p["tags"]),
        })
    import json
    return """
var PAGES = """ + json.dumps(items) + """;
function initSearch() {
    var input = document.getElementById('search-input');
    var results = document.getElementById('search-results');
    if (!input) return;
    input.addEventListener('input', function() {
        var q = this.value.toLowerCase().trim();
        if (q.length < 2) { results.style.display = 'none'; return; }
        var matches = PAGES.filter(function(p) {
            return p.t.toLowerCase().indexOf(q) !== -1 ||
                   p.k.toLowerCase().indexOf(q) !== -1 ||
                   p.tags.toLowerCase().indexOf(q) !== -1;
        }).slice(0, 15);
        if (matches.length === 0) { results.style.display = 'none'; return; }
        var prefix = '';
        if (window.location.pathname.indexOf('/sources/') !== -1 ||
            window.location.pathname.indexOf('/entities/') !== -1 ||
            window.location.pathname.indexOf('/concepts/') !== -1 ||
            window.location.pathname.indexOf('/comparisons/') !== -1 ||
            window.location.pathname.indexOf('/meta/') !== -1) {
            prefix = '../';
        }
        results.innerHTML = matches.map(function(p) {
            return '<a href="' + prefix + p.k + '.html">' + p.t +
                   ' <small style="color:#888">(' + p.type + ')</small></a>';
        }).join('');
        results.style.display = 'block';
    });
    document.addEventListener('click', function(e) {
        if (!results.contains(e.target) && e.target !== input) {
            results.style.display = 'none';
        }
    });
}
document.addEventListener('DOMContentLoaded', initSearch);
"""


def page_header(prefix=""):
    return f"""<div class="site-header">
    <div class="logo">
        <div class="logo-icon">G</div>
        <div>
            <h1>{SITE_TITLE}</h1>
            <div class="subtitle">{SITE_SUBTITLE}</div>
        </div>
    </div>
    <div class="search-container">
        <div class="search-box">
            <input type="text" id="search-input" placeholder="Search wiki...">
        </div>
        <div class="search-results" id="search-results"></div>
    </div>
</div>
<div class="tabs">
    <a href="{prefix}index.html" class="active">Article</a>
    <a href="{prefix}all-tags.html">Tags</a>
</div>"""


def sidebar_html(pages, prefix=""):
    sections = {
        "Navigation": [
            ("Main page", f"{prefix}index.html"),
            ("All pages", f"{prefix}all-pages.html"),
            ("All tags", f"{prefix}all-tags.html"),
        ],
    }

    cats = {}
    for p in pages:
        t = p["type"]
        label = t.capitalize() + ("s" if t != "meta" else "")
        if label not in cats:
            cats[label] = []
        cats[label].append((p["title"], f"{prefix}{p['key']}.html"))

    h = ['<div class="sidebar">']
    for sec, links in sections.items():
        h.append(f"<h3>{sec}</h3><ul>")
        for title, href in links:
            h.append(f'<li><a href="{href}">{title}</a></li>')
        h.append("</ul>")

    for cat in ["Sources", "Entities", "Concepts", "Comparisons", "Meta"]:
        if cat in cats:
            links = sorted(cats[cat], key=lambda x: x[0])
            h.append(f"<h3>{cat} ({len(links)})</h3><ul>")
            for title, href in links[:30]:
                short = title if len(title) < 35 else title[:32] + "..."
                h.append(f'<li><a href="{href}">{html.escape(short)}</a></li>')
            if len(links) > 30:
                h.append(f'<li><a href="{prefix}all-pages.html">...and {len(links)-30} more</a></li>')
            h.append("</ul>")
    h.append("</div>")
    return "\n".join(h)


def right_sidebar_html(pages, prefix=""):
    recent = sorted(
        [p for p in pages if p["last_updated"]],
        key=lambda p: p["last_updated"],
        reverse=True,
    )[:8]

    tag_counts = {}
    for p in pages:
        for t in p["tags"]:
            tag_counts[t] = tag_counts.get(t, 0) + 1
    top_tags = sorted(tag_counts.items(), key=lambda x: -x[1])[:12]

    total = len(pages)
    type_counts = {}
    for p in pages:
        type_counts[p["type"]] = type_counts.get(p["type"], 0) + 1

    h = ['<div class="right-sidebar">']

    # Stats box
    h.append('<div class="box"><h3>About</h3><div class="box-content">')
    h.append(f"<p>{SITE_TITLE} is a knowledge base covering AI engineering, data engineering, and related topics.</p>")
    h.append(f"<p><strong>{total}</strong> articles: ")
    parts = []
    for t in ["source", "entity", "concept", "comparison", "meta"]:
        if t in type_counts:
            parts.append(f"{type_counts[t]} {t}s" if t != "meta" else f"{type_counts[t]} meta")
    h.append(", ".join(parts) + ".</p>")
    h.append("</div></div>")

    # Recently updated
    h.append('<div class="box"><h3>Recently Updated</h3><div class="box-content"><ul>')
    for p in recent:
        h.append(f'<li><a href="{prefix}{p["key"]}.html">{html.escape(p["title"])}</a> '
                 f'<small style="color:#888">({p["last_updated"]})</small></li>')
    h.append("</ul></div></div>")

    # Top tags
    h.append('<div class="box"><h3>Top Tags</h3><div class="box-content">')
    for tag, count in top_tags:
        h.append(f'<a href="{prefix}all-tags.html#{tag}" class="tag">{tag} ({count})</a> ')
    h.append("</div></div>")

    h.append("</div>")
    return "\n".join(h)


def wrap_page(title, body_html, pages, prefix="", page_data=None):
    meta_html = ""
    if page_data and page_data["type"] not in ("index", "unknown"):
        meta_html = '<div class="page-meta">'
        meta_html += f'<span class="meta-type">{page_data["type"]}</span>'
        if page_data.get("category"):
            meta_html += f' &mdash; {page_data["category"]}'
        if page_data["last_updated"]:
            meta_html += f' &middot; Updated: {page_data["last_updated"]}'
        if page_data["tags"]:
            meta_html += '<div class="tags">' + "".join(
                f'<span class="tag">{t}</span>' for t in page_data["tags"]
            ) + "</div>"
        meta_html += "</div>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)} - {SITE_TITLE}</title>
    <link rel="stylesheet" href="{prefix}style.css">
    <script src="{prefix}search.js"></script>
</head>
<body>
{page_header(prefix)}
<div class="layout">
{sidebar_html(pages, prefix)}
<div class="main-content">
<div class="article">
{meta_html}
<h1>{html.escape(title)}</h1>
{body_html}
</div>
</div>
{right_sidebar_html(pages, prefix)}
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------

def build_home(pages):
    total = len(pages)
    type_counts = {}
    for p in pages:
        type_counts[p["type"]] = type_counts.get(p["type"], 0) + 1

    tag_counts = {}
    for p in pages:
        for t in p["tags"]:
            tag_counts[t] = tag_counts.get(t, 0) + 1

    # Pick a featured article (largest concept page)
    concepts = [p for p in pages if p["type"] == "concept"]
    featured = max(concepts, key=lambda p: len(p["body"])) if concepts else None

    h = []
    h.append('<div class="welcome-banner">')
    h.append(f"<h1>Welcome to {SITE_TITLE}</h1>")
    h.append(f"<p>{SITE_SUBTITLE}</p>")
    h.append(f'<p class="stats">{total} articles across {len(tag_counts)} tags</p>')
    h.append("</div>")

    if featured:
        h.append('<div class="featured-box">')
        h.append("<h2>Featured Article</h2>")
        excerpt = featured["body"][:400].rsplit(" ", 1)[0] + "..."
        h.append(f'<p><a href="{featured["key"]}.html"><strong>{html.escape(featured["title"])}</strong></a>'
                 f' ({featured["type"]}) &mdash; {html.escape(excerpt)}</p>')
        h.append(f'<p><a href="{featured["key"]}.html">Read more &rarr;</a></p>')
        h.append("</div>")

    h.append('<div class="browse-section">')
    h.append("<h2>Browse by Category</h2>")

    for cat_type, cat_label in [("entity", "Entities"), ("concept", "Concepts"),
                                 ("source", "Sources"), ("comparison", "Comparisons"),
                                 ("meta", "Meta")]:
        cat_pages = sorted([p for p in pages if p["type"] == cat_type], key=lambda p: p["title"])
        if cat_pages:
            h.append(f"<h3>{cat_label} ({len(cat_pages)})</h3><ul>")
            for p in cat_pages:
                h.append(f'<li><a href="{p["key"]}.html">{html.escape(p["title"])}</a>'
                         f' &mdash; {p["type"]}</li>')
            h.append("</ul>")

    h.append("</div>")

    body = "\n".join(h)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{SITE_TITLE} - {SITE_SUBTITLE}</title>
    <link rel="stylesheet" href="style.css">
    <script src="search.js"></script>
</head>
<body>
{page_header()}
<div class="layout">
{sidebar_html(pages)}
<div class="main-content">
{body}
</div>
{right_sidebar_html(pages)}
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# All pages & tags listing
# ---------------------------------------------------------------------------

def build_all_pages(pages):
    sorted_pages = sorted(pages, key=lambda p: p["title"].lower())
    h = ["<ul>"]
    for p in sorted_pages:
        tags_str = ", ".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        h.append(f'<li><a href="{p["key"]}.html">{html.escape(p["title"])}</a>'
                 f' <small>({p["type"]})</small> {tags_str}</li>')
    h.append("</ul>")
    return wrap_page("All Pages", "\n".join(h), pages)


def build_all_tags(pages):
    tag_map = {}
    for p in pages:
        for t in p["tags"]:
            if t not in tag_map:
                tag_map[t] = []
            tag_map[t].append(p)

    h = ['<p style="font-family:sans-serif;font-size:13px">']
    for tag in sorted(tag_map.keys()):
        h.append(f'<a href="#{tag}" class="tag">{tag} ({len(tag_map[tag])})</a> ')
    h.append("</p><hr>")

    for tag in sorted(tag_map.keys()):
        h.append(f'<h2 id="{tag}">{tag} ({len(tag_map[tag])})</h2><ul>')
        for p in sorted(tag_map[tag], key=lambda x: x["title"]):
            h.append(f'<li><a href="{p["key"]}.html">{html.escape(p["title"])}</a>'
                     f' <small>({p["type"]})</small></li>')
        h.append("</ul>")

    return wrap_page("All Tags", "\n".join(h), pages)


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build():
    print(f"Building {SITE_TITLE} static site...")

    # Clean output
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Collect pages (skip index.md and log.md)
    pages = []
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        rel = md_file.relative_to(WIKI_DIR)
        if rel.name in ("index.md", "log.md"):
            continue
        pages.append(parse_page(md_file))

    print(f"  Found {len(pages)} pages")

    # Write CSS
    (OUTPUT_DIR / "style.css").write_text(css(), encoding="utf-8")

    # Write search JS
    (OUTPUT_DIR / "search.js").write_text(search_js(pages), encoding="utf-8")

    # Write individual pages
    for p in pages:
        out_path = OUTPUT_DIR / (p["key"] + ".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # Determine prefix for assets (css/js)
        depth = len(Path(p["key"]).parts) - 1
        prefix = "../" * depth if depth > 0 else ""

        body_html = md_to_html(p["body"], page_prefix=prefix)
        page_html = wrap_page(p["title"], body_html, pages, prefix=prefix, page_data=p)
        out_path.write_text(page_html, encoding="utf-8")

    # Write home page
    (OUTPUT_DIR / "index.html").write_text(build_home(pages), encoding="utf-8")

    # Write all-pages
    (OUTPUT_DIR / "all-pages.html").write_text(build_all_pages(pages), encoding="utf-8")

    # Write all-tags
    (OUTPUT_DIR / "all-tags.html").write_text(build_all_tags(pages), encoding="utf-8")

    print(f"  Generated {len(pages) + 3} HTML files")
    print(f"  Output: {OUTPUT_DIR}")
    print("  Done! Open index.html in a browser to view.")


if __name__ == "__main__":
    build()
