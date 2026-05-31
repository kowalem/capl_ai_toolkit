"""CAPL Mutation Strategy: Event-Driven Purity

Enforces the 'No Blocking Loops' Iron Law.
"""

import re

def apply(content: str) -> str:
    """Check for blocking loop patterns and replace with timer suggestions."""
    # Find patterns like 'while(1)' or 'while (true)' in code blocks
    blocking_patterns = [
        r'while\s*\(\s*1\s*\)',
        r'while\s*\(\s*true\s*\)',
        r'for\s*\(\s*;\s*;\s*\)'
    ]
    
    modified = content
    for pattern in blocking_patterns:
        if re.search(pattern, modified):
            # Instead of a complex regex replacement, we add a specific warning 
            # to the Iron Laws section if it's missing the explicit blocking loop ban.
            if "No blocking loops" not in modified:
                iron_laws_match = re.search(r'## Iron Laws\n', modified)
                if iron_laws_match:
                    insert_pos = iron_laws_match.end()
                    modified = modified[:insert_pos] + "- NEVER use blocking loops (while(1)); use msTimer instead.\n" + modified[insert_pos:]
    
    return modified
