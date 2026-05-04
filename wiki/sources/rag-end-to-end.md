---
type: source
title: "RAG Explained End to End"
source_file: "RAG End to End.pdf"
source_type: pdf
date_ingested: 2026-04-15
tags: [rag, system-design, interview-prep]
---

# RAG Explained End to End

## Summary

A comprehensive end-to-end RAG walkthrough by Rajesh Mane covering why LLMs hallucinate without RAG, the 4 stages of the RAG pipeline (Ingestion, Retrieval, Augmentation, Generation), vector embeddings (sparse vs dense), chunking strategies, RAG vs fine-tuning, common RAG failures, and an introduction to agentic RAG. Emphasis on production engineering decisions.

## Key Points

- **Why RAG**: training data frozen at cutoff, no access to private data, confident-but-wrong answers, retraining is expensive/slow
- **The Hallucination Cost**: Google Bard's wrong JWST answer contributed to $100B market cap drop
- **4 Stages**: Ingestion (load, clean, chunk, embed) → Retrieval (embed query, top-k search, permission filters) → Augmentation (combine context + query, structured prompt, token budget) → Generation (grounded answer with citations)
- **Sparse vs Dense vectors**: BM25 (keyword frequency, exact match) vs embeddings (semantic meaning, synonyms) — hybrid combining both wins in production
- **Production recommendation**: start with 0.6 dense / 0.4 sparse weighting for hybrid search
- **Chunking strategies**: fixed size (200-512 tokens), semantic chunking, hierarchical chunking, sliding window with 10-20% overlap
- **RAG vs Fine-tuning**: RAG for current/private knowledge with citations; fine-tuning for style/format consistency; use both together for best results
- **Common failures**: wrong chunk size, no permission filtering at retrieval, skipping reranker, not measuring retrieval quality
- **Key insight**: "Quality of RAG is 80% retrieval, 20% generation"
- **Agentic RAG**: multi-step retrieval, tool-augmented retrieval, CRAG (Corrective RAG)
- **Security**: apply permission filters at retrieval time, NEVER after generation

## Entities Mentioned

- [[entities/pinecone]] -- vector database example
- [[entities/weaviate]] -- vector database example

## Concepts Covered

- [[concepts/retrieval-augmented-generation]] -- complete 4-stage pipeline
- [[concepts/embeddings]] -- sparse vs dense, hybrid search
- [[concepts/chunking]] -- 4 strategies with trade-offs
- [[concepts/hybrid-search]] -- dense + sparse fusion in production
- [[concepts/re-ranking]] -- skipping reranker as common failure
- [[concepts/agentic-rag]] -- multi-step, tool-augmented, CRAG
- [[concepts/fine-tuning]] -- RAG vs fine-tuning comparison
- [[concepts/guardrails]] -- permission filtering at retrieval time

## Notable Quotes or Data

- "The quality of a RAG system is 80 percent retrieval and 20 percent generation"
- "Bad chunking cannot be rescued — no reranker, no model upgrade, and no prompt engineering can fix a poorly chunked knowledge base"
- "Applying access controls after generation is a security failure"
- Hybrid search recommendation: 0.6 dense / 0.4 sparse starting weight
- Chunk size recommendation: 100-500 tokens, with 200 for precision and 512 for context
- Google Bard JWST incident: $100B market cap loss from a single hallucination

## Related Sources

- [[sources/rag-techniques]] -- 34 detailed techniques expanding on this overview
- [[sources/rag-components]] -- 15 components with code
- [[sources/rag-eval-metrics]] -- metrics for measuring RAG quality
- [[sources/how-agentic-rag-works]] -- deep dive on agentic RAG concepts
