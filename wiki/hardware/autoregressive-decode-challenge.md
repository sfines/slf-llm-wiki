# Autoregressive Decode Challenge

The Autoregressive Decode phase is the primary bottleneck in Large Language Model (LLM) inference, making it fundamentally different from the training phase or the initial Prefill phase.

## Concept

In Transformer models, the inference process is split into two phases:
1. **Prefill:** Similar to training, it processes all tokens of an input sequence simultaneously. It is inherently parallel and generally compute-bound.
2. **Decode:** The phase where the model generates output tokens one by one (autoregressively). Because each step depends on the previous ones and generates only one token, it cannot be parallelized across tokens. This sequential nature makes the Decode phase heavily **memory-bound**.

## Impacts on Hardware

Current datacenter AI accelerators (like GPUs and TPUs) are historically designed with training in mind (high compute FLOPS). The Decode phase challenges this paradigm because:
- **Low Arithmetic Intensity:** Generating a single token requires accessing massive weight matrices and the KV Cache, meaning the system spends more time moving data from memory to compute units than performing calculations.
- **Latency Sensitivity:** For user-facing applications, the time-to-first-token and time-to-completion must be very low. Memory bandwidth limits how fast each Decode iteration can run.

## Exacerbating Trends

Recent AI software trends further strain the Decode phase:
- **Mixture of Experts (MoE):** Drastically increases model size, meaning more weights must be loaded from memory.
- **Reasoning Models:** Generate many "thought" tokens before yielding user-facing output, heavily expanding the sequential Decode workload.
- **Long Contexts & RAG:** Increases the size of the KV cache that must be accessed during both Prefill and Decode.

Addressing the Autoregressive Decode challenge requires paradigm shifts in hardware, emphasizing memory capacity, memory bandwidth, and interconnect latency over brute-force compute FLOPS.

## References
- [Challenges and Research Directions for Large Language Model Inference Hardware](../../raw/llm-inference-hardware-paper.md)
