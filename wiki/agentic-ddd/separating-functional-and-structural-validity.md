# Separating Functional and Structural Validity

When evaluating the performance of LLM coding agents, it is critical to decouple functional correctness from structural compliance.

## Dual Evaluation Methodology

Traditional benchmarks often reward functionally correct but structurally arbitrary solutions. To rigorously test an agent's ability to build production systems, evaluations must measure two orthogonal axes:
1.  **Functional Correctness:** This is evaluated using end-to-end behavioral tests (e.g., HTTP test suites built against an OpenAPI specification). This tests the API behavior rather than its implementation, decoupling the evaluation from the internal code structure.
2.  **Structural Compliance:** This is assessed using static verifier functions that scan the generated codebase to ensure that the required architectural layers, database engines, and ORMs are actually present and properly utilized.

Task success is defined strictly as the intersection of both: passing the behavioral tests *while* satisfying the structural constraints.

---
[Source](../../raw/constraint-decay-paper.md)