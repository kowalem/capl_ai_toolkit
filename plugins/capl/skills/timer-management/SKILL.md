---
name: timer-management
description: Patterns for cyclic and delayed actions using timers in CAPL. Use when implementing time-dependent logic or polling.
compatibility: [antigravityCLI, geminiCLI, claudeCLI, copilotCLI]
---

# Timer Management Skill

Patterns for cyclic and delayed actions using timers.

## Iron Laws
- NO blocking loops for delays; use `msTimer` or `timer` objects.
- ALWAYS return control to the kernel immediately from timer event procedures.
- ENSURE cyclic timers are re-set at the end of the handler.

## Key Patterns
- **Declaration:** `msTimer t_Cyclic;`
- **Starting:** `setTimer(t_Cyclic, 100);`
- **Handling:** `on timer t_Cyclic { ... setTimer(this, 100); }`

## Example
```c
on timer t_SendStatus {
  message StatusMsg msg;
  output(msg);
  setTimer(this, 500); // 500ms cyclic
}
```
