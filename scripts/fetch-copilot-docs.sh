#!/bin/bash
# Fetch latest GitHub Copilot CLI documentation.
# Output: .copilot/docs-cache/*.md

set -euo pipefail

CACHE_DIR=".copilot/docs-cache"
mkdir -p "$CACHE_DIR"

BASE="https://docs.github.com/en/copilot/github-copilot-in-the-cli"
PAGES=(
  "installing-github-copilot-in-the-cli"
  "using-github-copilot-in-the-cli"
)

# Additional related docs
EXTRA_BASE="https://docs.github.com/en/copilot"
EXTRA_PAGES=(
  "customizing-copilot/adding-custom-instructions-for-github-copilot"
  "managing-copilot/managing-github-copilot-in-the-cli"
)

echo "Fetching GitHub Copilot CLI docs to $CACHE_DIR..."
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

for page_path in "${EXTRA_PAGES[@]}"; do
  page=$(basename "$page_path")
  url="$EXTRA_BASE/$page_path"
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
