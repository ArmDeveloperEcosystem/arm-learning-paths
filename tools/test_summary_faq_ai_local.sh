#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "tools/test_summary_faq_ai_local.sh is deprecated." >&2
echo "Use tools/generate-summary-faq instead." >&2
echo >&2

exec "$SCRIPT_DIR/generate-summary-faq" "$@"
