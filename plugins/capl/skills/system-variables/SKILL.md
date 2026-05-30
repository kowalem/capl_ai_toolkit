# System Variables Skill

Patterns for interacting with CANoe system variables.

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
