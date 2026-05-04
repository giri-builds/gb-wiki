---
type: source
title: "RAG Techniques: 34 Strategies with Pseudocode"
source_file: "RAG Techniques.pdf"
source_type: pdf
date_ingested: 2026-04-15
tags: [rag, agents, evaluation, system-design]
---

# RAG Techniques: 34 Strategies with Pseudocode

## Summary

A comprehensive catalog of 34 RAG techniques by Lamhot Siagian, each with pseudocode (PydanticAI/Python), pros/cons, applications, and tooling recommendations. Organized into 8 categories from foundational to advanced architectures. Covers the full spectrum from basic top-k retrieval to sophisticated controllable agents with verification loops. Includes evaluation techniques (DeepEval, GroUSE) and advanced architectures (GraphRAG, RAPTOR, Self-RAG, CRAG).

## Key Points

- **Foundational**: Basic RAG (top-k + prompt), RAG with CSV (row-wise indexing), Reliable RAG (validation loop with relevance/grounding checks), chunk size optimization, proposition chunking (atomic facts)
- **Query Enhancement**: Query transformations (rewrite/decompose), HyDE (embed hypothetical answer passage), HyPE (embed task-focused instructions)
- **Context Enrichment**: Contextual chunk headers (section-aware prefixes), relevant segment extraction (span-level after retrieval), context window enhancement (neighbor chunks), semantic chunking (topic boundary splitting), contextual compression (query-focused summaries), document augmentation (synthetic Q&A at index time)
- **Advanced Retrieval**: Fusion retrieval (RRF combining dense + BM25), reranking (cross-encoder second stage), multi-faceted filtering (ACL/tenant/time metadata), hierarchical indices (doc→section→chunk coarse-to-fine), ensemble retrieval (multiple retrievers merged), dartboard retrieval (MMR diversity)
- **Multimodal**: Multi-modal RAG with captioning (BLIP/GPT-4o + CLIP embeddings)
- **Iterative**: Feedback loop (user feedback improves retrieval), adaptive retrieval (intent-based routing), iterative retrieval (multi-round retrieve→analyze→retry)
- **Evaluation**: DeepEval (automated RAG eval harness), GroUSE (grounded evaluation + judge reliability)
- **Advanced Architecture**: Graph RAG (graph traversal + vector search), Microsoft GraphRAG (community summaries), RAPTOR (recursive summary tree), Self-RAG (decide whether to retrieve + groundedness check), CRAG (corrective retrieval + fallback), Sophisticated Controllable Agent (deterministic decision graph + verification)
- All pseudocode uses PydanticAI Agent pattern with async tool calling
- Recommended hybrid search starting point: 0.6 dense / 0.4 sparse weighting

## Entities Mentioned

- [[entities/langchain]] -- orchestration framework
- [[entities/langgraph]] -- agent workflow framework
- [[entities/llamaindex]] -- hierarchical nodes
- [[entities/deepeval]] -- RAG evaluation framework
- [[entities/pydantic-ai]] -- agent framework used in pseudocode
- [[entities/cohere]] -- reranker provider
- [[entities/neo4j]] -- graph database for Graph RAG
- [[entities/elasticsearch]] -- hybrid search infrastructure

## Concepts Covered

- [[concepts/retrieval-augmented-generation]] -- foundational pipeline and all variants
- [[concepts/agentic-rag]] -- agentic, Self-RAG, CRAG, controllable agent
- [[concepts/chunking]] -- 5+ chunking strategies (fixed, semantic, proposition, hierarchical, sliding window)
- [[concepts/re-ranking]] -- cross-encoder second stage with code examples
- [[concepts/query-refinement]] -- query rewriting, decomposition, HyDE, HyPE
- [[concepts/hybrid-search]] -- fusion retrieval with RRF
- [[concepts/graph-rag]] -- graph traversal + vector search, Microsoft GraphRAG, RAPTOR
- [[concepts/evaluation]] -- DeepEval, GroUSE, correctness/faithfulness/relevancy metrics
- [[concepts/multimodal-ai]] -- captioning-based multimodal RAG

## Notable Quotes or Data

- 34 distinct RAG techniques cataloged with pseudocode
- Recommended chunk sizes to test: 256, 512, 800, 1200 tokens
- Hybrid search starting weight: 0.6 dense / 0.4 sparse
- References: Nir Diamant's RAG_Techniques repo, Cole Medin's oTTomator Agents

## Related Sources

- [[sources/how-agentic-rag-works]] -- conceptual foundation for agentic techniques
- [[sources/rag-end-to-end]] -- end-to-end pipeline overview
- [[sources/rag-components]] -- 15 core components
- [[sources/rag-eval-metrics]] -- evaluation metrics detail
