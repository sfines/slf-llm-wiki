# Agent Experiential Memory

**Experiential Memory** is the storage of an [Autonomous Agent's](autonomous-agents.md) past experiences, including trajectories, actions taken, successes, and failures.

## Role in Learning
Experiential memory is the foundation for [Continual Learning](continual-learning.md). It allows agents to:
- **Avoid Repeating Mistakes:** Recognizing failure patterns from previous attempts.
- **Reuse Successful Plans:** Retrieving high-performing strategies (see [Agentic Plan Caching](agentic-plan-caching.md)).
- **Self-Improve:** Providing the evidence base for [Agentic Context Engineering (ACE)](agentic-context-engineering.md) and [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md).

## Implementation
- **[Persistent Note-Taking](confucius-persistent-notes.md):** Formalizing "lessons learned" into structured documents.
- **Trajectory Caching:** Storing the full logs of successful sessions for future retrieval or offline training.
- **Self-Reflection:** Agents periodically review their experiential memory to update their internal "playbooks."

## See Also
- [Agent Memory](agent-memory.md)
- [Continual Learning](continual-learning.md)
- [Agentic Plan Caching](agentic-plan-caching.md)
