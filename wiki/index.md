---
type: index
title: "gb-wiki Content Index"
last_updated: 2026-04-23
---

# gb-wiki Content Index

> Auto-maintained by Claude Code. Do not edit manually outside of wiki operations.
> Total pages: 67 | Sources ingested: 20/31

## Sources (20 pages)

| Page | Source File | Tags | Summary |
|------|------------|------|---------|
| [[sources/how-agentic-rag-works]] | how-agentic-rag-works.md | rag, agents, llm | Agentic RAG control loop replacing linear RAG pipeline; routing, refinement, self-evaluation |
| [[sources/ai-projects-2026]] | AI Projects 2026.md | project-ideas, rag, fine-tuning, observability, slm | Five production-grade AI projects with tech stacks for 2026 |
| [[sources/ai-engineer-requirements]] | AI Engineer Requirements.md | career, agents, rag, system-design | AI engineer skills, four-layer AI stack, portfolio guidance for 2026 |
| [[sources/data-engineering-projects]] | Data Engineering.md | data-engineering, project-ideas | 20 hands-on data engineering projects from basic to advanced |
| [[sources/setting-up-evaluations-for-llms]] | Setting up Evaluations for LLMs.html | evaluation, observability, llm | LLM eval taxonomy, LangSmith architecture, RRR pattern, CI/CD integration |
| [[sources/rag-techniques]] | RAG Techniques.pdf | rag, agents, evaluation, system-design | 34 RAG strategies with pseudocode; foundational to advanced architectures |
| [[sources/rag-terminology]] | RAG Terminology.pdf | rag, agents, cheatsheet, interview-prep | 35+ agentic RAG terms across 6 categories |
| [[sources/rag-end-to-end]] | RAG End to End.pdf | rag, system-design, interview-prep | Complete 4-stage RAG walkthrough; chunking strategies; RAG vs fine-tuning |
| [[sources/rag-components]] | RAG Components.pdf | rag, cheatsheet, interview-prep | 15 essential RAG components with Python code examples |
| [[sources/rag-eval-metrics]] | RAG - Eval Metrics.pdf | rag, evaluation | Retrieval and generation evaluation metrics with formulas |
| [[sources/why-language-models-hallucinate]] | why-language-models-hallucinate.pdf | llm, evaluation, ai-fundamentals | Theoretical framework: hallucinations as binary classification errors; binary grading reinforces guessing |
| [[sources/defeating-nondeterminism-in-llm-inference]] | Defeating Nondeterminism in LLM Inference.pdf | llm, ml-systems, system-design | Batch invariance as true cause of LLM inference nondeterminism; kernel-level fixes |
| [[sources/llms-50-interview-questions]] | LLMs 50 Interview Qtns.pdf | llm, interview-prep, cheatsheet | 50 LLM interview questions checklist covering fundamentals through applied topics |
| [[sources/agentic-ai-interview-questions]] | Agentic AI Interview Qtns.pdf | agents, interview-prep, orchestration | 25 agentic AI interview Q&As: agent architecture, tool calling, ReAct, LangGraph |
| [[sources/slms-future-of-agentic-ai]] | SLMs - Future of Agentic AI.pdf | slm, agents, system-design, ml-systems | NVIDIA position paper: SLMs are sufficiently powerful, more suitable, and more economical for agentic AI |
| [[sources/langchain-langgraph-projects]] | LangChain-LangGraph-Projects.pdf | project-ideas, orchestration, agents, rag | 10 enterprise LangChain/LangGraph portfolio projects with tech stacks and best practices |
| [[sources/claude-common-workflows]] | claude_common_workflows.md | anthropic, tools, prompt-engineering | 6 Claude Code workflow guides: codebase exploration, debugging, Plan Mode, testing, worktrees, power tips |
| [[sources/claude-architect-exam-guide]] | Claude Certified Architect – Foundations Certification Exam Guide.pdf | certification, anthropic, agents, prompt-engineering, system-design | Anthropic certification exam: 5 domains, 6 scenarios, sample questions on Agent SDK, MCP, Claude Code, prompting, context management |
| [[sources/claude-50-interview-questions]] | 50 Claude Interview Qtns.pdf | anthropic, interview-prep, cheatsheet | 50 Claude interview questions checklist: fundamentals, safety, agents, workflows, production, ethics |
| [[sources/context-engineering]] | Context Engineering.pdf | prompt-engineering, agents, system-design, llm, ai-fundamentals | Academic framework: formal CE definition, four-era model (1.0-4.0), entropy reduction, context collection/management/usage |

## Entities (20 pages)

