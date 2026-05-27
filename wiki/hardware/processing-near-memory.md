# Processing Near Memory (PNM)

Processing-Near-Memory (PNM) is a hardware architecture strategy that places memory and compute logic on nearby but physically separate dies. It aims to bridge the memory bandwidth gap without the severe manufacturing and thermal constraints of integrating compute directly into memory cells.

## PIM vs. PNM

In recent computer architecture research, two terms are often contrasted:
- **Processing-in-Memory (PIM):** Compute logic and memory reside on the *same* die.
- **Processing-Near-Memory (PNM):** Compute logic and memory are on *separate* dies, but packaged closely together (e.g., using interposers or advanced 2D/3D packaging).

## Advantages for Datacenter LLMs

For datacenter-scale Large Language Models (LLMs), PNM is currently favored over PIM for several reasons:

1. **Software Sharding:** PIM requires LLM data structures to be sharded into very small pieces (e.g., 32–64 MB) to map onto individual memory banks, which makes software partitioning complex and increases communication overhead. PNM allows for much larger shards (e.g., 16–32 GB), vastly simplifying software orchestration.
2. **Logic Efficiency (PPA):** Integrating logic into a DRAM process (as required by PIM) typically results in slower, higher-power compute components. PNM allows the compute logic to be manufactured on a cutting-edge logic node, optimizing Performance, Power, and Area (PPA).
3. **Power and Thermal Budgets:** Memory dies have strict thermal limits. Placing high-performance compute on a memory die restricts how fast the compute can run before overheating the memory. PNM relaxes these constraints.
4. **Economics:** PNM can utilize commodity memory pricing, whereas PIM requires custom, lower-volume memory manufacturing.

*Note on Mobile Devices:* While PNM excels in the datacenter, PIM may still be viable for mobile LLM inference. Mobile workloads operate under tighter energy constraints, smaller batch sizes, and shorter contexts, which mitigates many of PIM's sharding and thermal disadvantages.

## Examples of PNM
- [3D Memory-Logic Stacking](3d-memory-logic-stacking.md) (which is a vertical form of PNM)
- Attaching compute units to DDR buffer chips (e.g., Samsung AXDIMM)
- Utilizing CXL interfaces to connect memory and compute expansions (e.g., Marvell Structera)

## References
- [Challenges and Research Directions for Large Language Model Inference Hardware](../../raw/llm-inference-hardware-paper.md)
