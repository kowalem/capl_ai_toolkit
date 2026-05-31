---
name: test-assertions
description: Patterns for structured testing and reporting in CAPL. Use when creating automated test modules for validation.
compatibility: [antigravityCLI, geminiCLI, claudeCLI, copilotCLI]
---

# Test Assertions Skill

Patterns for structured testing and reporting.

## Iron Laws
- EVERY test case must conclude with an explicit pass/fail verdict.
- USE `testStep()` to document important milestones in reports.
- NEVER leave a test case without a final verdict.

## Key Patterns
- **Test Case:** `testcase MyTestCase() { ... }`
- **Pass:** `testStepPass("Label", "Description");`
- **Fail:** `testStepFail("Label", "Description");`

## Example
```c
testcase tc_CheckSignal() {
  if (getSignal(EngineSpeed) > 0) {
    testStepPass("SignalCheck", "Engine speed is active");
  } else {
    testStepFail("SignalCheck", "Engine speed is zero");
  }
}
```
