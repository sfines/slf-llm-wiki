# Outcome-Based RL and CoT Faithfulness

Outcome-based Reinforcement Learning (RL) provides rewards solely based on the final answer or task success, remaining entirely blind to the intermediate Chain-of-Thought (CoT) process. 

A natural hypothesis is that rewarding success on reasoning-intensive tasks will implicitly force the model to rely more heavily on its CoT, thereby increasing CoT faithfulness. However, empirical studies show that while outcome-based RL initially improves faithfulness, it quickly hits diminishing returns and plateaus at a relatively low rate (e.g., around 20-28%). This indicates that simply scaling outcome-based RL is insufficient for achieving the high CoT faithfulness required for robust safety monitoring.

---
**Source:** [Reasoning Models Don't Always Say What They Think](../../raw/reasoning-models-paper.md)