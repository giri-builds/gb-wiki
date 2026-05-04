---
type: concept
title: "Graph RAG"
aliases: ["GraphRAG", "knowledge graph RAG", "graph-augmented retrieval"]
tags: [rag, system-design]
sources: [sources/rag-techniques]
last_updated: 2026-04-15
---

# Graph RAG

## Definition

Graph RAG combines knowledge graph traversal with vector-based retrieval for relationship-heavy, multi-hop questions. Instead of retrieving isolated chunks, it uses entity relationships in a graph to find connected context.

## How It Works

### Basic Graph RAG (with LangChain)
1. Extract entities from the question
2. Look up entity nodes in the knowledge graph
3. Traverse graph neighbors (1-2 hops)
4. Retrieve chunks associated with those nodes via vector search
5. Generate answer from graph-contextualized chunks

### Microsoft GraphRAG
1. Build a knowledge graph from documents with entity extraction
2. Cluster graph into communities
3. Pre-compute community summaries
4. At query time: select relevant communities → fetch summaries + local chunks → generate

### RAPTOR (Recursive Abstract Processing)
1. Build a tree of recursive summaries (leaves = chunks, parents = summaries)
2. Search at summary level first, then drill down to leaf chunks
3. Enables efficient retrieval over very long documents

## Why It Matters

- Strong multi-hop performance — follows relationships between entities
- Entity consistency across retrieved context
- Microsoft GraphRAG handles corpus-wide thematic questions via community summaries
- RAPTOR enables efficient high-level + detailed retrieval over long documents

## Key Variants or Approaches

- **Graph RAG with LangChain**: entity extraction → graph traversal → vector retrieval
- **Microsoft GraphRAG**: community detection + summary generation + local retrieval
- **RAPTOR**: recursive summary tree with multi-level retrieval

## Related Concepts

- [[concepts/retrieval-augmented-generation]] -- Graph RAG extends standard RAG
- [[concepts/agentic-rag]] -- graph traversal is often agent-orchestrated
- [[concepts/chunking]] -- hierarchical chunking relates to RAPTOR's tree structure

## Related Entities

- [[entities/neo4j]] -- graph database for Graph RAG
- [[entities/langchain]] -- Graph RAG implementation

## Source References

- [[sources/rag-techniques]] -- Graph RAG, Microsoft GraphRAG, RAPTOR with pseudocode
