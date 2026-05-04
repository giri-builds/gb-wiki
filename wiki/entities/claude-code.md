---
type: entity
title: "Claude Code"
category: tool
tags: [anthropic, tools]
sources: [sources/claude-common-workflows, sources/claude-architect-exam-guide]
last_updated: 2026-04-23
---

## What It Is

Claude Code is Anthropic's official CLI tool for AI-assisted software engineering. It provides an interactive agent that reads, understands, and modifies codebases through natural language conversation, with access to file editing, terminal commands, and version control.

## Key Details

- **Interfaces**: CLI terminal, desktop app (Mac/Windows), web app (claude.ai/code), IDE extensions (VS Code, JetBrains)
- **Plan Mode**: read-only analysis mode activated via `Shift+Tab` x2 or `--permission-mode plan`; iterative refinement before implementation
- **Git worktrees**: `--worktree <name>` creates isolated working copies for parallel feature development
- **Session management**: `--continue` (resume last), `--resume` (browse all), `-n <name>` (named sessions), `--from-pr N` (resume PR context)
- **Unix integration**: supports piping (`cat file | claude -p 'prompt'`), output formats (text/json/stream-json), scriptable in CI/CD
- **Test generation**: analyzes existing test patterns and generates tests matching project style and framework
- **PR creation**: auto-generates title and description via `gh` CLI
- **Scheduling**: Routines (cloud-based), desktop scheduled tasks, GitHub Actions integration, `/loop` for session polling
- **Extended thinking**: on by default; `Ctrl+O` to view reasoning; "ultrathink" for maximum depth
- **CLAUDE.md hierarchy**: user-level (`~/.claude/CLAUDE.md`), project-level (`.claude/CLAUDE.md` or root `CLAUDE.md`), directory-level (subdirectory `CLAUDE.md` files); `@import` for modular configs
- **`.claude/rules/`**: topic-specific rule files with YAML frontmatter `paths` fields containing glob patterns for conditional activation (e.g., `paths: ["**/*.test.tsx"]`)
- **Commands**: project-scoped in `.claude/commands/` (version-controlled) vs personal in `~/.claude/commands/`
- **Skills**: `.claude/skills/` with `SKILL.md` frontmatter supporting `context: fork` (isolated sub-agent), `allowed-tools`, and `argument-hint`
- **CI/CD integration**: `-p`/`--print` flag for non-interactive mode; `--output-format json` and `--json-schema` for structured CI output; session context isolation (independent review instances beat self-review)
- **Built-in tools**: Read, Write, Edit, Bash, Grep, Glob — Grep for content search, Glob for file path patterns, Edit for targeted modifications, Read+Write fallback when Edit can't find unique text
- **Explore subagent**: isolates verbose discovery output, returns summaries to preserve main conversation context

## How It Fits In

Claude Code is a key component of the [[concepts/ai-engineering-stack]] at the application layer. It leverages Claude LLMs from [[entities/anthropic]] and integrates with version control (Git/GitHub) and CI/CD pipelines. It competes with GitHub Copilot, Cursor, and other AI coding assistants but differentiates through its agentic CLI-first approach with full codebase understanding.

## Source References

- [[sources/claude-common-workflows]] — 6 workflow guides covering exploration, debugging, Plan Mode, testing, worktrees, and power-user tips
- [[sources/claude-architect-exam-guide]] — Domain 3: Claude Code Configuration & Workflows (20% of exam); CLAUDE.md hierarchy, rules, commands, skills, CI/CD integration
