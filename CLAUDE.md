# CAPL AI Toolkit - Iron Laws

This guide defines the non-negotiable standards for CAPL (Communication Access Programming Language) development within the CAPL AI Toolkit.

## 1. Event-Driven Purity
- **No Blocking Loops:** Never use `while(1)`, `do-while`, or long-running `for` loops inside event procedures (e.g., `on message`, `on timer`, `on start`).
- **Use Timers:** All cyclic or delayed actions must be handled via `msTimer` or `timer` objects.
- **Run-to-Completion:** Event procedures must be short and return control to the CANoe/CANalyzer kernel immediately.

## 2. Memory & Stability
- **No Pointers:** CAPL does not support pointers. Never attempt to simulate pointer behavior through risky memory offsets.
- **Static Locals:** Be aware that local variables in CAPL are **static by default**. They retain their values between calls. Always initialize them explicitly if you need fresh state.
- **Array Bounds:** Always check array bounds before access to prevent simulation crashes.

## 3. Network & Database Integration
- **Symbolic Access:** Always use database-defined symbols for messages and signals (e.g., `msg.EngineRPM = 3000;`) instead of raw byte manipulation (e.g., `msg.byte(0) = 0xFF;`).
- **Output Responsibility:** Only use `output()` for sending messages on the bus. Ensure messages are fully populated before calling `output()`.
- **System Variables:** Use `@sysvar` for global simulation state and user interface interaction.

## 4. Diagnostics (UDS/OBD)
- **Request/Response Pattern:** Use `diagRequest` objects for sending requests and `on diagResponse` for handling asynchronous responses.
- **Timeout Management:** Always implement a timeout mechanism when waiting for diagnostic responses.

## 5. Automated Testing
- **Test Modules:** Use `testcase` and `testfunction` for structured testing.
- **Explicit Verdicts:** Every test case must conclude with an explicit pass/fail verdict using `testStepPass()` or `testStepFail()`.
- **Reporting:** Use `testStep()` to document important milestones in the CANoe test report.

## 6. Project Structure
- **Modularization:** Use `.cin` (CAPL Include) files to share common functions, variables, and event handlers across multiple `.can` files.
- **Naming Conventions:** Use PascalCase for event procedures and camelCase for local variables. Prefix timers with `t_` and messages with `msg_`.
