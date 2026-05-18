# Multi-Principal Workflow Composition

Many enterprise workflows require actions that involve more than one independently authorized agent. Instead of attempting to merge separate credentials into one, the model handles this through multi-principal composition.

## Independent Evaluation

Each agent's credential is evaluated independently against its own issuer trust, semantic profile, and the request context. 

## Workflow Policy

The receiver's workflow policy determines which combination of valid credentials or attestations is required to approve an action. The safe default is a conjunctive composition where all necessary participant authorizations must pass, and the final action operates within the intersection of their constraints.

## See Also
- [Portable Agent Authorization](portable-agent-authorization.md)
- [Three-Layer Authorization Architecture](three-layer-authorization-architecture.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
