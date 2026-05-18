# Stateful Enforcement Profiles

While the core authorization model is stateless to maximize performance, advanced workflows often require managing cumulative risk, such as enforcing aggregate spending limits over a sequence of actions.

## Cumulative Limit Constraints

This advanced extension bounds total aggregate exposure. It requires the credential to include a cryptographically signed pointer to an authoritative state source (e.g., a ledger or registry). 

## Verifiable State Proofs

In decentralized environments, agents may carry cryptographically signed state vouchers that act as verifiable state proofs. These vouchers ensure monotonic sequencing and freshness to prevent replay attacks and synchronization lag.

## See Also
- [Typed Constraint Algebra](typed-constraint-algebra.md)
- [Three-Layer Authorization Architecture](three-layer-authorization-architecture.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
