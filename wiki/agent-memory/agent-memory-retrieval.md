# Memory Retrieval Mechanisms

**Memory Retrieval** encompasses the techniques used by an [Autonomous Agent](../core-concepts/autonomous-agents.md) to access relevant information from its memory systems during a reasoning task.

## Common Methods
- **Vector Search:** Using semantic similarity embeddings to find relevant chunks in a database ([RAG](../advanced-retrieval/rag.md)).
- **Graph Traversal:** Following relationships between entities in a [Knowledge Graph](../advanced-retrieval/pseudo-knowledge-graph.md).
- **Heuristic Retrieval:** Using rules or keywords to select information (e.g., always loading the "system prompt rules").
- **Agent-Guided Retrieval:** The agent identifies its own information gaps and formulates specific queries to its memory system.

## Challenges
- **Relevance Tuning:** Balancing between "too little" context (missing facts) and "too much" context (saturation).
- **Interference:** Retrieving similar but irrelevant memories that cause the model to hallucinate or get confused.

## See Also
- [Agent Memory](agent-memory.md)
- [Pseudo-Knowledge Graph (PKG)](../advanced-retrieval/pseudo-knowledge-graph.md)
- [RAG (Retrieval-Augmented Generation)](../advanced-retrieval/rag.md)
