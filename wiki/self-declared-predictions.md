# Self-Declared Predictions (AHE)

A **Self-Declared Prediction** is a foundational concept in the [Decision Observability](ahe-decision-observability.md) pillar of [Agentic Harness Engineering](agentic-harness-engineering.md).

## The Falsifiable Contract
When the "evolving agent" makes a change to the harness, it must explicitly state what it expects to happen. This turns a simple edit into a **falsifiable contract**:
- **Hypothesis:** "Adding this `grep` rule will prevent the agent from using `cat` on large binary files."
- **Prediction:** "This will reduce the `ExecutionTimeout` error rate by 15%."

## Closing the Loop
After the next round of benchmark execution (e.g., on [Terminal-Bench 2](terminal-bench-2.md)):
1.  The system calculates the actual performance change.
2.  It compares the result to the agent's prediction.
3.  The agent receives a "Prediction Accuracy Report."

## Why it Matters
This mechanism prevents **Stochastic Hill Climbing**, where an agent makes random changes that happen to improve scores in the short term but don't encode deep engineering principles.

## See Also
- [AHE Pillar: Decision Observability](ahe-decision-observability.md)
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
