---
type: log
title: "gb-wiki Operations Log"
---

# gb-wiki Operations Log

> Append-only. Most recent entries at the bottom.

---

## [2026-04-14] bootstrap | Project initialized
- Created CLAUDE.md schema
- Created wiki directory structure (sources/, entities/, concepts/, comparisons/, meta/)
- Created empty index.md and log.md
- Created outputs directory structure (presentations/, charts/, exports/)
- Sources awaiting ingest: 43 (38 PDF, 4 MD, 1 HTML)
- Assets cataloged: 51 images/media in raw/assets/

## [2026-04-14] ingest | how-agentic-rag-works.md
- Created: sources/how-agentic-rag-works.md
- Created: entities/bytebytego.md (skipped — minor entity)
- Created: concepts/retrieval-augmented-generation.md, concepts/agentic-rag.md, concepts/embeddings.md, concepts/vector-databases.md, concepts/ai-agents.md, concepts/multi-agent-systems.md
- Created: comparisons/standard-rag-vs-agentic-rag.md
- Pages touched: 8

## [2026-04-14] ingest | AI Projects 2026.md
- Created: sources/ai-projects-2026.md
- Created: entities/langchain.md, entities/langgraph.md, entities/chromadb.md, entities/weaviate.md, entities/ollama.md, entities/fastapi.md, entities/langsmith.md, entities/langfuse.md, entities/hugging-face.md, entities/ragas.md, entities/pydantic.md (skipped — minor)
- Created: concepts/re-ranking.md, concepts/small-language-models.md, concepts/observability.md, concepts/fine-tuning.md, concepts/lora.md
- Pages touched: 16

## [2026-04-14] ingest | AI Engineer Requirements.md
- Created: sources/ai-engineer-requirements.md
- Created: entities/anthropic.md, entities/openai.md, entities/pinecone.md, entities/llamaindex.md, entities/mcp.md, entities/a2a-protocol.md
- Created: concepts/ai-engineering-stack.md, concepts/prompt-engineering.md, concepts/function-calling.md, concepts/guardrails.md
- Updated: concepts/retrieval-augmented-generation.md, concepts/embeddings.md, concepts/vector-databases.md, concepts/multi-agent-systems.md, concepts/evaluation.md, concepts/observability.md, entities/langchain.md, entities/langsmith.md, entities/langfuse.md, entities/fastapi.md, entities/weaviate.md, entities/chromadb.md
- Pages touched: 22

## [2026-04-14] ingest | Data Engineering.md
- Created: sources/data-engineering-projects.md
- Created: concepts/etl.md, concepts/change-data-capture.md, concepts/dimensional-modeling.md
- Pages touched: 4

## [2026-04-14] ingest | Setting up Evaluations for LLMs.html
- Created: sources/setting-up-evaluations-for-llms.md
- Created: concepts/evaluation.md, concepts/llm-as-a-judge.md, concepts/regression-testing-for-ai.md
- Updated: entities/langsmith.md, entities/langchain.md, concepts/guardrails.md, concepts/observability.md
- Pages touched: 7

## [2026-04-14] round-1-complete | 5 sources ingested
- Total sources ingested: 5/43
- Total wiki pages: 38 (5 sources, 16 entities, 16 concepts, 1 comparison)
- Remaining sources: 38 (all PDF)

## [2026-04-15] ingest | RAG Techniques.pdf
- Created: sources/rag-techniques.md
- Created: concepts/chunking.md, concepts/hybrid-search.md, concepts/graph-rag.md, concepts/query-refinement.md
- Created: entities/deepeval.md, entities/cohere.md
- Updated: concepts/retrieval-augmented-generation.md, concepts/agentic-rag.md
- Pages touched: 8

## [2026-04-15] ingest | RAG Terminology.pdf
- Created: sources/rag-terminology.md
- Updated: concepts/retrieval-augmented-generation.md (added source)
- Pages touched: 1

## [2026-04-15] ingest | RAG End to End.pdf
- Created: sources/rag-end-to-end.md
- Updated: concepts/retrieval-augmented-generation.md (4-stage pipeline detail, chunking strategies, RAG vs fine-tuning)
- Pages touched: 1

## [2026-04-15] ingest | RAG Components.pdf
- Created: sources/rag-components.md
- Updated: concepts/retrieval-augmented-generation.md (15 components)
- Pages touched: 1

## [2026-04-15] ingest | RAG - Eval Metrics.pdf
- Created: sources/rag-eval-metrics.md
- Created: concepts/rag-eval-metrics.md
- Pages touched: 2

## [2026-04-15] round-2-complete | 5 RAG sources ingested
- Total sources ingested: 10/43
- Total wiki pages: 50 (10 sources, 18 entities, 22 concepts, 1 comparison)
- New concepts: chunking, hybrid-search, graph-rag, query-refinement, rag-eval-metrics
- New entities: deepeval, cohere
- Significantly updated: retrieval-augmented-generation (now richest page in wiki), agentic-rag (9 variants)
- Remaining sources: 33 (all PDF)

