---
type: concept
title: "Agentic RAG"
aliases: ["agentic retrieval-augmented generation"]
tags: [rag, agents]
sources: [sources/how-agentic-rag-works, sources/rag-techniques, sources/rag-end-to-end, sources/rag-components, sources/rag-terminology]
last_updated: 2026-04-15
---

# Agentic RAG

## Definition

Agentic RAG replaces the linear retrieve-then-generate pipeline of standard [[concepts/retrieval-augmented-generation]] with a control loop. An AI agent evaluates retrieval quality, decides whether to answer or retry, and can route queries to different sources, refine them, or self-correct — all before generating a response.

## How It Works

1. Agent receives query
2. Agent decides which source(s) to query (**routing**)
3. Agent optionally rewrites the query for better retrieval (**[[concepts/query-refinement]]**)
4. Retrieval executes against selected source(s)
5. Agent evaluates results: relevant? complete? consistent? (**self-evaluation**)
6. If insufficient → loop back to step 2 or 3 with different strategy
7. If sufficient → generate response

### Three Core Capabilities
- **Tool use and routing**: selecting the right knowledge source per question type
- **Query refinement**: rewriting queries before and after retrieval
- **Self-evaluation**: judging retrieval quality before committing to generation

### Spectrum of Complexity
- Simple: router selecting between 2-3 knowledge bases
- Medium: [[concepts/react-framework]] with multi-step reasoning and acting
- Advanced: [[concepts/multi-agent-systems]] with orchestrated specialists

## Why It Matters

- Fixes three failure modes of standard RAG: ambiguous queries, scattered evidence, false confidence
- Enables complex multi-source, multi-step question answering
- Reflects broader trend from rigid pipelines to systems with feedback loops

## Key Variants or Approaches

- **Router-based**: simple query routing to different knowledge bases (adaptive retrieval)
- **ReAct-based**: alternating reasoning and retrieval steps
- **Reliable RAG**: validation loop with relevance + grounding checks, re-retrieves on failure
- **Self-RAG**: decides whether to retrieve at all; verifies groundedness before finalizing; retries on weak support
- **CRAG (Corrective RAG)**: scores retrieval quality (0-1); if <0.6, rewrites query and retries with expanded retrieval; optional web search fallback
- **Iterative retrieval**: multi-round retrieve→analyze→follow-up loop until evidence is sufficient (max 3 rounds typical)
- **Sophisticated Controllable Agent**: deterministic decision graph with plan→execute→verify loop; auditable steps
- **Multi-agent**: specialized agents coordinated by an orchestrator
- **[[concepts/graph-rag]]**: graph traversal combined with vector retrieval for multi-hop questions

## Related Concepts

- [[concepts/retrieval-augmented-generation]] -- the base pattern this extends
- [[concepts/ai-agents]] -- the agent architecture enabling the control loop
- [[concepts/react-framework]] -- reasoning + acting framework
- [[concepts/query-refinement]] -- query rewriting sub-capability
- [[concepts/multi-agent-systems]] -- advanced multi-agent variant

## Related Entities

- [[entities/langgraph]] -- framework for building agentic workflows

## Source References

- [[sources/how-agentic-rag-works]] -- primary source, full architecture and trade-offs
- [[sources/rag-techniques]] -- Self-RAG, CRAG, Reliable RAG, Controllable Agent with pseudocode
- [[sources/rag-end-to-end]] -- agentic RAG as "next evolution", CRAG, tool-augmented retrieval
- [[sources/rag-components]] -- agentic RAG plan/search/reason/synthesize pattern
- [[sources/rag-terminology]] -- agentic RAG terminology (planner, executor, self-reflection, memory)
