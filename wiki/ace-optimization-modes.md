# Offline vs. Online Context Optimization

The [Agentic Context Engineering (ACE)](agentic-context-engineering.md) framework distinguishes between two modes of context refinement: **Offline** and **Online** optimization.

## Online Optimization
- **Trigger:** Happens during the execution of a task.
- **Mechanism:** The agent updates its [Working Memory](agent-working-memory.md) or intermediate plans based on immediate feedback.
- **Focus:** Short-term task completion.

## Offline Optimization
- **Trigger:** Happens between task sessions.
- **Mechanism:** A specialized pipeline performs [Generation](ace-process-generation.md), [Reflection](ace-process-reflection.md), and [Curation](ace-process-curation.md) over a batch of trajectories.
- **Focus:** Long-term strategy refinement and updating the [Dynamic Cheatsheet](ace-dynamic-cheatsheets.md).

## Synergy
ACE combines both modes, using online feedback to solve immediate problems and offline optimization to formalize those solutions into the agent's permanent "playbook."

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [ACE Adaptive Memory](ace-adaptive-memory.md)
- [Continual Learning](continual-learning.md)
