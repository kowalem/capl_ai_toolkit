---
name: system-variables
description: Patterns for interacting with CANoe system variables in CAPL. Use when managing simulation state or UI elements.
compatibility: [antigravityCLI, geminiCLI, claudeCLI, copilotCLI]
---

# System Variables Skill

Patterns for interacting with CANoe system variables.

## Iron Laws
- ALWAYS use `@sysvar` for global simulation state interaction.
- NEVER assume system variables are initialized; check values if necessary.
- USE `on sysvar` for reactive logic instead of polling.

## Key Patterns
- **Access:** `@Namespace::VariableName = 1;`
- **Change Event:** `on sysvar Namespace::VariableName { ... }`

## Example
```c
on sysvar Engine::StartButton {
  if (@this == 1) {
    setTimer(t_EngineRun, 10);
  }
}
```
