# Automated Aggregate Design

**Automated Aggregate Design** is the fourth stage of the [Automating DDD Framework](ddd-prompting-framework.md), focusing on the internal structure of [Bounded Contexts](bounded-contexts-in-mas.md).

## Task
The LLM is tasked with identifying:
- **Entities:** Objects with a unique identity (e.g., `User`).
- **Value Objects:** Descriptors without identity (e.g., `Address`).
- **Aggregate Roots:** The primary entry points for each cluster of entities.

## Challenges
The research ([Eisenreich et al., 2026](../raw/automating-ddd-paper.md)) noted that this stage is where **[Error Propagation](ddd-error-propagation.md)** begins to significantly impact utility. LLMs often struggle to define the "right" boundaries for aggregates without a deep understanding of consistency requirements.

## See Also
- [Agentic State Management](agentic-state-management.md)
- [Bounded Contexts in MAS](bounded-contexts-in-mas.md)
- [Automating DDD Framework](ddd-prompting-framework.md)
