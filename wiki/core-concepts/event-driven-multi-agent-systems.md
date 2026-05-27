# Event-Driven Multi-Agent Systems

Event-driven multi-agent systems (MAS) operate in environments where state transitions are triggered by discrete events rather than synchronous, fixed time steps.

## Characteristics
In these systems, decisions are intrinsically asynchronous. Agents do not act continuously; instead, they are activated only when newly realized world events (e.g., a job arrival, a machine breakdown, or a resource release) or protocol messages make a new decision legally necessary.

This architecture closely mirrors real-world physical and industrial processes. Platforms like [DESBench](desbench.md) utilize an event-driven core to study how physical environment evolution and protocol-level coordination are deeply intertwined. 

## Coordination Complexity
Because events happen asynchronously, agents must deal with multi-timescale decision processes and partial observability. They must react to immediate events while also adhering to [Dynamically Coupled Constraints](dynamically-coupled-constraints.md) that unfold over longer horizons. The choice of coordination—whether using a [Centralized Coordination Paradigm](centralized-coordination-paradigm.md), [Hierarchical Coordination Paradigm](hierarchical-coordination-paradigm.md), [Heterarchical Coordination Paradigm](heterarchical-coordination-paradigm.md), or [Holonic Coordination Paradigm](holonic-coordination-paradigm.md)—dictates how these asynchronous events are distributed, escalated, and resolved across the agent network.

## References
- [When Does Hierarchy Help? Benchmarking Agent Coordination in Event-Driven Industrial Scheduling](../../raw/when-does-hierarchy-help-paper.md) (Source)
- [Dynamically Coupled Constraints](dynamically-coupled-constraints.md)