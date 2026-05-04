---
type: concept
title: "Evaluation"
aliases: ["LLM evaluation", "AI evaluation", "evals"]
tags: [evaluation, llm]
sources: [sources/setting-up-evaluations-for-llms, sources/ai-engineer-requirements, sources/ai-projects-2026, sources/why-language-models-hallucinate]
last_updated: 2026-04-20
---

# Evaluation

## Definition

Evaluation in the context of LLM systems is the systematic measurement of model and pipeline behavior — moving from intuition ("vibe-eval") to programmatic infrastructure. It encompasses heuristic checks, statistical comparisons, and LLM-as-a-Judge assessments across dimensions like accuracy, faithfulness, safety, and consistency.

## How It Works

### Three-Layer Taxonomy (escalating cost and capability)

**Layer A — Heuristic Evals** (cheap, deterministic):
- Valid JSON? Within token limits? No disallowed phrases?
- Catches obvious structural failures — run on everything

**Layer B — Statistical Evals** (moderate cost):
- Cosine similarity, embedding distance, BERTScore against reference answers
- Catches directional correctness but misses precision failures

**Layer C — [[concepts/llm-as-a-judge]]** (expensive, most capable):
- Stronger model evaluates weaker model output with structured rubrics
- Catches nuanced failures: hallucinations, logical inconsistencies, policy violations
- Uses the **Rubric-Reasoning-Result (RRR) pattern**

### Dataset Construction
- **Static gold standards**: 50-100 curated input→output pairs
- **Synthetic expansion**: teacher models generate edge cases
- **Dynamic production logs**: failed traces become permanent test cases

## Why It Matters

- LLM outputs are non-deterministic — manual inspection doesn't scale
- Enables safe iteration on prompts, data, and system design without regressions
- Foundation for [[concepts/regression-testing-for-ai]] in CI/CD pipelines
- Key production skill for AI engineers in 2026
- **Binary grading reinforces [[concepts/llm-hallucination]]**: Kalai et al. (2025) show that 9 of 10 major benchmarks (GPQA, MMLU-Pro, IFEval, BBH, MATH, MuSR, Omni-MATH, SWE-bench, HLE) use 0/1 scoring with zero credit for IDK, making abstention strictly suboptimal and rewarding confident guessing

## Related Concepts

- [[concepts/llm-as-a-judge]] -- strongest evaluation layer
- [[concepts/llm-hallucination]] -- binary grading in benchmarks enables hallucination persistence
- [[concepts/observability]] -- runtime monitoring (complementary to offline evals)
- [[concepts/guardrails]] -- heuristic evals as runtime safety checks
- [[concepts/regression-testing-for-ai]] -- automated CI/CD eval pipelines

## Related Entities

- [[entities/langsmith]] -- evaluation orchestration platform
- [[entities/langfuse]] -- open-source alternative
- [[entities/ragas]] -- RAG-specific evaluation
- [[entities/bertscore]] -- statistical eval metric

## Source References

- [[sources/setting-up-evaluations-for-llms]] -- comprehensive eval system design
- [[sources/ai-engineer-requirements]] -- evaluation as key AI engineer skill
- [[sources/ai-projects-2026]] -- observability project with eval components
- [[sources/why-language-models-hallucinate]] -- theoretical analysis of how binary grading reinforces hallucination
