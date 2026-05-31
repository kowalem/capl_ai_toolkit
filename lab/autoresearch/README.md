# CAPL Autoresearch

Automated self-improvement loop for CAPL AI Skills.

## Goal
To iteratively improve the instructions in `plugins/capl/skills/` by ensuring they strictly adhere to the **CAPL Iron Laws** defined in `CLAUDE.md`.

## How it Works
1. **Target Identification:** Selects a skill and identifies its weakest dimension (Accuracy, Safety, Completeness, etc.) using the `lab/eval` framework.
2. **Iron Law Alignment:** Maps the weakness to a specific CAPL Iron Law (e.g., Event-Driven Purity, Memory Stability).
3. **Mutation:** Generates a targeted improvement to the `SKILL.md` content.
4. **Validation:**
   - Runs `lab/eval/scorer.py` to check for score improvement.
   - Runs `npm run lint` to ensure formatting remains valid.
5. **Persistence:** Commits the change if it is a verified improvement, otherwise reverts.

## CAPL Specific Mutation Strategies
- **Loop-to-Timer Conversion:** Ensuring skills never suggest `while(1)` for delays.
- **Static Init Guard:** Forcing instructions to mention that local variables are static and must be initialized.
- **Symbolic-First:** Stripping raw byte manipulation examples in favor of database-driven signal access.
- **Diagnostic Timeouts:** Mandatory addition of timeout logic to any diagnostic request examples.
