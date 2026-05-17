# Unified Agent Orchestrator

A **Unified Agent Orchestrator** is the central management module in the [Confucius Code Agent (CCA)](confucius-code-agent.md) that coordinates the reasoning loops and tool interactions.

## Key Responsibilities
- **Workflow Management:** Sequencing high-level steps (e.g., Analyze -> Plan -> Execute -> Verify).
- **Tool Coordination:** Resolving tool calls, handling parameters, and feeding results back to the agent.
- **Memory Integration:** Interfacing with [Hierarchical Working Memory](confucius-hierarchical-memory.md) and the [Persistent Note-Taking System](confucius-persistent-notes.md).

## Design Philosophy
The CCA orchestrator is designed for **Scalability** and **Transparency**. It avoids deep nested pipelines in favor of a "flat" execution model that is easier for the model to navigate and for humans to audit.

## See Also
- [Confucius Code Agent (CCA)](confucius-code-agent.md)
- [Agent Harness](agent-harness.md)
- [Multi-Agent Systems (MAS)](multi-agent-systems.md)
