# Topology-Dependent Error Amplification

Topology-dependent error amplification refers to how different multi-agent communication structures propagate or contain mistakes throughout an execution chain.

## Structural Differences

The architecture of a multi-agent system heavily influences its error dynamics:
*   **Independent Systems (Maximal Amplification):** Architectures where agents operate independently and simply aggregate their isolated outputs suffer from unchecked error propagation. In such systems, errors can be amplified dramatically (e.g., up to 17.2x) because a single individual mistake cascades directly into the final output without peer review.
*   **Centralized Coordination (Error Containment):** Architectures that employ a centralized orchestrator enforce a validation bottleneck. The orchestrator acts as a filter, intercepting and evaluating agent outputs before aggregation. This hierarchy contains error propagation (e.g., reducing amplification to 4.4x), making the system significantly more robust against individual agent hallucinations.

---
[Source](../../raw/scaling-agent-systems-paper.md)