# Agent State Recovery

Agent State Recovery is the final dimension of the triadic exception management model. It specifies how an agent must repair its internal memory, context, or external environment following an exception, ensuring consistency before the workflow resumes.

## Recovery Mechanisms

State recovery uses three distinct strategies to manage side effects:
- **No-op**: No state repair is required because the exception caused no persistent side effects (e.g., a read-only API call timing out).
- **Rollback**: The agent restores its internal state to a previously verified, clean checkpoint. This is critical for clearing out poisoned memory, hallucinated context, or toxic prompt injections.
- **Compensate**: The agent triggers a logical reversal to undo external side effects. For example, if an agent erroneously created a database record before crashing, it must issue a `DELETE` command as compensation.

## Maintaining Consistency

Without rigorous state recovery, LLM agents easily fall victim to "Error Propagation," where faulty assumptions or orphaned data pollute subsequent reasoning cycles. Proper state recovery guarantees that agents always operate from a baseline of semantic and operational truth.

## See Also
- [Agent Exception Flow Control](./agent-exception-flow-control.md)
- [Agent Local Handling](./agent-local-handling.md)
- [Phase-Aware Recovery](./phase-aware-recovery.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)