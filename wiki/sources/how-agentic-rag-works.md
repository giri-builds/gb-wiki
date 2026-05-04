---
type: source
title: "How Agentic RAG Works"
source_file: "how-agentic-rag-works.md"
source_type: md
date_ingested: 2026-04-14
tags: [rag, agents, llm]
---

# How Agentic RAG Works

## Summary

A ByteByteGo Newsletter article explaining how Agentic RAG improves upon standard RAG by replacing the linear retrieve-then-generate pipeline with a control loop that includes decision points. The agent can evaluate retrieval quality, refine queries, route to multiple sources, and retry — addressing the three core failure modes of standard RAG: ambiguous queries, scattered evidence, and false confidence. The article also covers significant trade-offs including latency, cost, debugging complexity, and the evaluator paradox.

## Key Points

- Standard RAG is a one-shot pipeline: query → embedding → vector search → LLM generation, with no checkpoint or retry mechanism
- Three failure modes of standard RAG: ambiguous queries, scattered evidence across documents, and false confidence from similarity scores
- Agentic RAG introduces a control loop with three key capabilities: tool use/routing, query refinement, and self-evaluation
- **Tool use and routing**: agent selects which knowledge source to query based on question type (SQL DB, document store, or both)
- **Query refinement**: agent rewrites ambiguous queries before retrieval and reformulates after weak results
- **Self-evaluation**: agent examines results for relevance, completeness, and consistency before generating a response
- Agentic RAG exists on a spectrum — from simple routing to ReAct (Reasoning + Acting) to full multi-agent orchestration
- **Trade-offs**: 3-10x cost increase, 5-10x latency increase, harder debugging/testing, evaluator paradox (LLM judging LLM), and risk of overcorrection
- Not all queries need agentic RAG — direct factual lookups against clean single-source knowledge bases work fine with standard RAG
- If RAG failures stem from bad chunking or stale data, fixing retrieval quality helps more than adding an agentic layer

## Entities Mentioned

- [[entities/bytebytego]] -- newsletter/publication source

## Concepts Covered

- [[concepts/retrieval-augmented-generation]] -- standard RAG pipeline
- [[concepts/agentic-rag]] -- RAG with agent control loop
- [[concepts/embeddings]] -- numerical representations of semantic meaning
- [[concepts/vector-databases]] -- databases optimized for similarity search
- [[concepts/ai-agents]] -- software systems that perceive, decide, and act
- [[concepts/react-framework]] -- Reasoning + Acting framework for agents
- [[concepts/query-refinement]] -- rewriting queries for better retrieval
- [[concepts/multi-agent-systems]] -- specialized agents coordinated by an orchestrator

## Notable Quotes or Data

- "The main problem with standard RAG systems isn't the retrieval or the generation. It's that nothing sits in the middle deciding whether the retrieval was actually good enough before the generation happens."
- "A standard RAG query might take 1-2 seconds. An agentic query with three or four loops could take 10 seconds or more."
- "Each agent decision consumes tokens. A system handling thousands of queries per day can see costs multiply 3-10x compared to standard RAG."
- "The pipeline-to-loop shift also isn't unique to RAG. It reflects a broader pattern in how AI systems are evolving."

## Related Sources

- [[sources/rag-components]] (pending ingest)
- [[sources/rag-techniques]] (pending ingest)
- [[sources/rag-eval-metrics]] (pending ingest)
