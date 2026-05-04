---
type: source
title: "Claude Code Common Workflows"
source_file: "claude_common_workflows.md"
source_type: md
date_ingested: 2026-04-23
tags: [anthropic, tools, prompt-engineering]
---

## Summary

A collection of 6 LinkedIn-style posts introducing Claude Code workflows for beginners. Covers codebase exploration, debugging/refactoring, Plan Mode, test writing and PR creation, Git worktrees for parallel work, and power-user productivity tips (session resumption, Unix piping, scheduling, hooks).

## Key Points

- **Codebase exploration**: start broad ("overview"), go deeper ("trace the login flow"), use `@` references for files/directories
- **Debugging**: share exact errors/stack traces, let Claude see raw output, always end refactoring with "run the tests"
- **Plan Mode**: activated via `Shift+Tab` x2, `--permission-mode plan`, or headless `-p`; iterative refinement before implementation; `Ctrl+G` to edit plan in editor
- **Test generation**: Claude matches existing test style, framework, and assertion patterns; can find uncovered functions
- **PR workflow**: `create a pr` generates title + description via `gh`; `--from-pr 123` resumes context later
- **Git worktrees**: `--worktree <name>` creates isolated branch+directory; `.worktreeinclude` copies gitignored files; auto-cleanup if no changes
- **Session management**: `--continue`, `--resume`, `-n <name>` for named sessions
- **Unix piping**: `cat file | claude -p 'prompt' > output.txt` for scriptable usage
- **Output formats**: `--output-format text|json|stream-json`
- **Scheduling options**: Routines (cloud), Desktop scheduled tasks (local), GitHub Actions (repo events), `/loop` (session polling)
- **Extended thinking**: on by default; `Ctrl+O` to view; "ultrathink" for maximum depth

## Entities Mentioned

- [[entities/claude-code]] — CLI tool for AI-assisted software engineering
- [[entities/anthropic]] — company behind Claude Code

## Concepts Covered

- [[concepts/prompt-engineering]] — structuring requests to Claude Code for best results

## Notable Quotes or Data

- "Claude doesn't just read files — it understands how components connect."
- "Think of Plan Mode as your 'measure twice, cut once' tool."
- "Small, testable increments beat big-bang rewrites every time."
- "These small workflow habits compound fast."

## Related Sources

- [[sources/langchain-langgraph-projects]] — complementary tool ecosystem for AI engineering
