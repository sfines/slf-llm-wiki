# Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation is a technique that grants LLMs access to external knowledge sources to improve the accuracy and relevance of their responses.

## RAG in Agentic Systems
In [Agentic DDD](agentic-ddd-overview.md), RAG systems are often indexed using the [Ubiquitous Language](ubiquitous-language-for-ai.md) to ensure the agent retrieves information that is semantically aligned with the domain.

## Advanced Techniques
- **[Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md):** Combines vector retrieval with meta-path guided graph traversal and in-graph text preservation to solve fragmentation issues.

## Components
- **Vector Database:** Stores embeddings of the knowledge base.
- **Retriever:** Identifies the most relevant chunks of data for a given query.
- **Generator:** The LLM that synthesizes the final response using the retrieved context.