## [2026-04-20] ingest | why-language-models-hallucinate.pdf
- Created: sources/why-language-models-hallucinate.md
- Created: concepts/llm-hallucination.md
- Updated: concepts/evaluation.md (binary grading reinforces hallucination)
- Pages touched: 3

## [2026-04-20] ingest | Defeating Nondeterminism in LLM Inference.pdf
- Created: sources/defeating-nondeterminism-in-llm-inference.md
- Created: concepts/llm-inference-nondeterminism.md
- Pages touched: 2

## [2026-04-20] ingest | LLMs 50 Interview Qtns.pdf
- Created: sources/llms-50-interview-questions.md
- Pages touched: 1

## [2026-04-20] round-3-complete | 3 LLM core sources ingested
- Total sources ingested: 13/31
- Total wiki pages: 56 (13 sources, 18 entities, 24 concepts, 1 comparison, 1 meta)
- New concepts: llm-hallucination, llm-inference-nondeterminism
- Updated: evaluation (binary grading insight)
- Remaining sources: 18

## [2026-04-21] ingest | Agentic AI Interview Qtns.pdf
- Created: sources/agentic-ai-interview-questions.md (existed from prior partial ingest)
- Updated: concepts/ai-agents.md (reactive/deliberative taxonomy, ReAct pattern, when NOT to use agents)
- Updated: entities/langgraph.md (graph topology, typed state, checkpointing, time travel)
- Updated: concepts/function-calling.md (tool selection, registry design, safety pre-conditions, failure modes)
- Updated: entities/langchain.md (architectural limitations from Q21)
- Pages touched: 5

## [2026-04-21] ingest | SLMs - Future of Agentic AI.pdf
- Created: sources/slms-future-of-agentic-ai.md
- Updated: concepts/small-language-models.md (major expansion: NVIDIA position paper, SLM families, heterogeneous architecture, LLM-to-SLM conversion algorithm, economics)
- Pages touched: 2

## [2026-04-21] ingest | LangChain-LangGraph-Projects.pdf
- Created: sources/langchain-langgraph-projects.md
- Updated: entities/langchain.md (added source), entities/langgraph.md (added source)
- Pages touched: 3

## [2026-04-21] round-4-complete | 3 Agents & Orchestration sources ingested
- Total sources ingested: 16/31
- Total wiki pages: 59 (16 sources, 18 entities, 24 concepts, 1 comparison, 1 meta)
- New source pages: agentic-ai-interview-questions, slms-future-of-agentic-ai, langchain-langgraph-projects
- Significantly updated: small-language-models (now richest SLM page), function-calling (tool-calling depth), ai-agents, langchain, langgraph
- Remaining sources: 15

## [2026-04-23] ingest | claude_common_workflows.md
- Created: sources/claude-common-workflows.md
- Created: entities/claude-code.md
- Updated: entities/anthropic.md (added source, Claude Code link)
- Pages touched: 3

## [2026-04-23] ingest | Claude Certified Architect – Foundations Certification Exam Guide.pdf
- Created: sources/claude-architect-exam-guide.md
- Created: entities/claude-agent-sdk.md, concepts/context-window-management.md
- Updated: entities/mcp.md (server scoping, isError, tool distribution), entities/claude-code.md (CLAUDE.md hierarchy, rules, skills, CI/CD)
- Updated: concepts/ai-agents.md (agentic loop lifecycle, hooks), concepts/multi-agent-systems.md (hub-and-spoke, error propagation)
- Updated: concepts/function-calling.md (tool_choice, structured output, Message Batches API), concepts/prompt-engineering.md (few-shot, explicit criteria, iterative refinement, multi-pass review)
- Pages touched: 11

## [2026-04-23] ingest | 50 Claude Interview Qtns.pdf
- Created: sources/claude-50-interview-questions.md
- Pages touched: 1

## [2026-04-23] ingest | Context Engineering.pdf
- Created: sources/context-engineering.md
- Created: concepts/context-engineering.md
- Updated: concepts/context-window-management.md (added source), concepts/prompt-engineering.md (added source, CE relationship)
- Pages touched: 4

## [2026-04-23] round-5-complete | 4 Claude & Anthropic sources ingested
- Total sources ingested: 20/31
- Total wiki pages: 67 (20 sources, 20 entities, 27 concepts, 1 comparison, 1 meta)
- New source pages: claude-common-workflows, claude-architect-exam-guide, claude-50-interview-questions, context-engineering
- New entities: claude-code, claude-agent-sdk
- New concepts: context-window-management, context-engineering
- Significantly updated: ai-agents, multi-agent-systems, function-calling, prompt-engineering, mcp
- Note: The-Complete-Guide-to-Building-Skill-for-Claude.pdf was not found in raw/ — 4 of 5 planned files ingested
- Remaining sources: 11
