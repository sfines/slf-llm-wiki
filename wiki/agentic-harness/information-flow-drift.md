# Information-Flow Drift

Information-flow drift is a constraint failure mode where sensitive content improperly crosses boundaries—such as agent-to-agent messages, shared memory, tool arguments, or external queries—despite high-level privacy directives.

## Internal Exposure vs. Final Output

Many agent safety checks evaluate only the final output delivered to the user. Information-flow drift highlights the reality that safety is compromised long before the final answer is generated. For instance, an agent might strip an API key from the final response (passing output filters), but inadvertently expose it in an internal memory write or an external tool API call earlier in the trajectory.

## Taints and Budgets

Addressing information-flow drift requires maintaining explicit flow control, utilizing labels, data taints, and channel budgets. This ensures that sensitive information is tracked and blocked at the transition layer, not just the output layer.

## See Also
- [Constraint Drift](constraint-drift.md)
- [AgentLeak Case Study](agentleak-case-study.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
