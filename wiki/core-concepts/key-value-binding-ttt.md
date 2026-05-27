# Key-Value Binding in Test-Time Training (TTT-KVB)

Key-Value Binding (KVB) is an early formulation of Test-Time Training where the model explicitly trains a sequence modeling layer to replace self-attention.

## Process
Instead of caching keys and values (as in standard self-attention), TTT-KVB learns to predict each value from its key implicitly during test time. This layer-wise reconstruction loss trains a linear or non-linear model inside the transformer block. 
Recent advancements, such as TTT-E2E, simplify this by replacing the layer-wise KVB reconstruction loss with a single standard next-token prediction loss at the end of the entire network. This transitions the focus from architectural internal state tracking to holistic continual learning.

## References
- [End-to-End Test-Time Training for Long Context](../../raw/ttt-long-context.md)
