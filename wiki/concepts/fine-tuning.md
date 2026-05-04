---
type: concept
title: "Fine-Tuning"
aliases: ["model fine-tuning", "LLM fine-tuning"]
tags: [fine-tuning, llm]
sources: [sources/ai-projects-2026]
last_updated: 2026-04-14
---

# Fine-Tuning

## Definition

Fine-tuning is the process of further training a pre-trained LLM on task-specific data to improve performance on particular tasks where prompting alone falls short — such as structured JSON extraction, tool call accuracy, or domain-specific language.

## How It Works

### Phase 1 — Supervised Fine-Tuning (SFT)
- Train on curated input→output pairs for the target task
- Use parameter-efficient methods like [[concepts/lora]] or QLoRA to reduce compute requirements
- Trainable on single GPUs (A100, T4) with QLoRA

### Phase 2 — Preference Tuning (DPO)
- Show the model comparisons of "good" vs "bad" outputs
- Direct Preference Optimization aligns the model without requiring a reward model
- Improves output quality beyond what SFT achieves alone

## Why It Matters

- Fills the gap when prompting falls short on specific tasks
- Parameter-efficient methods (LoRA/QLoRA) make it accessible on modest hardware
- Key skill for AI engineers — knowing **when** to fine-tune vs when to prompt

## Key Variants or Approaches

- **SFT**: supervised fine-tuning on labeled data
- **DPO**: direct preference optimization from comparisons
- **RLHF**: reinforcement learning from human feedback (heavier-weight)
- **[[concepts/lora]]**: parameter-efficient adapter approach

## Related Concepts

- [[concepts/lora]] -- parameter-efficient fine-tuning technique
- [[concepts/prompt-engineering]] -- alternative to fine-tuning for many tasks

## Related Entities

- [[entities/hugging-face]] -- TRL library for SFT and DPO
- [[entities/ollama]] -- running fine-tuned models locally

## Source References

- [[sources/ai-projects-2026]] -- Project 4 with two-phase SFT→DPO approach
