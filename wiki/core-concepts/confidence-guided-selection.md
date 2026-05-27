# Confidence-Guided Selection

Confidence-Guided Selection is a mechanism to stabilize answer identification across multiple generated candidate reasoning paths.

## Process
In complex multi-agent frameworks, parallel generation scaling produces multiple potential answers. To find the optimal one:
- **Perplexity as a Signal:** Models use internal consistency metrics, specifically perplexity, to measure uncertainty. High perplexity triggers additional rounds of adjudication.
- **Mitigating Position Bias:** The selection process is decoupled from ordinal heuristics by permuting candidate positions (e.g., using Latin Square designs).
- **Iterative Refinement:** Prior selection outcomes and confidence scores are iteratively fed back into the prompt, Bayesian-updating the probabilities to amplify high-confidence candidates and suppress noisy ones.

## References
- [ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control](../../raw/rethinker.md)
