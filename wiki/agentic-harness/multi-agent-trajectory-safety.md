# Multi-Agent Trajectory Safety

Multi-Agent Trajectory Safety shifts the focus of LLM agent evaluation from the final output delivered to the user to the entire sequence of actions, delegations, and internal messages that led to that output.

## The Insufficiency of Final Output Checks

Traditional guardrails act as filters on the final response. However, modern LLM agents execute long-horizon workflows utilizing tools, reading files, and coordinating. A system might deliver a perfectly compliant final message while having already leaked sensitive data internally, modified restricted files, or bypassed testing boundaries. 

## Maintaining Safety Across the Graph

To guarantee multi-agent trajectory safety, constraints must remain operative throughout the entire execution graph. Benchmarks and evaluations must measure not just the success rate of the final patch or response, but whether at every transition layer the constraints were preserved, audited, and enforced.

## See Also
- [Constraint Drift](constraint-drift.md)
- [Safe Multi-Agent Behavior Paradigms](safe-multi-agent-behavior-paradigms.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
