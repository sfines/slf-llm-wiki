# Long-Context Continual Learning

Addressing long context windows via continual learning treats the intake of sequence tokens as an ongoing learning task, diverging from the traditional sliding-window or full-attention caching architectures.

## Concept
Humans do not recall every exact detail of their past to reason about the present; rather, they compress experience into intuition. Long-Context Continual Learning applies this to Language Models by updating the model's weights sequentially (Test-Time Training) as it ingests context. The model "learns" the context through backpropagation on the prompt, embedding the sequence information into its multi-layer perceptrons (MLPs), circumventing the quadratic scaling costs of full attention.

## References
- [End-to-End Test-Time Training for Long Context](../../raw/ttt-long-context.md)
