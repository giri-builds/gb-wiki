---
type: concept
title: "Observability"
aliases: ["AI observability", "LLM monitoring"]
tags: [observability, evaluation]
sources: [sources/ai-projects-2026, sources/ai-engineer-requirements, sources/setting-up-evaluations-for-llms]
last_updated: 2026-04-14
---

# Observability

## Definition

Observability for AI systems is the practice of instrumenting, tracing, and monitoring every step of an LLM pipeline in production. It covers runtime metrics (latency, cost, error rates), execution traces (what chunks were retrieved, what prompts were sent), and quality signals.

## How It Works

- **Tracing**: instrument each pipeline step (retrieval, prompt construction, LLM call, post-processing)
- **Metrics**: track SRE-style measurements — P50/P95 latency, cost per request, failure rates, token usage
- **Quality monitoring**: track eval scores over time, detect degradation
- **Production → eval loop**: convert failed production traces into eval dataset examples

## Why It Matters

- AI systems are non-deterministic — you can't rely on traditional testing alone
- Enables diagnosis of quality degradation, cost overruns, and latency issues
- Bridges the gap between offline [[concepts/evaluation]] and live production behavior

## Related Concepts

- [[concepts/evaluation]] -- offline quality measurement (complementary)
- [[concepts/regression-testing-for-ai]] -- CI/CD eval pipelines
- [[concepts/ai-engineering-stack]] -- cross-cutting production concern

## Related Entities

- [[entities/langsmith]] -- full-lifecycle observability platform
- [[entities/langfuse]] -- open-source alternative

## Source References

- [[sources/ai-projects-2026]] -- Project 3 dedicated to observability
- [[sources/ai-engineer-requirements]] -- monitoring as key production skill
- [[sources/setting-up-evaluations-for-llms]] -- LangSmith tracing architecture
