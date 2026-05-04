---
type: concept
title: "Hybrid Search"
aliases: ["fusion retrieval", "hybrid retrieval", "dense + sparse"]
tags: [rag]
sources: [sources/rag-techniques, sources/rag-end-to-end, sources/rag-components, sources/rag-terminology]
last_updated: 2026-04-15
---

# Hybrid Search

## Definition

Hybrid search combines keyword-based retrieval (BM25/sparse vectors) with semantic retrieval (dense embeddings) to get the best of both worlds: exact term matching for specific terms and semantic understanding for conceptual queries.

## How It Works

1. **BM25/sparse search**: keyword frequency scoring — excellent for exact terms (model names, IDs, error codes) but misses synonyms
2. **Dense/vector search**: embedding similarity — captures semantic meaning ('car' matches 'automobile') but can miss exact technical terms
3. **Score fusion**: combine scores using methods like:
   - **Reciprocal Rank Fusion (RRF)**: `score = sum(1/(60 + rank))` across both result sets
   - **Weighted linear combination**: `alpha * keyword_score + (1-alpha) * semantic_score`

### Production Recommendation
Start with **0.6 dense / 0.4 sparse** weighting. Tune the ratio on your own query logs once you have production data.

## Why It Matters

- "Hybrid search combining both consistently outperforms either approach alone" in production
- Dense retrieval misses exact technical terms; BM25 misses paraphrases
- Production RAG systems almost always use hybrid search

## Related Concepts

- [[concepts/embeddings]] -- dense vector component
- [[concepts/re-ranking]] -- often applied after hybrid retrieval
- [[concepts/retrieval-augmented-generation]] -- hybrid search in the retrieval stage
- [[concepts/vector-databases]] -- some support native hybrid search (e.g., [[entities/weaviate]])

## Related Entities

- [[entities/weaviate]] -- native hybrid search support
- [[entities/elasticsearch]] -- BM25 + vector search

## Source References

- [[sources/rag-techniques]] -- Fusion Retrieval with RRF pseudocode
- [[sources/rag-end-to-end]] -- sparse vs dense comparison table, 0.6/0.4 recommendation
- [[sources/rag-components]] -- hybrid search with alpha weighting code
- [[sources/rag-terminology]] -- hybrid search definition
