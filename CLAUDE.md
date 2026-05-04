# gb-wiki -- LLM-Maintained Knowledge Wiki

## Identity

This is a **knowledge wiki** maintained by Claude Code. It is NOT a code project.
The human curates raw source materials. Claude reads them, writes wiki pages,
maintains the index, and keeps the knowledge graph healthy.

---

## Directory Layout

```
gb-wiki/
  CLAUDE.md          # This file. The schema. Read it on every session start.
  raw/               # Source materials. NEVER modify. Read-only.
    assets/          # Images, diagrams, cheat sheets referenced by sources.
  wiki/              # LLM-owned markdown pages. Claude writes everything here.
    index.md         # Master catalog of all wiki pages.
    log.md           # Append-only chronological record of operations.
    sources/         # One summary page per ingested raw source.
    entities/        # Pages for specific things (tools, products, companies, people).
    concepts/        # Pages for ideas, techniques, patterns, architectures.
    comparisons/     # Side-by-side analysis pages.
    meta/            # Synthesis, overview, gaps analysis, roadmaps.
  outputs/           # Generated artifacts (presentations, charts, exports).
    presentations/   # Marp markdown slide decks.
    charts/          # Generated diagrams or data visualizations.
    exports/         # PDF/HTML exports of wiki content.
```

---

## Rules

1. **Never modify anything under `raw/`.** Treat it as immutable input.
2. **Always update `wiki/index.md`** when creating, renaming, or deleting a wiki page.
3. **Always append to `wiki/log.md`** after every ingest, query-to-page, or lint operation.
4. **Use Obsidian-style wikilinks** `[[page-name]]` for all cross-references.
5. **One concept per page.** If a page covers two distinct ideas, split it.
6. **Prefer updating over duplicating.** Before creating a new entity/concept page, check if one exists. If it does, update it with new information and note the additional source.
7. **Cite sources.** Every factual claim should link back to a source page via `[[sources/filename]]`.
8. **Use kebab-case filenames.** Example: `vector-databases.md`, `rag-eval-metrics.md`.
9. **Every wiki page must have YAML frontmatter.** See templates below.
10. **Tag every page** with at least one tag from the taxonomy.

---

## Naming Conventions

| Directory       | Pattern                        | Example                              |
|-----------------|--------------------------------|--------------------------------------|
| `sources/`      | Slugified source filename      | `rag-components.md`                  |
| `entities/`     | Entity name, kebab-case        | `langchain.md`, `pinecone.md`        |
| `concepts/`     | Concept name, kebab-case       | `retrieval-augmented-generation.md`  |
| `comparisons/`  | `X-vs-Y.md`                    | `lora-vs-qlora.md`                   |
| `meta/`         | Descriptive, kebab-case        | `knowledge-gaps.md`, `overview.md`   |

---

## Page Types and Templates

### Source Summary (`wiki/sources/`)

Frontmatter:
```yaml
---
type: source
title: "<Human-readable title>"
source_file: "<exact filename in raw/>"
source_type: pdf | md | html
date_ingested: YYYY-MM-DD
tags: [tag1, tag2, tag3]
---
```

Body structure:
- `## Summary` -- 3-5 sentence overview of the source.
- `## Key Points` -- Bulleted list of the most important takeaways (5-15 items).
- `## Entities Mentioned` -- Bulleted list with wikilinks: `- [[entities/langchain]] -- orchestration framework`
- `## Concepts Covered` -- Bulleted list with wikilinks: `- [[concepts/rag]] -- retrieval augmented generation`
- `## Notable Quotes or Data` -- Direct quotes or statistics worth preserving.
- `## Related Sources` -- Wikilinks to other source pages covering overlapping material.

### Entity Page (`wiki/entities/`)

Frontmatter:
```yaml
---
type: entity
title: "<Entity Name>"
category: tool | framework | product | company | person | service | model | protocol
tags: [tag1, tag2]
sources: [sources/file1, sources/file2]
last_updated: YYYY-MM-DD
---
```

Body structure:
- `## What It Is` -- 2-3 sentence definition.
- `## Key Details` -- Bulleted facts, features, or characteristics.
- `## How It Fits In` -- Relationship to other entities/concepts (with wikilinks).
- `## Source References` -- List of source pages that mention this entity.

### Concept Page (`wiki/concepts/`)

Frontmatter:
```yaml
---
type: concept
title: "<Concept Name>"
aliases: ["<alternate names>"]
tags: [tag1, tag2]
sources: [sources/file1, sources/file2]
last_updated: YYYY-MM-DD
---
```

