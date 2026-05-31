#!/usr/bin/env python3
"""CAPL Autoresearch Manager

Identifies skills needing improvement and orchestrates the mutation loop.
"""

import os
import sys
import json
import argparse
import subprocess
from typing import List, Dict, Optional

# Add the root of the project to sys.path so we can import from lab.eval
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from lab.eval.scorer import score_skill, find_all_skills, find_eval
from lab.eval.schemas import EvalDefinition, SkillScore

class AutoresearchManager:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.plugin_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "plugins", "capl"))

    def get_skill_stats(self) -> List[Dict]:
        """Get scores for all skills and identify the weakest dimensions."""
        skills = find_all_skills()
        stats = []
        
        for skill_path in skills:
            skill_name = os.path.basename(os.path.dirname(skill_path))
            eval_path = find_eval(skill_name)
            eval_def = EvalDefinition.from_file(eval_path) if eval_path else None
            
            score = score_skill(skill_path, eval_def)
            
            # Find the weakest dimension (excluding those with score 1.0)
            weakest_dim = None
            lowest_score = 1.1
            
            for dim_name, dim_res in score.dimensions.items():
                if dim_res.score < lowest_score:
                    lowest_score = dim_res.score
                    weakest_dim = dim_name
            
            stats.append({
                "name": skill_name,
                "path": skill_path,
                "score": score.composite,
                "weakest_dimension": weakest_dim,
                "weakest_score": lowest_score
            })
            
        return sorted(stats, key=lambda x: x["score"])

    def run_iteration(self, target_skill: str = None):
        """Run a single improvement iteration."""
        stats = self.get_skill_stats()
        if not stats:
            print("No skills found.")
            return

        if target_skill:
            target = next((s for s in stats if s["name"] == target_skill), None)
            if not target:
                print(f"Target skill '{target_skill}' not found.")
                return
        else:
            target = stats[0] # Pick the weakest overall

        if target['score'] >= 1.0:
            print(f"All dimensions for {target['name']} are at 1.0. Nothing to do.")
            return

        print(f"Targeting skill: {target['name']}")
        print(f"Current score: {target['score']:.2f}")
        print(f"Weakest dimension: {target['weakest_dimension']} ({target['weakest_score']:.2f})")

        # In a real scenario, this would call an LLM. 
        # Here we apply a programmatic mutation if available, or just plan it.
        self.execute_mutation(target)

    def execute_mutation(self, target: Dict):
        """Perform the actual mutation and verify."""
        skill_path = target["path"]
        with open(skill_path, "r") as f:
            old_content = f.read()

        new_content = old_content
        
        # Apply CAPL-specific programmatic strategies
        if target['weakest_dimension'] == "safety":
            from lab.autoresearch.strategies import event_driven
            new_content = event_driven.apply(old_content)
        
        if new_content == old_content:
            print(f"No automated mutation applied for {target['weakest_dimension']}. Human/LLM intervention required.")
            print(f"Mutation Plan: Improve {target['weakest_dimension']} for {target['name']}.")
            return

        # Write and verify
        if not self.dry_run:
            with open(skill_path, "w") as f:
                f.write(new_content)
            
            # Re-score
            new_score = score_skill(skill_path)
            if new_score.composite > target['score']:
                print(f"Improvement verified! {target['score']:.2f} -> {new_score.composite:.2f}")
                self.commit_change(skill_path, target['name'])
            else:
                print("Mutation did not improve score. Reverting.")
                with open(skill_path, "w") as f:
                    f.write(old_content)
        else:
            print("[DRY RUN] Would have applied mutation and checked score.")

    def commit_change(self, skill_path: str, skill_name: str):
        """Commit the improvement via git."""
        try:
            subprocess.run(["git", "add", skill_path], check=True)
            msg = f"chore(lab): autoresearch improve {skill_name}"
            subprocess.run(["git", "commit", "-m", msg], check=True)
            print(f"Committed: {msg}")
        except subprocess.CalledProcessError as e:
            print(f"Git error: {e}")

def main():
    parser = argparse.ArgumentParser(description="CAPL Autoresearch Manager")
    parser.add_argument("--skill", help="Target a specific skill")
    parser.add_argument("--stats", action="store_true", help="Just show stats")
    parser.add_argument("--dry-run", action="store_true", help="Don't commit changes")
    args = parser.parse_args()

    manager = AutoresearchManager(dry_run=args.dry_run)
    
    if args.stats:
        stats = manager.get_skill_stats()
        print(json.dumps(stats, indent=2))
    else:
        manager.run_iteration(target_skill=args.skill)

if __name__ == "__main__":
    main()
