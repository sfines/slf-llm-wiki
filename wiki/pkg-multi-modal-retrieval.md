# PKG Multi-Modal Retrieval

**Multi-Modal Retrieval** in the [PKG framework](pseudo-knowledge-graph.md) refers to the hybrid use of different search techniques to maximize retrieval accuracy.

## The Hybrid Pipeline
PKG combines three primary retrieval modes:
1.  **Vector Retrieval:** Uses embedding similarity to identify "entry points" in the graph.
2.  **Graph Retrieval (Meta-paths):** Traverses the [Pseudo-Knowledge Graph](pseudo-knowledge-graph.md) from the entry points to gather relational context.
3.  **In-Graph Text Retrieval:** Directly retrieves the raw text associated with the discovered nodes and edges.

## Why Multi-Modal?
- **Vector-only:** Good for finding similar concepts but fails at relational hops.
- **Graph-only:** Great at relationships but requires a precise entry point and a well-structured schema.
- **PKG Hybrid:** Combines the "soft" matching of vectors with the "hard" structure of graphs.

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [Meta-Path Guided Retrieval](pkg-meta-path-retrieval.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)
