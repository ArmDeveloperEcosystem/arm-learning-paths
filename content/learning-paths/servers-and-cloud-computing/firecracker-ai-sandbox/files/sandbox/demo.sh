#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
    echo "ERROR: run with sudo: sudo $0" >&2
    exit 1
fi

echo "=== 1. Native Arm execution ==="
"$SCRIPT_DIR/run-job.sh" "$SCRIPT_DIR/examples/hello-arm.sh"

echo
echo "=== 2. Disposable filesystem, first execution ==="
"$SCRIPT_DIR/run-job.sh" "$SCRIPT_DIR/examples/write-marker.sh"

echo
echo "=== 3. Disposable filesystem, second execution ==="
"$SCRIPT_DIR/run-job.sh" "$SCRIPT_DIR/examples/write-marker.sh"

echo
echo "Demo complete. Both marker jobs began with a clean filesystem."

