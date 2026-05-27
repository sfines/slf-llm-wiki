# 3D Memory-Logic Stacking

3D Memory-Logic Stacking is an advanced packaging technique that stacks memory dies directly on top of or beneath compute logic dies, connecting them vertically using Through Silicon Vias (TSVs). It is a form of [Processing Near Memory (PNM)](processing-near-memory.md).

## Concept

Traditional 2D hardware places memory and logic side-by-side on an interposer or PCB, requiring data to travel horizontally through shoreline I/O pins. This limits the number of connections and increases the distance data must travel. 

By stacking dies vertically, 3D packaging utilizes TSVs to create a wide-and-dense memory interface. This drastically shortens the physical data path, leading to:
- **Massively Higher Bandwidth**
- **Lower Power Consumption (Joules/bit)**

## Implementation Approaches

There are two primary ways 3D memory-logic stacking is currently being explored for LLM inference:
1. **Compute-on-HBM-Base-Die:** This approach reuses existing High Bandwidth Memory (HBM) designs but replaces or augments the bottom logic base die of the HBM stack with a custom AI compute engine. It maintains standard HBM bandwidth but lowers power consumption by 2–3X because the data no longer has to travel off the stack to a separate GPU/TPU.
2. **Custom 3D Solutions:** Designing a completely new memory and logic stack from the ground up, utilizing an even wider memory interface than HBM to push bandwidth and bandwidth-per-watt limits further.

## Challenges

While 3D stacking offers immense bandwidth benefits for the memory-bound [Autoregressive Decode phase](autoregressive-decode-challenge.md), it faces notable engineering hurdles:
- **Thermals:** Stacking dies vertically reduces the surface area available for heat dissipation. Because LLM Decode has low arithmetic intensity, one solution is to intentionally run the compute logic at lower clock speeds and voltages to prevent the memory from overheating.
- **Standardization:** Achieving widespread adoption requires an industry standard for the memory-logic interface in 3D stacks, preventing proprietary lock-in.

## References
- [Challenges and Research Directions for Large Language Model Inference Hardware](../../raw/llm-inference-hardware-paper.md)
