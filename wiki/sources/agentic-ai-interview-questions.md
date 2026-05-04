---
type: source
title: "25 Agentic AI Interview Questions"
source_file: "Agentic AI Interview Qtns.pdf"
source_type: pdf
date_ingested: 2026-04-20
tags: [agents, interview-prep, orchestration]
---

## Summary

Social media carousel by Naresh Edagotti (PracticAI) presenting 25 agentic AI interview questions with concise bullet-point answers. Organized into 5 categories: core understanding of agents, reactive vs deliberative agents, tool-calling agents, ReAct pattern and reasoning loops, and LangChain/LangGraph. Provides practical interview-ready answers covering agent architecture, failure modes, tool safety, loop detection, and framework trade-offs.

## Key Points

**Core Understanding (Q1-5)**
- Agents differ from chatbots: multi-step decision loops (Plan -> Act -> Observe) vs single-step inference (Input -> LLM -> Output)
- Agents are WORSE for: deterministic tasks, latency-critical systems, high-stakes/irreversible actions, regulatory systems
- Autonomy measured by: task completion rate without human intervention, error recovery capability, clarification rate
- Tool routing relies on robust tool descriptions and system instructions; strong agents use tools only when answer isn't in general knowledge
- Every LLM output in an agent dictates an action with real consequences -- wrong tool cascades into downstream failures

**Reactive vs Deliberative (Q6-10)**
- Reactive: no internal state, maps inputs directly to actions (fast). Deliberative: maintains world model, plans ahead (slow but adaptable)
- Top agents are hybrids: reactive for simple queries, deliberative for complex tasks
- Adaptive depth: use a classifier to route simple vs complex tasks; match reasoning depth to stakes
- Deliberative agents require hard limits on tokens, loop counts, execution time (error compounding, goal drift, infinite loops)

**Tool-Calling (Q11-15)**
- Pre-conditions for safe tool calls: authorization, input validation, idempotency safety, confidence thresholds
- Tool descriptions are the most critical signal; must define inputs AND "when NOT to use"
- Ambiguous tools cause: incorrect selection, hallucinated arguments, duplicate calls, cascading failures
- Tool registry needs: standard schema, permissions system, dynamic loading (context-relevant tools only), health monitoring
- Failure modes: network/timeout, validation (malformed JSON), semantic (empty results), partial (bulk action stops halfway)

**ReAct & Reasoning Loops (Q16-20)**
- ReAct cycle: Thought -> Action -> Observation -> Thought. Advantages: transparency, grounding, debuggability
- Uncontrolled loops cause: circular reasoning, tool failure loops (burning API costs), goal ambiguity. Fix: hardcoded max iteration limit
- Detect stuck loops via: state hashing, repetition tracking, cosine similarity on consecutive thoughts, explicit "I am STUCK" mechanism
- CoT limitations: error propagation, token exhaustion, plan rigidity. Fix: planner-executor architectures
- Prevent hallucinated tool outputs: strict separation (tool runs outside LLM), grounding prompts, structured XML/JSON markers, verification step

**LangChain & LangGraph (Q21-25)**
- LangChain limitations: linear execution, opaque abstractions, stateful rigidity. LangGraph replaces it for complex workflows
- LangGraph advantages: graph topology (cycles, conditional edges), typed state (AgentState), native checkpointing (Postgres/Redis), human-in-the-loop, time travel
- Structured output: Pydantic parsers, output fixing parsers, native function calling (JSON schema). Syntax != semantic truth
- LangGraph state: shared AgentState, reducers (overwrite vs append), automatic checkpointing, time travel to past steps
- Avoid frameworks when: strict latency, complex error handling (circuit breakers), obfuscated debugging. Rule: frameworks for prototyping, custom for scale

## Entities Mentioned

- [[entities/langchain]] -- architectural limitations discussed (Q21)
- [[entities/langgraph]] -- state management, checkpointing, human-in-the-loop (Q22, Q24)
- [[entities/pydantic]] -- structured output validation (Q23)

## Concepts Covered

- [[concepts/ai-agents]] -- core agent architecture, autonomy, reactive vs deliberative taxonomy
- [[concepts/function-calling]] -- tool selection, tool registry design, safety pre-conditions
- [[concepts/multi-agent-systems]] -- planner-executor architectures mentioned
- [[concepts/guardrails]] -- tool safety, authorization, confidence thresholds
- [[concepts/prompt-engineering]] -- CoT prompting, grounding prompts
- [[concepts/llm-hallucination]] -- hallucinated tool outputs and prevention

## Notable Quotes or Data

- "Chatbots rely on single-step inference (Input -> LLM -> Output). Agents operate in multi-step decision loops (Plan -> Act -> Observe)."
- "A hardcoded maximum iteration limit is non-negotiable for production."
- "Use frameworks for fast prototyping; custom logic for massive scale."

## Related Sources

- [[sources/how-agentic-rag-works]] -- agentic RAG control loop patterns
- [[sources/ai-engineer-requirements]] -- agents as key AI engineer skill area
- [[sources/ai-projects-2026]] -- agent project examples with LangGraph
