#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Run the Learning Path summary/FAQ generator locally against the Arm OpenAI proxy.

Usage:
  tools/test_summary_faq_ai_local.sh [options]

Options:
  --path PATH        Learning Path directory or _index.md file to test.
                     Default: content/learning-paths/servers-and-cloud-computing/nginx_tune
  --category SLUG    Top-level Learning Path category slug to process.
                     Example: servers-and-cloud-computing
  --model MODEL      OpenAI model/deployment name exposed by the proxy.
                     Default: gpt-4.1-mini
  --base-url URL     OpenAI-compatible Responses endpoint URL.
                     Default: https://openai-api-proxy.geo.arm.com/api/providers/openai/v1/responses/
  --ca-bundle FILE   Optional CA bundle file for Python TLS verification.
  --insecure         Skip TLS certificate verification for local testing only.
  --log-file FILE    Text file that captures progress, errors, and summary output.
                     Default: reports/generated-summary-faq/local-run.txt
  --report-file FILE YAML report file for this run.
                     Default: reports/generated-summary-faq/local-test.yml
  --write            Write generated content back to the selected _index.md file.
                     Default: dry-run
  --template         Use deterministic template fallback instead of the AI proxy.
  --help             Show this help text.

Required for AI mode:
  export OPENAI_API_KEY="..."

Examples:
  OPENAI_API_KEY="..." tools/test_summary_faq_ai_local.sh
  tools/test_summary_faq_ai_local.sh --path content/learning-paths/servers-and-cloud-computing/nginx_tune --write
  tools/test_summary_faq_ai_local.sh --template
EOF
}

PATH_FILTER="content/learning-paths/servers-and-cloud-computing/nginx_tune"
CATEGORY_FILTER=""
OPENAI_MODEL_VALUE="${OPENAI_MODEL:-gpt-4.1-mini}"
OPENAI_BASE_URL_VALUE="${OPENAI_BASE_URL:-https://openai-api-proxy.geo.arm.com/api/providers/openai/v1/responses/}"
OPENAI_CA_BUNDLE_VALUE="${OPENAI_CA_BUNDLE:-${SSL_CERT_FILE:-}}"
LOG_FILE_VALUE="reports/generated-summary-faq/local-run.txt"
REPORT_FILE_VALUE="reports/generated-summary-faq/local-test.yml"
MODE="--dry-run"
GENERATION_MODE="ai"
TLS_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --path)
      PATH_FILTER="${2:-}"
      shift 2
      ;;
    --category)
      CATEGORY_FILTER="${2:-}"
      PATH_FILTER=""
      shift 2
      ;;
    --model)
      OPENAI_MODEL_VALUE="${2:-}"
      shift 2
      ;;
    --base-url)
      OPENAI_BASE_URL_VALUE="${2:-}"
      shift 2
      ;;
    --ca-bundle)
      OPENAI_CA_BUNDLE_VALUE="${2:-}"
      shift 2
      ;;
    --insecure)
      TLS_ARGS+=(--openai-insecure-skip-verify)
      shift
      ;;
    --log-file)
      LOG_FILE_VALUE="${2:-}"
      shift 2
      ;;
    --report-file)
      REPORT_FILE_VALUE="${2:-}"
      shift 2
      ;;
    --write)
      MODE="--write"
      shift
      ;;
    --template)
      GENERATION_MODE="template"
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$PATH_FILTER" && -z "$CATEGORY_FILTER" ]]; then
  echo "--path cannot be empty." >&2
  exit 2
fi

if [[ "$GENERATION_MODE" == "ai" && -z "${OPENAI_API_KEY:-}" ]]; then
  echo "OPENAI_API_KEY is required for AI mode." >&2
  echo "Run: export OPENAI_API_KEY=\"...\"" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

echo "Summary/FAQ local test"
echo "  generation_mode: $GENERATION_MODE"
if [[ -n "$CATEGORY_FILTER" ]]; then
  echo "  category: $CATEGORY_FILTER"
else
  echo "  path: $PATH_FILTER"
fi
echo "  mode: ${MODE#--}"
echo "  log_file: $LOG_FILE_VALUE"
echo "  report_file: $REPORT_FILE_VALUE"
if [[ "$GENERATION_MODE" == "ai" ]]; then
  echo "  openai_base_url: $OPENAI_BASE_URL_VALUE"
  echo "  openai_model: $OPENAI_MODEL_VALUE"
  if [[ -n "$OPENAI_CA_BUNDLE_VALUE" ]]; then
    echo "  openai_ca_bundle: $OPENAI_CA_BUNDLE_VALUE"
  fi
  if [[ ${#TLS_ARGS[@]} -gt 0 || "${OPENAI_INSECURE_SKIP_VERIFY:-}" == "true" ]]; then
    echo "  openai_tls_verify: disabled"
  fi
fi
echo

CMD=(
  python3 tools/generate_summary_faq.py
  --generation-mode "$GENERATION_MODE" \
  --openai-base-url "$OPENAI_BASE_URL_VALUE" \
  --openai-model "$OPENAI_MODEL_VALUE" \
  --openai-ca-bundle "$OPENAI_CA_BUNDLE_VALUE" \
  --path-filter "$PATH_FILTER" \
  --category "$CATEGORY_FILTER" \
  --report-file "$REPORT_FILE_VALUE" \
  --log-file "$LOG_FILE_VALUE" \
  "$MODE"
)

if [[ ${#TLS_ARGS[@]} -gt 0 ]]; then
  CMD+=("${TLS_ARGS[@]}")
fi

"${CMD[@]}"
