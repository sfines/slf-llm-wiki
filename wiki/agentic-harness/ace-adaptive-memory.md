# ACE Adaptive Memory

**Adaptive Memory** is the memory architecture used in [Agentic Context Engineering (ACE)](agentic-context-engineering.md) to manage the lifecycle of [Dynamic Cheatsheets](ace-dynamic-cheatsheets.md).

## Core Functionality
Adaptive memory is responsible for:
- **Accumulation:** Gathering successful strategies from different task sessions.
- **Refinement:** Consolidating similar strategies to remove redundancy.
- **Selection:** Choosing the most relevant pieces of information for the current task context.

## Contrast with Static Prompts
While a static prompt remains fixed, adaptive memory allows the agent's "worldview" to evolve and grow more sophisticated as it encounters more edge cases and failures.

## Relationship to Factual Memory
While [Factual Memory](../agent-memory/agent-factual-memory.md) focuses on external data (RAG), Adaptive Memory focuses on **Internal Strategic Knowledge**—the "how-to" knowledge learned through experience.

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [ACE Dynamic Cheatsheets](ace-dynamic-cheatsheets.md)
- [Agent Memory](../agent-memory/agent-memory.md)
