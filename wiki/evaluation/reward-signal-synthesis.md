# Reward Signal Synthesis

Reward Signal Synthesis is the process of translating complex, multi-dimensional LLM agent evaluations into dense reward signals or preference pairs suitable for reinforcement learning (e.g., RLHF or Direct Preference Optimization).

By utilizing detailed rubrics and step-by-step scoring, frameworks like AdaRubric can compare filtered trajectories to isolate high-quality preferred paths and informative dispreferred paths. By calculating the score margin between two trajectories, the system produces preference pairs ($+$ and $-$ pairs) where the magnitude of the margin can further modulate the DPO loss weight. This allows models to learn targeted, task-directed reasoning strategies rather than merely adopting surface-level stylistic preferences.

## References
- [AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning](../../raw/adarubric-paper.md)