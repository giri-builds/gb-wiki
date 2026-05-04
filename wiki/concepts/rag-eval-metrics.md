---
type: concept
title: "RAG Evaluation Metrics"
aliases: ["RAG metrics", "retrieval metrics", "generation metrics"]
tags: [rag, evaluation]
sources: [sources/rag-eval-metrics, sources/rag-techniques, sources/rag-end-to-end]
last_updated: 2026-04-15
---

# RAG Evaluation Metrics

## Definition

RAG evaluation metrics measure the quality of both the retriever and generator components of a RAG system. They replace subjective assessment ("it sounds right") with measurable scores.

## How It Works

### Retrieval-Level Metrics

| Metric | What It Measures | Formula |
|--------|-----------------|---------|
| **Recall@K** | Is the correct chunk in the top K results? | Relevant retrieved / Total relevant |
| **Precision@K** | How many of the K retrieved chunks are useful? | Relevant retrieved / K |
| **Context Relevancy** | How strongly related is retrieved context to the question? | LLM or similarity model score |

### Generation-Level Metrics

| Metric | What It Measures | Key Signal |
|--------|-----------------|------------|
| **Faithfulness** | Is every claim supported by retrieved context? | Detects hallucinations |
| **Answer Relevancy** | Does the answer address the user's question? | Detects off-topic answers |
| **Groundedness** | How strongly is the answer tied to source documents? | Detects source dependence |

### Additional Metrics (from DeepEval/GroUSE)
- **Correctness**: does the answer match a reference answer?
- **Judge reliability**: how consistent is the evaluation itself?

## Why It Matters

- "Most RAG failures are retrieval failures" — measure retrieval first
- Enables comparing different RAG configurations objectively
- Foundation for [[concepts/regression-testing-for-ai]] pipelines
- Key interview topic for AI engineer roles

## Related Concepts

- [[concepts/evaluation]] -- broader eval taxonomy (heuristic, statistical, LLM-as-a-Judge)
- [[concepts/llm-as-a-judge]] -- LLM judges used for context relevancy and faithfulness
- [[concepts/retrieval-augmented-generation]] -- the system being evaluated
- [[concepts/regression-testing-for-ai]] -- metrics used in CI/CD pipelines

## Related Entities

- [[entities/ragas]] -- specialized RAG metrics (faithfulness, context relevance)
- [[entities/deepeval]] -- LLM-based evaluation scoring
- [[entities/langsmith]] -- evaluation orchestration platform

## Source References

- [[sources/rag-eval-metrics]] -- detailed metric definitions with formulas and examples
- [[sources/rag-techniques]] -- DeepEval and GroUSE evaluation techniques
- [[sources/rag-end-to-end]] -- "measure retrieval quality before anything else"
