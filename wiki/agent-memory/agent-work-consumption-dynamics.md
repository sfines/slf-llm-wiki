# Agent Work-Consumption Dynamics

Agent Work-Consumption Dynamics form the core decision-making loop for individual household agents within economic simulations. This dynamic dictates how an agent allocates its time and resources.

## The Two Core Choices
At any given decision interval, the agent must evaluate two primary probabilities:
1. **Willingness to Work**: Determines the agent's participation in the labor market.
2. **Consumption Propensity**: Determines the proportion of the agent's income that will be allocated to immediate spending versus savings.

## Environmental Variables
The LLM driving the agent makes these decisions by weighing several real-world economic inputs:
- **Individual Income & Savings**: Current wealth and financial security.
- **Market Prices**: The prevailing cost of essential goods.
- **Unemployment Rate**: Affecting job availability and perceived job security.
- **Interest Rates**: Influencing the attractiveness of saving money versus borrowing and spending.

By passing these environmental variables into the agent's cognitive module, the resulting work and consumption behaviors organically shift to align with established economic theories.

## See Also
- [Household vs Firm Agent Roles](household-vs-firm-agent-roles.md)
- [Long-Term Strategic Economic Planning](long-term-strategic-economic-planning.md)
- [Raw Source: EconAI Paper](../../raw/econai-paper.md)