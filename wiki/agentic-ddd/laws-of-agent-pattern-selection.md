# Laws of Agent Pattern Selection

Huang and Zhou (2026) derived five empirical laws governing how environmental constraints dictate the architectural choices within the [Two-Dimensional AI Agent Framework](./two-dimensional-agent-framework.md).

1. **Law 1: Time pressure determines architectural complexity.** Seconds afford simple Chains; minutes afford Routes and Loops; days afford complex Hierarchies and Orchestration.
2. **Law 2: Action authority determines governance pattern.** Advisory systems need Approval Gates; low-risk auto-execution requires [Blast Radius Control](./blast-radius-control-pattern.md).
3. **Law 3: Failure cost asymmetry reshapes reflection.** If false negatives are fatal (e.g., healthcare), reflection patterns (like Generator-Critic) must be deliberately biased toward safe errors.
4. **Law 4: Volume determines collaboration needs.** Single items need no collaboration; moderate volume needs Fan-Out/Gather; high volume requires Hierarchical Delegation.
5. **Law 5: Same pattern, different parameterization.** A pattern is a structural template, not a behavioral prescription. The exact implementation varies entirely by domain context.

## References
- Huang, J., & Zhou, J. T. (2026). A Two-Dimensional Framework for AI Agent Design Patterns.


## Source
- [A Two-Dimensional Framework for AI Agent Design Patterns](../../raw/two-dimensional-ai-agent-patterns-paper.md)
