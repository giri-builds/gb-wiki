---
type: concept
title: "Vector Databases"
aliases: ["vector stores", "vector DBs"]
tags: [vector-databases, rag]
sources: [sources/how-agentic-rag-works, sources/ai-engineer-requirements, sources/ai-projects-2026]
last_updated: 2026-04-14
---

# Vector Databases

## Definition

Vector databases are specialized storage systems optimized for indexing and querying high-dimensional embedding vectors via similarity search. They are the retrieval backbone of [[concepts/retrieval-augmented-generation]] systems.

## How It Works

- Documents are chunked, embedded, and stored as vectors
- At query time, the query embedding is compared against stored vectors
- Returns top-K most similar results based on distance metrics (cosine, dot product, etc.)
- Some support hybrid search combining keyword (BM25) and vector similarity

## Why It Matters

- Enable semantic search — finding content by meaning rather than keywords
- Core infrastructure in the **retrieval layer** of the [[concepts/ai-engineering-stack]]
- Scale from prototyping (ChromaDB) to production (Pinecone, Weaviate)

## Key Variants or Approaches

- **Managed services**: [[entities/pinecone]] (fully managed, no infra)
- **Open-source**: [[entities/weaviate]] (hybrid search), [[entities/chromadb]] (lightweight/embedded)
- **Extensions**: pgvector (PostgreSQL), FAISS (Meta, in-memory)

## Related Concepts

- [[concepts/embeddings]] -- the vectors being stored
- [[concepts/retrieval-augmented-generation]] -- primary use case
- [[concepts/re-ranking]] -- post-retrieval precision layer

## Source References

- [[sources/how-agentic-rag-works]] -- vector DBs in RAG pipeline
- [[sources/ai-engineer-requirements]] -- vector DBs in retrieval layer
- [[sources/ai-projects-2026]] -- ChromaDB/Weaviate for production RAG
