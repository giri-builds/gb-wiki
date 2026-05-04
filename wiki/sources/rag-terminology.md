---
type: source
title: "Agentic RAG: Must-Know Terminologies"
source_file: "RAG Terminology.pdf"
source_type: pdf
date_ingested: 2026-04-15
tags: [rag, agents, cheatsheet, interview-prep]
---

# Agentic RAG: Must-Know Terminologies

## Summary

A glossary by Ketan Sagare covering 35+ essential terms for agentic RAG systems, organized into 6 categories: LLM & Generation Basics, Retrieval Fundamentals, Embeddings & Vector Search, Knowledge & Context Management, Agentic RAG Concepts, and Production & Reliability. Designed as interview prep material with concise definitions.

## Key Points

- **LLM Basics**: LLM, prompt, context window, tokens, temperature, hallucination
- **Retrieval Fundamentals**: retrieval, corpus, chunking, chunk size, overlap, top-K retrieval, similarity search, re-ranking
- **Embeddings & Vector Search**: embeddings, embedding model, vector store, distance metrics (cosine, dot product, L2), ANN (Approximate Nearest Neighbor), index
- **Knowledge & Context Management**: context injection, grounding, source attribution, metadata, filters, hybrid search
- **Agentic RAG Concepts**: agent, tool calling, ReAct, planner, executor, memory, multi-step retrieval, self-reflection, orchestration
- **Production & Reliability**: latency, throughput, caching, observability, guardrails, evaluation, idempotency

## Entities Mentioned

(No specific tools/products — this is a terminology reference)

## Concepts Covered

- [[concepts/retrieval-augmented-generation]] -- all RAG terminology
- [[concepts/agentic-rag]] -- agent, ReAct, planner/executor, self-reflection
- [[concepts/embeddings]] -- embedding model, distance metrics, ANN
- [[concepts/vector-databases]] -- vector store, index, ANN
- [[concepts/chunking]] -- chunk size, overlap
- [[concepts/re-ranking]] -- re-ranking definition
- [[concepts/hybrid-search]] -- BM25 + vector search
- [[concepts/ai-agents]] -- agent, tool calling, orchestration
- [[concepts/evaluation]] -- evaluation, faithfulness
- [[concepts/guardrails]] -- guardrails definition
- [[concepts/observability]] -- observability, latency, throughput

## Notable Quotes or Data

- "Very important in interviews" label on Production & Reliability section
- Idempotency called out as key production concept (ensuring repeated tool calls don't create inconsistent results)

## Related Sources

- [[sources/rag-techniques]] -- detailed implementations of these concepts
- [[sources/rag-components]] -- hands-on component coverage
- [[sources/rag-end-to-end]] -- end-to-end pipeline context
