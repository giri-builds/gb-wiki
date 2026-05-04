---
type: concept
title: "Guardrails"
aliases: ["AI guardrails", "output validation"]
tags: [guardrails, evaluation]
sources: [sources/ai-engineer-requirements, sources/setting-up-evaluations-for-llms]
last_updated: 2026-04-14
---

# Guardrails

## Definition

Guardrails are deterministic safety checks applied to LLM inputs and outputs to ensure they meet structural, content, and policy constraints. They form the first (cheapest) layer of the [[concepts/evaluation]] taxonomy — catching obvious failures before more expensive checks run.

## How It Works

- **Input guardrails**: validate user input before sending to LLM (content filtering, injection detection)
- **Output guardrails**: check LLM output for valid JSON, token limits, disallowed phrases, formatting errors
- Run on every request — they are fast, deterministic, and free compared to LLM-based evals

## Why It Matters

- First line of defense in production AI systems
- Catches structural failures without the cost of LLM-based evaluation
- Required production skill for AI engineers in 2026

## Related Concepts

- [[concepts/evaluation]] -- guardrails are the heuristic eval layer
- [[concepts/llm-as-a-judge]] -- escalation when guardrails can't catch nuanced failures

## Source References

- [[sources/ai-engineer-requirements]] -- guardrails as production reliability skill
- [[sources/setting-up-evaluations-for-llms]] -- heuristic evals as "cheap gate"
