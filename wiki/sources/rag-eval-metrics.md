---
type: source
title: "RAG Evaluation Metrics"
source_file: "RAG - Eval Metrics.pdf"
source_type: pdf
date_ingested: 2026-04-15
tags: [rag, evaluation]
---

# RAG Evaluation Metrics

## Summary

A guide by Naresh Edagotti (PracticAI) covering RAG evaluation metrics at two levels: retrieval-level (Recall@K, Precision@K, Context Relevancy) and generation-level (Faithfulness, Answer Relevancy, Groundedness). Includes formulas, examples, and a list of evaluation tools.

## Key Points

- **RAG has two brains**: Retriever (finds relevant chunks) and Generator/LLM (uses chunks to answer)
- **Retrieval-Level Metrics**:
  - **Recall@K**: measures if the correct chunk is in the top K results. Formula: relevant chunks retrieved / total relevant chunks
  - **Precision@K**: measures how many of the K retrieved chunks are actually useful. Formula: relevant retrieved chunks / K
  - **Context Relevancy**: how strongly related the retrieved context is to the question (scored by LLM or similarity model)
- **Generation-Level Metrics**:
  - **Faithfulness**: is every claim in the answer supported by retrieved context? Detects hallucinations. "Paris is capital of France and has population 5 million" → population not in context = unfaithful
  - **Answer Relevancy**: does the answer actually address the user's question? (vs going off-topic)
  - **Groundedness**: how strongly the answer is tied to provided documents (source dependence)
- **Evaluation Tools**: Ragas (RAG-specific metrics), TruLens (grounding + feedback), DeepEval (LLM-based scoring), LangChain (evaluation chains), LlamaIndex (built-in eval modules)
- Key insight: move from "it sounds right" → "it is measured"

## Entities Mentioned

- [[entities/ragas]] -- specialized RAG evaluation metrics
- [[entities/deepeval]] -- LLM-based evaluation scoring
- [[entities/langchain]] -- evaluation chains
- [[entities/llamaindex]] -- built-in eval modules

## Concepts Covered

- [[concepts/evaluation]] -- complete RAG evaluation framework
- [[concepts/rag-eval-metrics]] -- Recall@K, Precision@K, Context Relevancy, Faithfulness, Answer Relevancy, Groundedness
- [[concepts/retrieval-augmented-generation]] -- evaluation of both retriever and generator

## Notable Quotes or Data

- Faithfulness example: "Paris is capital of France and has population 5 million" — population not in context = unfaithful
- Precision@3 example: 1 relevant out of 3 retrieved = 0.33
- Recall@2 = 1 (perfect) when relevant chunk is present in top 2

## Related Sources

- [[sources/setting-up-evaluations-for-llms]] -- LangSmith-based eval infrastructure
- [[sources/rag-techniques]] -- DeepEval and GroUSE technique details
- [[sources/rag-end-to-end]] -- measuring retrieval quality as priority
