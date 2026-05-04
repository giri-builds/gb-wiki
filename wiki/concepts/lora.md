---
type: concept
title: "LoRA"
aliases: ["Low-Rank Adaptation", "QLoRA"]
tags: [fine-tuning, llm]
sources: [sources/ai-projects-2026]
last_updated: 2026-04-14
---

# LoRA

## Definition

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that freezes the pre-trained model weights and injects small trainable rank-decomposition matrices into each layer. QLoRA extends this by quantizing the base model to 4-bit precision, further reducing memory requirements.

## How It Works

- Base model weights are frozen (not modified during training)
- Small adapter matrices are added to attention layers
- Only the adapter parameters are trained — typically <1% of total parameters
- QLoRA additionally quantizes the base model to 4-bit (GGUF Q4/Q5 formats)
- At inference, adapters are merged with the base model or applied on-the-fly

## Why It Matters

- Makes [[concepts/fine-tuning]] accessible on single consumer/cloud GPUs (T4, A100)
- Dramatically reduces memory and compute requirements
- Enables fine-tuning of large models (7B-70B) that wouldn't fit in memory otherwise

## Related Concepts

- [[concepts/fine-tuning]] -- the broader process LoRA enables
- [[concepts/small-language-models]] -- LoRA/QLoRA often applied to smaller models

## Related Entities

- [[entities/hugging-face]] -- TRL and Axolotl support LoRA/QLoRA training

## Source References

- [[sources/ai-projects-2026]] -- QLoRA recommended for Project 4 fine-tuning on single GPU
