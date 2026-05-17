# AHE Component: Execution-Risk Middleware

**Execution-Risk Middleware** is a critical component of an [Agent Harness](agent-harness.md) that monitors for "unproductive" or "dangerous" agent behaviors during long-horizon tasks.

## Targeted Risks
The [AHE framework](agentic-harness-engineering.md) evolves middleware to mitigate:
- **Infinite Loops:** Detecting when an agent repeats the same failing command without modification.
- **Resource Exhaustion:** Monitoring token usage or execution time for a single sub-task.
- **Action Hallucination:** Identifying when an agent attempts to use a tool that has not been defined in its current [Bounded Context](../agentic-ddd/bounded-contexts-in-mas.md).

## Observability-Driven Evolution
By analyzing trajectories via the [Agent Debugger](ahe-agent-debugger.md), the system can identify new "risk patterns" and automatically generate middleware to prevent them in future runs.

## See Also
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
- [AHE Pillar: Component Observability](ahe-component-observability.md)
- [AHE Shell-Tool Guardrails](ahe-shell-tool-guardrails.md)
