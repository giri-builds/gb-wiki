---
type: concept
title: "Function Calling"
aliases: ["tool use", "tool calling", "structured output"]
tags: [agents, llm]
sources: [sources/ai-engineer-requirements, sources/agentic-ai-interview-questions, sources/claude-architect-exam-guide]
last_updated: 2026-04-23
---

# Function Calling

## Definition

Function calling (also called tool use) is the capability of LLMs to invoke external functions, APIs, or tools based on natural language instructions. The model decides which function to call, generates the required arguments, and processes the returned results.

## How It Works

- Tools are described to the model via schemas (name, description, parameters)
- Model decides when to call a tool based on the user's request
- Model generates structured arguments matching the tool's schema
- External system executes the function and returns results
- Model incorporates results into its response

### Tool Selection

Tool descriptions are the single most critical signal for correct selection. Best practices:
- Define inputs AND "when NOT to use" each tool to prevent overlap
- Function-calling models are explicitly tuned to output JSON schema
- Chain-of-thought prompting before calling drastically improves accuracy
- Direct responses for conceptual/summarization tasks; tool calls for external data, state access, or real-time info

### Safe Tool Calling Pre-conditions

- **Authorization**: agent has explicit permission for the specific action
- **Input validation**: arguments strictly formatted (e.g., date formats, JSON schema)
- **Idempotency safety**: knowing if an action is safe to retry on failure (reads vs writes)
- **Confidence thresholds**: tools that modify data should halt when uncertain

### Tool Registry Design

Production agents benefit from a structured tool registry:
- Standard schema: name, version, parameter types per tool
- Permissions system: dynamic restriction based on user authorization
- Dynamic loading: only tools relevant to current task context
- Health monitoring: automatically remove tools with high failure/timeout rates

### Failure Modes

- **Network/timeout**: external API doesn't respond
- **Validation**: tool rejects malformed JSON arguments
- **Semantic**: execution succeeds but returns empty/useless results
- **Partial**: bulk action stops halfway — recovery must resume, not restart

### `tool_choice` Configuration (Claude API)

- **`"auto"`**: model may return text instead of calling a tool — default behavior
- **`"any"`**: model must call a tool but can choose which — guarantees structured output when multiple schemas exist
- **Forced selection**: `{"type": "tool", "name": "extract_metadata"}` — model must call the specific named tool; useful for ensuring a particular extraction runs before enrichment steps
- Strict JSON schemas via `tool_use` eliminate syntax errors but do **not** prevent semantic errors (e.g., line items that don't sum to total)

### Structured Output via Tool Use

- Define extraction tools with JSON schemas as input parameters; extract structured data from the `tool_use` response
- Design schema fields as optional (nullable) when source documents may not contain the information — prevents model from fabricating values to satisfy required fields
- Use enum values like "unclear" for ambiguous cases and "other" + detail fields for extensible categorization
- Validation-retry pattern: append specific validation errors to the prompt on retry to guide model toward self-correction
- Retries are ineffective when information is absent from source (vs format/structural errors)

### Message Batches API

- 50% cost savings with up to 24-hour processing window, no guaranteed latency SLA
- Appropriate for non-blocking workloads (overnight reports, weekly audits); **not** for blocking pre-merge checks
- Does not support multi-turn tool calling within a single request
- `custom_id` fields for correlating batch request/response pairs; resubmit only failed documents

## Why It Matters

- Transforms LLMs from text generators into [[concepts/ai-agents]] that can take actions
- Enables real-world interactions: web search, database queries, API calls, file operations
- Foundation for [[concepts/agentic-rag]] routing and tool selection
- Part of the **orchestration layer** in the [[concepts/ai-engineering-stack]]

## Related Concepts

- [[concepts/ai-agents]] -- function calling enables agent behavior
- [[concepts/prompt-engineering]] -- structured output is a related technique
- [[concepts/multi-agent-systems]] -- agents coordinate via tool calls

## Related Entities

- [[entities/claude-agent-sdk]] -- implements agentic loops with tool_use and stop_reason handling
- [[entities/mcp]] -- standardizes function calling across tools
- [[entities/langchain]] -- provides function calling abstractions

## Source References

- [[sources/ai-engineer-requirements]] -- function calling as key LLM skill
- [[sources/agentic-ai-interview-questions]] -- tool selection, registry design, safety pre-conditions, failure modes (Q11-Q15)
- [[sources/claude-architect-exam-guide]] -- tool_choice options, tool_use for structured output, Message Batches API, validation-retry patterns (Domains 2 & 4)
