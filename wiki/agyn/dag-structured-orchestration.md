# DAG-Structured Orchestration

Directed Acyclic Graph (DAG) Structured Orchestration defines multi-agent workflows as a series of interconnected nodes, where data flows in a single direction without cycles. It provides a highly visual and deterministic state-machine abstraction for complex processes.

## Workflow Components

- **Nodes**: Represent distinct processing steps, API calls, or specialized LLM agents dedicated to a single operational task.
- **Edges**: Define the conditional routing and data dependencies between nodes, dictating the flow of the pipeline.

## Advantages in Finance

- Enables parallel execution (e.g., simultaneous sector and competitor analysis) followed by convergent synthesis nodes.
- Makes the logical flow of due diligence transparent, auditable, and easily modifiable for non-technical investment teams.

## See Also

- [Event-Driven Orchestration Architecture](event-driven-orchestration-architecture.md)
- [Task Decomposition in Financial Agents](task-decomposition-in-financial-agents.md)
- [Raw Source: VC Due Diligence Paper](../../raw/multi-agent-vc-due-diligence-paper.md)
