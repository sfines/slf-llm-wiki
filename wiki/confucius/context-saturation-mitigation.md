# Context Saturation Mitigation

**Context Saturation Mitigation** is a set of techniques used in the [Confucius SDK](confucius-code-agent.md) to maintain agent performance in massive codebases.

## The Challenge
In a 100k+ file repository, a simple "read all files" approach leads to:
- **Noise:** Irrelevant files cluttering the context window.
- **Loss of Detail:** Important information being "pushed out" by the model's sliding window.
- **Performance Degradation:** LLMs struggle to reason over extremely large, unstructured context buffers.

## Mitigation Strategies
CCA employs several strategies to solve this:
1.  **[Hierarchical Working Memory](confucius-hierarchical-memory.md):** Organizing context into distinct layers.
2.  **Relevant Chunking:** Using [RAG](../advanced-retrieval/rag.md) and [Pseudo-Knowledge Graphs](../advanced-retrieval/pseudo-knowledge-graph.md) to retrieve only the most pertinent code snippets.
3.  **Active Summarization:** The agent periodically summarizes its current findings to "free up" context space while preserving key insights.
4.  **[Persistent Note-Taking](confucius-persistent-notes.md):** Offloading long-term knowledge to external storage.

## See Also
- [Confucius Hierarchical Working Memory](confucius-hierarchical-memory.md)
- [Agent Working Memory](../agent-memory/agent-working-memory.md)
- [Agentic Context Engineering (ACE)](../agentic-harness/agentic-context-engineering.md)
