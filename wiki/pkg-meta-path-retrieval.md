# Meta-Path Guided Retrieval

**Meta-Path Retrieval** is an advanced traversal technique used in the [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md) to navigate complex relationships between entities.

## Definition
A **Meta-path** is a pre-defined template of relationships (e.g., `Author -> Paper -> Institution -> Location`). It defines a specific semantic "route" through the graph.

## Role in RAG
In a standard [RAG](rag.md) system, multi-hop reasoning is difficult because vector search only finds "islands" of similarity. Meta-path retrieval allows the system to:
1.  **Start** at a relevant node found via vector search.
2.  **Follow** a meta-path to discover logically connected nodes that might not be semantically similar to the original query but are crucial for the answer.

## Performance on MultiHop-RAG
PKG's use of meta-paths has demonstrated significant improvements on the **MultiHop-RAG** benchmark, where questions require connecting multiple disparate facts to form a complete answer.

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [MultiHop-RAG Benchmark Evaluation](multihop-rag-evaluation.md)
- [Relational Awareness in RAG](rag-relational-awareness.md)
