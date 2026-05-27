# Dimension-Aware Filtering

Dimension-Aware Filtering is a selection strategy used during agent evaluation that mandates a trajectory meet a minimum score threshold across *all* distinct evaluation dimensions simultaneously, rather than just relying on a global average score.

Relying on a single Absolute Threshold or global average can result in "dimension-level quality masking," where an agent trajectory fails completely at one critical dimension (e.g., reasoning or error handling) but still passes the global threshold because it scores perfectly on other dimensions (e.g., extraction or safety). Dimension-Aware Filtering provably prevents this masking, yielding high-quality preference pairs suitable for robust reward modeling and DPO training.

## References
- [AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning](../../raw/adarubric-paper.md)