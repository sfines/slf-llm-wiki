# Agent Architecture-Task Alignment

The principle of architecture-task alignment dictates that the success of a multi-agent system is determined not by the sheer number of agents, but by how well the system's communication topology matches the structure of the task.

## Task Dependencies

Different tasks require distinct coordination mechanisms:
*   **Parallelizable Tasks:** Tasks like broad financial reasoning benefit immensely from centralized coordination, where an orchestrator can delegate independent sub-tasks to workers and synthesize the results.
*   **High-Entropy Search Spaces:** Tasks like dynamic web navigation benefit from decentralized (peer-to-peer) coordination, allowing for lateral information fusion and consensus formation.
*   **Strictly Sequential Tasks:** For tasks requiring strict sequential state-dependent reasoning (e.g., crafting items in a game where step B requires the output of step A), multi-agent systems universally degrade performance. The forced decomposition of a sequential problem into artificial sub-tasks generates massive coordination overhead and fragments the reasoning process, making a Single-Agent System (SAS) vastly superior.

---
[Source](../../raw/scaling-agent-systems-paper.md)