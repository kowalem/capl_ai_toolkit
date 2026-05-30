#!/bin/bash
# Basic verifier for CAPL Iron Laws
FILE_PATH="$1"
if grep -qE "while\(1\)|while \(1\)" "$FILE_PATH"; then
  echo "Violation: Blocking loop (while(1)) found in $FILE_PATH. Use timers instead."
  exit 1
fi
exit 0
