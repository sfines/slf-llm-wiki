# AutoPR Exception Case Study

The AutoPR Exception Case Study empirically validates the effectiveness of the SHIELDA framework in diagnosing and resolving complex, cross-phase errors in real-world LLM software engineering agents.

## The Flawed Scenario

In the evaluation, an AutoPR agent was given an ambiguous, high-level prompt instructing it to add a reviewer to a repository. Driven by flawed reasoning, the agent formulated an illegal plan: modifying its own GitHub Actions CI/CD `.yaml` file to automate the assignment. During execution, the platform predictably rejected the `git push` command, resulting in a `ProtocolMismatchException`.

## Multi-Stage Recovery Trace

The framework resolved this crash through Phase-Aware Recovery:
1. **Local Failure**: The initial `Retry with Backoff` local handler failed, as permissions were fundamentally blocked.
2. **Root Cause Analysis**: The Escalation Controller analyzed the AgentOps logs, tracing the rejected workflow file artifact backward to discover the true error: a `Faulty Task Structuring` exception in the reasoning phase.
3. **Plan Repair**: SHIELDA automatically aborted the execution thread, formulated a corrective prompt forbidding `.yaml` modifications, and fed this to the Reasoning Module.
4. **Resolution**: The agent successfully generated a compliant, alternative plan and resolved the task safely.

This case study proves that autonomous agents require closed-loop, cross-phase analysis rather than simple isolated retry scripts.

## See Also
- [Phase-Aware Recovery](./phase-aware-recovery.md)
- [SHIELDA Framework](./shielda-framework.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)