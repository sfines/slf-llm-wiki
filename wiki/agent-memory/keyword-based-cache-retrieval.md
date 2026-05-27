# Keyword-Based Cache Retrieval

In the context of agent memory and plan caching, Keyword-Based Cache Retrieval replaces naive semantic query matching. Traditional query-based semantic similarity often struggles in agentic environments, triggering false positives when contexts differ but wording is similar.

## Mechanism
- **Intent Extraction:** A cost-effective language model extracts a keyword or key phrase that captures the higher-level intent of the input task (e.g., extracting "mean calculation" from a verbose instruction to compute an average).
- **Exact Matching:** The cache stores `(keyword, plan template)` pairs. By applying an exact match against these extracted keywords, the system minimizes false positives and ensures the most relevant generalized plan template is retrieved.

## References
- [Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents](../../raw/agentic-plan-caching.md)
