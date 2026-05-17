# Relational Awareness in RAG

**Relational Awareness** is the ability of a [Retrieval-Augmented Generation (RAG)](rag.md) system to understand and leverage the connections between disparate pieces of information.

## The "Island" Problem
Traditional vector-based RAG treats every text chunk as an independent "island." It can find chunks that are similar to the query but cannot see how Chunk A relates to Chunk B if they aren't semantically similar.

## Achieving Awareness
Frameworks like [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md) solve this by:
- **Explicit Linking:** Connecting related chunks via edges in a graph.
- **[Meta-path Traversal](pkg-meta-path-retrieval.md):** Following paths to discover the "connective tissue" of the knowledge base.
- **Maintaining Hierarchy:** Representing the parent-child or part-whole relationships inherent in the original data.

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [Context Fragmentation in RAG](rag-context-fragmentation.md)
- [In-Graph Text Preservation](pkg-in-graph-text.md)
