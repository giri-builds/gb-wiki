---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
aliases: ["RAG", "retrieval augmented generation"]
tags: [rag, llm]
sources: [sources/how-agentic-rag-works, sources/ai-projects-2026, sources/ai-engineer-requirements, sources/rag-techniques, sources/rag-end-to-end, sources/rag-components, sources/rag-terminology, sources/rag-eval-metrics]
last_updated: 2026-04-15
---

# Retrieval-Augmented Generation (RAG)

## Definition

RAG is an architecture pattern where an LLM generates answers grounded in externally retrieved context rather than relying solely on its training data. The system converts a query into an embedding, searches a vector database for semantically similar content, and passes the retrieved chunks to the LLM alongside the original question.

## How It Works

### The 4 Stages (from RAG End to End)
1. **Ingestion**: load, clean, chunk documents → embed → store in vector DB
2. **Retrieval**: embed user query → search vector DB for top-k matches → apply permission filters
3. **Augmentation**: combine retrieved passages with query into a grounded prompt
4. **Generation**: LLM generates answer grounded in retrieved context with source citations

### 15 Core Components
Retrieval, [[concepts/embeddings]], [[concepts/vector-databases]], Retriever, [[concepts/chunking]], Context Window, Grounding, [[concepts/re-ranking]], [[concepts/hybrid-search]], Metadata Filtering, Similarity Search, Prompt Injection defense, Hallucination mitigation, [[concepts/agentic-rag]], Latency optimization

### Production Enhancements
- **[[concepts/hybrid-search]]**: combining BM25 keyword search with vector search (0.6 dense / 0.4 sparse recommended starting weight)
- **[[concepts/re-ranking]]**: cross-encoder models re-score retrieved chunks for precision
- **[[concepts/chunking]]**: highest-leverage decision — test multiple strategies on real queries
- **[[concepts/evaluation]]**: faithfulness metrics via [[entities/ragas]] or [[entities/langsmith]]
- **[[concepts/query-refinement]]**: rewrite/decompose queries for better retrieval (HyDE, HyPE)

## Why It Matters

- Gives LLMs access to private, up-to-date, or domain-specific knowledge
- Reduces hallucination by grounding answers in source documents
- Most common production AI application pattern in 2026
- Foundation for more advanced patterns like [[concepts/agentic-rag]]

## Key Variants or Approaches

- **Standard RAG**: one-shot retrieve-then-generate pipeline
- **[[concepts/agentic-rag]]**: adds agent control loop with routing, refinement, and self-evaluation
- **[[concepts/hybrid-search]]**: combines keyword (BM25) and semantic (vector) retrieval
- **[[concepts/graph-rag]]**: graph traversal + vector search for multi-hop questions (incl. Microsoft GraphRAG, RAPTOR)
- **Multi-source RAG**: routes queries to different knowledge bases based on content type
- **Self-RAG**: decides whether to retrieve; verifies groundedness before finalizing
- **CRAG (Corrective RAG)**: grades retrieval quality; rewrites query and retries if score is low
- **Reliable RAG**: validation loop checking relevance and grounding before generation
- **34+ techniques** cataloged in RAG Techniques source with pseudocode

## Related Concepts

- [[concepts/agentic-rag]] -- evolution with agent decision loops
- [[concepts/embeddings]] -- vector representations for semantic search
- [[concepts/vector-databases]] -- storage and retrieval infrastructure
- [[concepts/chunking]] -- highest-leverage decision in RAG
- [[concepts/hybrid-search]] -- dense + sparse fusion retrieval
- [[concepts/re-ranking]] -- precision improvement layer
- [[concepts/query-refinement]] -- query rewriting, HyDE, HyPE
- [[concepts/graph-rag]] -- graph-augmented retrieval
- [[concepts/evaluation]] -- measuring RAG quality (faithfulness, relevance)
- [[concepts/rag-eval-metrics]] -- Recall@K, Precision@K, Faithfulness, etc.
- [[concepts/fine-tuning]] -- complementary approach (style/format vs knowledge)

## Related Entities

- [[entities/langchain]], [[entities/llamaindex]] -- orchestration frameworks
- [[entities/pinecone]], [[entities/weaviate]], [[entities/chromadb]] -- vector stores
- [[entities/ragas]] -- RAG evaluation framework

## Source References

- [[sources/how-agentic-rag-works]] -- standard RAG pipeline and failure modes
- [[sources/ai-projects-2026]] -- production RAG project with hybrid retrieval
- [[sources/ai-engineer-requirements]] -- RAG as core AI engineer skill
- [[sources/rag-techniques]] -- 34 techniques with pseudocode (comprehensive)
- [[sources/rag-end-to-end]] -- complete 4-stage walkthrough, chunking strategies, failures
- [[sources/rag-components]] -- 15 core components with Python code
- [[sources/rag-terminology]] -- 35+ essential RAG terms
- [[sources/rag-eval-metrics]] -- retrieval and generation evaluation metrics
