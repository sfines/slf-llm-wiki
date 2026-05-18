# Agent Cross-Boundary Trust Tiers

The authorization model separates the evaluation logic from how trust is established between an issuer and an evaluator. It formally accommodates three varying tiers of trust infrastructure maturity.

## Three Trust Tiers

- **Tier 1 - Bilateral:** Both parties have a prior relationship, exchanging keys directly or relying on simple endpoints (e.g., JWKS).
- **Tier 2 - Federated:** The parties may not interact directly but share a common trust anchor, relying on PKI or X.509 certificate chains.
- **Tier 3 - Decentralized:** No prior relationship is required. Verifiable Credentials carry their own trust chain, resolved dynamically through decentralized registries.

## Uniform Semantics

Regardless of the trust tier, the authorization semantics, constraint types, and attenuation rules remain identical across all deployments.

## See Also
- [Three-Layer Authorization Architecture](three-layer-authorization-architecture.md)
- [Portable Agent Authorization](portable-agent-authorization.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
