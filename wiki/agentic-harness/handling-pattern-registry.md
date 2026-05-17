# Handling Pattern Registry

The Handling Pattern Registry is a centralized, indexed library of predefined recovery blueprints within the SHIELDA framework. It maps specific exception types to highly optimized mitigation strategies.

## Pattern Composition

Rather than housing monolithic scripts, the registry stores patterns composed of a triadic combination of mechanisms:
- **Local Handling**: The atomic action to attempt (e.g., `Retry with Backoff`, `Plan Repair`, `Graph Validation`).
- **Flow Control**: The thread resolution logic (e.g., `Continue`, `Abort`, `Skip`).
- **State Recovery**: The environmental cleanup action (e.g., `Rollback`, `Compensate`, `No-op`).

For example, pattern `P018` is defined as `[Retry with Backoff, Continue, No-op]`, which is highly effective for transient API timeouts.

## Exception Mapping

The registry maps the 36 taxonomy exceptions to 48 unique pattern IDs. Because many disparate errors share underlying recovery needs, treating handlers as composable patterns allows for massive scalability. For instance, both `Memory Poisoning` and `Tool Output Exception` can share a state-rollback pattern, while `Ambiguous Goal` and `Contradictory Reasoning` both utilize clarification patterns.

## See Also
- [Structured Handling Executor](./structured-handling-executor.md)
- [Exception Classifier](./exception-classifier.md)
- [SHIELDA Framework](./shielda-framework.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)