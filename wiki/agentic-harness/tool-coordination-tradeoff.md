# Tool-Coordination Trade-off

The tool-coordination trade-off is a fundamental scaling limit in multi-agent systems where tool-heavy tasks suffer disproportionately from coordination overhead.

## Mechanism

In agentic systems operating under fixed computational token budgets, adding more agents fragments the available reasoning capacity. When a task requires complex, multi-step orchestration of various tools, the overhead of inter-agent communication (message passing, synchronization, state reconciliation) consumes a significant portion of the context window and token budget. 

As a result, agents are left with insufficient capacity to execute complex tool logic. The efficiency penalties compound as environmental complexity increases. In contrast, a single-agent system avoids this coordination tax, allowing it to dedicate its entire budget to tool orchestration and sequential reasoning.

---
[Source](../../raw/scaling-agent-systems-paper.md)