---
type: entity
title: "LangGraph"
category: framework
tags: [orchestration, agents]
sources: [sources/ai-projects-2026, sources/agentic-ai-interview-questions, sources/langchain-langgraph-projects]
last_updated: 2026-04-21
---

# LangGraph

## What It Is

LangGraph is a framework for building stateful, multi-step agent workflows as graphs. It extends [[entities/langchain]] with explicit control over agent execution flow, state management, and tool orchestration.

## Key Details

- Designed for complex agentic workflows that go beyond simple chains
- Part of the [[entities/langchain]] ecosystem
- Recommended for production RAG orchestration in AI Projects 2026
- **Graph topology**: supports cycles, conditional edges, and complex state flows (vs LangChain's linear chains)
- **Typed state**: entire graph shares a first-class, strictly typed `AgentState` object; reducers dictate overwrite vs append semantics
- **Native checkpointing**: automatic state serialization at every node boundary to Postgres/Redis; enables "time travel" to past intermediate steps
- **Human-in-the-loop**: execution can pause, await human review, and resume natively
- **When to avoid**: strict latency requirements, complex error handling (circuit breakers), or when team prefers pure Python. Rule of thumb: frameworks for prototyping, custom logic for massive scale.

## How It Fits In

- Sits within the [[concepts/ai-engineering-stack]] orchestration layer
- Implements [[concepts/agentic-rag]] and [[concepts/multi-agent-systems]] patterns
- Complements [[entities/llamaindex]] as an orchestration choice

## Source References

- [[sources/ai-projects-2026]] -- recommended for Project 1 (RAG) orchestration
- [[sources/agentic-ai-interview-questions]] -- LangGraph state management, checkpointing, vs LangChain
- [[sources/langchain-langgraph-projects]] -- 10 enterprise portfolio projects; LangGraph used for all workflows
