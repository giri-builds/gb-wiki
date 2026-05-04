---
type: entity
title: "Weaviate"
category: service
tags: [vector-databases, rag]
sources: [sources/ai-projects-2026, sources/ai-engineer-requirements]
last_updated: 2026-04-14
---

# Weaviate

## What It Is

Weaviate is an open-source vector database that supports semantic search, hybrid search (combining keyword and vector), and integrations with popular ML frameworks.

## Key Details

- Open-source with managed cloud option
- Supports hybrid search (BM25 + vector) natively
- One of the recommended vector stores for production RAG

## How It Fits In

- Part of the **retrieval layer** in the [[concepts/ai-engineering-stack]]
- Alternative to [[entities/pinecone]], [[entities/chromadb]], pgvector, and FAISS

## Source References

- [[sources/ai-projects-2026]] -- recommended for Project 1 (RAG) vector store
- [[sources/ai-engineer-requirements]] -- listed in retrieval layer
