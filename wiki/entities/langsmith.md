---
type: entity
title: "LangSmith"
category: service
tags: [observability, evaluation]
sources: [sources/ai-projects-2026, sources/ai-engineer-requirements, sources/setting-up-evaluations-for-llms]
last_updated: 2026-04-14
---

# LangSmith

## What It Is

LangSmith is a full-lifecycle evaluation and observability platform for LLM applications, built by the LangChain team. It manages datasets, traces execution steps, and runs evaluators — turning evaluation into a continuous, measurable part of the development lifecycle.

## Key Details

- Three core pillars: **Datasets** (input/output pairs), **Traces** (step-by-step execution logs), **Evaluators** (scoring logic)
- Supports the **Rubric-Reasoning-Result (RRR) pattern** for LLM-as-a-Judge evaluation
- Can run **multi-model jury** evaluations (e.g., Gemini + Claude as joint judges)
- Integrates with CI/CD: PR triggers experiment → compare scores → auto-block on regression
- Allows converting production traces directly into eval dataset examples
- Handles parallelization, retries, and UI visualization of results

## How It Fits In

- Part of the [[entities/langchain]] ecosystem
- Primary tool for implementing [[concepts/evaluation]] and [[concepts/observability]] in AI systems
- Competes with / complements [[entities/langfuse]] (open-source alternative) and Braintrust
- Central to [[concepts/regression-testing-for-ai]] workflows

## Source References

- [[sources/setting-up-evaluations-for-llms]] -- core focus, detailed architecture walkthrough
- [[sources/ai-projects-2026]] -- recommended for Project 3 (monitoring/observability)
- [[sources/ai-engineer-requirements]] -- listed as production monitoring tool
