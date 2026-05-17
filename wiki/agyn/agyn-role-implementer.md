# Agent Role: Implementer

The **Implementer** is a specialized role within the [Agyn Framework](agyn-framework.md) responsible for executing code changes.

## Key Responsibilities
- **Code Generation:** Writing the actual implementation based on the [Researcher's](agyn-role-researcher.md) specification.
- **Pull Request (PR) Creation:** Formatting changes into a clear, reviewable PR.
- **Testing:** Running existing test suites and writing new tests to verify the fix.
- **Sandbox Execution:** Operating within [Isolated Sandboxes](agyn-sandbox-environments.md) to ensure safety.

## Interaction Loop
The Implementer works in a tight loop with the [Reviewer](agyn-role-reviewer.md). If a review fails, the Implementer must address the feedback and resubmit the changes.

## See Also
- [Agyn Framework](agyn-framework.md)
- [Agent Role: Researcher](agyn-role-researcher.md)
- [Agent Role: Reviewer](agyn-role-reviewer.md)
- [Agent Sandbox Environments](agyn-sandbox-environments.md)
