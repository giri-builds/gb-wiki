---
type: concept
title: "Prompt Engineering"
aliases: ["prompting"]
tags: [prompt-engineering, llm]
sources: [sources/ai-engineer-requirements, sources/claude-architect-exam-guide, sources/context-engineering]
last_updated: 2026-04-23
---

# Prompt Engineering

## Definition

Prompt engineering is the practice of designing and optimizing the instructions, context, and structure given to LLMs to elicit consistent, high-quality outputs. It ranges from basic query formulation to advanced techniques like chain-of-thought reasoning and structured output schemas.

## How It Works

- **System prompts**: define the model's role, constraints, and output format
- **Chain of Thought (CoT)**: instruct the model to reason step-by-step
- **Few-shot learning**: provide examples of desired input→output pairs
- **Structured output**: enforce JSON schemas or specific formats via [[concepts/function-calling]]

### Explicit Criteria over Vague Instructions

- "Flag comments only when claimed behavior contradicts actual code behavior" beats "check that comments are accurate"
- General instructions like "be conservative" or "only report high-confidence findings" fail to improve precision
- Define specific categorical criteria: which issues to report (bugs, security) vs skip (minor style, local patterns)
- High false positive rates undermine developer trust in accurate categories

### Few-Shot Prompting Patterns

- Most effective technique when detailed instructions alone produce inconsistent results
- Create 2-4 targeted examples for ambiguous scenarios showing reasoning for why one action was chosen over alternatives
- Examples enable generalization to novel patterns, not just matching pre-specified cases
- Effective for reducing hallucination in extraction tasks (informal measurements, varied document structures)
- Include examples showing acceptable code patterns vs genuine issues to reduce false positives

### Iterative Refinement Techniques

- **Input/output examples**: most effective way to communicate expected transformations when prose is interpreted inconsistently
- **Test-driven iteration**: write test suites first, iterate by sharing test failures to guide progressive improvement
- **Interview pattern**: have Claude ask questions to surface considerations the developer may not have anticipated before implementing
- **Batching strategy**: provide all issues in a single message for interacting problems; fix sequentially for independent problems

### Multi-Pass Review Architecture

- Self-review is weak: the same session retains reasoning context, less likely to question its own decisions
- Independent review instances (without prior reasoning context) catch more subtle issues
- Split large reviews into per-file local passes + cross-file integration passes to avoid attention dilution

## Why It Matters

- First approach to try before [[concepts/fine-tuning]] — often sufficient for most tasks
- Systematic prompting produces consistent, reproducible results vs ad-hoc queries
- Key differentiator between junior and senior AI engineers

## Related Concepts

- [[concepts/context-engineering]] — prompt engineering is a subset of the broader context engineering discipline
- [[concepts/fine-tuning]] -- alternative when prompting falls short
- [[concepts/function-calling]] -- structured output via tool use
- [[concepts/evaluation]] -- measuring prompt quality systematically

- [[concepts/guardrails]] -- explicit criteria reduce false positives
- [[concepts/context-window-management]] -- prompt structure affects context utilization

## Related Entities

- [[entities/claude-code]] -- CLAUDE.md configuration is prompt engineering for agent behavior
- [[entities/claude-agent-sdk]] -- system prompts and few-shot examples used in agent definitions

## Source References

- [[sources/ai-engineer-requirements]] -- listed as core AI engineer skill
- [[sources/claude-architect-exam-guide]] -- Domain 4: Prompt Engineering & Structured Output (20% of exam); explicit criteria, few-shot patterns, iterative refinement, multi-pass review
