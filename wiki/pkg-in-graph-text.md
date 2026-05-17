# In-Graph Text Preservation

**In-Graph Text** is a core technical feature of the [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md) framework that preserves the richness of natural language within a graph structure.

## Contrast with Traditional KGs
- **Traditional Knowledge Graphs:** Decompose text into strict (Subject, Predicate, Object) triplets. This process often loses nuance, modal qualifiers, and context.
- **PKG Approach:** Nodes and edges in the graph contain chunks of raw **natural language text**. The graph structure provides the "relational skeleton," while the text provides the "semantic meat."

## Benefits
- **Zero Information Loss:** Prevents the "extraction bottlenecks" where critical details are discarded during formal KG construction.
- **Improved Contextualization:** LLMs can reason over the raw text while using graph links to jump between related concepts.
- **Richer Representation:** Captures complex ideas that are difficult to express in simple triplets (e.g., conditional statements, nuanced descriptions).

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [Relational Awareness in RAG](rag-relational-awareness.md)
- [PKG Construction Algorithm](pkg-construction-algorithm.md)
