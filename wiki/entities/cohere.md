---
type: entity
title: "Cohere"
category: company
tags: [rag, tools]
sources: [sources/ai-projects-2026, sources/rag-techniques]
last_updated: 2026-04-15
---

# Cohere

## What It Is

Cohere is an AI company that provides NLP APIs, including a widely-used re-ranker model for improving retrieval precision in [[concepts/retrieval-augmented-generation]] systems.

## Key Details

- Cohere re-ranker is commonly used as the second-stage scoring model after initial vector retrieval
- Provides cross-encoder models for [[concepts/re-ranking]]
- Also offers embedding models and LLM APIs

## How It Fits In

- Key provider for the [[concepts/re-ranking]] step in production RAG pipelines
- Alternative cross-encoder sources: Sentence Transformers (open-source), bge-reranker

## Source References

- [[sources/ai-projects-2026]] -- recommended re-ranker for production RAG
- [[sources/rag-techniques]] -- listed in reranking tooling
