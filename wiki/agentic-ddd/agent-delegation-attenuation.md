# Agent Delegation Attenuation

Delegation allows an authorized entity to grant a subset of its authority to another agent. This model enforces a strict, monotonic attenuation invariant: authority can only be narrowed, never widened.

## Attenuation Rules

- **Permissions:** A delegate's permissions must be a subset of the delegator's.
- **Constraints:** A delegate must retain all parent constraints. Constraints can be tightened (e.g., lowering a spending ceiling or shortening a time window) but never omitted or loosened.

## Delegation vs Invocation

The model recommends keeping delegation chains local to a shared trust domain. Across trust boundaries, it is safer for independent agents to use service invocation, as cross-boundary delegation introduces severe accountability and audit complexity.

## See Also
- [Typed Constraint Algebra](typed-constraint-algebra.md)
- [Portable Agent Authorization](portable-agent-authorization.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
