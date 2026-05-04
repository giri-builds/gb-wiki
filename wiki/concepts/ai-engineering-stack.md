---
type: concept
title: "AI Engineering Stack"
aliases: ["AI stack", "AI application stack"]
tags: [system-design, ai-fundamentals]
sources: [sources/ai-engineer-requirements]
last_updated: 2026-04-14
---

# AI Engineering Stack

## Definition

The AI engineering stack is a four-layer architecture that describes how production AI applications are built. Each layer builds on the one below, from foundational models at the bottom to user-facing applications at the top.

## How It Works

### Layer 1 — Models (Foundation)
- **Proprietary models**: accessed via API from [[entities/openai]], [[entities/anthropic]], Google
- **Open-source models**: run independently or via inference providers ([[entities/ollama]], Fireworks AI, Groq)
- Engineers must understand trade-offs between models — different strengths and failure modes

### Layer 2 — Retrieval
- Gives AI apps access to external knowledge (company docs, product info)
- [[concepts/embeddings]]: text converted to numerical vectors
- [[concepts/vector-databases]]: [[entities/pinecone]], [[entities/weaviate]], [[entities/chromadb]]
- Retrieval strategies: hybrid search, [[concepts/re-ranking]]

### Layer 3 — Orchestration
- Manages application logic, connects models to retrieval and tools
- Frameworks: [[entities/langchain]], [[entities/llamaindex]], [[entities/langgraph]]
- Capabilities: chaining, [[concepts/function-calling]], memory, planning

### Layer 4 — Application
- User interfaces (chatbots, co-pilots, assistants)
- Exposed APIs ([[entities/fastapi]])
- Integrations into existing software ecosystems

### Cross-cutting: Production & Observability
- Deployment: [[entities/docker]], Kubernetes
- Monitoring: [[entities/langsmith]], [[entities/langfuse]]
- [[concepts/evaluation]]: measuring accuracy and quality

## Why It Matters

- Provides a mental map for understanding where any tool, framework, or technique fits
- Helps AI engineers communicate about architecture decisions
- Defines the skill areas needed for the AI engineer role in 2026

## Related Concepts

- [[concepts/retrieval-augmented-generation]] -- primary pattern using layers 1-3
- [[concepts/observability]] -- cross-cutting production concern
- [[concepts/evaluation]] -- cross-cutting quality concern

## Source References

- [[sources/ai-engineer-requirements]] -- primary source defining all four layers
