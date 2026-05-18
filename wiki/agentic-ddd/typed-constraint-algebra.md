# Typed Constraint Algebra

The typed constraint algebra defines a compact, deterministic set of rules that constrain an agent's authority. By avoiding open-ended execution logic, it ensures independent receivers can evaluate constraints consistently and safely.

## Core Constraint Types

- **NumericLimitConstraint:** Bounded quantitative authority (e.g., spending limits, ceilings, and floors).
- **TemporalWindowConstraint:** Validity periods enforcing when an agent's permission applies.
- **EnumeratedListConstraint:** Categorical or recipient restrictions (allow-lists and deny-lists).
- **StringPatternConstraint:** Namespace or resource scoping, matching exact strings, prefixes, suffixes, or restricted globs.

## Evaluation Semantics

Evaluation is conjunctive, total, and fail-closed. All constraints must pass for a request to be allowed, and any unknown constraint type automatically results in a denial.

## See Also
- [Three-Layer Authorization Architecture](three-layer-authorization-architecture.md)
- [Agent Delegation Attenuation](agent-delegation-attenuation.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
