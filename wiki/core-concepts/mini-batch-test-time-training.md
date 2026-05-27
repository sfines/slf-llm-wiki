# Mini-Batch Test-Time Training

During Test-Time Training (TTT), sequential token-by-token gradient updates (online gradient descent) can be computationally inefficient and highly unstable, prone to gradient explosion.

## Optimization
Mini-Batch TTT addresses this by partitioning the context into mini-batches. Gradients are accumulated over a fixed window size (e.g., 1K tokens) before taking a gradient step. 
However, this causes the model to act like a bigram model *within* the batch. To solve this, Mini-Batch TTT is paired with Sliding-Window Attention. The sliding window covers the local intra-batch context, ensuring the model remembers immediate local context before the MLP weights are updated at the end of the batch.

## References
- [End-to-End Test-Time Training for Long Context](../../raw/ttt-long-context.md)
