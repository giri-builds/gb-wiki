---
type: concept
title: "Regression Testing for AI"
aliases: ["AI CI/CD", "eval pipelines"]
tags: [evaluation, system-design]
sources: [sources/setting-up-evaluations-for-llms]
last_updated: 2026-04-14
---

# Regression Testing for AI

## Definition

Regression testing for AI systems is the practice of automatically evaluating model/prompt changes against a baseline dataset to ensure quality doesn't degrade. It integrates [[concepts/evaluation]] into CI/CD pipelines so that every code change is quality-gated before deployment.

## How It Works

1. **Trigger**: PR or code push triggers evaluation pipeline
2. **Run**: new prompt/model runs against regression dataset in [[entities/langsmith]]
3. **Compare**: scores compared between main branch and feature branch
4. **Gate**: auto-block PR if key metrics (e.g., faithfulness) drop beyond threshold (>5%)

## Why It Matters

- Prevents silent quality regressions when prompts, data, or models change
- Makes AI system changes as testable as traditional software changes
- Converts evaluation from manual inspection to automated infrastructure

## Related Concepts

- [[concepts/evaluation]] -- the eval taxonomy feeding into CI/CD
- [[concepts/llm-as-a-judge]] -- often used as the evaluator in regression pipelines
- [[concepts/observability]] -- production monitoring complements offline regression testing

## Related Entities

- [[entities/langsmith]] -- orchestrates regression experiments

## Source References

- [[sources/setting-up-evaluations-for-llms]] -- detailed CI/CD integration pattern
