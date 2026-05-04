---
type: concept
title: "Chunking"
aliases: ["document chunking", "text splitting", "chunk strategies"]
tags: [rag, system-design]
sources: [sources/rag-techniques, sources/rag-end-to-end, sources/rag-components, sources/rag-terminology]
last_updated: 2026-04-15
---

# Chunking

## Definition

Chunking is the process of splitting large documents into smaller segments that preserve semantic meaning while fitting within model context limits. It is the highest-leverage decision in a [[concepts/retrieval-augmented-generation]] system — bad chunking cannot be rescued by any downstream component.

## How It Works

Documents are divided into retrievable units before being embedded and indexed. The chunking strategy determines the precision/context trade-off of the entire pipeline.

### Strategies (from simplest to most sophisticated)

1. **Fixed-size chunking** (200-512 tokens): splits at token count regardless of sentence boundaries. Good starting point but can split mid-sentence. Use with 10-20% overlap.

2. **Sliding window with overlap**: chunks overlap by 10-20% to prevent relevant content from being split at boundaries. Works well for dense prose.

3. **Semantic chunking**: splits at natural topic boundaries using sentence embeddings and similarity thresholds. More coherent chunks, better conceptual retrieval. More compute.

4. **Proposition chunking**: LLM extracts atomic factual statements from text. Highest precision for factual Q&A but high index-time cost and may lose narrative flow.

5. **Hierarchical chunking**: stores large summary chunks and small detail chunks. Retrieval fetches summary first, drills into detail. Best for long reports. Used in RAPTOR.

6. **Contextual chunk headers**: prepend document title and section heading path to each chunk before embedding to reduce ambiguity.

### Key Parameters
- **Chunk size**: too large buries the answer, too small loses context. Test with real queries.
- **Overlap**: 10-20% prevents information loss at boundaries
- Recommended sizes to test: 256, 512, 800, 1200 tokens

## Why It Matters

- "Bad chunking cannot be rescued — no reranker, no model upgrade, and no prompt engineering can fix a poorly chunked knowledge base"
- Chunk strategy is the highest-leverage decision in RAG
- Directly determines retrieval quality, which gates everything downstream
- "Quality of RAG is 80% retrieval, 20% generation" — and chunking is the foundation of retrieval

## Related Concepts

- [[concepts/retrieval-augmented-generation]] -- chunking is stage 1 (ingestion)
- [[concepts/embeddings]] -- chunks are embedded for similarity search
- [[concepts/vector-databases]] -- chunks are stored as vectors
- [[concepts/re-ranking]] -- can partially compensate for chunking issues
- [[concepts/evaluation]] -- measure retrieval quality to validate chunking

## Source References

- [[sources/rag-techniques]] -- 5+ chunking strategies with pseudocode
- [[sources/rag-end-to-end]] -- chunking as foundation, 4 strategies compared
- [[sources/rag-components]] -- chunking with code example
- [[sources/rag-terminology]] -- chunk size and overlap definitions
