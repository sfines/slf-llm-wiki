# Solver-Critic-Selector Architecture

The Solver-Critic-Selector architecture is a multi-agent staging paradigm used to deeply reason over complex scientific queries.

## Stages
1. **Solver:** Executes multiple rounds of tool interactions (e.g., executing Python, searching the web) to synthesize an initial solution. It acts as an exploratory generator, often producing diverse but noisy hypotheses.
2. **Critic:** Takes the reasoning trajectory from the solver and performs a structured summary-and-guidance reflection. It diagnoses logical flaws or strategic errors missed by simple verification, thereby amplifying global solution quality.
3. **Selector:** Aggregates outputs from parallel solver-critic paths. It leverages internal uncertainty metrics (like perplexity) and iterative re-selection to definitively choose the best candidate answer, ensuring stability.

## References
- [ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control](../../raw/rethinker.md)
