---
type: source
title: "Why Language Models Hallucinate"
source_file: "why-language-models-hallucinate.pdf"
source_type: pdf
date_ingested: 2026-04-20
tags: [llm, evaluation, ai-fundamentals]
---

## Summary

Academic paper by Kalai, Nachum, Vempala, and Zhang (OpenAI / Georgia Tech, September 2025) providing a computational learning theory framework for why LLMs hallucinate. The paper argues hallucinations originate as errors in binary classification during pretraining and persist because post-training evaluations reward guessing over expressing uncertainty. The key contribution is a formal reduction from supervised learning (binary classification) to unsupervised learning (density estimation), proving that generative error rate is at least twice the Is-It-Valid (IIV) misclassification rate. The authors propose modifying existing benchmark scoring to include explicit confidence targets rather than creating new hallucination-specific evaluations.

## Key Points

- **Hallucinations are not mysterious** -- they originate as errors in binary classification; if incorrect statements cannot be distinguished from facts, pretraining will produce them via natural statistical pressures.
- **Is-It-Valid (IIV) reduction**: any language model can be used as a binary classifier ("is this output valid?"); generative error rate >= 2 * IIV misclassification rate.
- **Singleton rate theorem**: hallucination rate after pretraining is bounded below by the fraction of training facts appearing exactly once (building on Good-Turing missing mass estimator).
- **Calibrated base models must hallucinate**: cross-entropy pretraining produces calibrated models, and calibration + density estimation implies errors. Non-hallucinating models must sacrifice calibration.
- **Hallucinations are NOT inevitable for all models** -- a Q&A database with calculator and IDK fallback would never hallucinate; the inevitability applies specifically to calibrated base models.
- **Post-training reinforces hallucinations**: binary grading (0/1 scoring) in benchmarks makes abstention strictly suboptimal (Observation 1). Under binary grading, guessing always beats "I don't know."
- **Epidemic of misaligned evaluations**: 9 of 10 major benchmarks analyzed (GPQA, MMLU-Pro, IFEval, BBH, MATH, MuSR, Omni-MATH, SWE-bench, HLE) use binary grading with zero credit for IDK. Only WildBench offers partial credit.
- **Error factors for base models**: (1) arbitrary facts / epistemic uncertainty (no learnable pattern, e.g., birthdays), (2) poor models (model family can't represent the concept, e.g., tokenization prevents letter counting), (3) GIGO (training data errors), (4) distribution shift, (5) computational hardness.
- **Reasoning models help**: DeepSeek-R1 reliably counts letters by spelling them out in chain-of-thought, overcoming the tokenization problem that DeepSeek-V3 fails on.
- **Proposed fix -- explicit confidence targets**: append instructions like "Answer only if >t confident; mistakes penalized t/(1-t) points" to evaluation prompts. This creates behavioral calibration rather than requiring probabilistic confidence outputs.
- **Socio-technical problem**: modifying existing mainstream benchmark scoring (not just adding hallucination-specific evals) is necessary because the abundance of misaligned primary evaluations drowns out any hallucination evaluation.
- **Search and RAG are not panaceas**: Observation 1 (binary grading rewards guessing) holds for any language model including RAG-augmented ones; search doesn't help with intrinsic hallucinations like miscalculations.

## Entities Mentioned

- [[entities/openai]] -- paper authors' affiliation; GPT-4, GPT-4o, o3 referenced
- [[entities/deepeval]] -- related: hallucination evaluation frameworks
- [[entities/ragas]] -- related: RAG evaluation

## Concepts Covered

- [[concepts/llm-hallucination]] -- core topic: theoretical framework for why hallucinations occur and persist
- [[concepts/evaluation]] -- binary grading in benchmarks as root cause of hallucination persistence
- [[concepts/fine-tuning]] -- RLHF, RLAIF, DPO discussed as post-training techniques that reduce but don't eliminate hallucinations
- [[concepts/retrieval-augmented-generation]] -- RAG noted as reducing but not eliminating hallucinations

## Notable Quotes or Data

- "Like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty."
- "(generative error rate) >= 2 * (IIV misclassification rate)" -- the core mathematical relationship
- "If 20% of birthday facts appear exactly once in the pretraining data, then one expects base models to hallucinate on at least 20% of birthday facts."
- GPT-4 calibration: pretrained model ECE = 0.007 (well-calibrated); post-RLHF model ECE = 0.074 (worse calibration)
- DeepSeek-V3 returned wrong letter counts for "DEEPSEEK" ("2" or "3" in ten trials); DeepSeek-R1 correctly counted via chain-of-thought
- All 3 tested models (ChatGPT, DeepSeek, Llama) fabricated the wrong dissertation title for the paper's first author

## Related Sources

- [[sources/rag-eval-metrics]] -- evaluation metrics for RAG systems
- [[sources/setting-up-evaluations-for-llms]] -- practical LLM evaluation setup
