# Data-Dependent Caching in LLMs

Data-dependent caching addresses the limitations of standard semantic caching when an LLM's response relies not only on the input prompt but also on external or dynamically retrieved data.

## The Problem
For a chatbot, two semantically similar queries generally yield the same response. However, for a data-intensive reasoning agent or a web navigation agent, the exact same intent (e.g., "delete the top comment") requires a different set of literal actions depending on the dynamic environmental context (e.g., screen size, coordinate changes).

## The Solution
To cache effectively in data-dependent scenarios, agents must cache generalized plans or templates rather than final raw outputs. When a cache hit occurs, a smaller adaptation model is used to inject the current dynamic data into the generalized template to form the correct sequence of actions.

## References
- [Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents](../../raw/agentic-plan-caching.md)
