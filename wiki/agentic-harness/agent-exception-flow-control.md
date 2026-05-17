# Agent Exception Flow Control

Agent Exception Flow Control represents the second dimension of the triadic exception management model. It determines the overarching execution trajectory of the agentic workflow after a local handling tactic has been applied to an error.

## Flow Control Decisions

Flow control utilizes a simple, deterministic set of commands to manage thread progression:
- **Continue**: The agent proceeds to the next planned step. This is typically invoked when a local handler (like a retry or a plan repair) successfully resolves the exception.
- **Skip**: The agent bypasses the current faulty subgoal or step. This is useful for non-critical tasks where partial completion is acceptable.
- **Abort**: The agent immediately terminates the current task or execution thread. This is triggered when an exception is unrecoverable, or when a deeply flawed reasoning plan must be destroyed before a fresh execution thread can begin.

## Workflow Orchestration

By decoupling the flow logic from the immediate error-correction tactics, agent architectures gain massive flexibility. An agent can abort a poisoned thread gracefully without crashing the entire multi-agent system, allowing supervisors to dispatch a new task cleanly.

## See Also
- [Agent Local Handling](./agent-local-handling.md)
- [Agent State Recovery](./agent-state-recovery.md)
- [Structured Handling Executor](./structured-handling-executor.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)