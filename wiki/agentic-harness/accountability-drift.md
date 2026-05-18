# Accountability Drift

Accountability drift happens when an agent's action is executed and logged without the reconstructable state, authority, or evidence necessary to justify why the action was permitted.

## The Audit Gap

In a safe multi-agent execution pipeline, it is not enough that an action was theoretically permissible; there must be proof. Accountability drift is the loss of the "why." If a destructive command (e.g., file deletion) occurs, but the audit log lacks the hashed capability token, the active constraint digest, or the explicit reasoning that admitted the action, the system suffers from an accountability gap.

## Tamper-Evident Evidence

To counteract this drift, systems must employ robust event logging that ties every realized action to the exact state of constraints at the time of execution. If evidence cannot be reconstructed, the action represents an accountability failure.

## See Also
- [Constraint Drift](constraint-drift.md)
- [Constraint State Governance](constraint-state-governance.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
