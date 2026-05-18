# AgentLeak Case Study

AgentLeak is a benchmark used to empirically demonstrate the reality of constraint drift, specifically information-flow drift, in LLM-based multi-agent systems.

## Internal Exposure Vulnerabilities

In an empirical replay of AgentLeak traces, researchers demonstrated that relying solely on output-level filtering makes the final answer look safe, but leaves internal communication channels severely exposed (e.g., 68.8% exposure rate). Sensitive information easily bleeds across inter-agent messages and shared memory writes.

## CSG Lite Remediation

By implementing "CSG Lite"—a transition-level governance check that evaluates actions against a disclosure policy before they are realized—the internal exposure rate was drastically reduced (down to 5.7%). The case study proves that safety checks must be moved to the channels where information actually flows, transitioning final-boundary monitoring into actionable, step-by-step audit evidence.

## See Also
- [Information-Flow Drift](information-flow-drift.md)
- [Constraint State Governance](constraint-state-governance.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
