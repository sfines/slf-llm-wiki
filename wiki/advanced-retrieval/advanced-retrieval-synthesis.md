# Advanced Retrieval (RAG): Area Synthesis

## State of Current Thought
Modern retrieval is shifting from naive semantic vector search to structured, relational models like Pseudo-Knowledge Graphs (PKG). Maintaining in-graph text and mapping meta-paths allow agents to perform multi-hop reasoning with high vector information density, overcoming the traditional limits of context fragmentation.

## Areas of Controversy / Ongoing Conversation
- **Graph vs. Vector vs. Hybrid:** While PKGs offer superior relational awareness, the computational overhead of constructing and updating them during active agent sessions remains contested. Is the latency trade-off worth it compared to denser embeddings?
- **Context Saturation vs. Fragmentation:** Striking the balance between providing enough retrieved context to avoid fragmentation, while avoiding context saturation that degrades LLM reasoning.

## See Also
- [Rag](./rag.md)
- [Pseudo Knowledge Graph](./pseudo-knowledge-graph.md)
