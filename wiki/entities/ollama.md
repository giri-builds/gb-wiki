---
type: entity
title: "Ollama"
category: tool
tags: [slm, tools]
sources: [sources/ai-projects-2026]
last_updated: 2026-04-14
---

# Ollama

## What It Is

Ollama is a local model runner that allows you to download and run open-source LLMs entirely offline on your own hardware. It handles model management, quantization formats, and provides a simple API for inference.

## Key Details

- Runs models like Llama 3.2, Phi-4, Mistral 7B locally
- Supports quantized formats (GGUF Q4/Q5) for performance/quality trade-offs
- Useful for privacy-sensitive, low-latency, or cost-constrained deployments
- Can be wrapped with [[entities/fastapi]] for API access

## How It Fits In

- Enables [[concepts/small-language-models]] deployment on local hardware
- Alternative to cloud API providers like [[entities/openai]] and [[entities/anthropic]]

## Source References

- [[sources/ai-projects-2026]] -- core tool for Project 2 (Local AI Assistant)
