---
type: concept
title: "LLM Hallucination"
aliases: ["hallucination", "confabulation", "plausible falsehood", "model hallucination"]
tags: [llm, evaluation, ai-fundamentals]
sources: [sources/why-language-models-hallucinate]
last_updated: 2026-04-20
---

## Definition

LLM hallucination is the generation of plausible yet incorrect statements by a language model -- confident-sounding outputs that contradict facts, training data, or the user's prompt. Unlike human hallucination (a perceptual phenomenon), LLM hallucination is a statistical artifact of how models learn and are evaluated. The term covers both **intrinsic hallucinations** (contradicting the prompt, e.g., miscounting letters in a given word) and **extrinsic hallucinations** (contradicting training data or external reality, e.g., fabricating a person's birthday).

## How It Works

### Pretraining Origins

Hallucinations arise naturally from the density estimation objective of pretraining. A formal reduction from Kalai et al. (2025) connects generative errors to binary classification:

1. **Is-It-Valid (IIV) problem**: Given a candidate output, classify it as valid (+) or error (-). Any language model can be used as an IIV classifier by thresholding its output probability.
2. **Core bound**: `generative error rate >= 2 * IIV misclassification rate`. If the model can't distinguish valid outputs from errors in a domain, it will generate errors in that domain.
3. **Calibration trap**: Cross-entropy pretraining produces calibrated models (predicted probabilities match actual frequencies). But calibrated models that do density estimation must generate errors -- the only way to avoid errors is to sacrifice calibration (e.g., always output IDK).

### Error Factors

| Factor | Mechanism | Example |
|--------|-----------|---------|
| **Arbitrary facts** | No learnable pattern; singleton facts appear once in training | Fabricating birthdates for obscure people |
| **Poor models** | Model architecture can't represent the concept | Letter counting fails due to tokenization (D/EEP/SEE/K) |
| **GIGO** | Training data contains errors that get replicated | Conspiracy theories in training corpus |
| **Distribution shift** | Test prompts differ from training distribution | "What's heavier, a pound of feathers or a pound of lead?" |
| **Computational hardness** | Problem is intractable regardless of intelligence | Decryption, NP-hard graph problems |

### Singleton Rate Theorem

The hallucination rate after pretraining is approximately the **singleton rate** -- the fraction of training facts that appear exactly once. If 20% of birthday facts are singletons in the training data, expect at least 20% hallucination on birthday questions. This builds on Turing's Good-Turing missing mass estimator (1953).

### Post-Training Persistence

Hallucinations survive post-training (RLHF, DPO, RLAIF) because:

1. **Binary grading rewards guessing**: Under 0/1 scoring, abstaining (IDK) always scores 0, while guessing has a chance of scoring 1. For any belief distribution over correct answers, the optimal strategy is never to abstain.
2. **Evaluation epidemic**: 9 of 10 major benchmarks (GPQA, MMLU-Pro, IFEval, BBH, MATH, MuSR, Omni-MATH, SWE-bench, HLE) give zero credit for IDK. Models are always in "test-taking mode."
3. **Bluffing incentive**: Like students on exams, models produce overconfident, specific answers ("September 30") rather than hedged ones ("sometime in autumn") because specificity scores better under binary grading.

## Why It Matters

- **Trust erosion**: Hallucinations are the primary barrier to deploying LLMs in high-stakes domains (medicine, law, finance).
- **Not fully solvable by scaling**: The singleton rate bound shows hallucinations are tied to training data coverage, not just model size.
- **RAG reduces but doesn't eliminate**: [[concepts/retrieval-augmented-generation]] helps with extrinsic hallucinations by grounding in retrieved documents, but binary grading still rewards guessing when retrieval fails. RAG doesn't help with intrinsic hallucinations (miscalculations, letter counting).
- **Reasoning models help with some types**: Chain-of-thought reasoning (e.g., DeepSeek-R1) overcomes "poor model" hallucinations by decomposing problems, but doesn't address arbitrary-fact or GIGO hallucinations.

## Key Variants or Approaches

### Detection Methods

- **SelfCheckGPT**: Compare multiple samples for consistency; inconsistency signals hallucination (Manakul et al., 2023)
- **Semantic entropy**: Detect hallucinations by measuring entropy across semantically-clustered samples (Farquhar et al., 2024)
- **Internal activations**: Model activations encode signals about factual accuracy and uncertainty (Kadavath et al., 2022)

### Mitigation Approaches

- **Post-training**: RLHF, RLAIF, DPO reduce GIGO-type hallucinations (conspiracy theories, misconceptions)
- **Retrieval augmentation**: [[concepts/retrieval-augmented-generation]] grounds outputs in external documents
- **Explicit confidence targets**: Proposed by Kalai et al. -- modify eval scoring to penalize wrong answers more than IDK (e.g., "answer only if >75% confident; mistakes penalized 2 points")
- **Behavioral calibration**: Rather than requiring probabilistic confidence outputs, models learn to abstain when confidence is below a stated threshold
- **Fine-tuning for factuality**: Can initially decrease hallucination rates, but rates may later increase with continued training on novel information (Gekhman et al., 2024)

### Inevitability Debate

- **Inevitable for calibrated base models**: Mathematical proof that calibration + density estimation implies errors (Kalai & Vempala, 2024; Kalai et al., 2025)
- **Consistency-breadth tradeoff**: Any model generalizing beyond training data will either hallucinate or suffer mode collapse (Kalavasis et al., 2025; Kleinberg & Mullainathan, 2024)
- **NOT inevitable for all systems**: A Q&A database + calculator + IDK fallback would never hallucinate; the inevitability is specific to general-purpose language models doing density estimation

## Related Concepts

- [[concepts/evaluation]] -- binary grading in benchmarks is the key enabler of persistent hallucination
- [[concepts/guardrails]] -- output validation can catch some hallucinations post-generation
- [[concepts/llm-as-a-judge]] -- LLM judges may incorrectly grade hallucinated long responses as correct
- [[concepts/fine-tuning]] -- post-training techniques (RLHF, DPO) partially mitigate hallucinations
- [[concepts/prompt-engineering]] -- prompting for uncertainty expression or chain-of-thought can reduce some hallucination types

## Related Entities

- [[entities/openai]] -- paper authors; GPT-4 calibration data; proposed evaluation reforms
- [[entities/deepeval]] -- hallucination evaluation tooling
- [[entities/ragas]] -- hallucination metrics (faithfulness, groundedness)

## Source References

- [[sources/why-language-models-hallucinate]] -- primary theoretical framework (Kalai et al., 2025)
- [[sources/rag-eval-metrics]] -- faithfulness and groundedness metrics for detecting hallucination in RAG
- [[sources/setting-up-evaluations-for-llms]] -- practical evaluation setup including hallucination detection
