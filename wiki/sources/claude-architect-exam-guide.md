---
type: source
title: "Claude Certified Architect – Foundations Exam Guide"
source_file: "Claude Certified Architect – Foundations Certification Exam Guide.pdf"
source_type: pdf
date_ingested: 2026-04-23
tags: [certification, anthropic, agents, prompt-engineering, system-design]
---

## Summary

Official Anthropic exam guide for the Claude Certified Architect – Foundations certification. Covers 5 domains: Agentic Architecture & Orchestration (27%), Tool Design & MCP Integration (18%), Claude Code Configuration & Workflows (20%), Prompt Engineering & Structured Output (20%), and Context Management & Reliability (15%). Tests practical judgment on production tradeoffs across Claude Code, Claude Agent SDK, Claude API, and MCP. Includes 6 exam scenarios, 12 sample questions with explanations, 4 preparation exercises, and a full technology appendix.

## Key Points

- **Exam format**: multiple choice, pass/fail (720/1000 minimum), scenario-based questions drawn from 6 production scenarios
- **Domain 1 — Agentic Architecture (27%)**: agentic loop lifecycle (`stop_reason` "tool_use" vs "end_turn"), hub-and-spoke multi-agent orchestration, subagent context isolation, programmatic enforcement (hooks) vs prompt-based guidance, task decomposition (prompt chaining vs dynamic), session management (`--resume`, `fork_session`)
- **Domain 2 — Tool Design & MCP (18%)**: tool descriptions as primary selection mechanism, MCP `isError` flag for structured errors (transient/validation/permission), scoped tool access (4-5 tools per agent ideal), `tool_choice` options ("auto"/"any"/forced), MCP server scoping (`.mcp.json` project vs `~/.claude.json` user), MCP resources for content catalogs, built-in tools (Read/Write/Edit/Bash/Grep/Glob)
- **Domain 3 — Claude Code Configuration (20%)**: CLAUDE.md hierarchy (user/project/directory), `@import` for modular configs, `.claude/rules/` with YAML frontmatter glob patterns, `.claude/commands/` (project-scoped) vs `~/.claude/commands/` (personal), `.claude/skills/` with `context: fork`, `allowed-tools`, `argument-hint`, plan mode vs direct execution, CI/CD integration (`-p` flag, `--output-format json`, `--json-schema`)
- **Domain 4 — Prompt Engineering (20%)**: explicit criteria over vague instructions, few-shot examples for ambiguous scenarios, `tool_use` with JSON schemas for guaranteed structured output, nullable fields prevent hallucination, validation-retry with error feedback, Message Batches API (50% cost, 24h window, no multi-turn tools), multi-pass review architectures (independent instances beat self-review)
- **Domain 5 — Context Management (15%)**: progressive summarization risks (losing numeric facts), "lost in the middle" effect, trimming verbose tool outputs, persistent "case facts" blocks, structured claim-source mappings for provenance, escalation triggers (customer request, policy gaps, no progress), scratchpad files for long sessions, `/compact` for context reduction
- **Key anti-patterns**: parsing NL for loop termination, arbitrary iteration caps, sentiment-based escalation, generic error messages, giving agents 18+ tools, self-review in same session
- **Key patterns**: programmatic prerequisites for critical sequences, structured handoff summaries, PostToolUse hooks for data normalization, parallel subagent spawning in single turn, stratified random sampling for quality monitoring

## Entities Mentioned

- [[entities/claude-code]] — CLI tool and configuration system (CLAUDE.md, commands, skills, rules)
- [[entities/claude-agent-sdk]] — SDK for building agentic applications with Claude
- [[entities/mcp]] — Model Context Protocol for tool/resource integration
- [[entities/anthropic]] — company behind all tested technologies

## Concepts Covered

- [[concepts/ai-agents]] — agentic loop lifecycle, stop_reason handling, hooks
- [[concepts/multi-agent-systems]] — coordinator-subagent patterns, hub-and-spoke, context isolation
- [[concepts/function-calling]] — tool_choice options, tool_use for structured output
- [[concepts/prompt-engineering]] — few-shot prompting, explicit criteria, iterative refinement
- [[concepts/context-window-management]] — token budgets, summarization risks, position effects
- [[concepts/evaluation]] — human review workflows, confidence calibration, stratified sampling

## Notable Quotes or Data

- "When deterministic compliance is required, prompt instructions alone have a non-zero failure rate" — justifying programmatic hooks over prompt-based enforcement
- "Giving an agent access to too many tools (e.g., 18 instead of 4-5) degrades tool selection reliability"
- "A model retains reasoning context from generation, making it less likely to question its own decisions in the same session" — independent review instances > self-review
- "Aggregate accuracy metrics (e.g., 97% overall) may mask poor performance on specific document types or fields"
- Passing score: 720/1000; 6+ months practical experience recommended

## Related Sources

- [[sources/claude-common-workflows]] — practical Claude Code workflows complementing exam theory
- [[sources/agentic-ai-interview-questions]] — overlapping agent architecture concepts
- [[sources/ai-engineer-requirements]] — AI engineering stack referenced in exam domains
