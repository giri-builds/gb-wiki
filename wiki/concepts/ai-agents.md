---
type: concept
title: "AI Agents"
aliases: ["AI agent", "autonomous agents", "LLM agents"]
tags: [agents, llm]
sources: [sources/how-agentic-rag-works, sources/ai-engineer-requirements, sources/agentic-ai-interview-questions, sources/claude-architect-exam-guide]
last_updated: 2026-04-23
---

# AI Agents

## Definition

An AI agent is a software system that can perceive its environment, make decisions, and take actions to achieve specific goals with some degree of independence. In the LLM context, an agent is an LLM that has been given the ability to choose and execute actions — such as running searches, querying databases, calling APIs, or deciding it needs more information.

## How It Works

### Agentic Loop Lifecycle (Claude Agent SDK)

1. Send request to Claude with tools and conversation history
2. Inspect `stop_reason`: if "tool_use" → execute the requested tool and append result to history; if "end_turn" → present final response
3. Loop continues until `stop_reason` is "end_turn"
4. **Anti-patterns**: parsing natural language signals for termination, arbitrary iteration caps as primary stop, checking for assistant text content as completion indicator

### General Agent Loop

- LLM receives a goal or query
- Agent decides which tool(s) to use ([[concepts/function-calling]])
- Executes the tool, observes the result
- Decides next action: answer, retry, use a different tool, or gather more info
- Loop continues until the goal is met or a stopping condition is reached

## Why It Matters

- Transforms LLMs from text generators into autonomous task executors
- Enables complex multi-step workflows that adapt based on intermediate results
- Foundation for [[concepts/agentic-rag]], [[concepts/multi-agent-systems]], and agentic applications
- Core skill area for AI engineers in 2026

## Key Variants or Approaches

- **Reactive agents**: no internal state; map current inputs directly to actions. Lightning fast but limited. Best for fraud detection, real-time control loops, deterministic tasks.
- **Deliberative agents**: maintain rich internal world model and plan multiple steps ahead. Slower but adaptable. Require hard limits on tokens, loop counts, and execution time to prevent error compounding, goal drift, and infinite loops.
- **Hybrid agents**: today's top agents combine both — reactive for simple queries, deliberative for complex tasks. Use a classifier to route by task complexity.
- **Simple routing agents**: decide which tool/source to query
- **ReAct pattern**: Thought -> Action -> Observation -> Thought cycle. Advantages: transparency, grounding in tool output, debuggability, easy human-in-the-loop.
- **Planner-executor**: separate planning from execution; outperforms simple CoT loops for multi-step workflows
- **[[concepts/multi-agent-systems]]**: specialized agents coordinated by an orchestrator

### When NOT to Use Agents

- **Deterministic tasks**: hardcoded workflows are faster and more reliable
- **Latency-critical systems**: agent reasoning loops add significant seconds
- **High-stakes environments**: irreversible actions require strict human guardrails
- **Regulatory systems**: agents introduce non-determinism and unpredictability

### Agent SDK Hooks

- **PostToolUse hooks**: intercept tool results for transformation (normalizing timestamps, status codes) before the model processes them
- **Tool call interception hooks**: enforce compliance rules by blocking policy-violating actions (e.g., refunds exceeding $500) and redirecting to alternative workflows
- **Programmatic enforcement vs prompt-based guidance**: hooks provide deterministic guarantees; prompt instructions have non-zero failure rate — use hooks for critical business logic

## Related Concepts

- [[concepts/agentic-rag]] -- agents applied to retrieval
- [[concepts/function-calling]] -- mechanism for tool use
- [[concepts/multi-agent-systems]] -- multi-agent coordination
- [[concepts/react-framework]] -- reasoning + acting pattern

## Related Entities

- [[entities/claude-agent-sdk]] -- Anthropic's framework for building agentic applications
- [[entities/langgraph]] -- agent workflow framework
- [[entities/mcp]] -- agent-tool communication protocol
- [[entities/a2a-protocol]] -- agent-to-agent communication

## Source References

- [[sources/how-agentic-rag-works]] -- agents in RAG context
- [[sources/ai-engineer-requirements]] -- agentic workflows as key skill
- [[sources/agentic-ai-interview-questions]] -- 25 Q&As on agent architecture, tool calling, ReAct, LangGraph
- [[sources/claude-architect-exam-guide]] -- agentic loop lifecycle, hooks, session management, programmatic enforcement patterns
