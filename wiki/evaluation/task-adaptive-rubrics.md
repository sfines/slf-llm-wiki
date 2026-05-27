# Task-Adaptive Rubrics

Task-Adaptive Rubrics evaluate LLM agent trajectories using criteria dynamically generated for the specific task at hand, moving away from the dominant paradigm of static LLM-as-a-Judge rubrics (e.g., standardizing on Helpfulness, Fluency, and Safety).

Different tasks require distinct evaluation dimensions. For instance, a code debugging agent should be evaluated on Correctness and Error Handling, whereas a web search agent should be graded on Search Efficiency and Coverage. The AdaRubric framework utilizes an LLM's parametric knowledge of task structures and domain conventions to output orthogonal, task-relevant evaluation dimensions along with calibrated 1-5 scoring criteria, vastly improving the correlation with human expert judgment.

## References
- [AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning](../../raw/adarubric-paper.md)