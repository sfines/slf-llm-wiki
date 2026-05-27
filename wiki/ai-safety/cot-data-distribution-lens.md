# CoT Data Distribution Lens

The Data Distribution Lens proposes that Chain-of-Thought (CoT) reasoning is not a deliberate, human-like inferential process, but rather a structured inductive bias learned from in-distribution training data. 

Under this framework, CoT operates as a conditional pattern-matching and generation process that interpolates from statistical regularities present in the training distribution. The effectiveness of CoT is fundamentally bounded by the degree of distribution discrepancy between the training data and the test queries. When pushed beyond its training distribution—whether in task structure, sequence length, or prompt format—CoT reasoning is revealed to be a fragile "mirage" that quickly degrades.

---
**Source:** [Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens](../../raw/cot-mirage-paper.md)