# CoT Length Generalization

CoT Length Generalization investigates the robustness of a model's reasoning capabilities when it encounters problems requiring reasoning chains (or text outputs) that are significantly longer or shorter than those present in its training data.

Because the training data typically contains reasoning sequences within a specific length range, test cases outside this range represent a severe distributional shift. Research demonstrates that CoT's ability to extrapolate to longer sequences is highly fragile; performance degrades sharply as the required reasoning steps or token sequence lengths deviate from the learned distribution.

---
**Source:** [Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens](../../raw/cot-mirage-paper.md)