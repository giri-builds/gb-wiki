---
type: entity
title: "LangChain"
category: framework
tags: [orchestration, rag, agents]
sources: [sources/ai-projects-2026, sources/ai-engineer-requirements, sources/setting-up-evaluations-for-llms, sources/agentic-ai-interview-questions, sources/langchain-langgraph-projects]
last_updated: 2026-04-21
---

# LangChain

## What It Is

LangChain is an open-source framework for building applications powered by large language models. It provides abstractions for chaining multiple LLM calls, managing conversation memory, integrating external tools, and building agent workflows.

## Key Details

- Used in the **orchestration layer** of the AI engineering stack
- Supports chaining (output of one LLM call feeds the next), tool use (function calling), and memory/planning
- Ecosystem includes [[entities/langgraph]] (agent workflows), [[entities/langsmith]] (observability), and LangChain Hub (shared prompts)
- Commonly paired with vector databases like [[entities/chromadb]], [[entities/weaviate]], and [[entities/pinecone]] for RAG

### Architectural Limitations

- **Linear execution**: classic AgentExecutor is deeply sequential and struggles with parallelism
- **Opaque abstractions**: complex internal stack traces make debugging difficult
- **Stateful rigidity**: intermediate steps are hard to manipulate or query manually
- [[entities/langgraph]] replaces classic LangChain agents for complex workflows

## How It Fits In

- Core orchestration framework alongside [[entities/llamaindex]] in the [[concepts/ai-engineering-stack]]
- Implements [[concepts/retrieval-augmented-generation]], [[concepts/function-calling]], and [[concepts/multi-agent-systems]]
- LangChain Hub provides shared eval prompts used with [[concepts/llm-as-a-judge]]

## Source References

- [[sources/ai-projects-2026]] -- recommended for Project 1 (RAG) orchestration
- [[sources/ai-engineer-requirements]] -- listed as key orchestration framework skill
- [[sources/setting-up-evaluations-for-llms]] -- parent ecosystem for LangSmith
- [[sources/agentic-ai-interview-questions]] -- architectural limitations discussed (Q21)
- [[sources/langchain-langgraph-projects]] -- 10 enterprise portfolio projects using LangChain + LangGraph
