---
type: source
title: "Context Engineering 2.0: The Context of Context Engineering"
source_file: "Context Engineering.pdf"
source_type: pdf
date_ingested: 2026-04-23
tags: [prompt-engineering, agents, system-design, llm, ai-fundamentals]
---

## Summary

Academic paper from SJTU/SII/GAIR (arXiv:2510.26493, Oct 2025) providing a systematic theoretical framework for context engineering. Argues context engineering is not a recent LLM invention but a 20+ year discipline tracing back to 1990s ubiquitous computing and HCI. Proposes a four-era evolutionary model (1.0 primitive computing → 2.0 agent-centric → 3.0 human-level → 4.0 superhuman) and frames context engineering as entropy reduction — transforming high-entropy human intentions into low-entropy machine-understandable representations. Covers context collection, storage, management (textual processing, multimodal fusion, memory organization, context abstraction/self-baking), and usage (intra/cross-system sharing, context selection, proactive inference, lifelong preservation).

## Key Points

- **Formal definition**: context engineering is the systematic process of designing and optimizing context collection, storage, management, and usage to enhance machine understanding and task performance
- **Core insight**: context engineering is entropy reduction — bridging the cognitive gap between human (carbon-based) and machine (silicon-based) intelligence; more machine intelligence = lower human interaction cost
- **Four-era model**: 1.0 (1990s-2020, primitive computing, context as translation), 2.0 (2020-present, agents, context as instruction), 3.0 (future, human-level, context as scenario), 4.0 (speculative, superhuman, context as world). Currently in Era 2.0 transitioning to 3.0
- **Era 1.0 foundations**: Dey's 2001 definition of context, Context Toolkit (Widgets, Interpreters, Aggregators, Services, Discoverers), context-aware computing, ubiquitous computing (Mark Weiser 1991)
- **Era 2.0 shifts**: from structured inputs to human-native signals; from passive sensing to active understanding; from context-aware to context-cooperative systems
- **Context management strategies**: timestamp tagging, functional/semantic tagging, compression via QA pairs, hierarchical notes, multimodal fusion (shared vector space, self-attention, cross-attention)
- **Memory architecture**: layered model — short-term (temporal relevance) and long-term (importance-weighted); LLM context window analogous to RAM with context engineering as the OS deciding what to load
- **Context isolation**: subagents as functional isolation units (Claude Code example); lightweight references for token overhead reduction
- **Self-baking**: agents digest raw context into persistent knowledge structures — NL summaries, fixed schema extraction, hierarchical memory, progressive vector compression; "separates memory storage from learning"
- **Context selection factors**: semantic relevance, logical dependency, recency/frequency, overlapping information filtering, user preference adaptation
- **Cross-agent sharing patterns**: embedding context into prompts, structured message exchange, shared memory (memory blocks, blackboards, graph-based)
- **KV caching practices**: stable prefix prompts, append-only updates, deterministic serialization, cache warm-up/prefetch
- **Tool design insights**: precise descriptions and limited scale (DeepSeek-v3 performance declines beyond 30 tools, near-guaranteed failure beyond 100)
- **Design principles**: Minimal Sufficiency (collect only necessary context), Semantic Continuity (maintain meaning, not just data)
- **Lifelong challenges**: storage bottlenecks, O(n²) attention degradation, system instability from accumulated errors, evaluation difficulty

## Entities Mentioned

- [[entities/claude-code]] — cited for structured notes, subagent context isolation, and self-baking memory patterns
- [[entities/langchain]] — referenced as Era 2.0 system
- [[entities/anthropic]] — cited for Claude's context engineering practices

## Concepts Covered

- [[concepts/context-engineering]] — core subject; formal definition and four-era framework
- [[concepts/context-window-management]] — memory architecture, self-baking, context selection
- [[concepts/prompt-engineering]] — positioned as subset of context engineering 2.0
- [[concepts/retrieval-augmented-generation]] — RAG pipelines as context engineering mechanism
- [[concepts/multi-agent-systems]] — cross-agent context sharing patterns
- [[concepts/ai-agents]] — agent-centric intelligence as Era 2.0 driver
- [[concepts/embeddings]] — multimodal fusion into shared vector spaces

## Notable Quotes or Data

- "Context engineering is the systematic process of designing and optimizing context collection, storage, management, and usage to enhance machine understanding"
- "AI coding performance often decreases when context windows exceed roughly 50% fullness"
- "DeepSeek-v3 performance declined beyond 30 tools and was nearly guaranteed to fail beyond 100"
- "Self-baking is what separates memory storage from learning. Without self-baking, agents simply recall; with it, they accumulate knowledge"
- "The more intelligent machines are, the more natural context engineering becomes, and the lower the cost of human-machine interaction"

## Related Sources

- [[sources/claude-architect-exam-guide]] — overlapping coverage of context management (Domain 5) and tool design
- [[sources/claude-common-workflows]] — practical context engineering via Claude Code
