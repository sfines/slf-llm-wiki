# Terminal-Bench 2

**Terminal-Bench 2** is a rigorous benchmark used to evaluate the performance of [Coding Agents](../core-concepts/autonomous-agents.md) in terminal-based environments.

## Role in AHE
In the [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md) paper, Terminal-Bench 2 served as the primary evaluation environment for the evolving harness. 

## Key Metrics
- **Pass@1:** The primary success metric, representing the percentage of tasks resolved in a single attempt.
- **Token Efficiency:** AHE demonstrated that evolved harnesses could achieve higher Pass@1 scores while using **12% fewer tokens**.

## Performance Gains
Through 10 iterations of the AHE loop:
- **Baseline:** 69.7% Pass@1.
- **AHE Evolved:** 77.0% Pass@1.
- **Comparison:** Outperformed the human-designed **Codex-CLI** harness (71.9%).

## See Also
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
- [AHE Pillar: Decision Observability](ahe-decision-observability.md)
