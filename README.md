# gb-wiki

**An LLM-maintained knowledge wiki for AI and Data Engineering.**

gb-wiki is a personal knowledge base where a human curates raw source materials (PDFs, markdown files, HTML pages) and an LLM (Claude Code) reads them, extracts structured knowledge, writes interconnected wiki pages, and generates a browsable Wikipedia-style HTML site — all from the terminal.

```
Human drops a PDF into raw/  →  Claude ingests it  →  Wiki pages appear  →  HTML site rebuilds
```

---

## Table of Contents

- [Why This Project Exists](#why-this-project-exists)
- [What It Looks Like](#what-it-looks-like)
- [Architecture](#architecture)
- [Directory Structure](#directory-structure)
- [How the Wiki Works](#how-the-wiki-works)
  - [Page Types](#page-types)
  - [The Schema (CLAUDE.md)](#the-schema-claudemd)
  - [Frontmatter and Tags](#frontmatter-and-tags)
  - [Wikilinks](#wikilinks)
- [How Ingestion Works](#how-ingestion-works)
  - [Step-by-Step Walkthrough](#step-by-step-walkthrough)
  - [What Happens to a Single PDF](#what-happens-to-a-single-pdf)
  - [Entity and Concept Extraction](#entity-and-concept-extraction)
- [How the HTML Site Generator Works](#how-the-html-site-generator-works)
  - [The Build Pipeline](#the-build-pipeline)
  - [Markdown-to-HTML Conversion](#markdown-to-html-conversion)
  - [Wikilink Resolution](#wikilink-resolution)
  - [Page Layout and Templates](#page-layout-and-templates)
  - [Client-Side Search](#client-side-search)
- [How to Use It](#how-to-use-it)
  - [Adding a New Source](#adding-a-new-source)
  - [Querying the Wiki](#querying-the-wiki)
  - [Building the HTML Site](#building-the-html-site)
  - [Running a Health Check](#running-a-health-check)
- [Design Decisions](#design-decisions)
- [Current Stats](#current-stats)
- [Project Timeline](#project-timeline)
- [Lessons Learned](#lessons-learned)

---

## Why This Project Exists

Learning AI engineering means reading dozens of PDFs, blog posts, papers, and documentation pages. The problem: knowledge stays trapped in those individual files. You forget where you read something, you can't see connections between topics, and you re-read the same ground without building on it.

gb-wiki solves this by turning an LLM into a knowledge librarian:

1. **You collect sources** — drop PDFs, markdown notes, and HTML articles into a folder.
2. **Claude reads and extracts** — it identifies entities (tools, frameworks, companies), concepts (techniques, patterns, architectures), and relationships between them.
3. **Claude writes structured wiki pages** — each entity gets its own page, each concept gets its own page, cross-linked with Obsidian-style wikilinks.
4. **A build script generates a browsable HTML site** — Wikipedia-style layout with sidebar navigation, search, tags, and cross-references.

The result is a personal encyclopedia that grows with every source you add, where knowledge compounds instead of scattering.

---

## What It Looks Like

The HTML site follows a Wikipedia-inspired three-column layout:

- **Left sidebar** — Navigation links and all pages grouped by category (Sources, Entities, Concepts, Comparisons, Meta)
- **Main content** — Article with metadata badge (type, tags, last updated), headings, tables, code blocks, and cross-reference links
- **Right sidebar** — About box with article counts, recently updated pages, and top tags

The home page has a welcome banner with wiki stats, a featured article (auto-selected as the longest concept page), and a browse-by-category listing of every page.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        gb-wiki Architecture                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   raw/                    CLAUDE.md                wiki/        │
│   ├── PDF files           (Schema)                 ├── index.md │
│   ├── Markdown files         │                     ├── log.md   │
│   └── HTML files             │                     ├── sources/ │
│         │                    │                     ├── entities/│
│         │                    ▼                     ├── concepts/│
│         │            ┌──────────────┐              ├── compare/ │
│         └───────────▶│  Claude Code  │─────────────▶└── meta/   │
│                      │  (LLM Agent)  │                    │     │
│                      └──────────────┘                     │     │
│                        reads source,                      │     │
│                        extracts knowledge,                ▼     │
│                        writes pages              ┌─────────────┐│
│                                                  │ build-wiki  ││
│                                                  │   .py       ││
│                                                  └──────┬──────┘│
│                                                         │       │
│                                                         ▼       │
│                                              outputs/exports/   │
│                                              html-wiki/         │
│                                              ├── index.html     │
│                                              ├── style.css      │
│                                              ├── search.js      │
│                                              ├── concepts/*.html│
│                                              ├── entities/*.html│
│                                              └── sources/*.html │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

There are three distinct systems working together:

| Layer | What It Is | Who/What Operates It |
|-------|-----------|---------------------|
| **Raw sources** (`raw/`) | Immutable input — PDFs, markdown, HTML files the human collects | Human (read-only, never modified) |
| **Wiki pages** (`wiki/`) | Structured markdown with YAML frontmatter and wikilinks | Claude Code (reads sources, writes and updates pages) |
| **HTML site** (`outputs/exports/html-wiki/`) | Static Wikipedia-style website generated from wiki pages | Python build script (`build-wiki.py`) |

The key insight: `CLAUDE.md` is the glue. It defines the schema — page types, templates, frontmatter fields, tag taxonomy, naming conventions, and step-by-step workflows. Claude reads this file at the start of every session and follows it like a specification document.

---

## Directory Structure

```
gb-wiki/
│
├── CLAUDE.md                  # The schema — rules, templates, workflows, tag taxonomy
├── README.md                  # This file
├── build-wiki.py              # Static HTML site generator (Python, ~1100 lines)
│
├── raw/                       # Source materials (NEVER modified by Claude)
│   ├── RAG Techniques.pdf     # Example: a PDF about RAG strategies
│   ├── AI Engineer Requirements.md
│   ├── Setting up Evaluations for LLMs.html
│   └── assets/                # Images, diagrams referenced by sources
│
├── wiki/                      # LLM-written markdown pages
│   ├── index.md               # Master catalog — every page listed with summary
│   ├── log.md                 # Append-only operation log (what was ingested when)
│   ├── sources/               # One summary page per ingested raw source
│   │   ├── rag-techniques.md
│   │   └── ai-engineer-requirements.md
│   ├── entities/              # Pages for specific things (tools, companies, etc.)
│   │   ├── langchain.md
│   │   ├── pinecone.md
│   │   └── claude-code.md
│   ├── concepts/              # Pages for ideas, techniques, patterns
│   │   ├── retrieval-augmented-generation.md
│   │   ├── chunking.md
│   │   └── embeddings.md
│   ├── comparisons/           # Side-by-side analysis pages
│   │   └── standard-rag-vs-agentic-rag.md
│   └── meta/                  # Synthesis, overview, gap analysis
│       └── ingestion-plan.md
│
└── outputs/
    └── exports/
        └── html-wiki/         # Generated static HTML site
            ├── index.html     # Home page with stats and browse-by-category
            ├── style.css      # Wikipedia-style CSS
            ├── search.js      # Client-side search across all pages
            ├── all-pages.html # Alphabetical listing of every page
            ├── all-tags.html  # Tag index with per-tag page lists
            ├── concepts/      # One .html per concept
            ├── entities/      # One .html per entity
            ├── sources/       # One .html per source summary
            ├── comparisons/   # One .html per comparison
            └── meta/          # One .html per meta page
```

---

## How the Wiki Works

### Page Types

The wiki uses five page types, each with a defined template and purpose:

| Type | Directory | Purpose | Example |
|------|-----------|---------|---------|
| **Source** | `wiki/sources/` | Summary of one raw file — key points, entities, concepts mentioned | `rag-techniques.md` summarizes a 34-strategy RAG PDF |
| **Entity** | `wiki/entities/` | A specific thing — tool, framework, company, model, protocol | `langchain.md` describes the LangChain framework |
| **Concept** | `wiki/concepts/` | An idea, technique, pattern, or architecture | `chunking.md` explains document splitting strategies |
| **Comparison** | `wiki/comparisons/` | Side-by-side analysis of two related things | `standard-rag-vs-agentic-rag.md` |
| **Meta** | `wiki/meta/` | Synthesis pages — overviews, gap analysis, roadmaps | `ingestion-plan.md` tracks what's left to ingest |

One concept per page. If a page covers two distinct ideas, it gets split. This keeps navigation clean and cross-references precise.

### The Schema (CLAUDE.md)

`CLAUDE.md` is a ~340-line specification file that Claude reads at the start of every session. It defines:

- **Rules** (10 numbered rules): never modify `raw/`, always update the index, use wikilinks, one concept per page, prefer updating over duplicating, cite sources, kebab-case filenames, YAML frontmatter required, tag every page.
- **Templates**: exact frontmatter fields and body section headings for each page type.
- **Tag taxonomy**: ~25 domain tags (`rag`, `agents`, `llm`, `evaluation`, etc.), context tags (`interview-prep`, `certification`), and provider tags (`anthropic`, `openai`, `langchain`).
- **Workflows**: step-by-step procedures for ingestion, querying, batch ingestion, and linting.

This is the core design decision of the project: **the schema is the product**. The wiki pages are just the output of an LLM following a well-designed schema.

### Frontmatter and Tags

Every wiki page starts with YAML frontmatter. Here's a real example from `wiki/concepts/chunking.md`:

```yaml
---
type: concept
title: "Chunking"
aliases: ["document chunking", "text splitting"]
tags: [rag, system-design]
sources: [sources/rag-techniques, sources/rag-end-to-end]
last_updated: 2026-04-15
---
```

Frontmatter serves three purposes:
1. **Type system** — the build script uses `type` to determine how to render and categorize the page.
2. **Source tracking** — `sources` lists which raw files contributed to this page, creating an audit trail.
3. **Discovery** — `tags` enable the tag index page and help the search system.

### Wikilinks

Pages cross-reference each other using Obsidian-style wikilinks:

```markdown
RAG systems use [[concepts/embeddings]] stored in [[entities/pinecone]] or [[entities/chromadb]].
```

The build script converts these to HTML links with correct relative paths. This creates a densely connected knowledge graph — you can navigate from a concept to the tools that implement it, to the sources that discuss it, and back.

---

## How Ingestion Works

### Step-by-Step Walkthrough

When you say "ingest RAG Techniques.pdf" to Claude Code, here's exactly what happens:

```
1. READ the source
   └── Claude reads raw/RAG Techniques.pdf (in 15-20 page chunks for large PDFs)

2. CREATE source summary
   └── wiki/sources/rag-techniques.md
       ├── ## Summary (3-5 sentences)
       ├── ## Key Points (5-15 bullet points)
       ├── ## Entities Mentioned (wikilinks to entity pages)
       ├── ## Concepts Covered (wikilinks to concept pages)
       ├── ## Notable Quotes or Data
       └── ## Related Sources

3. FOR EACH entity substantively discussed
   ├── entities/cohere.md → CREATE (new entity)
   └── entities/langchain.md → UPDATE (add new info + source ref)

4. FOR EACH concept substantively discussed
   ├── concepts/chunking.md → CREATE (new concept)
   ├── concepts/hybrid-search.md → CREATE (new concept)
   └── concepts/retrieval-augmented-generation.md → UPDATE (add new info)

5. CHECK for comparison opportunities
   └── If source compares X vs Y → create comparisons/x-vs-y.md

6. UPDATE wiki/index.md
   └── Add rows for every new page, update summaries for modified pages

7. APPEND to wiki/log.md
   └── Record what was created/updated with page count
```

### What Happens to a Single PDF

Let's trace what happened when `RAG Techniques.pdf` (a 34-strategy guide) was ingested:

**Input**: A PDF covering 34 RAG strategies with pseudocode, from basic to advanced.

**Output**:
- 1 source summary page (`sources/rag-techniques.md`)
- 4 new concept pages (`chunking.md`, `hybrid-search.md`, `graph-rag.md`, `query-refinement.md`)
- 2 new entity pages (`deepeval.md`, `cohere.md`)
- 2 existing concept pages updated (`retrieval-augmented-generation.md`, `agentic-rag.md`)
- **Total: 8 pages touched**

The source summary captures the PDF's key points. But the real value is that the knowledge gets decomposed into reusable atoms — a `chunking` page that now links to every source discussing chunking, an `entities/cohere` page that tracks what Cohere does across all sources.

### Entity and Concept Extraction

Not every mention becomes a page. The schema enforces selectivity:

- **Entities**: only if discussed substantively (at least a paragraph or multiple mentions). A passing mention of "Pinecone" in a list doesn't create `entities/pinecone.md`, but a paragraph comparing Pinecone's architecture does.
- **Concepts**: only if there's enough substance to fill the template (definition, how it works, why it matters). A brief mention gets noted in the source summary but doesn't get its own page.
- **Updates over duplicates**: before creating a new page, Claude checks if one already exists. If it does, the existing page gets updated with new information and a new source reference.

This is what creates compound knowledge — the `retrieval-augmented-generation.md` page has been updated by 8 different sources, each adding depth to different sections.

---

## How the HTML Site Generator Works

`build-wiki.py` is a ~1100-line Python script with zero external dependencies (beyond PyYAML, which ships with most Python installs). It converts the wiki's markdown pages into a static HTML site you can open in any browser.

### The Build Pipeline

```
1. SCAN wiki/ for all .md files (skip index.md and log.md)
      │
2. PARSE each file
      ├── Extract YAML frontmatter (type, title, tags, sources, etc.)
      └── Separate body markdown from frontmatter
      │
3. CONVERT markdown → HTML
      ├── Headings, lists, tables, code blocks, blockquotes
      ├── Inline formatting (bold, italic, code spans)
      └── Resolve [[wikilinks]] to <a href="..."> with correct relative paths
      │
4. WRAP each page in the HTML template
      ├── Site header (logo, search box)
      ├── Tab bar (Article, Tags)
      ├── Left sidebar (navigation + page listings by category)
      ├── Main content (metadata badge + converted HTML)
      └── Right sidebar (About box, Recently Updated, Top Tags)
      │
5. GENERATE special pages
      ├── index.html (home page with stats, featured article, browse-by-category)
      ├── all-pages.html (alphabetical listing)
      └── all-tags.html (tag index)
      │
6. WRITE static assets
      ├── style.css (Wikipedia-style theme)
      └── search.js (client-side search index)
```

### Markdown-to-HTML Conversion

Since external packages can't be installed in all environments, the script includes its own markdown parser. It handles:

- **Block elements**: headings (H1-H6 with anchor IDs), unordered/ordered lists, fenced code blocks with language hints, tables, blockquotes, horizontal rules, paragraphs
- **Inline elements**: bold (`**text**`), italic (`*text*`), code spans (`` `text` ``), standard markdown links (`[text](url)`), and wikilinks (`[[target]]`)

The parser is a single-pass line scanner with state tracking for multi-line constructs (code blocks, tables, blockquotes, lists).

### Wikilink Resolution

Wikilinks are the most important conversion. A wikilink like `[[concepts/embeddings]]` in the source markdown needs to become a working HTML link. The challenge: the correct `href` depends on where the current page lives in the directory tree.

```
From concepts/chunking.html:
  [[concepts/embeddings]]  →  <a href="../concepts/embeddings.html">Embeddings</a>
  [[entities/pinecone]]    →  <a href="../entities/pinecone.html">Pinecone</a>

From index.html (root):
  [[concepts/embeddings]]  →  <a href="concepts/embeddings.html">Embeddings</a>
```

The script tracks a `_current_page_prefix` (e.g., `"../"` for pages one level deep) and prepends it to every resolved wikilink during conversion.

Display text is auto-generated from the target path: `concepts/hybrid-search` becomes "Hybrid Search" (split on `/`, take last segment, replace hyphens with spaces, title-case).

### Page Layout and Templates

Every page gets wrapped in a three-column layout:

```html
<div class="layout">
  <div class="sidebar">          <!-- Left: navigation + category listings -->
  <div class="main-content">     <!-- Center: article content -->
  <div class="right-sidebar">    <!-- Right: About, Recently Updated, Top Tags -->
</div>
```

Article pages include a metadata badge at the top showing the page type, category (for entities), last-updated date, and tags as colored pills. This gives readers instant context about what kind of page they're reading.

The CSS uses CSS custom properties (variables) for theming and follows Wikipedia's color palette — serif body text, blue links, light gray backgrounds, subtle borders.

### Client-Side Search

The build script generates a `search.js` file containing a JSON array of all page titles, keys, types, and tags. The search input in the header filters this array client-side as you type (no server needed):

```javascript
var PAGES = [
  {"t": "Retrieval-Augmented Generation (RAG)", "k": "concepts/retrieval-augmented-generation", "type": "concept", "tags": "rag llm"},
  {"t": "LangChain", "k": "entities/langchain", "type": "entity", "tags": "orchestration rag agents"},
  ...
];
```

Type 2+ characters and a dropdown shows matching pages. It searches across titles, keys, and tags.

---

## How to Use It

### Adding a New Source

```bash
# 1. Drop your file into raw/
cp "My New Paper.pdf" raw/

# 2. Open Claude Code in the project directory
claude

# 3. Tell Claude to ingest it
> ingest My New Paper.pdf

# Claude will:
#   - Read the PDF (in chunks if large)
#   - Create wiki/sources/my-new-paper.md
#   - Create/update entity and concept pages
#   - Update wiki/index.md
#   - Append to wiki/log.md
#   - Report what it created/updated
```

For batch ingestion:
```
> ingest round 6
```
Claude will process all files planned for that round (defined in `wiki/meta/ingestion-plan.md`), updating the index and log once at the end.

### Querying the Wiki

```
> What does the wiki say about chunking strategies?

# Claude reads the index, identifies relevant pages, reads them,
# and synthesizes an answer with [[wikilink]] citations.
```

```
> Compare LangChain and LlamaIndex based on what we've ingested

# Claude reads both entity pages, finds overlapping sources,
# and can create a new comparisons/langchain-vs-llamaindex.md if you ask.
```

### Building the HTML Site

```bash
python3 build-wiki.py

# Output:
# Building GB-Wiki static site...
#   Found 72 pages
#   Generated 75 HTML files
#   Output: outputs/exports/html-wiki
#   Done! Open index.html in a browser to view.

open outputs/exports/html-wiki/index.html
```

Rebuild after any wiki changes. The script clears the output directory and regenerates everything from scratch (takes <1 second for ~70 pages).

### Running a Health Check

```
> lint the wiki

# Claude will check for:
#   - Orphan pages (not in index.md)
#   - Broken wikilinks
#   - Missing cross-references
#   - Stale pages
#   - Tag inconsistencies
#   - Frontmatter validation errors
#   - Source coverage gaps
```

---

## Design Decisions

**Why CLAUDE.md as the schema?**
Claude Code reads `CLAUDE.md` automatically at session start. By putting the entire wiki specification there — templates, rules, workflows, tag taxonomy — every session starts with full context. No separate config files, no database, no build tool configuration. The schema *is* the documentation.

**Why not a database?**
Markdown files in directories are the simplest possible storage. They're human-readable, git-friendly, greppable, and don't require any runtime. The YAML frontmatter gives you structured metadata without leaving the file. The index.md file serves as the "database index" — a single file you can read to find any page.

**Why a custom HTML generator instead of MkDocs/Hugo?**
Three reasons: (1) zero dependency installation — the script runs on Python stdlib + PyYAML, which was already available; (2) full control over the Wikipedia-style layout, which would require significant theme customization in any static site generator; (3) the wiki's structure (frontmatter schema, wikilinks, page types) is specific enough that a 1100-line purpose-built script is simpler than configuring a general-purpose tool.

**Why Obsidian-style wikilinks?**
`[[concepts/chunking]]` is faster to write than `[Chunking](../concepts/chunking.md)` and more readable in raw markdown. It's also compatible with Obsidian if you want to browse the wiki in that tool. The build script handles conversion to HTML links.

**Why one concept per page?**
Dense pages that cover multiple concepts are hard to link to precisely. If "chunking" and "embeddings" are on the same page, a wikilink to that page doesn't tell the reader which concept they're being directed to. Atomic pages make the knowledge graph navigable.

**Why "prefer updating over duplicating"?**
This is what creates compound knowledge. When 8 sources discuss RAG, you don't want 8 separate RAG pages. You want one authoritative page that synthesizes all 8 perspectives, with source citations showing where each fact came from. The `retrieval-augmented-generation.md` page is the richest page in the wiki precisely because it's been updated by 8 different source ingestions.

**Why an append-only log?**
`wiki/log.md` gives you a chronological audit trail. You can see exactly what was ingested when, what pages were created or updated, and how the wiki grew over time. It's also useful for resuming work — check the log to see where you left off.

---

## Current Stats

| Metric | Count |
|--------|-------|
| Raw source files | 32 |
| Sources ingested | 20 |
| Total wiki pages | 72 |
| Source summaries | 20 |
| Entity pages | 20 |
| Concept pages | 30 |
| Comparison pages | 1 |
| Meta pages | 1 |
| HTML pages generated | 75 |
| Ingestion rounds completed | 5 |
| Tags in taxonomy | ~25 |

---

## Project Timeline

| Date | Milestone |
|------|-----------|
| 2026-04-14 | Project bootstrapped — CLAUDE.md schema written, directory structure created |
| 2026-04-14 | Round 1 — first 5 sources ingested (markdown + HTML), 38 wiki pages created |
| 2026-04-15 | Round 2 — 5 RAG PDFs ingested, RAG concept page became richest in wiki |
| 2026-04-20 | Round 3 — LLM core sources (hallucination, nondeterminism, interview prep) |
| 2026-04-21 | Round 4 — Agents & orchestration (agentic AI, SLMs, LangGraph projects) |
| 2026-04-23 | Round 5 — Claude & Anthropic (Claude Code, Agent SDK, context engineering) |
| 2026-05-04 | HTML site generator built — Wikipedia-style static site from wiki content |

---

## Lessons Learned

**Schema-first design pays off.** Writing `CLAUDE.md` before ingesting a single source meant every page follows the same structure from day one. No retroactive cleanup needed. The schema took ~2 hours to write; it saved dozens of hours of inconsistency fixes.

**Chunk large PDFs aggressively.** Reading more than 20 PDF pages at once causes the LLM to lose detail from early pages. The 15-20 page chunking rule with interim notes between passes produces much better extraction.

**Compound pages beat fresh pages.** The most valuable pages in the wiki are the ones updated by many sources. `retrieval-augmented-generation.md` (8 sources) is far more useful than any single source summary. The "prefer updating over duplicating" rule is the most important rule in the schema.

**Tags enable discovery.** Without tags, you'd need to read every page title to find what you're looking for. With 25 domain/context tags, the tag index page becomes a browsable entry point into any topic.

**Wikilinks create serendipity.** When reading about chunking, you see links to hybrid-search, re-ranking, and graph-rag. These connections exist because the schema requires cross-references. In a flat file system, you'd never discover these relationships.

**A custom build script beats a framework for domain-specific sites.** MkDocs can't resolve `[[wikilinks]]` or render page-type metadata badges without plugins. A purpose-built generator does exactly what you need in one file.
