# Governed Semantic Resolution

To enable portable authorization without forcing all organizations to use identical internal schemas, the model relies on a hub-and-spoke architecture for semantic resolution.

## Minimum Viable Vocabulary (MVV)

The horizontal core defines a set of reserved, industry-agnostic semantic identifiers (e.g., `core.amount`, `core.request_time`) that every conformant engine must recognize.

## Vertical Industry Profiles

Domain-specific vocabularies extend the core for specific use cases (like insurance or aerospace). Receivers use governed mapping profiles to map signed identifiers to their own local fields.

## Type-Safe Coercion

Mappings must be unambiguous and type-safe. If an alias is missing, conflicts, or implies an incompatible type, the evaluation fails closed immediately.

## See Also
- [Pre-Flight Authorization Discovery](pre-flight-authorization-discovery.md)
- [Typed Constraint Algebra](typed-constraint-algebra.md)
- [Raw Source: Digital Identity for Agentic Systems](../../raw/digital-identity-agentic-systems-paper.md)
