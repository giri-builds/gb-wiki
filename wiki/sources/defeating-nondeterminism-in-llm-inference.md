---
type: source
title: "Defeating Nondeterminism in LLM Inference"
source_file: "Defeating Nondeterminism in LLM Inference.pdf"
source_type: pdf
date_ingested: 2026-04-20
tags: [llm, ml-systems, system-design]
---

## Summary

Technical blog post by Horace He / Thinking Machines Lab (September 2025) explaining why LLM inference is nondeterministic even at temperature 0, debunking the common "concurrency + floating point" hypothesis. The real culprit is **batch invariance** -- GPU kernels produce different floating-point results for the same input element depending on the batch size, and since server load (which determines batch size) varies nondeterministically, users see nondeterministic outputs. The post provides solutions for making RMSNorm, matrix multiplication, and attention kernels batch-invariant, with a working implementation on vLLM. Experiments show 1000 temp=0 completions produce 80 unique results without the fix, but become perfectly identical with batch-invariant kernels.

## Key Points

- **The "concurrency + floating point" hypothesis is mostly wrong for LLM inference** -- all kernels in an LLM forward pass are run-to-run deterministic (no atomic adds needed). The same script on the same GPU always produces the same output.
- **Floating-point non-associativity is the root cause of numerical differences**: `(a + b) + c != a + (b + c)` with floats. Adding numbers in different orders yields different results (an 8-element array can produce 102 unique sums depending on order).
- **Batch invariance is the missing property**: matrix multiplication results for a given input element change depending on the batch size (demonstrated empirically: max difference of 1669.25 between batch=1 and batch=2048 in bfloat16).
- **Nondeterminism = batch-size-dependent numerics + nondeterministic server load**: since concurrent user requests change the batch size, and batch size changes reduction strategies, individual users see nondeterministic results.
- **This is NOT GPU-specific** -- CPU and TPU inference endpoints have the same nondeterminism source.
- **Three operations need batch invariance** in a transformer: RMSNorm, matrix multiplication, and attention (ordered by difficulty).
- **RMSNorm**: naturally batch-invariant with data-parallel strategy (one batch element per core); only breaks when batch becomes too small and split reduction is needed.
- **Matrix multiplication**: batch invariance breaks when small batch sizes require split-K or different tensor core instructions. Fix: compile one kernel config for all shapes (~20% performance loss vs cuBLAS).
- **Attention is hardest**: reduces over both feature and sequence dimensions; must handle chunked prefill and prefix caching. Fix: use fixed split-size (not fixed split-count) for KV dimension; update KV cache before attention kernel.
- **Experimental results**: Qwen3-235B at temp=0, 1000 completions of "Tell me about Richard Feynman" produced 80 unique completions (first divergence at token 103). With batch-invariant kernels: all 1000 identical.
- **Performance overhead**: vLLM default 26s vs deterministic 42s (improved attention) for 1000 sequences -- about 60% overhead, acceptable for reproducibility-critical workloads.
- **True on-policy RL**: deterministic inference enables bitwise-identical results between sampler and trainer, achieving 0 KL divergence. Without this, on-policy RL is implicitly off-policy, which can cause reward collapse.
- **Implementation**: released as `thinking-machines-lab/batch-invariant-ops` library, integrates with vLLM via `torch.Library` for operator substitution.

## Entities Mentioned

- [[entities/openai]] -- ChatGPT referenced as example of nondeterministic API

## Concepts Covered

- [[concepts/llm-inference-nondeterminism]] -- core topic: why LLM inference is nondeterministic and how to fix it
- [[concepts/fine-tuning]] -- RLHF/on-policy RL training affected by inference nondeterminism

## Notable Quotes or Data

- "The primary reason nearly all LLM inference endpoints are nondeterministic is that the load (and thus batch-size) nondeterministically varies!"
- "Running the same matrix multiplication on the same data repeatedly will always provide bitwise equal results" -- individual kernels are deterministic
- Qwen3-235B temp=0: 80 unique completions out of 1000 requests (992 said "Queens, New York", 8 said "New York City" at token 103)
- Max difference between batch=1 and batch=2048 matmul: 1669.25 (bfloat16, [2048,4096] x [4096,4096])
- True on-policy RL: 0 KL divergence between sampler and trainer; without it, RL can crash around step 318

## Related Sources

- [[sources/why-language-models-hallucinate]] -- complementary view: statistical causes of LLM errors vs computational causes of nondeterminism