| Page | Category | Tags | Summary |
|------|----------|------|---------|
| [[entities/langchain]] | framework | orchestration, rag, agents | Open-source LLM orchestration framework; chaining, memory, tool use |
| [[entities/langgraph]] | framework | orchestration, agents | Stateful multi-step agent workflow framework extending LangChain |
| [[entities/langsmith]] | service | observability, evaluation | Full-lifecycle LLM evaluation and observability platform |
| [[entities/langfuse]] | service | observability, evaluation | Open-source observability and evaluation platform for LLM apps |
| [[entities/llamaindex]] | framework | orchestration, rag | Data framework for LLM apps; ingestion, indexing, querying |
| [[entities/fastapi]] | framework | api-development | Modern Python web framework for building AI-serving APIs |
| [[entities/pinecone]] | service | vector-databases, rag | Managed vector database for production RAG |
| [[entities/weaviate]] | service | vector-databases, rag | Open-source vector DB with native hybrid search |
| [[entities/chromadb]] | tool | vector-databases, rag | Lightweight open-source embedding database |
| [[entities/ollama]] | tool | slm | Local model runner for offline LLM inference |
| [[entities/anthropic]] | company | anthropic, llm | AI safety company; builds Claude models, MCP protocol |
| [[entities/openai]] | company | openai, llm | AI research company; builds GPT models, Evals framework |
| [[entities/hugging-face]] | company | huggingface, fine-tuning, llm | ML platform; TRL, Axolotl, model hub |
| [[entities/mcp]] | protocol | agents, anthropic | Model Context Protocol for agent-tool communication |
| [[entities/a2a-protocol]] | protocol | agents | Google's agent-to-agent communication protocol |
| [[entities/ragas]] | tool | evaluation, rag | Open-source RAG evaluation framework |
| [[entities/deepeval]] | tool | evaluation, rag | LLM-based RAG evaluation and regression testing framework |
| [[entities/cohere]] | company | rag, tools | AI company; widely-used re-ranker models for RAG precision |
| [[entities/claude-code]] | tool | anthropic, tools | Anthropic's CLI for AI-assisted software engineering: Plan Mode, worktrees, CLAUDE.md hierarchy, skills, commands, CI/CD integration |
| [[entities/claude-agent-sdk]] | framework | anthropic, agents, orchestration | Anthropic's framework for agentic apps: agentic loops, hooks, subagent spawning, session management |

## Concepts (27 pages)

| Page | Tags | Summary |
|------|------|---------|
| [[concepts/retrieval-augmented-generation]] | rag, llm | 4-stage pipeline (ingest/retrieve/augment/generate); 15 components; 34+ technique variants |
| [[concepts/agentic-rag]] | rag, agents | RAG with agent control loop; Self-RAG, CRAG, iterative, controllable agent variants |
| [[concepts/ai-agents]] | agents, llm | Software systems that perceive, decide, act; LLMs with tool use |
| [[concepts/multi-agent-systems]] | agents, system-design | Specialized agents coordinated by orchestrator |
| [[concepts/embeddings]] | embeddings, rag | Vector representations capturing semantic meaning; sparse vs dense |
| [[concepts/vector-databases]] | vector-databases, rag | Specialized storage for similarity search on embeddings |
| [[concepts/chunking]] | rag, system-design | Document splitting strategies: fixed, semantic, proposition, hierarchical, sliding window |
| [[concepts/hybrid-search]] | rag | Dense + BM25 fusion retrieval; RRF; 0.6/0.4 starting weight |
| [[concepts/re-ranking]] | rag | Cross-encoder re-scoring for retrieval precision |
| [[concepts/query-refinement]] | rag | Query rewriting, decomposition, HyDE, HyPE techniques |
| [[concepts/graph-rag]] | rag, system-design | Graph traversal + vector search; Microsoft GraphRAG; RAPTOR |
| [[concepts/rag-eval-metrics]] | rag, evaluation | Recall@K, Precision@K, Context Relevancy, Faithfulness, Groundedness |
| [[concepts/evaluation]] | evaluation, llm | Three-layer eval taxonomy: heuristic, statistical, LLM-as-a-Judge |
| [[concepts/llm-as-a-judge]] | evaluation, llm | Stronger LLM evaluates outputs via RRR pattern |
| [[concepts/observability]] | observability, evaluation | Tracing, metrics, and monitoring for AI systems in production |
| [[concepts/regression-testing-for-ai]] | evaluation, system-design | CI/CD integration for automated eval pipelines |
| [[concepts/guardrails]] | guardrails, evaluation | Deterministic safety checks on LLM inputs/outputs |
| [[concepts/fine-tuning]] | fine-tuning, llm | SFT and DPO for task-specific model adaptation |
| [[concepts/lora]] | fine-tuning, llm | Parameter-efficient fine-tuning via low-rank adaptation |
| [[concepts/small-language-models]] | slm, llm, agents, system-design | Compact models (<10B params) for local/edge deployment; SLM-first heterogeneous agentic architecture |
| [[concepts/prompt-engineering]] | prompt-engineering, llm | Designing prompts for consistent, high-quality LLM output |
| [[concepts/function-calling]] | agents, llm | LLM capability to invoke external tools/APIs; tool selection, registry design, safety pre-conditions |
| [[concepts/ai-engineering-stack]] | system-design, ai-fundamentals | Four-layer architecture: models, retrieval, orchestration, application |
| [[concepts/etl]] | data-engineering | Extract, Transform, Load data pipeline pattern |
| [[concepts/dimensional-modeling]] | dimensional-modeling, data-engineering | Star schema with fact and dimension tables |
| [[concepts/change-data-capture]] | data-engineering | Incremental change tracking between systems |
| [[concepts/llm-hallucination]] | llm, evaluation, ai-fundamentals | Plausible falsehoods from LLMs; IIV reduction; binary grading rewards guessing; singleton rate bound |
| [[concepts/llm-inference-nondeterminism]] | llm, ml-systems, system-design | Batch-size-dependent numerics cause nondeterministic inference; batch-invariant kernels fix it |
| [[concepts/context-window-management]] | llm, system-design, agents | Token budgets, progressive summarization risks, lost-in-the-middle, scratchpad files, layered memory, self-baking |
| [[concepts/context-engineering]] | prompt-engineering, agents, system-design, llm, ai-fundamentals | Meta-discipline for context collection, management, and usage; four-era model; entropy reduction framework |

## Comparisons (1 page)

| Page | Subjects | Tags | Summary |
|------|----------|------|---------|
| [[comparisons/standard-rag-vs-agentic-rag]] | RAG, Agentic RAG | rag, agents | Linear pipeline vs control loop; latency/cost/complexity trade-offs |

## Meta (1 page)

| Page | Tags | Summary |
|------|------|---------|
| [[meta/ingestion-plan]] | meta | Revised ingestion plan: 22 files across 7 rounds (R3-R9) |
