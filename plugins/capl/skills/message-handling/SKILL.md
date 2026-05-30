# Message Handling Skill

Patterns for sending and receiving network messages.

## Key Patterns
- **Reception:** `on message MessageName { ... }`
- **Transmission:** `message MessageName msg; output(msg);`
- **Signal Access:** `msg.SignalName = value;`

## Example
```c
on message EngineData {
  if (this.EngineRPM > 5000) {
    write("RPM too high!");
  }
}
```
