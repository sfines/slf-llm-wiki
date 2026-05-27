# Area Synthesis: Evaluation

## Definition
Agent and LLM evaluation focuses on rigorously assessing the performance, safety, and reliability of models and multi-agent systems using dynamic, task-adaptive rubrics rather than static benchmarks.

## Key Algorithms & Patterns
- Task-Adaptive Rubrics
- Confidence-Weighted Evaluation
- Dimension-Aware Filtering

## Defining Papers
- *AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning*

## Summary of the Field
Evaluation is shifting from static, one-size-fits-all datasets to dynamic, LLM-generated rubrics that adapt to the specific dimensions of a given task, improving inter-rater reliability and producing denser reward signals.

## State of Current Thought
There is a growing consensus that standard metrics fail to capture the multidimensional nature of agent performance. Modern evaluation frameworks prioritize dimension-aware filtering to prevent catastrophic failures in critical dimensions from being masked by high overall scores.

## Areas of Controversy / Ongoing Conversation
The primary debate involves the reliability of "LLM-as-a-judge" paradigms and whether models can effectively synthesize reward signals without inheriting their own parametric biases.
