---
type: concept
title: "LLM-as-a-Judge"
aliases: ["LLM judge", "model grading"]
tags: [evaluation, llm]
sources: [sources/setting-up-evaluations-for-llms]
last_updated: 2026-04-14
---

# LLM-as-a-Judge

## Definition

LLM-as-a-Judge is an evaluation technique where a stronger LLM evaluates the output of another model (or the same model) using structured rubrics. It is the most capable layer of the [[concepts/evaluation]] taxonomy, able to catch nuanced failures like hallucinations, logical inconsistencies, and policy violations.

## How It Works

### Rubric-Reasoning-Result (RRR) Pattern
1. **Rubric**: Define specific scoring criteria (e.g., "Score 1-5 for Technical Accuracy. A 5 means every fact is supported by context. A 1 means dangerous hallucination.")
2. **Reasoning**: Force the judge to produce a chain-of-thought explanation before scoring
3. **Result**: Structured score across multiple dimensions (accuracy, faithfulness, safety)

### Multi-Model Jury
- Use multiple judge models (e.g., Gemini + Claude) to reduce single-model bias
- Consensus threshold: "Only pass if both give a score > 4"

## Why It Matters

- Only evaluation layer that reliably catches subtle hallucinations, logical errors, and constraint violations
- Enables automated quality gating in CI/CD (e.g., block PR if faithfulness drops >5%)
- Addresses the "evaluator paradox" — quality depends on the judge model's capability

## Related Concepts

- [[concepts/evaluation]] -- parent concept; LLM-as-a-Judge is one layer
- [[concepts/regression-testing-for-ai]] -- uses LLM judges in CI/CD pipelines
- [[concepts/guardrails]] -- heuristic evals complement LLM judges

## Related Entities

- [[entities/langsmith]] -- orchestrates LLM-as-a-Judge evaluations

## Source References

- [[sources/setting-up-evaluations-for-llms]] -- detailed RRR pattern and multi-model jury
