# Adaptive Trajectory Recycling

Adaptive trajectory recycling is a post-training data synthesis strategy that transforms successful multi-round reasoning traces into high-quality supervision data for LLM agents, eliminating the need for manual annotation.

## Pipeline
1. **Generation:** Agents generate multi-path reasoning trajectories interacting with environments and tools.
2. **Filtration:** Trajectories are passed through a multi-stage quality assurance pipeline. They are filtered based on absolute outcome correctness, tool-invocation efficiency, and logical coherence.
3. **Recycling:** Only the highest-fidelity trajectories (capturing error recovery patterns and optimal tool-use sequences) are retained. These traces teach subsequent models how to "rethink" and logically deduce rather than relying on strict pattern memorization.

## References
- [ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control](../../raw/rethinker.md)
