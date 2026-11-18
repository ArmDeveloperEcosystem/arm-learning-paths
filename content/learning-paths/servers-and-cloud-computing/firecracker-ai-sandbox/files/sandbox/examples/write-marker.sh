#!/usr/bin/env bash
set -euo pipefail

MARKER=/tmp/ai-sandbox-marker
if [[ -e "$MARKER" ]]; then
    echo "Unexpected: marker survived from an earlier execution" >&2
    exit 1
fi

echo "created by job at $(date -u +%FT%TZ)" > "$MARKER"
echo "Created $MARKER inside this microVM."
echo "Run this example again: the marker will be absent because the disk is disposable."

