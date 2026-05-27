# Silent Error Review

Silent Error Review is a post-tool middleware component that detects "soft failures" in API and tool responses. 

## The Soft Failure Problem

A common scenario in agentic tool usage is an API returning a successful HTTP status code (e.g., "200 OK") while the actual body of the response contains an error message like "Service under maintenance" or "No results found." Traditional agents often blindly accept the 200 OK status, interpreting the error text as a valid final answer, which leads to unintended downstream behavior.

## Mitigation Strategy

The Silent Error Review component operates immediately after a tool is called. It uses a prompt-based approach to analyze:
*   The original user query
*   The raw tool response
*   The tool specification (optional)

Based on this context, it categorizes the response as "ACCOMPLISHED," "PARTIALLY ACCOMPLISHED," or "NOT ACCOMPLISHED." If a silent error is detected, the agent is alerted, allowing it to retry or switch strategies instead of proceeding with flawed data.

---
[Source](../../raw/altk-paper.md)