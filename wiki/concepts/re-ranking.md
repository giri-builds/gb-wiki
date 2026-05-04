---
type: concept
title: "Re-ranking"
aliases: ["cross-encoder re-ranking", "reranking"]
tags: [rag]
sources: [sources/ai-projects-2026, sources/ai-engineer-requirements]
last_updated: 2026-04-14
---

# Re-ranking

## Definition

Re-ranking is a retrieval precision technique where a cross-encoder model re-scores the initial set of retrieved documents to improve the quality of results passed to the LLM. It sits between the initial retrieval step and the generation step in a [[concepts/retrieval-augmented-generation]] pipeline.

## How It Works

- Initial retrieval returns top-K candidates via embedding similarity
- Cross-encoder model takes each (query, document) pair and produces a relevance score
- Documents are re-ordered by cross-encoder score — more accurate than embedding similarity alone
- Top results after re-ranking are passed to the LLM for generation

## Why It Matters

- Significantly improves precision over embedding-only retrieval
- Cross-encoders understand query-document interaction better than bi-encoders
- Key component of production-grade RAG systems

## Related Concepts

- [[concepts/retrieval-augmented-generation]] -- re-ranking improves the retrieval step
- [[concepts/embeddings]] -- initial retrieval uses embedding similarity
- [[concepts/vector-databases]] -- provide the initial candidate set

## Related Entities

- [[entities/cohere]] -- provides re-ranker models

## Source References

- [[sources/ai-projects-2026]] -- Cohere re-ranker / Sentence Transformers cross-encoders
- [[sources/ai-engineer-requirements]] -- re-ranking in retrieval strategies
