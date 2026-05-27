# Sliding-Window Attention in Test-Time Training

Sliding-Window Attention (SWA) is critical when utilizing Test-Time Training (TTT) on mini-batches to model long contexts.

## Role in TTT
If a model updates its weights only at the end of a mini-batch of tokens, it effectively suffers from complete amnesia regarding earlier tokens within that exact same mini-batch. SWA acts as the local, short-term memory buffer. By setting the sliding window size slightly larger than or equal to the mini-batch size, SWA provides strict, lossless local context. Once the batch boundary is hit, TTT executes a gradient step to compress that local information structurally into the model's MLP weights for long-term retention. 

## References
- [End-to-End Test-Time Training for Long Context](../../raw/ttt-long-context.md)
