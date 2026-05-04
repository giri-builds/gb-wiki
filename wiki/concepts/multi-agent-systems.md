---
type: concept
title: "Multi-Agent Systems"
aliases: ["multi-agent", "agent orchestration"]
tags: [agents, system-design]
sources: [sources/how-agentic-rag-works, sources/ai-engineer-requirements, sources/claude-architect-exam-guide]
last_updated: 2026-04-23
---

# Multi-Agent Systems

## Definition

Multi-agent systems are architectures where multiple specialized AI agents collaborate to accomplish complex tasks, coordinated by an orchestrator agent. Each agent has a specific role, tools, and domain expertise.

## How It Works

### Hub-and-Spoke Architecture (Claude Agent SDK)

- **Coordinator agent** manages all inter-subagent communication, error handling, and information routing
- **Subagents operate with isolated context** — they do not inherit the coordinator's conversation history automatically
- Coordinator handles: task decomposition, delegation, result aggregation, and dynamic subagent selection based on query complexity
- **Parallel spawning**: coordinators emit multiple `Task` tool calls in a single response for concurrent subagent execution
- **Iterative refinement loops**: coordinator evaluates synthesis output for gaps, re-delegates to search/analysis subagents with targeted queries, re-invokes synthesis until coverage is sufficient

### Context Passing Patterns

- Subagent context must be explicitly provided in the prompt — include complete findings from prior agents
- Use structured data formats to separate content from metadata (source URLs, document names, page numbers) for attribution
- Design coordinator prompts with research goals and quality criteria, not step-by-step procedures

### Error Propagation

- Return structured error context: failure type, attempted query, partial results, alternative approaches
- Distinguish access failures (timeouts) from valid empty results (no matches)
- Subagents implement local recovery for transient failures; propagate only unresolvable errors to coordinator
- Anti-patterns: generic error statuses, silently suppressing errors, terminating entire workflows on single failures

### General Pattern

- **Orchestrator agent** decomposes tasks and routes to specialists
- **Specialist agents** handle specific domains (search, analysis, code, etc.)
- Agents communicate via protocols like [[entities/mcp]] (agent-to-tool) and [[entities/a2a-protocol]] (agent-to-agent)
- Results are aggregated and synthesized by the orchestrator

## Why It Matters

- Enables complex tasks that exceed any single agent's capability
- Allows specialization — each agent optimized for its domain
- Represents the most advanced end of the [[concepts/agentic-rag]] spectrum

## Related Concepts

- [[concepts/ai-agents]] -- the building blocks
- [[concepts/agentic-rag]] -- multi-agent variant for retrieval
- [[concepts/function-calling]] -- how agents interact with tools

- [[concepts/context-window-management]] -- critical for managing token budgets across agents

## Related Entities

- [[entities/claude-agent-sdk]] -- Anthropic's framework for coordinator-subagent patterns
- [[entities/mcp]] -- agent-to-tool communication protocol
- [[entities/a2a-protocol]] -- agent-to-agent communication protocol
- [[entities/langgraph]] -- framework for multi-agent workflows

## Source References

- [[sources/how-agentic-rag-works]] -- multi-agent as most advanced agentic RAG form
- [[sources/ai-engineer-requirements]] -- multi-agent systems as key 2026 skill
- [[sources/claude-architect-exam-guide]] -- coordinator-subagent patterns, context passing, error propagation, parallel execution (Domain 1, 27% of exam)
