# Three-Layer Authorization Architecture

To support portability and interoperability across ecosystems, the authorization model separates the cryptographic envelope from the semantic meaning and runtime evaluation of the authority.

## Layer 1: Credential Container

The cryptographic envelope that carries the payload, providing authenticity and tamper evidence. Examples include JSON Web Tokens (JWT) or W3C Verifiable Credentials.

## Layer 2: Authorization Payload

The normative core that defines what the agent is authorized to do. It contains the agent identity, issuer identity, declared permissions, and typed policy constraints.

## Layer 3: Enforcement Engine

The receiver's runtime system that extracts the payload, evaluates constraints against the current context, merges with local policy, and produces a definitive allow-or-deny decision.

## See Also
- [Portable Agent Authorization](portable-agent-authorization.md)
- [Typed Constraint Algebra](typed-constraint-algebra.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
