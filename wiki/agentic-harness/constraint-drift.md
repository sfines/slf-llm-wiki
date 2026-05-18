# Constraint Drift

Constraint drift is the loss of operational force of a safety critical constraint across a multi-agent trajectory. In LLM-based agentic systems, a constraint may be present in an initial prompt but lose effectiveness as it is summarized, passed across agent delegations, communicated through channels, used in tool calls, or overlooked during optimization.

## The Drift Phenomenon

In a traditional single-turn LLM response, safety is governed locally at the output layer. For long-horizon agentic execution, a system may produce a compliant final answer while violating constraints along the way (e.g., leaking data internally or deleting a file). Constraint drift occurs when a safety rule ceases to be:
- **Fresh**: Actively applied to the current context.
- **Inherited**: Passed down accurately during delegation.
- **Enforceable**: Checked against the actual semantic effect of an action.
- **Auditable**: Reconstructable from execution traces.

## System-Level Preservation Failure

This drift is specifically a *preservation failure*. It differs from reward hacking or specification gaming in that it does not fundamentally require an adversarial proxy objective; rather, it results from the fragility of natural language constraints being diluted through complex execution pipelines, multi-agent handoffs, and memory loss.

## See Also
- [Memory Drift](memory-drift.md)
- [Authority Drift](authority-drift.md)
- [Information-Flow Drift](information-flow-drift.md)
- [Accountability Drift](accountability-drift.md)
- [Utility-Induced Drift](utility-induced-drift.md)
- [Constraint State Governance](constraint-state-governance.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
