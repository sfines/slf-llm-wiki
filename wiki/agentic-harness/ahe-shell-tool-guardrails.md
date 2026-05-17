# AHE Component: Shell-Tool Guardrails

**Shell-Tool Guardrails** are a specific type of [Harness Component](agent-harness.md) evolved and managed within the [AHE framework](agentic-harness-engineering.md).

## Definition
Guardrails are modular logic components that wrap around an agent's terminal tools. They serve as a "semantic filter" for inputs and outputs.

## Evolution Examples
Through the AHE loop, the system might evolve guardrails such as:
- **Input Sanitization:** Automatically stripping dangerous or redundant flags from shell commands.
- **Output Truncation:** Summarizing massive `ls -R` outputs into a high-level directory tree to save context tokens.
- **Error Remediation:** Intercepting a `FileNotFound` error and suggesting the agent use `find` or `grep` to locate the target.

## Observability
Each guardrail has a file-level representation ([Component Observability](ahe-component-observability.md)), allowing the system to track exactly how it affects agent performance.

## See Also
- [AHE Pillar: Component Observability](ahe-component-observability.md)
- [Agent Harness](agent-harness.md)
- [Execution-Risk Middleware](ahe-execution-risk-middleware.md)
