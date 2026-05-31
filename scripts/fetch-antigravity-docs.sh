#!/bin/bash
# Fetch latest Antigravity CLI documentation.
# Output: .antigravity/docs-cache/*.md

set -euo pipefail

CACHE_DIR=".antigravity/docs-cache"
mkdir -p "$CACHE_DIR"

BASE="https://antigravity.google/docs"
PAGES=(
  "cli-overview"
  "installation-and-auth"
  "cli-reference"
  "core-slash-commands"
  "default-keybindings"
)

echo "Fetching Antigravity CLI docs to $CACHE_DIR..."
for page in "${PAGES[@]}"; do
  url="$BASE/$page"
  out="$CACHE_DIR/${page}.md"
  echo "  -> $url"
  if command -v curl &>/dev/null; then
    curl -sL "$url" -o "$out" || echo "  (failed $page, skipping)"
  else
    echo "  curl not available — skipping"
    exit 0
  fi
done

echo "Done."
