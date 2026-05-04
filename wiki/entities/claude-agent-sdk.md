---
type: entity
title: "Claude Agent SDK"
category: framework
tags: [anthropic, agents, orchestration]
sources: [sources/claude-architect-exam-guide]
last_updated: 2026-04-23
---

## What It Is

The Claude Agent SDK is Anthropic's framework for building agentic applications with Claude. It provides agent definitions, agentic loop control flow, hook-based interception, subagent spawning, and lifecycle management for production-grade AI agent systems.

## Key Details

- **Agentic loop lifecycle**: send request to Claude, inspect `stop_reason` ("tool_use" to continue, "end_turn" to terminate), execute requested tools, append results to conversation history, repeat
- **Agent definitions**: `AgentDefinition` configuration with descriptions, system prompts, and `allowedTools` restrictions per agent type
- **Subagent spawning**: via `Task` tool — `allowedTools` must include "Task" for coordinators; subagents operate with isolated context (no automatic parent context inheritance)
- **Hooks**: `PostToolUse` for transforming tool results before model processes them; tool call interception hooks for enforcing compliance rules (e.g., blocking refunds above threshold)
- **Session management**: `--resume <session-name>` for named sessions, `fork_session` for parallel exploration branches from shared baseline
- **Parallel execution**: coordinators can spawn parallel subagents by emitting multiple `Task` tool calls in a single response
- **Key anti-patterns**: parsing natural language for loop termination, arbitrary iteration caps as primary stopping mechanism, checking for assistant text content as completion indicator

## How It Fits In

The Claude Agent SDK sits at the **orchestration layer** of the [[concepts/ai-engineering-stack]]. It enables building [[concepts/ai-agents]] with [[concepts/function-calling]] capabilities and coordinating [[concepts/multi-agent-systems]] in hub-and-spoke patterns. It integrates with [[entities/mcp]] for tool/resource access and [[entities/claude-code]] for developer workflows.

## Source References

- [[sources/claude-architect-exam-guide]] — comprehensive coverage across Domain 1 (Agentic Architecture) and Domain 2 (Tool Design)
