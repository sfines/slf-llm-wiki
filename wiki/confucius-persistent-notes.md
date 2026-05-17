# Confucius Persistent Note-Taking

The **Persistent Note-Taking System** in the [Confucius Code Agent (CCA)](confucius-code-agent.md) enables [Continual Learning](continual-learning.md) across different sessions and tasks.

## Beyond Short-Term Memory
While [Hierarchical Working Memory](confucius-hierarchical-memory.md) manages information within a single session, the note-taking system allows the agent to capture insights that should persist.

## Mechanics
- **Self-Generated Documentation:** The agent writes notes about repository structure, discovered bugs, or successful debugging strategies.
- **External Storage:** These notes are stored outside the immediate session context (e.g., in a dedicated `notes/` directory or a vector database).
- **Retrieval-on-Demand:** When starting a new task or encountering a similar problem, the agent can retrieve relevant notes to inform its reasoning.

## Continual Learning
This system allows the agent to "learn" from its own experience without requiring model fine-tuning. Over time, the agent builds a personalized knowledge base for the specific codebase it operates on.

## See Also
- [Confucius Code Agent (CCA)](confucius-code-agent.md)
- [Confucius Hierarchical Working Memory](confucius-hierarchical-memory.md)
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
