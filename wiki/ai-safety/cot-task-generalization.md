# CoT Task Generalization

CoT Task Generalization examines how well a model's Chain-of-Thought reasoning can transfer to previously unseen reasoning tasks or novel logical structures.

Evaluations within controlled environments show that CoT reasoning struggles with task generalization when introduced to novel transformations, elements, or compositions that deviate from the training set. There exists a critical threshold of task generalization complexity beyond which the probability of generating a correct CoT reasoning chain drops exponentially. This indicates that LLMs struggle to apply underlying logic to novel tasks, relying instead on structural memorization.

---
**Source:** [Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens](../../raw/cot-mirage-paper.md)