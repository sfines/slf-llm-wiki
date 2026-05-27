# High Bandwidth Flash (HBF)

High Bandwidth Flash (HBF) is an emerging memory architecture designed to combine the massive capacity of NAND flash with the high bandwidth of High Bandwidth Memory (HBM).

## Concept

HBF stacks flash dies in a manner similar to HBM, using vertical integration to achieve a dense, wide interface. The primary goal is to address the capacity limits and high costs of HBM by leveraging the economic and density advantages of flash memory. 

By replacing or supplementing HBM with HBF, datacenter nodes can achieve up to a **10X increase in memory capacity** per node while maintaining comparable read bandwidths.

## Benefits for LLM Inference

In the context of Large Language Models (LLMs), HBF offers several transformative benefits:
- **10X Weight Memory:** Since model weights remain frozen during inference, HBF can host massive models, such as giant Mixture of Experts (MoE) architectures, on far fewer chips.
- **10X Context Memory:** HBF can store massive, slow-changing contexts (like a web corpus, codebase, or academic library) for use in Retrieval-Augmented Generation (RAG) applications.
- **Reduced System Size:** By holding more data per chip, HBF reduces the total number of hardware nodes required for a model, cutting down on total cost of ownership (TCO), power, and interconnect latency.

## Limitations and Trade-offs

Flash memory brings two inherent restrictions that must be managed by software and hardware co-design:
1. **Limited Write Endurance:** Flash cells wear out after many write/erase cycles. Thus, HBF is unsuited for rapidly updating data like the KV cache for ongoing generations. It must be reserved for read-heavy, infrequently updated data.
2. **Page-based, High-Latency Reads:** Flash reads occur at page granularity with microsecond-scale latencies (compared to nanoseconds for DRAM). Small reads can severely diminish the effective bandwidth, requiring software to optimize data access patterns.

Because of these constraints, HBF is proposed as a complement to traditional DRAM/HBM, rather than a total replacement.

## References
- [Challenges and Research Directions for Large Language Model Inference Hardware](../../raw/llm-inference-hardware-paper.md)
