# Inter-Rater Reliability for LLM Evaluators

Inter-Rater Reliability, standardly measured by metrics like Krippendorff's $\alpha$ or Fleiss' $\kappa$, quantifies annotation agreement. In the context of LLM-as-a-Judge paradigms, it acts as a principled deployment criterion to assess whether the LLM evaluator is consistent across multiple independent scoring runs.

For robust evaluation, an LLM evaluator should ideally yield Krippendorff’s $\alpha \ge 0.80$, treating each independent evaluation run as an "annotator." Adaptive, context-specific rubrics generally produce much higher reliability scores than generic fixed rubrics or basic prompts, proving that structured guidelines stabilize LLM output variance during evaluation.

## References
- [AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning](../../raw/adarubric-paper.md)