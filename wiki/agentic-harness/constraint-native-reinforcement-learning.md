# Constraint Native Reinforcement Learning

Constraint Native Reinforcement Learning is an approach to optimizing multi-agent systems where utility is only improved over trajectories whose constraints remain explicitly maintained by an underlying governance layer.

## Admissible Trajectories

Unlike standard safe RL which often adds safety penalties directly to the reward signal, Constraint Native RL relies on Constraint State Governance (CSG) to pre-define an "admissible set" of trajectories. If a trajectory violates freshness, scope, information flow, or auditability, it is deemed outside the comparison set and cannot be rewarded as a high-utility success, no matter the final outcome.

## The Closed-Loop Advantage

The governance layer provides the RL algorithm with a verifiable rollout record. The RL improves policy utility *strictly within* the safe boundary. Concurrently, rejected actions provide violation evidence that can be used to refine and update the governance rules themselves, creating a closed-loop system where utility optimization does not erode safety.

## See Also
- [Constraint State Governance](constraint-state-governance.md)
- [Utility-Induced Drift](utility-induced-drift.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
