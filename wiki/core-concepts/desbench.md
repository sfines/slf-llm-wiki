# Distributed Event-driven Scheduling Benchmark (DESBench)

The Distributed Event-driven Scheduling Benchmark (DESBench) is a testing framework designed to evaluate agent coordination in hierarchical, event-driven industrial scheduling environments.

## Overview
Unlike traditional benchmarks that focus on task completion in weakly coupled environments, DESBench operates in a shared discrete-event simulation (DES) environment. It captures multi-timescale decision making, partial observability, and dynamically coupled constraints such as resource budgets and system capacity. Agent actions in this benchmark directly influence the evolution of the underlying system, impacting future availability and constraint pressure.

## Evaluation Dimensions
DESBench evaluates coordination paradigms across four key dimensions:
- **Effectiveness**: Measures schedule quality (e.g., mean makespan, tardiness, completed jobs).
- **Constraint Alignment**: Captures how well runs respect shared operational limits and resource budgets.
- **Coordination Efficiency**: Quantifies interaction cost, communication burden, and decision overhead induced by a given protocol.
- **Robustness**: Characterizes early termination, handling of dynamic disruptions, and residual work debt at episode end.

## References
- [When Does Hierarchy Help? Benchmarking Agent Coordination in Event-Driven Industrial Scheduling](../../raw/when-does-hierarchy-help-paper.md) (Source)
- [Centralized Coordination Paradigm](centralized-coordination-paradigm.md)
- [Hierarchical Coordination Paradigm](hierarchical-coordination-paradigm.md)
- [Heterarchical Coordination Paradigm](heterarchical-coordination-paradigm.md)
- [Holonic Coordination Paradigm](holonic-coordination-paradigm.md)