# Falsifiable Contracts in AI Development

A **Falsifiable Contract** is an architectural pattern where every automated system change is accompanied by a testable prediction, ensuring the system can "learn" from its own evolution.

## Application in Agentic Systems
This pattern is most prominently used in the [Decision Observability](ahe-decision-observability.md) pillar of [Agentic Harness Engineering](agentic-harness-engineering.md).

## Core Requirements
1.  **Explicit Intent:** The system must state "I am changing X to achieve Y."
2.  **Measurable Metric:** The outcome must be tied to a benchmark or log metric (e.g., [Terminal-Bench 2](terminal-bench-2.md) Pass@1).
3.  **Verification Loop:** The system must automatically compare the outcome to the prediction and update its internal strategy.

## Benefits
- **Empirical Grounding:** Moves AI development from "vibe-based" prompting to evidence-based engineering.
- **Safe Autonomy:** Allows agents to self-correct their own scaffolding without human oversight.

## See Also
- [AHE Pillar: Decision Observability](ahe-decision-observability.md)
- [Self-Declared Predictions (AHE)](self-declared-predictions.md)
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
