#!/bin/bash
# Fetch latest GitHub Copilot CLI changelog.
# Output: .copilot/changelog-cache.md

set -euo pipefail

CACHE_DIR=".copilot"
mkdir -p "$CACHE_DIR"
OUT="$CACHE_DIR/changelog-cache.md"

URL="https://raw.githubusercontent.com/github/copilot-cli/main/CHANGELOG.md"

echo "Fetching GitHub Copilot CLI changelog to $OUT..."
if command -v curl &>/dev/null; then
  curl -sL "$URL" -o "$OUT" && echo "Saved $(wc -l < "$OUT") lines."
else
  echo "curl not available — cannot fetch"
  exit 1
fi
