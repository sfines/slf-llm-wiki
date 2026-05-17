# Agent Working Memory

**Working Memory** in [Autonomous Agents](autonomous-agents.md) refers to the information currently "held in mind" for the immediate reasoning step or task session.

## Characteristics
- **Short-Term:** Information is typically transient and relevant only to the current execution context.
- **High Accessibility:** Must be immediately available for the agent's reasoning loop.
- **Limited Capacity:** Constrained by the model's context window.

## Implementation Patterns
- **[Hierarchical Working Memory](confucius-hierarchical-memory.md):** Organizing information into layers (goals, sub-tasks, episodic detail) to prevent context saturation.
- **Scratchpads/CoT:** Using a portion of the context to store intermediate reasoning steps.
- **Dynamic Context Loading:** Loading only the most relevant snippets of a task's history.

## See Also
- [Agent Memory](agent-memory.md)
- [Agentic State Management](agentic-state-management.md)
- [Confucius Hierarchical Working Memory](confucius-hierarchical-memory.md)
