# Memory Formation Dynamics

**Memory Formation** is the process by which an [Autonomous Agent](../core-concepts/autonomous-agents.md) encodes raw experiences and data into its storage systems.

## The Encoding Pipeline
1.  **Filtering:** Identifying which parts of a trajectory or document are "memory-worthy" to avoid noise.
2.  **Transformation:** Converting information into the target format (e.g., text for [Token-Level](agent-token-level-memory.md), embeddings for [RAG](../advanced-retrieval/rag.md), or weights for [Parametric](agent-parametric-memory.md)).
3.  **Indexing:** Assigning metadata or relational links (see [Pseudo-Knowledge Graphs](../advanced-retrieval/pseudo-knowledge-graph.md)) to facilitate later retrieval.

## Triggering Formation
Memory can be formed:
- **Passively:** Automatically saving all interactions.
- **Actively:** The agent explicitly decides to "take a note" (see [Persistent Note-Taking](../confucius/confucius-persistent-notes.md)).
- **Reflectively:** Periodically reviewing logs to extract lessons (see [ACE Reflection](../agentic-harness/ace-process-reflection.md)).

## See Also
- [Agent Memory](agent-memory.md)
- [Memory Evolution Dynamics](agent-memory-evolution.md)
- [Memory Retrieval Mechanisms](agent-memory-retrieval.md)
