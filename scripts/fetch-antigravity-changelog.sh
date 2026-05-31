#!/bin/bash
# Fetch latest Antigravity CLI changelog.
# Output: .antigravity/changelog-cache.md

set -euo pipefail

CACHE_DIR=".antigravity"
mkdir -p "$CACHE_DIR"
OUT="$CACHE_DIR/changelog-cache.md"

URL="https://raw.githubusercontent.com/google-antigravity/antigravity-cli/main/CHANGELOG.md"

echo "Fetching Antigravity CLI changelog to $OUT..."
if command -v curl &>/dev/null; then
  curl -sL "$URL" -o "$OUT" && echo "Saved $(wc -l < "$OUT") lines."
else
  echo "curl not available — cannot fetch"
  exit 1
fi
