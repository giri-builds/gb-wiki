---
type: concept
title: "LLM Inference Nondeterminism"
aliases: ["inference nondeterminism", "batch invariance", "LLM reproducibility"]
tags: [llm, ml-systems, system-design]
sources: [sources/defeating-nondeterminism-in-llm-inference]
last_updated: 2026-04-20
---

## Definition

LLM inference nondeterminism is the phenomenon where the same prompt with temperature 0 (greedy sampling) produces different outputs across requests to the same model. Contrary to popular belief, this is not caused by GPU thread-level concurrency or atomic adds. The real cause is **lack of batch invariance** -- GPU kernels produce different floating-point results for the same input depending on the batch size, and since server load (which determines batch size) varies unpredictably, users see nondeterministic outputs.

## How It Works

### Root Cause Chain

1. **Floating-point non-associativity**: `(a + b) + c != a + (b + c)` with IEEE floats. Adding numbers in different orders destroys different precision bits, yielding different results.
2. **Batch-size-dependent reduction strategies**: GPU matmul kernels change their internal tiling, split-K strategy, or tensor-core instruction based on batch dimensions. Different strategies sum floating-point numbers in different orders.
3. **Nondeterministic batch size**: in a serving system, concurrent user requests change the batch size that kernels run under. This is unknowable to any individual user.
4. **Result**: from any user's perspective, the same prompt yields different logits, and at token positions where the top-2 probabilities are close, a different token gets selected.

### What Is NOT the Cause

- **Atomic adds / thread-race nondeterminism**: while some GPU kernels use nondeterministic atomic adds, LLM forward passes use none. The forward pass is run-to-run deterministic for fixed inputs.
- **GPU-specific behavior**: the batch-invariance problem affects CPUs and TPUs equally.

### Three Operations That Need Batch Invariance

| Operation | Why It Breaks | Fix | Difficulty |
|-----------|--------------|-----|------------|
| **RMSNorm** | Small batches trigger split-reduction across cores instead of data-parallel | Accept small-batch slowdown or use consistent over-parallel strategy | Easy |
| **Matrix multiplication** | Small M/N triggers split-K or different tensor-core instructions | Compile one kernel config for all shapes; accept ~20% perf loss | Medium |
| **Attention** | Reduces over feature AND sequence dims; chunked prefill / KV cache split changes reduction order | Update KV cache before attention; use fixed split-size (not fixed split-count) for KV dimension | Hard |

### Fixed Split-Size Strategy (Attention)

Standard FlashDecoding divides the KV dimension evenly based on desired parallelism (e.g., KV=1000 / 4 splits = 250 each). This makes the split count batch-dependent. The fix is **fixed split-size**: always split at 256-token boundaries regardless of batch (e.g., KV=1000 becomes three 256-element splits + one 232-element split). This ensures identical reduction order no matter how many query tokens are being processed simultaneously.

## Why It Matters

- **Reproducibility**: scientific experiments with LLMs require deterministic outputs for valid comparisons. Without batch invariance, even temperature=0 produces different results.
- **Evaluation reliability**: nondeterministic outputs undermine benchmark scores and A/B tests.
- **True on-policy RL**: training with RLHF/RLVR requires that the sampling policy and training policy are identical. Inference nondeterminism introduces implicit off-policy divergence (measured as non-zero KL divergence), which can cause reward collapse during training.
- **Debugging**: nondeterministic outputs make it nearly impossible to isolate whether a behavior change came from a code change or random variation.

### Experimental Evidence

- Qwen3-235B at temp=0: 1000 identical requests produced **80 unique completions** without batch-invariant kernels. First divergence at token 103 ("Queens, New York" vs "New York City"). With batch-invariant kernels: **all 1000 identical**.
- True on-policy RL experiment: without off-policy correction, reward collapses at ~step 318 with a corresponding KL divergence spike. With deterministic inference, KL divergence stays at exactly 0.

## Key Variants or Approaches

- **Run-to-run determinism**: same script, same GPU, same inputs always produces same output. Already achieved by most GPU kernels (no atomic adds in LLM forward passes).
- **Batch invariance**: output for a given element is identical regardless of other elements in the batch. Requires custom kernel implementations.
- **Batch-position invariance**: output is independent of where the element sits within the batch. Most matmul libraries have this, but stream-k matmuls do not.
- **Hardware/software version invariance**: same results across different GPU models or PyTorch versions. Not generally achievable.

## Related Concepts

- [[concepts/llm-hallucination]] -- nondeterminism is a separate problem from hallucination; even correct outputs may vary token-by-token
- [[concepts/evaluation]] -- nondeterministic outputs undermine benchmark reliability
- [[concepts/fine-tuning]] -- on-policy RL training is implicitly degraded by inference nondeterminism

## Related Entities

- [[entities/openai]] -- ChatGPT exhibits nondeterminism even at temperature 0

## Source References

- [[sources/defeating-nondeterminism-in-llm-inference]] -- full technical analysis with batch-invariant kernel implementations
