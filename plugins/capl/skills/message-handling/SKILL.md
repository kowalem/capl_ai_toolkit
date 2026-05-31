---
name: message-handling
description: Patterns for sending and receiving network messages in CAPL. Use when interacting with CAN bus nodes to exchange data.
compatibility: [antigravityCLI, geminiCLI, claudeCLI, copilotCLI]
---

# Message Handling Skill

Patterns for sending and receiving network messages.

## Iron Laws
- NEVER use raw byte offsets for message access; use database symbols.
- ALWAYS call `output()` only after the message is fully populated.
- NO blocking loops in message event handlers.

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
