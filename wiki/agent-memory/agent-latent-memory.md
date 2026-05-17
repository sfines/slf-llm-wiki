# Latent Memory Research

**Latent Memory** is an emerging frontier in agent research where information is stored within the model's internal activations or hidden states rather than as tokens or weights.

## Core Concept
Unlike [Token-Level Memory](agent-token-level-memory.md), which uses external symbols, latent memory attempts to maintain state within the model's "mental space."

## Research Directions
- **Stateful Transformers:** Modifying transformer architectures to maintain a persistent internal state across tokens.
- **Recurrent Hidden States:** Using RNN-like mechanisms within LLMs to carry information over long horizons.
- **Dynamic State Management:** Developing methods for the model to explicitly read and write to its own latent space.

## Potential Benefits
- **Infinite Horizon:** Potentially overcoming the hard limits of context windows.
- **Higher Signal:** Storing information in a more compressed, semantically dense form than raw text.

## See Also
- [Agent Memory](agent-memory.md)
- [Token-Level Memory Realizations](agent-token-level-memory.md)
- [Memory Automation Frontiers](agent-memory-automation.md)
