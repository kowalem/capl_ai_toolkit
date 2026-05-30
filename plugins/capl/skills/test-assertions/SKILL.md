# Test Assertions Skill

Patterns for structured testing and reporting.

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
