# Execution-Phase Exceptions

Execution-Phase Exceptions represent operational breakdowns that occur when an LLM agent attempts to enact its plan by interacting with external tools, APIs, interfaces, or other agents.

## Tool and API Exceptions
Interacting with software boundaries is a primary source of execution failure:
- **Invocation Exceptions**: The agent formats a request incorrectly, hallucinates a tool, or provides semantically mismatched arguments.
- **Output and Response Malformations**: The tool succeeds, but returns data that is structurally broken, semantically incorrect, or missing required fields.
- **Unavailable Tools and Protocol Mismatches**: External APIs timeout, undergo unannounced schema evolution, or enforce strict privilege policies that the agent violates.

## UI and Environmental Failures
Agents operating visual or web-based interfaces face unique spatial challenges:
- **UI Element Misclicks**: The agent incorrectly targets a neighboring or visually similar button due to bounding-box or coordinate misalignment.
- **Text Recognition Errors**: OCR fails to parse the screen correctly due to low contrast or font scaling.
- **Environmental Noise and Not Ready States**: The agent acts during a loading screen or misinterprets layout shifts caused by resolution changes.

## Task Flow and Multi-Agent Friction
In complex execution pipelines, errors can propagate silently:
- **Error Propagation**: Early execution mistakes cascade downstream without being caught.
- **Agent Conflict and Role Violation**: Multiple agents interfere with each other, execute redundant actions, or step outside their designated responsibilities.
- **Communication Exceptions**: Agents fail to pass on necessary missing information or completely ignore peer messages.

## See Also
- [Agentic Exception Taxonomy](./agentic-exception-taxonomy.md)
- [Reasoning-Phase Exceptions](./reasoning-phase-exceptions.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)