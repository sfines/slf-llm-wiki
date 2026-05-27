# LLM JSON Processor Middleware

The JSON Processor is a post-tool middleware designed to handle voluminous, deeply nested JSON API responses without overwhelming an agent's context window. 

## The Token Efficiency Problem

Passing raw, massive JSON payloads directly into an LLM's context competes with the task prompt for attention, degrading reasoning accuracy and drastically increasing token costs. 

## The Code Generation Solution

Instead of treating the LLM as a reader of the JSON, the JSON Processor treats the LLM as a programmer. The process involves:
1.  Prompting the LLM to write a short, deterministic Python script to navigate the JSON structure.
2.  Applying filtering or aggregation logic within the script.
3.  Executing the script to extract only the specific answer needed.

When augmented with the API's JSON response schema, the model can reason about field names, data types, and nesting relationships. This output of the executed script is far smaller and slots cleanly into the next stage of the agent loop, eliminating formatting noise and verbosity.

---
[Source](../../raw/altk-paper.md)