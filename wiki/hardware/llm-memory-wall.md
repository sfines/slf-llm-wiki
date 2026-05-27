# The LLM Memory Wall

The "Memory Wall" refers to the growing disparity between improvements in compute capability (FLOPS) and memory bandwidth/capacity, which has become a critical bottleneck for Large Language Model (LLM) inference.

## Concept

While processor compute capabilities have scaled exponentially over the past decade (e.g., an 80X increase in 64-bit FLOPS for some GPUs from 2012 to 2022), memory bandwidth has scaled much more slowly (e.g., only a 17X increase). This gap is particularly detrimental to the [Autoregressive Decode phase](autoregressive-decode-challenge.md), which relies heavily on memory bandwidth rather than compute power.

## Diverging Cost Trends

Compounding the performance gap is the cost economics of memory technologies:
- **High Bandwidth Memory (HBM):** Current AI accelerators rely on HBM to maximize bandwidth. However, HBM is becoming increasingly expensive in terms of both $/GB (capacity) and $/GBps (bandwidth) due to packaging complexity and density limits.
- **DRAM Scaling Deceleration:** Standard DRAM density growth is slowing significantly. While capacity historically quadrupled every 3-6 years, current projections indicate it will take over a decade to achieve the next fourfold growth.

## SRAM-only Limitations

Early attempts to avoid the Memory Wall involved using full-reticle chips filled entirely with SRAM (e.g., wafer-scale integration). While SRAM provides massive bandwidth, modern LLMs have outgrown on-chip SRAM capacities, forcing these designs to eventually retrofit external DRAM.

## Future Directions

Overcoming the LLM Memory Wall requires new memory architectures, such as [High Bandwidth Flash](high-bandwidth-flash.md) for cheaper capacity, and [Processing Near Memory](processing-near-memory.md) or [3D Memory-Logic Stacking](3d-memory-logic-stacking.md) for improved bandwidth and power efficiency.

## References
- [Challenges and Research Directions for Large Language Model Inference Hardware](../../raw/llm-inference-hardware-paper.md)
