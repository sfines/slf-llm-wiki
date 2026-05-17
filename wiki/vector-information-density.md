# Information Density in Vector Databases

**Information Density** refers to the concentration of useful, relevant facts within a given volume of data.

## The Challenge in RAG
Large, enterprise-scale databases often have **Low Information Density**. Most of the text is "noise" (legal boilerplate, formatting, redundant statements) that clutters vector search results.

## Impact on Vector Search
In low-density environments, vector search suffers from:
- **Diluted Relevance:** Similar but irrelevant chunks are retrieved, "burying" the high-signal facts.
- **Sparse Connections:** The few high-signal facts are geographically distant in the vector space, making them hard to retrieve together.

## PKG Mitigation
The [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md) handles low-density data more effectively by using [Meta-paths](pkg-meta-path-retrieval.md) to "jump" across the noise and connect the high-signal nodes directly via relational links.

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [Relational Awareness in RAG](rag-relational-awareness.md)
- [Context Fragmentation in RAG](rag-context-fragmentation.md)
