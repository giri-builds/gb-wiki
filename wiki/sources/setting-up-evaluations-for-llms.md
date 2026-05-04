---
type: source
title: "Setting Up Evaluations for LLMs"
source_file: "Setting up Evaluations for LLMs - by Aishwarya Srinivasan.html"
source_type: html
date_ingested: 2026-04-14
tags: [evaluation, observability, llm]
---

# Setting Up Evaluations for LLMs

## Summary

A detailed guide by Aishwarya Srinivasan (AI with Aish newsletter) on building production-grade LLM evaluation systems using LangSmith as the orchestration layer. Covers the eval taxonomy (heuristic → statistical → LLM-as-a-Judge), dataset construction strategies, the Rubric-Reasoning-Result (RRR) pattern for LLM judges, and CI/CD integration for automated regression testing. The core thesis: evaluation must move from intuition ("vibe-eval") to infrastructure.

## Key Points

- **"Vibe-eval" fails** because it's subjective, lacks coverage, and is blind to regression
- **Eval taxonomy** has three layers, escalating in cost and capability:
  - **Heuristic evals**: deterministic checks (valid JSON, token limits, disallowed phrases) — cheap first line of defense
  - **Statistical evals**: semantic comparison via cosine similarity, embedding distance, BERTScore — catches directional correctness but misses precision failures
  - **LLM-as-a-Judge**: strongest model evaluates weaker model output with structured rubrics — only layer that catches nuanced failures (hallucinations, logical inconsistencies, policy violations)
- **LangSmith architecture** has three pillars: Datasets, Traces, and Evaluators
- **Dataset construction**: static gold standards (50-100 curated pairs), synthetic data expansion (teacher models generate edge cases), dynamic production logs (failed traces become test cases)
- **RRR pattern** (Rubric-Reasoning-Result): define strict rubric → force chain-of-thought reasoning → produce structured score (1-5 across dimensions)
- **Multi-model jury**: use multiple judge models (e.g., Gemini + Claude) with consensus threshold to avoid bias
- **CI/CD integration**: PR triggers LangSmith experiment → run against regression dataset → compare scores → auto-block PR if faithfulness drops >5%

## Entities Mentioned

- [[entities/langsmith]] -- evaluation orchestration platform (core focus of article)
- [[entities/langchain]] -- parent ecosystem
- [[entities/bertscore]] -- semantic evaluation metric
- [[entities/salesforce-agentforce]] -- enterprise AI agent platform (sponsor mention)

## Concepts Covered

- [[concepts/evaluation]] -- systematic LLM evaluation infrastructure
- [[concepts/llm-as-a-judge]] -- using LLMs to evaluate LLM outputs
- [[concepts/observability]] -- tracing and monitoring AI systems
- [[concepts/guardrails]] -- heuristic evals as first line of defense
- [[concepts/regression-testing-for-ai]] -- CI/CD pipelines for prompt/model changes
- [[concepts/eval-datasets]] -- gold standards, synthetic data, production logs

## Notable Quotes or Data

- "Evaluation has to move from intuition to infrastructure"
- "Vibe-eval fails because it's subjective, lacks coverage, and is blind to regression"
- CI/CD gate: auto-block PR if faithfulness score drops by more than 5%
- Multi-model jury pattern: "Only pass if both judges give a score > 4"

## Related Sources

- [[sources/ai-projects-2026]] -- Project 3 (monitoring/observability) connects directly
- [[sources/ai-engineer-requirements]] -- evaluation as key AI engineer skill
