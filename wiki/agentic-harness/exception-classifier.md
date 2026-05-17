# Exception Classifier

The Exception Classifier is the frontline diagnostic module within the SHIELDA framework. Its primary role is to intercept runtime errors, analyze their context, and map them to a standardized, structured taxonomy.

## Classification Mechanism

When an agentic workflow throws an error, the classifier ingests the error message, the active artifact, and the execution logs. It identifies three key pieces of metadata:
- **Exception Type**: Classifying the error into one of the 36 known semantic failure modes (e.g., `Tool.InvocationException` or `ProtocolMismatchException`).
- **Agent Workflow Phase**: Determining whether the error manifested in the Reasoning/Planning phase or the Execution phase.
- **Affected Artifact**: Pinpointing the specific component at fault, such as the Goal, Memory, External System, or Interface.

## Handoff to the Registry

By translating raw runtime traces into structured, semantic categories, the Exception Classifier enables the framework to consult the Handling Pattern Registry. This ensures the system retrieves the most contextually appropriate recovery pattern rather than relying on generic, unoptimized fallback logic.

## See Also
- [Agentic Exception Taxonomy](./agentic-exception-taxonomy.md)
- [Handling Pattern Registry](./handling-pattern-registry.md)
- [SHIELDA Framework](./shielda-framework.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)