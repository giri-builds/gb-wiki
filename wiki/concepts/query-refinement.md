---
type: concept
title: "Query Refinement"
aliases: ["query rewriting", "query transformation", "HyDE", "HyPE"]
tags: [rag]
sources: [sources/rag-techniques, sources/how-agentic-rag-works]
last_updated: 2026-04-15
---

# Query Refinement

## Definition

Query refinement is the practice of rewriting, decomposing, or expanding a user's query before retrieval to improve the quality of retrieved results. It is one of the three core capabilities of [[concepts/agentic-rag]] alongside routing and self-evaluation.

## How It Works

### Techniques (escalating sophistication)

1. **Query rewriting**: LLM generates faithful paraphrases of the original query. Improves recall on vague queries without changing intent.

2. **Query decomposition**: LLM breaks a complex multi-part question into sub-queries, retrieves for each, then merges results. Helps multi-hop questions.

3. **HyDE (Hypothetical Document Embedding)**: LLM generates a hypothetical passage that would answer the question. That passage is embedded and used for retrieval instead of the query. Boosts retrieval for short/vague queries.

4. **HyPE (Hypothetical Prompt Embedding)**: LLM generates task-focused instructions aligned with the query intent. Those instructions are embedded for retrieval. Useful for summarize/compare/extract tasks.

5. **Post-retrieval refinement**: after weak retrieval results, the agent reformulates the query and retries. Key component of Self-RAG and CRAG patterns.

## Why It Matters

- Directly addresses the "ambiguous query" failure mode of standard RAG
- No corpus changes needed — operates entirely at query time
- Enables the "second chance" that standard one-shot RAG lacks

## Related Concepts

- [[concepts/agentic-rag]] -- query refinement is a core agentic capability
- [[concepts/retrieval-augmented-generation]] -- refinement improves the retrieval step
- [[concepts/hybrid-search]] -- can be combined with query refinement

## Source References

- [[sources/rag-techniques]] -- Query Transformations, HyDE, HyPE with pseudocode
- [[sources/how-agentic-rag-works]] -- query refinement as core agentic capability
