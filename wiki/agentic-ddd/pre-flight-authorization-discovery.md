# Pre-Flight Authorization Discovery

Pre-flight discovery reduces integration brittleness by allowing agents to check their semantic compatibility with a receiver before initiating an action-bearing request.

## Governance Manifests

Service providers publish a signed, versioned governance contract (usually at a `.well-known` endpoint) declaring their supported vocabularies, profile versions, required context fields, and accepted trust anchors.

## Sender-Side Compatibility Checks

Agents compare their available credentials against this manifest to ensure they are properly scoped and supported. This check is purely advisory; authoritative policy enforcement still occurs entirely on the receiver side during admission.

## See Also
- [Governed Semantic Resolution](governed-semantic-resolution.md)
- [Agent Cross-Boundary Trust Tiers](agent-cross-boundary-trust-tiers.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
