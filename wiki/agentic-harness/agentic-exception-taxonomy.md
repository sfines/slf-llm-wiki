# Agentic Exception Taxonomy

The Agentic Exception Taxonomy is a comprehensive classification system mapping the diverse range of failures encountered by LLM-driven agents. Based on empirical studies, it categorizes 36 distinct exception types across 12 core agent artifacts.

## Taxonomy Artifacts

Exceptions are categorized by the underlying source or object of the failure. The 12 artifacts include:
- **Goal & Context**: Ambiguous goals, conflicting instructions, and context corruption.
- **Reasoning & Planning**: Contradictory logic, circular reasoning, faulty task structuring, and overextended planning.
- **Memory & Knowledge Base**: Memory poisoning, outdated memory, hallucinated facts, and knowledge conflicts.
- **Model & Tool**: Token limit exceeded, output malformations, tool invocation errors, and unavailable tools.
- **Interface & Task Flow**: API semantic mismatches, UI element misclicks, text recognition errors, and early stopping.
- **Multi-Agent & External Systems**: Communication failures, role violations, protocol mismatches, and external adversarial attacks.

## Workflow Phases

The taxonomy distinguishes exceptions across two critical phases to enable proper root cause analysis:
- **Reasoning and Planning (RP) Phase**: Cognitive-level breakdowns occurring before the agent acts on the external world.
- **Execution (E) Phase**: Operational breakdowns occurring when the agent invokes tools, APIs, or interfaces.

## See Also
- [Reasoning-Phase Exceptions](./reasoning-phase-exceptions.md)
- [Execution-Phase Exceptions](./execution-phase-exceptions.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)