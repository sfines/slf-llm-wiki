# MultiHop-RAG Benchmark Evaluation

**MultiHop-RAG** is a benchmark designed to evaluate the ability of [RAG](rag.md) systems to answer complex questions that require synthesizing information from multiple sources.

## Benchmark Characteristics
- **Multi-Step Reasoning:** Questions cannot be answered with a single text chunk.
- **Disparate Sources:** Relevant facts are often scattered across different documents or distant parts of the same document.
- **Relational Dependency:** The system must identify the relationship between Fact A and Fact B to arrive at the answer.

## PKG Performance
In the [Pseudo-Knowledge Graph research](pseudo-knowledge-graph.md), PKG demonstrated superior performance on MultiHop-RAG compared to standard vector-based baselines. This was attributed to its [Meta-path Guided Retrieval](pkg-meta-path-retrieval.md) which explicitly follows relational links that vector search would miss.

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [Meta-Path Guided Retrieval](pkg-meta-path-retrieval.md)
- [Relational Awareness in RAG](rag-relational-awareness.md)
