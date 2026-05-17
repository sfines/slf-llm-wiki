# Agent Local Handling

Agent Local Handling is the first dimension of the triadic exception management model. It defines the immediate, tactical, and atomic actions taken by an agent to mitigate an exception directly at the operation level.

## Tactics and Strategies

Local handling mechanisms are diverse and target specific modalities of failure:
- **Prompt and Context Adjustments**: `Clarify Prompt` (asking users for missing details), `Prompt Sanitization` (cleaning injected text), and `Context Tagging`.
- **Logic and Planning Fixes**: `Graph Validation`, `Logic Re-ranking`, `Plan Repair` (repairing broken task sequences), and `Constraint Pruning`.
- **Execution Level Fixes**: `Retry with Backoff` (for transient API failures), `Switch Tool` (fallback to alternatives), and `Schema Validation`.
- **Memory Fixes**: `Reset Memory`, `Memory Slot Isolation` (quarantining poisoned facts).
- **Escalation**: `Escalate to Human` when the agent lacks authorization or confidence.

## Role in the Triadic Model

The local handler attempts to neutralize the immediate error. Its success or failure subsequently dictates how the workflow's Flow Control component will orchestrate the continuation or termination of the current thread.

## See Also
- [Structured Handling Executor](./structured-handling-executor.md)
- [Handling Pattern Registry](./handling-pattern-registry.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)