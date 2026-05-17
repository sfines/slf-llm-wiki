# AppWorld Benchmark Evaluation

**AppWorld** is a complex, long-horizon benchmark used to evaluate agents in multi-app environments (e.g., managing email, calendar, and files simultaneously).

## ACE Performance
In the [Agentic Context Engineering (ACE)](agentic-context-engineering.md) research, the framework was evaluated on AppWorld:
- **Result:** ACE consistently outperformed strong baselines, matching top-ranked production agents.
- **Test-Challenge Split:** On the most difficult split of the benchmark, ACE surpassed commercial production systems despite using a smaller, open-source model.
- **Learning Rate:** The evaluation showed that ACE could rapidly adapt to the complex multi-app domain through only a few rounds of [Reflection](ace-process-reflection.md) and [Curation](ace-process-curation.md).

## Key Takeaway
The success on AppWorld demonstrates that **Structured Context Evolution** can compensate for smaller model sizes in highly complex, tool-rich domains.

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [SWE-Bench-Pro Analysis](swe-bench-pro.md)
- [Terminal-Bench 2](terminal-bench-2.md)
