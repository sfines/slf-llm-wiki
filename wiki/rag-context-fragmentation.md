# Context Fragmentation in RAG

**Context Fragmentation** is a common failure mode in traditional [RAG](rag.md) systems where the process of "chunking" text severs logical and semantic connections.

## Causes
- **Fixed-size Chunking:** Arbitrarily breaking text every 500 tokens often splits sentences or paragraphs in the middle of a complex argument.
- **Isolated Retrieval:** Retrieving the top-k chunks without their surrounding context leaves the LLM with "fragmented" evidence.

## Consequences
- **Hallucinations:** The model attempts to "fill in the gaps" between fragments.
- **Incompleteness:** Missing the "connective tissue" needed for multi-hop reasoning.
- **Reasoning Errors:** The LLM misinterprets a fragment because it lacks the necessary qualifiers from a neighboring (un-retrieved) chunk.

## Mitigation
Advanced frameworks like [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md) mitigate fragmentation by using [In-Graph Text](pkg-in-graph-text.md) and [Relational Awareness](rag-relational-awareness.md) to reconstruct the full context at test time.

## See Also
- [Relational Awareness in RAG](rag-relational-awareness.md)
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)
