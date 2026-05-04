---
type: concept
title: "Context Window Management"
aliases: ["context management", "token budgets", "context optimization"]
tags: [llm, system-design, agents]
sources: [sources/claude-architect-exam-guide, sources/context-engineering]
last_updated: 2026-04-23
---

## Definition

Context window management is the set of strategies for effectively using an LLM's finite input token budget across long conversations, multi-turn interactions, and multi-agent pipelines. Poor management leads to information loss, degraded output quality, and increased cost.

## How It Works

### Key Challenges

- **Progressive summarization risks**: condensing conversation history loses numerical values, percentages, dates, and customer-stated expectations into vague summaries
- **"Lost in the middle" effect**: models reliably process information at the beginning and end of long inputs but may omit findings from middle sections
- **Tool result bloat**: tool outputs accumulate in context disproportionate to their relevance (e.g., 40+ fields per order lookup when only 5 are relevant)
- **Context degradation**: in extended sessions, models start giving inconsistent answers and referencing "typical patterns" rather than specific discoveries from earlier

### Mitigation Strategies

- **Persistent "case facts" blocks**: extract transactional facts (amounts, dates, IDs, statuses) into a structured block included in each prompt, outside summarized history
- **Tool output trimming**: keep only relevant fields from verbose tool responses before they accumulate in context
- **Position-aware ordering**: place key findings summaries at the beginning of aggregated inputs; organize detailed results with explicit section headers
- **Structured subagent outputs**: require metadata (dates, sources, relevance scores) instead of verbose reasoning chains when downstream agents have limited budgets
- **Scratchpad files**: persist key findings across context boundaries in files that agents reference for subsequent questions
- **Subagent delegation**: isolate verbose exploration output in subagents while the main agent preserves high-level coordination
- **`/compact` command**: reduce context usage during extended exploration sessions

### Multi-Agent Context Patterns

- Subagent context must be explicitly provided in prompts — no automatic parent context inheritance
- Structured claim-source mappings preserve provenance through synthesis steps
- Upstream agents should return key facts and citations, not verbose content and reasoning chains
- Crash recovery via structured state exports (manifests) that coordinators load on resume

## Why It Matters

Context limits are the primary constraint on complex agentic workflows. Without deliberate management, agents lose critical information mid-conversation, produce inconsistent outputs, and waste tokens on irrelevant context. Effective context management directly impacts agent reliability, accuracy, and cost efficiency.

## Related Concepts

- [[concepts/context-engineering]] — parent discipline; context window management is one dimension of CE
- [[concepts/ai-agents]] — agents require careful context budgeting across tool calls
- [[concepts/multi-agent-systems]] — context isolation between coordinator and subagents
- [[concepts/prompt-engineering]] — prompt structure affects how context is utilized
- [[concepts/llm-hallucination]] — context loss can increase hallucination rates

## Related Entities

- [[entities/claude-code]] — provides `/compact` and session management for context control
- [[entities/claude-agent-sdk]] — manages context across agentic loops and subagent spawning

## Source References

- [[sources/claude-architect-exam-guide]] — Domain 5: Context Management & Reliability (15% of exam)
- [[sources/context-engineering]] — layered memory architecture, self-baking, context selection factors, lifelong context challenges
