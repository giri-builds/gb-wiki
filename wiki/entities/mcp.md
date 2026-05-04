---
type: entity
title: "MCP (Model Context Protocol)"
category: protocol
tags: [agents, anthropic]
sources: [sources/ai-engineer-requirements, sources/claude-architect-exam-guide]
last_updated: 2026-04-23
---

# MCP (Model Context Protocol)

## What It Is

MCP (Model Context Protocol) is an open protocol created by [[entities/anthropic]] that standardizes how AI agents communicate with external tools, data sources, and services. It provides a universal interface for agent-tool interaction.

## Key Details

- Standardizes tool discovery and invocation for AI agents
- Enables agents to interact with databases, APIs, file systems, and other services through a common protocol
- Complementary to Google's [[entities/a2a-protocol]] (agent-to-agent communication)
- **MCP tools**: action-oriented interfaces the agent can invoke; tool descriptions are the primary mechanism LLMs use for selection — minimal descriptions cause misrouting
- **MCP resources**: content catalogs (issue summaries, documentation hierarchies, database schemas) that reduce exploratory tool calls
- **`isError` flag**: structured error pattern with categories (transient/validation/permission), `isRetryable` boolean, and human-readable descriptions
- **Server scoping**: project-level (`.mcp.json`) for shared team tooling vs user-level (`~/.claude.json`) for personal/experimental servers
- **Environment variables**: `.mcp.json` supports `${GITHUB_TOKEN}` expansion for credential management without committing secrets
- **Tool distribution principle**: 4-5 tools per agent is ideal; 18+ tools degrades selection reliability

## How It Fits In

- Key protocol for [[concepts/multi-agent-systems]] and [[concepts/function-calling]]
- Part of the agent communication infrastructure in the [[concepts/ai-engineering-stack]]
- Mastering MCP is a 2026 AI engineer requirement

## Source References

- [[sources/ai-engineer-requirements]] -- listed as key protocol for agentic systems
- [[sources/claude-architect-exam-guide]] -- Domain 2: Tool Design & MCP Integration (18% of exam); server scoping, error patterns, tool descriptions, resources
