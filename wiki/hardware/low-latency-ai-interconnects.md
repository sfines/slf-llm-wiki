# Low-Latency AI Interconnects

As Large Language Models (LLMs) grow in size and complexity, inference workloads increasingly span multiple chips or entire datacenter clusters. In this distributed environment, interconnect **latency** has emerged as a bottleneck equal to, or sometimes greater than, interconnect bandwidth.

## The Shift from Bandwidth to Latency

Historically, datacenter interconnects were optimized for training, which requires massive bandwidth to synchronize large gradient updates across supercomputers. 

However, LLM inference—specifically the [Autoregressive Decode phase](autoregressive-decode-challenge.md)—has different networking characteristics:
- **Frequent, Small Messages:** Because the Decode phase generates one token at a time, batch sizes are small, and tensor parallelism results in frequent exchanges of small data packets across chips.
- **Hop Count Penalties:** Models using Mixture of Experts (MoE) or massive context windows require larger system sizes to hold memory capacity, increasing the physical distance and number of network hops between coordinating chips.

In this paradigm, the time it takes for a message to traverse the network (latency) becomes more critical than the volume of data that can be sent at once (bandwidth).

## Research Directions

To mitigate network latency in inference clusters, several architectural strategies are being researched:

1. **High-Connectivity Topologies:** Moving away from standard fat-tree designs toward topologies with lower hop counts, such as high-dimensional tori or dragonfly networks. These may sacrifice total bisection bandwidth in exchange for faster point-to-point latency.
2. **Processing-in-Network:** Offloading communication collectives (like all-reduce, broadcast, and MoE token dispatch) directly into the network switches. In-network aggregation allows data to be combined as it travels, reducing latency and freeing up endpoints.
3. **AI Chip Optimization:** Redesigning the accelerator chip itself by placing compute engines physically closer to the network interface, or routing small incoming network packets directly into low-latency on-chip SRAM instead of off-chip DRAM.
4. **Latency-Aware Reliability:** If a node fails, traditional networks incur massive latency spikes as workloads migrate. New strategies include maintaining local standby spares, or implementing soft-timeout mechanisms where the system accepts slightly degraded inference quality (using a prior result or approximation) rather than stalling the entire pipeline waiting for a straggler message.

## References
- [Challenges and Research Directions for Large Language Model Inference Hardware](../../raw/llm-inference-hardware-paper.md)
