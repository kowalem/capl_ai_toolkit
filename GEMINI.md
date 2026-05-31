# CAPL AI Toolkit - Gemini Context

This project is the **CAPL AI Toolkit**, a framework for developing, auditing, and evaluating AI agents and skills specialized in **CAPL (Communication Access Programming Language)** for CANoe/CANalyzer simulation environments.

## Project Overview

The toolkit consists of two primary pillars:
1.  **Plugin Content (`plugins/capl/`):**
    *   **Agents:** Markdown files in `agents/` defining specialized AI roles (e.g., `capl-reviewer`, `diagnostics-expert`).
    *   **Skills:** Directories in `skills/` containing `SKILL.md` files that provide detailed instructional context for specific CAPL tasks (e.g., `message-handling`, `timer-management`).
2.  **Laboratory Evaluation (`lab/eval/`):**
    *   A Python-based scoring framework that evaluates the quality, safety, and effectiveness of agents and skills across multiple dimensions (accuracy, completeness, conciseness, etc.).
    *   **Iron Laws:** Defined in `CLAUDE.md`, these are non-negotiable standards for CAPL development that agents must uphold and evaluations must enforce.

## Core Commands

The project uses `npm` for task management and `pytest` for testing the evaluation framework.

### Building and Running
*   `npm run lint`: Validates markdown files using `markdownlint`.
*   `npm run lint:fix`: Automatically fixes linting errors.

### Evaluation and Testing
*   `npm test`: Runs the Python unit tests for the evaluation framework (`pytest`).
*   `npm run eval`: Runs the evaluation pipeline on changed skills and agents.
*   `npm run eval:all`: Runs evaluation on all skills and agents.
*   `npm run eval:skills`: Runs evaluation on skills only.
*   `npm run eval:agents`: Runs evaluation on agents only.
*   `npm run eval:fix`: Identifies failing skills/agents and suggests fixes.
*   `npm run eval:triggers`: Runs expensive behavioral trigger tests (use sparingly).

## Development Conventions

### CAPL Iron Laws (Mandatory)
All AI-generated CAPL code must adhere to the rules in `CLAUDE.md`:
1.  **Event-Driven Purity:** No blocking loops (`while(1)`). Use `msTimer` for delays.
2.  **Memory & Stability:** No pointers. Locals are static by default; initialize them. Check array bounds.
3.  **Network Integration:** Use symbolic access (database signals) instead of raw bytes. Use `output()` for bus transmission.
4.  **Diagnostics:** Use `diagRequest` and `on diagResponse`. Implement timeouts.
5.  **Automated Testing:** Use `testcase`/`testfunction`. Explicit verdicts via `testStepPass`/`fail`.

### Skill and Agent Definition
*   **Skills (`SKILL.md`):** Should follow the established structure, including a frontmatter, a clear description, and an "Iron Laws" section.
*   **Agents:** Should be defined as senior-level experts with specific focus areas (Reviewer, Judge, Specialist).
*   **Modularization:** Use `.cin` files for shared logic.
*   **Naming:** PascalCase for event procedures, camelCase for local variables, `t_` prefix for timers, `msg_` for messages.

## Project Structure
*   `lab/eval/`: Scoring engine, dimension definitions (accuracy, behavioral, etc.), and tests.
*   `plugins/capl/agents/`: Specialized agent persona definitions.
*   `plugins/capl/skills/`: Domain-specific skill instructions.
*   `plugins/capl/hooks/`: Hooks and verifiers (e.g., `iron-law-verifier.sh`).
*   `CLAUDE.md`: The primary source of truth for CAPL coding standards.
