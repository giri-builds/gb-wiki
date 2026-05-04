---
type: source
title: "15 RAG Components You Can't Ignore"
source_file: "RAG Components.pdf"
source_type: pdf
date_ingested: 2026-04-15
tags: [rag, cheatsheet, interview-prep]
---

# 15 RAG Components You Can't Ignore

## Summary

A hands-on guide by Chandra Sekhar covering 15 essential RAG components, each with Python code examples. Components span the full RAG pipeline: Retrieval, Embeddings, Vector Databases, Retriever, Chunking, Context Window, Grounding, Re-Ranking, Hybrid Search, Metadata Filtering, Similarity Search, Prompt Injection, Hallucination, Agentic RAG, and Latency.

## Key Points

- **Retrieval**: finding and extracting relevant info from a knowledge base before generating a response
- **Embeddings**: numerical representations capturing semantic meaning; "King - Man + Woman = Queen" analogy
- **Vector Databases**: specialized DBs for high-dimensional similarity search using distance metrics; code example with ChromaDB
- **Retriever**: orchestrates retrieval — converts query to embedding, searches vector DB, returns top-k chunks
- **Chunking**: splitting documents into smaller segments; code example with fixed-size + overlap (500 chars, 50 overlap)
- **Context Window**: model's "working memory" — ranges from 4K (older) to 200K+ tokens (modern); must fit retrieved chunks within limit
- **Grounding**: ensuring answers are based on retrieved sources, not hallucinated; requires "use ONLY provided context" instruction
- **Re-Ranking**: two-stage process — fast broad retrieval (top 100) → precise cross-encoder scoring (top 5); code with `sentence_transformers.CrossEncoder`
- **Hybrid Search**: combining BM25 keyword + vector semantic search with alpha weighting; best-of-both-worlds
- **Metadata Filtering**: narrowing search by document metadata (year, department, type) before semantic search
- **Similarity Search**: cosine similarity or dot product between query and document embeddings; code example
- **Prompt Injection**: security vulnerability where users inject instructions; must sanitize inputs
- **Hallucination**: plausible but unsupported information; RAG reduces via grounding + source verification
- **Agentic RAG**: agent plans, reasons, decides retrieval strategy; multiple searches, analyze results, iterate
- **Latency**: optimize via caching embeddings, faster models, reduced search scope, parallelization; target sub-second to few-second

## Entities Mentioned

- [[entities/chromadb]] -- vector database code example
- [[entities/openai]] -- embedding model (text-embedding-3-small)

## Concepts Covered

- [[concepts/retrieval-augmented-generation]] -- all 15 components
- [[concepts/embeddings]] -- with code example
- [[concepts/vector-databases]] -- with ChromaDB code
- [[concepts/chunking]] -- fixed-size with overlap code
- [[concepts/re-ranking]] -- cross-encoder code example
- [[concepts/hybrid-search]] -- alpha-weighted fusion code
- [[concepts/agentic-rag]] -- plan/search/reason/synthesize pattern
- [[concepts/guardrails]] -- prompt injection defense, grounding

## Notable Quotes or Data

- Context windows range from 4K tokens (older models) to 200K+ tokens (modern)
- Re-ranking example: retrieve top 100 candidates, re-rank to top 5
- Hybrid search alpha parameter controls keyword vs semantic weighting

## Related Sources

- [[sources/rag-techniques]] -- 34 techniques expanding on these components
- [[sources/rag-end-to-end]] -- end-to-end pipeline walkthrough
- [[sources/rag-terminology]] -- terminology glossary
