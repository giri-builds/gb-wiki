---
type: entity
title: "FastAPI"
category: framework
tags: [api-development, tools]
sources: [sources/ai-projects-2026, sources/ai-engineer-requirements]
last_updated: 2026-04-14
---

# FastAPI

## What It Is

FastAPI is a modern Python web framework for building APIs, known for high performance, automatic documentation, and native support for async operations and type validation via [[entities/pydantic]].

## Key Details

- Used to build API endpoints that serve AI model capabilities
- Part of the **application layer** in the [[concepts/ai-engineering-stack]]
- Commonly used as a wrapper for local model inference (e.g., with [[entities/ollama]])
- Paired with [[entities/docker]] for containerized deployment

## How It Fits In

- Serves the **application layer** of the AI stack — exposing AI capabilities as REST endpoints
- Key skill for AI engineers alongside [[entities/docker]] and [[entities/kubernetes]]

## Source References

- [[sources/ai-projects-2026]] -- recommended for Project 2 (Local AI Assistant) API wrapper
- [[sources/ai-engineer-requirements]] -- listed as deployment tool
