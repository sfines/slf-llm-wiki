# Memory Retrieval Mechanisms

**Memory Retrieval** encompasses the techniques used by an [Autonomous Agent](autonomous-agents.md) to access relevant information from its memory systems during a reasoning task.

## Common Methods
- **Vector Search:** Using semantic similarity embeddings to find relevant chunks in a database ([RAG](rag.md)).
- **Graph Traversal:** Following relationships between entities in a [Knowledge Graph](pseudo-knowledge-graph.md).
- **Heuristic Retrieval:** Using rules or keywords to select information (e.g., always loading the "system prompt rules").
- **Agent-Guided Retrieval:** The agent identifies its own information gaps and formulates specific queries to its memory system.

## Challenges
- **Relevance Tuning:** Balancing between "too little" context (missing facts) and "too much" context (saturation).
- **Interference:** Retrieving similar but irrelevant memories that cause the model to hallucinate or get confused.

## See Also
- [Agent Memory](agent-memory.md)
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)
