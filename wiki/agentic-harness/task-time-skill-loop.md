# Task-Time Skill Loop

The Task-Time Loop in SkillOps operates as an executable Graph-of-Graphs planner, retrieving, validating, and stitching skills dynamically to solve an immediate multi-step objective.

## Core Stages

1. **Skill Matching**: Ranks skills combining lexical (BM25) and semantic relevance, filtering strictly by whether current state satisfies their preconditions.
2. **Dependency Stitching**: Constructs an execution plan enforcing both dependency and compatibility edges between selected skills.
3. **Validator and Adapter Insertion**: Detects unvalidated edges or type mismatches in the candidate plan, inserting missing validators or adapters dynamically to prevent silent failures.
4. **Local Repair**: Upon execution failure, substitutes the failed skill with an alternative (`alt` neighbor) or attempts localized repair using the error trace. Unrecoverable errors are pushed to the Library-Time buffer.

## See Also

- [Dependency Stitching](dependency-stitching.md)
- [Library-Time Skill Loop](library-time-skill-loop.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
