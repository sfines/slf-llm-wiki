# APWA Heterogeneous Data Support

The **Agent-Parallel Workload Architecture (APWA)** is designed to be data-agnostic, supporting a wide range of information formats and processing styles.

## Supported Data Types
- **Structured Data:** Direct interaction with SQL databases, CSV files, and spreadsheets via parallel workers.
- **Unstructured Text:** Analyzing massive sets of PDFs, web pages, or repository files.
- **Semi-Structured Data:** Parallel processing of JSON/XML logs and API responses.

## Domain Versatility
APWA has been demonstrated in diverse domains:
- **Software Engineering:** Large-scale code refactoring across thousands of files.
- **Financial Services:** Real-time risk analysis across global market data.
- **Legal/Compliance:** Automated review of massive contract repositories.

## Role of Semantic Tooling
To handle this heterogeneity, APWA workers utilize [Agent-Ready Interfaces](probabilistic-consumers.md) and [Ubiquitous Language](ubiquitous-language-for-ai.md). This ensures that regardless of the data type, the worker can reason over it using a standardized set of business concepts.

## See Also
- [Pseudo-Knowledge Graph (PKG)](pseudo-knowledge-graph.md)
- [Agent Factual Memory](agent-factual-memory.md)
- [Model Context Protocol (MCP)](mcp.md)