Body structure:
- `## Definition` -- Clear, concise explanation.
- `## How It Works` -- Mechanism, process, or architecture (use sub-headings if complex).
- `## Why It Matters` -- Practical significance, use cases, or business value.
- `## Key Variants or Approaches` -- Sub-types, alternatives, or flavors (if applicable).
- `## Related Concepts` -- Wikilinks to related concept pages.
- `## Related Entities` -- Wikilinks to tools/frameworks that implement this concept.
- `## Source References` -- List of source pages that discuss this concept.

### Comparison Page (`wiki/comparisons/`)

Frontmatter:
```yaml
---
type: comparison
title: "<X vs Y>"
subjects: ["entity-or-concept-1", "entity-or-concept-2"]
tags: [tag1, tag2]
sources: [sources/file1, sources/file2]
last_updated: YYYY-MM-DD
---
```

Body structure:
- `## Overview` -- What is being compared and why.
- `## Comparison Table` -- Markdown table with key dimensions as rows.
- `## Analysis` -- Prose discussion of trade-offs.
- `## When to Use Which` -- Practical decision guidance.
- `## Source References`

### Meta Page (`wiki/meta/`)

Frontmatter:
```yaml
---
type: meta
title: "<Descriptive Title>"
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
---
```

Body structure is flexible. Common meta pages:
- `overview.md` -- High-level map of all knowledge domains in the wiki.
- `knowledge-gaps.md` -- Topics mentioned in sources but not yet covered by wiki pages.
- `domain-synthesis.md` -- Cross-cutting insights that emerge from multiple sources.
- `learning-roadmap.md` -- Suggested reading/study order based on wiki content.

---

## Tags Taxonomy

Use these tags on every page. A page should have 1-5 tags. Prefer specific over broad.

### Domain Tags
- `ai-fundamentals` -- Core AI/ML concepts, vocabulary, model types
- `llm` -- Large language models, architecture, training, inference
- `slm` -- Small language models, on-device, edge inference
- `rag` -- Retrieval-augmented generation, all variants
- `agents` -- AI agents, agentic systems, multi-agent architectures
- `fine-tuning` -- LoRA, QLoRA, SFT, DPO, RLHF, preference tuning
- `prompt-engineering` -- Prompting techniques, context engineering, structured output
- `embeddings` -- Vector representations, embedding models, similarity search
- `vector-databases` -- Pinecone, Weaviate, Chroma, pgvector, FAISS
- `evaluation` -- LLM evals, RAG metrics, benchmarks, guardrails
- `guardrails` -- Safety, content filtering, output validation
- `data-engineering` -- Pipelines, ETL, warehousing, data modeling
- `dimensional-modeling` -- Star schema, SCD, fact/dimension tables
- `ml-systems` -- ML system design, MLOps, model deployment, monitoring
- `orchestration` -- LangChain, LangGraph, LlamaIndex, workflow frameworks
- `cloud-aws` -- AWS services, certifications, AI Practitioner
- `api-development` -- FastAPI, REST APIs, serving models
- `observability` -- Monitoring, tracing, Langfuse, LangSmith, cost tracking
- `caching` -- AI system caching, semantic cache, KV cache

### Context Tags
- `interview-prep` -- Interview questions, study guides
- `certification` -- AWS AI Practitioner, Claude Architect, exam guides
- `project-ideas` -- Portfolio projects, hands-on builds
- `career` -- AI engineer requirements, skills, hiring
- `cheatsheet` -- Quick-reference material, vocabulary lists
- `system-design` -- Architecture patterns, infrastructure decisions
- `tools` -- Specific tools, frameworks, products (use with a domain tag)

### Provider Tags
- `anthropic` -- Claude, Claude Code, MCP, Anthropic SDK
- `openai` -- GPT models, OpenAI API
- `langchain` -- LangChain, LangGraph, LangSmith
- `snowflake` -- Snowflake platform, Snowflake DE
- `huggingface` -- HF models, Transformers, TRL, datasets

---

## Workflows

### Ingest Workflow

Trigger: User says "ingest <filename>" or "process <filename>" or "add <filename> to the wiki".

Steps:

1. **Read the source** from `raw/<filename>`.
   - **Markdown/HTML (<256KB)**: read the full file.
   - **Small PDFs (<10 pages)**: read all pages at once via `pages: "1-10"`.
   - **Large PDFs (10-40 pages)**: read in two passes — `pages: "1-20"`, then `pages: "21-40"`. Take notes between passes (entities, concepts, key points) so earlier content isn't lost.
   - **Very large PDFs (40+ pages)**: read in batches of 15-20 pages. After each batch, write interim notes to a scratch section or directly into the source summary draft. Never try to hold 40+ PDF pages in a single context.
   - **User-pasted documents**: if the user pastes a PDF inline, it loads all pages at once. For documents over ~20 pages, ask the user to NOT paste the file and instead just name it so Claude can read it in controlled chunks via the Read tool.
   - **General rule**: never read more than 20 PDF pages in a single Read call. Use the `pages` parameter (e.g., `pages: "1-15"`, `pages: "16-30"`).

