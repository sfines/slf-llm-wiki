# The Sandwich Protocol

The Sandwich Protocol is an empirical testing framework used to evaluate scalable oversight techniques. It involves three roles:
1. **The Non-Expert (Weak Human):** A user who has intentions but cannot fully specify their intent or reliably verify the execution outcomes.
2. **The Model:** The AI system "sandwiched" in the middle, capable of performing the task but potentially misaligned with the user's intent.
3. **The Expert:** An evaluator who does not participate in generation but has the capability to reliably evaluate the output against the "golden standard" of the user's true intent.

The effectiveness of an oversight method is measured by the gap in alignment achieved under the non-expert's supervision versus what would be achievable under the expert's supervision.

---
**Source:** [Steering LLMs via Scalable Interactive Oversight](../../raw/interactive-oversight-paper.md)