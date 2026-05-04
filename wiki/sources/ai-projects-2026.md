---
type: source
title: "AI Projects 2026"
source_file: "AI Projects 2026.md"
source_type: md
date_ingested: 2026-04-14
tags: [project-ideas, rag, fine-tuning, observability, slm]
---

# AI Projects 2026

## Summary

A guide recommending five production-grade AI engineering projects for 2026, each with detailed descriptions and tech stacks. The projects progress from foundational (RAG) to advanced (real-time multimodal), covering the full AI engineering stack. Emphasis is on moving beyond demos to production-ready systems with proper evaluation, monitoring, and optimization.

## Key Points

- **Project 1 — Production RAG**: Domain-specific "ask my doc" system with hybrid retrieval (BM25 + vector), cross-encoder re-ranking, and faithfulness evaluation via Ragas
- **Project 2 — Local AI Assistant (SLMs)**: Run open-source models offline with Ollama; benchmark inference performance; compare quantized models (GGUF Q4/Q5)
- **Project 3 — Monitoring & Observability**: Instrument every pipeline step with tracing; track SRE-style metrics (P50/P95 latency, cost per request, failure rates)
- **Project 4 — Fine-Tuning**: Two phases — SFT with LoRA/QLoRA on clean data, then DPO preference tuning for alignment
- **Project 5 — Real-Time Multimodal**: Voice assistant pipeline with ASR → LLM → TTS; latency budget analysis per component
- Tech stacks span: LangChain/LangGraph, ChromaDB/Weaviate, Cohere re-ranker, Ollama, Llama 3.2/Phi-4/Mistral 7B, FastAPI, LangSmith/Langfuse, HF TRL/Axolotl, Deepgram/Whisper, ElevenLabs/Cartesia

## Entities Mentioned

- [[entities/langchain]] -- orchestration framework
- [[entities/langgraph]] -- agent workflow framework
- [[entities/chromadb]] -- vector database
- [[entities/weaviate]] -- vector database
- [[entities/cohere]] -- re-ranker provider
- [[entities/ollama]] -- local model runner
- [[entities/fastapi]] -- API framework
- [[entities/langsmith]] -- observability platform
- [[entities/langfuse]] -- open-source observability
- [[entities/hugging-face]] -- ML platform (TRL, Axolotl)
- [[entities/ragas]] -- RAG evaluation framework
- [[entities/deepgram]] -- speech recognition
- [[entities/pydantic]] -- data validation library

## Concepts Covered

- [[concepts/retrieval-augmented-generation]] -- production RAG with hybrid retrieval
- [[concepts/re-ranking]] -- cross-encoder re-ranking for precision
- [[concepts/small-language-models]] -- offline/edge inference with quantized models
- [[concepts/observability]] -- tracing, metrics, cost tracking for AI systems
- [[concepts/fine-tuning]] -- SFT and DPO for task-specific adaptation
- [[concepts/lora]] -- parameter-efficient fine-tuning
- [[concepts/multimodal-ai]] -- voice assistants, real-time streaming

## Notable Quotes or Data

- Quantized model formats: GGUF Q4 and Q5 for quality vs speed trade-off analysis
- Recommended compute for fine-tuning: single A100 or T4 GPU with QLoRA
- Observability metrics: P50/P95 latency, cost per request, failure rates

## Related Sources

- [[sources/ai-engineer-requirements]] -- overlapping tech stack coverage
- [[sources/setting-up-evaluations-for-llms]] -- evaluation connects to Project 3
