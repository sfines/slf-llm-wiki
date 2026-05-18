# Portable Agent Authorization

Portable agent authorization defines a standardized model for autonomous agents to carry explicit, bounded, and verifiable authority across organizational boundaries. It ensures that an agent's authority can be consistently interpreted by independent receivers regardless of the underlying infrastructure.

## Core Principles

- **Delegated Authority:** Agents must act with explicit, bounded authority granted by organizations or individuals.
- **Portability:** The authorization payload is container-agnostic and maintains stable evaluation semantics whether encoded in JWTs, Verifiable Credentials, or other formats.
- **Fail-Closed Execution:** Any unidentifiable constraint, missing context, or failed semantic mapping results in an immediate denial.

## See Also
- [Agent Identity vs Authorization](agent-identity-vs-authorization.md)
- [Three-Layer Authorization Architecture](three-layer-authorization-architecture.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
