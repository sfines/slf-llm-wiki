# Phase-Aware Recovery

Phase-Aware Recovery is an advanced diagnostic and repair capability that enables agentic frameworks to trace low-level execution failures back to their high-level reasoning root causes. It bridges the gap between the execution phase and the reasoning/planning phase.

## The Need for Cross-Phase Tracing

In autonomous systems, an exception thrown during tool invocation (e.g., an API permission error) is often just a symptom. The true fault frequently lies upstream, such as the agent formulating a logically flawed plan that violates system constraints. Phase-aware recovery utilizes deep log analysis to trace the artifact that caused the execution crash back to its origin in the reasoning context.

## Closed-Loop Re-planning

Once the root cause is identified, phase-aware recovery initiates a closed-loop "diagnose-repair-re-execute" cycle. Instead of simply terminating the workflow, the system uses mechanisms like **Plan Repair** to:
1. Inject the newly discovered constraints back into the agent's reasoning prompt.
2. Force the agent to discard its initial flawed assumptions.
3. Generate a novel, safe alternative plan that bypasses the execution bottleneck.

This drastically improves agent resilience by actively correcting operational assumptions at runtime.

## See Also
- [AutoPR Exception Case Study](./autopr-exception-case-study.md)
- [Reasoning-Phase Exceptions](./reasoning-phase-exceptions.md)
- [Execution-Phase Exceptions](./execution-phase-exceptions.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)