2. **Create source summary page** at `wiki/sources/<slugified-name>.md` following the Source Summary template. Extract key points, entities, and concepts.

3. **For each entity mentioned** (tools, frameworks, products, companies, people, models):
   - Check if `wiki/entities/<entity-name>.md` exists.
   - If YES: update the page -- add new information, add the new source to the `sources:` frontmatter list and Source References section.
   - If NO: create the page following the Entity Page template.
   - **Selectivity**: only create entity pages for entities that are discussed substantively (at least a paragraph or multiple mentions). Skip passing mentions.

4. **For each concept discussed** (techniques, patterns, architectures, ideas):
   - Check if `wiki/concepts/<concept-name>.md` exists.
   - If YES: update with new information and source references.
   - If NO: create the page following the Concept Page template.
   - **Selectivity**: only create concept pages for concepts with enough substance to fill the template. Brief mentions should be noted in the source summary but don't need their own page.

5. **Check for comparison opportunities.** If the source directly compares two things (e.g., "LoRA vs QLoRA"), create or update a comparison page.

6. **Update `wiki/index.md`** -- add entries for every new page created. Update summaries for modified pages if the one-liner changed.

7. **Append to `wiki/log.md`** with this format:
   ```
   ## [YYYY-MM-DD] ingest | <source filename>
   - Created: sources/<name>.md
   - Created: entities/<name>.md, entities/<name>.md
   - Updated: concepts/<name>.md
   - Created: comparisons/<name>.md
   - Pages touched: N
   ```

8. **Report to user**: List all pages created and updated, with a count.

### Batch Ingest Workflow

Trigger: User says "ingest round N" or asks to process multiple files.

When ingesting multiple files in a batch:
- Process **one source at a time** through the full ingest workflow.
- **Defer index/log updates** to the end of the batch (one combined update).
- For PDFs, read each one using the chunked approach above.
- After all sources in the batch: update `wiki/index.md` once, append a combined entry to `wiki/log.md`.

### Query Workflow

Trigger: User asks a question about wiki content.

Steps:

1. **Search the wiki** -- read `wiki/index.md` to identify relevant pages by title, category, and tags. Read the most relevant pages.

2. **Synthesize an answer** from wiki content, citing source pages with wikilinks.

3. **If the user requests it**, file the answer as a new wiki page (typically under `meta/` or as a new concept/comparison page). Update index and log.

4. **If the answer reveals gaps**, note them and optionally update `wiki/meta/knowledge-gaps.md`.

### Lint Workflow

Trigger: User says "lint the wiki" or "health check".

Steps:

1. **Orphan check** -- Find pages not linked from `wiki/index.md`.
2. **Broken link check** -- Find `[[wikilinks]]` that point to non-existent pages.
3. **Missing cross-references** -- Find entity/concept pages sharing tags but not linking to each other.
4. **Stale claims** -- Flag pages where `last_updated` is older than 90 days and newer sources exist on the same topic.
5. **Tag consistency** -- Flag pages with missing tags or tags not in the taxonomy.
6. **Frontmatter validation** -- Ensure every page has required frontmatter fields for its type.
7. **Source coverage** -- List raw sources not yet ingested (no corresponding `wiki/sources/` page).
8. **Report findings** as a checklist. Optionally write to `wiki/meta/lint-report.md`.
9. **Append to `wiki/log.md`**.

---

## Index Format

`wiki/index.md` is organized by page type using markdown tables:

```
## Sources (N pages)
| Page | Source File | Tags | Summary |
|------|------------|------|---------|

## Entities (N pages)
| Page | Category | Tags | Summary |
|------|----------|------|---------|

## Concepts (N pages)
| Page | Tags | Summary |
|------|------|---------|

## Comparisons (N pages)
| Page | Subjects | Tags | Summary |
|------|----------|------|---------|

## Meta (N pages)
| Page | Tags | Summary |
|------|------|---------|
```

---

## Log Format

`wiki/log.md` is append-only. Newest entries at the bottom.
Each entry is an H2 with a consistent prefix for parsing:
`## [YYYY-MM-DD] operation | Subject`

Example:
```
## [2026-04-14] ingest | RAG Components.pdf
- Created: sources/rag-components.md
- Created: entities/pinecone.md, entities/weaviate.md
- Updated: concepts/retrieval-augmented-generation.md
- Pages touched: 4
```

Parse recent entries: `grep "^## \[" wiki/log.md | tail -5`
