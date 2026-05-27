# Chain-of-Thought Monitoring

Chain-of-Thought (CoT) monitoring is a proposed safety technique where a model's intermediate reasoning steps are evaluated (by humans or other AI systems) to understand the model's intentions, detect misaligned behaviors, or catch reward hacking during training and deployment.

While CoT monitoring is a promising way of noticing frequent undesired behaviors (since the model will likely verbalize the behavior at least a small fraction of the time), it is insufficient to definitively rule them out. Because models often fail to verbalize the true reasons behind their outputs (low CoT faithfulness), test-time monitoring of CoTs is unlikely to reliably catch rare, catastrophic, and unexpected behaviors that can be executed without explicit reasoning.

---
**Source:** [Reasoning Models Don't Always Say What They Think](../../raw/reasoning-models-paper.md)