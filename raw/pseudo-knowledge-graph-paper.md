# Pseudo-Knowledge Graph: Meta-Path Guided Retrieval and In-Graph Text for RAG-Equipped LLM

**Authors:** Yuxin Yang, Haoyang Wu, Tao Wang, Jia Yang, Hao Ma, Guojie Luo
**Date:** March 2025
**Source:** arXiv:2503.00309
**DOI:** 10.48550/arXiv.2503.00309

## Abstract Summary
This paper introduces the **Pseudo-Knowledge Graph (PKG)** framework to address limitations in traditional [RAG](../wiki/advanced-retrieval/rag.md) systems, particularly fragmented answers and lack of relational awareness in low-information-density databases. PKG integrates **Meta-path Retrieval**, **In-graph Text**, and **Vector Retrieval** to provide a richer knowledge representation and more precise information retrieval.

## Core Mechanisms
1.  **Pseudo-Knowledge Graph (PKG):** A framework that preserves natural language text within a graph structure, bridging the gap between unstructured text and formal knowledge graphs.
2.  **Meta-path Retrieval:** Leverages pre-defined paths through the graph to capture complex relationships and improve retrieval precision in multi-hop scenarios.
3.  **In-graph Text:** Preserves the original natural language context within the nodes/edges of the graph to avoid information loss during knowledge graph construction.
4.  **Vector Retrieval:** Complements graph-based retrieval with standard embedding-based searches.

## Key Results
- Evaluated on Open Compass and MultiHop-RAG benchmarks.
- Demonstrates superior effectiveness in managing large volumes of data and complex relationships compared to standard RAG.
- Improves accuracy and context-awareness in LLM responses.

## Reference
Yang, Y., et al. (2025). Pseudo-Knowledge Graph: Meta-Path Guided Retrieval and In-Graph Text for RAG-Equipped LLM. arXiv preprint arXiv:2503.00309.
