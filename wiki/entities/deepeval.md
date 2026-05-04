---
type: entity
title: "DeepEval"
category: tool
tags: [evaluation, rag]
sources: [sources/rag-techniques, sources/rag-eval-metrics]
last_updated: 2026-04-15
---

# DeepEval

## What It Is

DeepEval is an open-source evaluation framework for RAG systems that provides automated metrics (correctness, faithfulness, relevancy) and regression testing with CI integration.

## Key Details

- Evaluates RAG on three core metrics: correctness (vs reference), faithfulness (vs context), relevancy (vs question)
- CI-friendly — integrates into automated testing pipelines
- Uses golden datasets for regression protection
- Can use LLM-based judges for scoring

## How It Fits In

- Alternative/complement to [[entities/ragas]] for RAG evaluation
- Part of the [[concepts/evaluation]] tooling landscape alongside [[entities/langsmith]] and [[entities/langfuse]]
- Used in [[concepts/regression-testing-for-ai]] workflows

## Source References

- [[sources/rag-techniques]] -- DeepEval technique with evaluation pseudocode
- [[sources/rag-eval-metrics]] -- listed as LLM-based scoring tool
