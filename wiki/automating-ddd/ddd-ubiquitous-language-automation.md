# Ubiquitous Language Generation

**Ubiquitous Language Generation** is the first step of the [Automating DDD Framework](ddd-prompting-framework.md), used to establish a semantic foundation for the system.

## Process
The LLM analyzes unstructured domain text (requirements, meeting transcripts, documentation) to extract:
- **Core Entities:** Nouns that represent key business concepts.
- **Actions:** Verbs that represent business processes.
- **Glossary:** Clear, unambiguous definitions for each term.

## Importance
As the foundation of the chain, this step is critical. Errors here lead to the most severe [Error Propagation](ddd-error-propagation.md) in later architectural stages.

## See Also
- [Ubiquitous Language for AI](../agentic-ddd/ubiquitous-language-for-ai.md)
- [Automating DDD Framework](ddd-prompting-framework.md)
- [Rich Domain Models for Agents](../agentic-ddd/rich-domain-models-for-agents.md)
