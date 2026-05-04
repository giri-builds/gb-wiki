---
type: entity
title: "Anthropic"
category: company
tags: [anthropic, llm]
sources: [sources/ai-engineer-requirements, sources/claude-common-workflows]
last_updated: 2026-04-23
---

# Anthropic

## What It Is

Anthropic is an AI safety company that builds the Claude family of large language models. It provides proprietary models accessed via API and SDK, and is one of the leading foundational model providers alongside [[entities/openai]] and Google.

## Key Details

- Builds the **Claude** model family (Claude 4.6 Opus, Sonnet, Haiku)
- Provides the Anthropic SDK for API integration
- Created the [[entities/mcp]] (Model Context Protocol) for agent-tool communication
- [[entities/claude-code]] is their CLI agent tool for software engineering (Plan Mode, worktrees, session management, scheduling)

## How It Fits In

- Part of the **models layer** in the [[concepts/ai-engineering-stack]] (proprietary models)
- SDK proficiency is a key AI engineer skill for 2026
- Claude models used as both generators and evaluators ([[concepts/llm-as-a-judge]])

## Source References

- [[sources/ai-engineer-requirements]] -- Anthropic SDK listed as key proficiency
- [[sources/setting-up-evaluations-for-llms]] -- Claude 4.6 used in multi-model jury evaluation
- [[sources/claude-common-workflows]] -- Claude Code workflows for codebase exploration, debugging, testing, PRs
