---
name: lab:autoresearch
description: >
  Self-improving loop for CAPL AI skills. Orchestrates a Cycle of 
  Evaluate -> Identify Weakness -> Mutate -> Re-evaluate -> Commit/Revert.
  Targets Iron Law compliance and evaluation scores.
compatibility: [geminiCLI]
---

# CAPL Autoresearch Skill

Iteratively improve CAPL skills using the autoresearch pattern.

## Workflow
1. **Selection:** Identifies the skill with the lowest evaluation score.
2. **Diagnosis:** Pinpoints the weakest dimension (e.g., Safety, Accuracy).
3. **Instructional Mutation:** 
   - Uses an LLM to rewrite specific sections of the `SKILL.md`.
   - Focuses on enforcing **CAPL Iron Laws** (CLAUDE.md).
4. **Verification:**
   - Runs `lab/eval/scorer.py` to ensure the composite score has increased.
   - Runs `npm run lint` to prevent formatting regressions.
5. **Finalization:** Keeps the change via git if it's a net positive; otherwise, reverts to the previous state.

## Usage
```bash
# Run on the weakest skill
python3 lab/autoresearch/manager.py

# Target a specific skill
python3 lab/autoresearch/manager.py --skill message-handling

# Just see current stats
python3 lab/autoresearch/manager.py --stats
```

## Iron Laws for Mutation
- **Preserve Structure:** Never remove required frontmatter or header levels.
- **Strict Adherence:** Any code examples must strictly follow CLAUDE.md (no blocking loops, symbolic access).
- **Incrementalism:** Change one thing at a time to isolate improvements.
