# Economic Belief Quantification

Economic Belief Quantification is the methodological translation of an agent's qualitative economic outlook into a concrete, numerical value that can be directly applied to algorithmic decision-making.

## Mechanism of Action
While LLMs are highly capable of generating rich, text-based reflections on the state of an economy, utilizing raw text for every micro-decision is computationally heavy and difficult to track across a massive simulation. Frameworks like EconAI resolve this by distilling the LLM's reflection into an index (e.g., the Economic Sentiment Index). 

## Impact on Simulation
This quantified belief acts as a mathematical modifier on the agent's base probability to act. If the quantified belief is negative, it algorithmically reduces the agent's consumption-to-income ratio and boosts labor participation rates. If positive, it has the inverse effect. This provides a computationally inexpensive way to ensure that subjective confidence consistently and predictably influences simulated aggregate demand and labor supply.

## See Also
- [Economic Sentiment Indexing](economic-sentiment-indexing.md)
- [Agent Work-Consumption Dynamics](agent-work-consumption-dynamics.md)
- [Raw Source: EconAI Paper](../../raw/econai-paper.md)