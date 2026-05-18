# Agent Identity vs Authorization

In agentic systems, identifying an agent is not sufficient; the system must also verify its authority. While traditional systems often conflate the two by using bearer tokens as proxies for access, autonomous action requires explicitly separating identity from authorization.

## Authentication is Not Enough

Federated workload identities or API keys confirm *who* is acting, but they do not define *what* the agent is permitted to do, under what constraints, or whether its delegation is valid.

## Policy-Bound Authority

Authorization must reflect business and regulatory rules—such as monetary ceilings, temporal windows, and disclosure boundaries—that travel with the agent. This allows receivers to verify compliance before processing an action.

## See Also
- [Portable Agent Authorization](portable-agent-authorization.md)
- [Agent Cross-Boundary Trust Tiers](agent-cross-boundary-trust-tiers.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
