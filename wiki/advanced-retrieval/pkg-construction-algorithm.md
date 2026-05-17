# PKG Construction Algorithm

The **PKG Construction Algorithm** is the process by which raw natural language text is transformed into a [Pseudo-Knowledge Graph](pseudo-knowledge-graph.md).

## Workflow Stages
1.  **Entity Identification:** Using LLMs or NER (Named Entity Recognition) to identify the core concepts in the text.
2.  **Relation Extraction:** Identifying the semantic links between entities (e.g., "acquired by", "located in", "authored by").
3.  **Graph Mapping:** Creating nodes for entities and edges for relations, while preserving the raw [In-Graph Text](pkg-in-graph-text.md) within each node/edge.
4.  **Vector Indexing:** Generating embeddings for the text within each node to enable initial [Multi-Modal Retrieval](pkg-multi-modal-retrieval.md).

## Key Innovation
The algorithm's primary innovation is the **preservation of raw text** alongside the graph structure, avoiding the lossy compression of traditional triplet extraction.

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [In-Graph Text Preservation](pkg-in-graph-text.md)
- [Relational Awareness in RAG](rag-relational-awareness.md)
