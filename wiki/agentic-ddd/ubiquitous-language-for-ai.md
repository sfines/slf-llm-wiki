# Ubiquitous Language for AI

**Ubiquitous Language** is a core DDD concept that, in [Agentic DDD](agentic-ddd-overview.md), becomes the bridge between human intent and AI execution.

## The Semantic Bridge
In Agentic DDD, the Ubiquitous Language is used to:
- **Prompt Engineering:** System prompts should use the precise terminology of the domain.
- **Tool Definitions:** Function names and parameter descriptions must align with domain concepts.
- **Knowledge Retrieval:** [RAG (Retrieval-Augmented Generation)](../advanced-retrieval/rag.md) systems index data using the domain's shared vocabulary.

## Benefits of Semantic Alignment
- **Reduced Hallucinations:** When agents use the same language as their training data or tools, they are more likely to reason correctly.
- **Better Tool Selection:** Clear, domain-specific tool descriptions help agents choose the right action for a given context.
- **Human-Agent Collaboration:** Domain experts can audit agent reasoning because the agent "thinks" in the language of the business.

## Guidelines for AI Ubiquitous Language
1. **Be Unambiguous:** Avoid terms that have different meanings in different [Bounded Contexts](bounded-contexts-in-mas.md).
2. **Use Nouns for Entities:** Ensure [Entities and Aggregates](agentic-state-management.md#entities-and-aggregates-as-guardrails) are clearly named.
3. **Use Verbs for Actions:** Tools should be named after business actions (e.g., `process_claim` instead of `update_db_row`).

## See Also
- [Agentic Domain-Driven Design Overview](agentic-ddd-overview.md)
- [Bounded Contexts in MAS](bounded-contexts-in-mas.md)
