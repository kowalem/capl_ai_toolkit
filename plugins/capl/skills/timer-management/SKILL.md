# Timer Management Skill

Patterns for cyclic and delayed actions using timers.

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
