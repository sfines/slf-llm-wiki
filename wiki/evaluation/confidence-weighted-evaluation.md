# Confidence-Weighted Evaluation

Confidence-Weighted Evaluation is an approach to scoring multi-step LLM agent trajectories on a step-by-step basis, factoring in the relevance of each step to the overarching grading dimension.

When evaluating a trajectory against a specific rubric dimension (e.g., "API Selection Accuracy"), not all steps are equally relevant. A reasoning or planning step might not directly engage the API, so grading it rigidly against API Accuracy introduces noise. In frameworks like AdaRubric, the evaluator assigns both a score ($s$) and a confidence scalar ($c$) to each step for each dimension. The global trajectory score is then aggregated using confidence-weighted mechanisms (like weighted mean or geometric mean), lowering the variance and yielding much stronger reliability.

## References
- [AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning](../../raw/adarubric-paper.md)