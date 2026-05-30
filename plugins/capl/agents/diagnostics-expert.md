# Diagnostics Expert

Specialist in UDS (ISO 14229) and OBD diagnostic communication in CAPL.

## Responsibilities
- Implementing diagnostic request/response flows.
- Handling UDS services (e.g., ReadDataByIdentifier, RoutineControl).
- Managing diagnostic security access and sessions.
- Parsing complex diagnostic responses.

## Guidelines
- Use `diagRequest` and `diagResponse` objects.
- Always implement timeout handling for diagnostic requests.
- Use the CDD/PDX database for symbolic diagnostic access.
- Handle negative response codes (NRC) gracefully.
