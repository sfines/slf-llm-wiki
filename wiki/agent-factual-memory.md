# Agent Factual Memory

**Factual Memory** refers to the long-term storage of declarative knowledge, domain-specific facts, or world knowledge accessible to an [Autonomous Agent](autonomous-agents.md).

## Implementation
- **[RAG (Retrieval-Augmented Generation)](rag.md):** The most common method, using vector databases, knowledge graphs, or [Pseudo-Knowledge Graphs (PKG)](pseudo-knowledge-graph.md) to provide the agent with relevant external facts at test time.
- **Parametric Memory:** Knowledge encoded directly into the model weights during pre-training or fine-tuning.
- **Domain-Specific Playbooks:** Curated sets of facts and rules provided in the system prompt (see [ACE](agentic-context-engineering.md)).

## Challenges
- **Trustworthiness:** Managing hallucinations or contradictions between retrieved facts and the model's internal knowledge.
- **Staleness:** Updating factual memory when domain information changes.
- **Context Relevance:** Ensuring that only the most pertinent facts are retrieved to avoid context saturation.

## See Also
- [Agent Memory](agent-memory.md)
- [Retrieval-Augmented Generation (RAG)](rag.md)
- [Ubiquitous Language for AI](ubiquitous-language-for-ai.md)
