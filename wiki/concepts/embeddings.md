---
type: concept
title: "Embeddings"
aliases: ["vector embeddings", "text embeddings"]
tags: [embeddings, rag]
sources: [sources/how-agentic-rag-works, sources/ai-engineer-requirements]
last_updated: 2026-04-14
---

# Embeddings

## Definition

Embeddings are numerical vector representations that capture the semantic meaning of text (or other data types). They enable similarity-based operations — semantically similar content maps to nearby points in vector space.

## How It Works

- Text is passed through an embedding model which outputs a fixed-length vector (e.g., 768 or 1536 dimensions)
- Similar meanings produce vectors with high cosine similarity
- These vectors are stored in [[concepts/vector-databases]] for efficient retrieval
- At query time, the query is embedded and compared against stored vectors

## Why It Matters

- Foundation of [[concepts/retrieval-augmented-generation]] — enables semantic search over documents
- Used in [[concepts/evaluation]] (statistical evals via cosine similarity, BERTScore)
- Bridge between human-readable text and machine-processable representations

## Related Concepts

- [[concepts/vector-databases]] -- storage and retrieval of embedding vectors
- [[concepts/retrieval-augmented-generation]] -- primary use case
- [[concepts/evaluation]] -- embedding distance as eval metric

## Source References

- [[sources/how-agentic-rag-works]] -- embeddings in standard RAG pipeline
- [[sources/ai-engineer-requirements]] -- embeddings in retrieval layer of AI stack
