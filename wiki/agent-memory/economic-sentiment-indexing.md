# Economic Sentiment Indexing (ESI)

The Economic Sentiment Index (ESI) is a mechanism utilized within the EconAI framework to quantify the subjective economic beliefs and emotional states of simulated agents. It acknowledges that human decision-making is not purely objective or data-dependent, but heavily influenced by emotions like over-optimism during booms or extreme pessimism during recessions.

## Quantifying Emotional Influence
Rather than weighting all historical memory equally, the ESI acts as a dynamic modifier that represents an agent's confidence in the economic outlook. The ESI value is actively tracked, updated each quarter, and stored in the agent's memory module.

## Behavioral Adjustments
The stored ESI directly modulates agent behavior by acting as a confidence multiplier on the final generated decisions:
- **Low Belief (ESI < 0)**: When pessimistic about the economy, agents will preemptively reduce consumption and increase their willingness to work to build financial security.
- **High Belief (ESI > 0)**: Conversely, during periods of economic optimism, agents increase their consumption propensity and may reduce their immediate willingness to work.

By translating LLM reflection into a quantifiable metric, ESI both reduces computational overhead and ensures that agents react realistically to market cycles without suffering from extreme, unbuffered volatility.

## See Also
- [Economic Belief Quantification](economic-belief-quantification.md)
- [Agent Memory Weighting](agent-memory-weighting.md)
- [Agent Work-Consumption Dynamics](agent-work-consumption-dynamics.md)
- [Raw Source: EconAI Paper](../../raw/econai-paper.md)