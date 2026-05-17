# Pseudo-Knowledge Graph (PKG)

The **Pseudo-Knowledge Graph** is an advanced [RAG](rag.md) framework designed to improve information retrieval for LLMs by combining the benefits of unstructured text and relational knowledge graphs.

## The Problem: RAG Fragmentation
Traditional RAG systems often suffer from:
- **[Relational Unawareness](rag-relational-awareness.md):** Chunks of text are retrieved in isolation, losing the connections between them.
- **[Context Fragmentation](rag-context-fragmentation.md):** Breaking text into fixed-size chunks can sever logical flows.
- **[Low Information Density](vector-information-density.md):** Finding specific facts in large, sparse datasets is difficult with only vector search.

## PKG Architecture
The PKG framework, built via a specialized **[Construction Algorithm](pkg-construction-algorithm.md)**, addresses these issues through three main pillars:

### 1. [In-Graph Text](pkg-in-graph-text.md)
Unlike traditional Knowledge Graphs that decompose text into strict (Subject, Predicate, Object) triplets, PKG preserves **natural language text** within its nodes and edges.

### 2. [Meta-Path Retrieval](pkg-meta-path-retrieval.md)
PKG uses **Meta-paths**—pre-defined templates of relationships—to navigate the graph. This is particularly effective for "Multi-hop" questions.

### 3. [Multi-Modal Retrieval](pkg-multi-modal-retrieval.md)
PKG combines graph-based traversal with traditional **Vector Retrieval**.

## Performance and Evaluation
PKG has been extensively evaluated using **Open Compass** and **[MultiHop-RAG](multihop-rag-evaluation.md)** benchmarks.

## Benefits for Agents
For [Autonomous Agents](autonomous-agents.md), PKG provides a more robust [Factual Memory](agent-factual-memory.md). It enables agents to:
- Reason over complex relationships in a codebase or document set.
- Maintain context across long-horizon research tasks.
- Reduce hallucinations by providing the agent with the "connective tissue" between facts.

## See Also
- [Retrieval-Augmented Generation (RAG)](rag.md)
- [Agent Factual Memory](agent-factual-memory.md)
- [Ubiquitous Language for AI](ubiquitous-language-for-ai.md)
- [Raw Source: Pseudo-Knowledge Graph Paper](../raw/pseudo-knowledge-graph-paper.md)
