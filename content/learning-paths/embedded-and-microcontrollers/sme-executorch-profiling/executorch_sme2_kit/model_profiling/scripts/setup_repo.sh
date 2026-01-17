#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"  # executorch_sme2_kit/model_profiling/scripts/ -> executorch_sme2_kit/
EXECUTORCH_DIR="${ROOT_DIR}/executorch"
VENV_DIR="${ROOT_DIR}/.venv"

echo "[sme2-profiling] Working directory: ${ROOT_DIR}"

on_err() {
  echo "❌ setup_repo.sh failed near: ${BASH_COMMAND}" >&2
  echo "   Tip: run 'bash -x scripts/setup_repo.sh' for a full trace." >&2
}
trap on_err ERR

if [[ -x "${ROOT_DIR}/model_profiling/scripts/check_prereqs.sh" ]]; then
  bash "${ROOT_DIR}/model_profiling/scripts/check_prereqs.sh"
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found. Install Python 3.9+ and retry." >&2
  exit 1
fi

python3 - <<'PY'
import sys
if sys.version_info < (3, 9):
    raise SystemExit("ERROR: Python 3.9+ required")
print("[sme2-profiling] Python OK:", sys.version.split()[0])
PY

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git not found. Install git and retry." >&2
  exit 1
fi

echo "[sme2-profiling] Creating venv: ${VENV_DIR}"
python3 -m venv "${VENV_DIR}"

echo "[sme2-profiling] Activating venv"
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

echo "[sme2-profiling] Ensuring pip tooling is available"
if ! python -m pip --version >/dev/null 2>&1; then
  echo "ERROR: pip is not available in the venv. Recreate the venv and retry." >&2
  exit 1
fi

# Use a repo-local pip cache to avoid permissions issues (and to reuse downloads).
export PIP_CACHE_DIR="${ROOT_DIR}/.pip-cache"
mkdir -p "${PIP_CACHE_DIR}"

# Optional escape hatch for corporate proxies / broken SSL trust stores.
# This is NOT recommended for normal environments.
if [[ "${SME2_PIP_INSECURE:-0}" == "1" ]]; then
  echo "⚠️  SME2_PIP_INSECURE=1 enabled: pip will trust hosts for PyPI. Use only if you understand the risk." >&2
  export PIP_CONFIG_FILE="${VENV_DIR}/pip.conf"
  cat > "${PIP_CONFIG_FILE}" <<'EOF'
[global]
trusted-host =
  pypi.org
  files.pythonhosted.org
EOF
fi

# Best-effort upgrade. If a user has corporate SSL/proxy issues, we still want them to proceed
# (venv already ships with a working pip/setuptools baseline).
if python -m pip install --upgrade pip wheel setuptools >/dev/null 2>&1; then
  echo "[sme2-profiling] pip tooling upgraded"
else
  echo "⚠️  Could not upgrade pip/wheel/setuptools (network/SSL/proxy issue). Continuing with existing versions." >&2
  echo "    If later installs fail, fix Python certificates/proxy settings and re-run this script." >&2
fi

if [[ ! -d "${EXECUTORCH_DIR}/.git" ]]; then
  echo "[sme2-profiling] Cloning ExecuTorch (tracks main): ${EXECUTORCH_DIR}"
  git clone https://github.com/pytorch/executorch.git "${EXECUTORCH_DIR}"
fi

echo "[sme2-profiling] Updating ExecuTorch to latest origin/main"
git -C "${EXECUTORCH_DIR}" fetch origin main --depth 1
git -C "${EXECUTORCH_DIR}" checkout -B main origin/main

echo "[sme2-profiling] Preflight: verify pip can download required wheels"
TORCH_REQ_LINE="$(grep -E '^torch==[0-9]+' "${EXECUTORCH_DIR}/requirements-dev.txt" 2>/dev/null | head -1 || true)"
TORCH_REQ="${TORCH_REQ_LINE:-torch}"
TORCH_EXTRA_INDEX="https://download.pytorch.org/whl/nightly/cpu"
TMP_DL_DIR="${ROOT_DIR}/.tmp_pip_downloads"
rm -rf "${TMP_DL_DIR}" && mkdir -p "${TMP_DL_DIR}"

echo "  - downloading: packaging==25.0 (PyPI)"
python -m pip download --no-deps -d "${TMP_DL_DIR}" packaging==25.0 >/dev/null

echo "  - downloading: ${TORCH_REQ} (PyTorch nightly index)"
python -m pip download --no-deps -d "${TMP_DL_DIR}" --extra-index-url "${TORCH_EXTRA_INDEX}" "${TORCH_REQ}" >/dev/null

rm -rf "${TMP_DL_DIR}"
echo "[sme2-profiling] Preflight OK: pip downloads working"

echo "[sme2-profiling] Installing ExecuTorch (editable)"
if (
  cd "${EXECUTORCH_DIR}"
  ./install_executorch.sh --editable
); then
  echo "[sme2-profiling] ExecuTorch install OK"
else
  echo "❌ ExecuTorch install failed." >&2
  echo "Common causes:" >&2
  echo "  - Corporate proxy / TLS certificates (e.g., 'OSStatus -26276' on macOS)" >&2
  echo "    Fix: ensure your Python trusts system certs, then re-run." >&2
  echo "    If you must (not recommended), re-run with SME2_PIP_INSECURE=1." >&2
  echo "  - Missing build tooling (rerun: bash scripts/check_prereqs.sh)" >&2
  exit 1
fi

echo "[sme2-profiling] Done."
echo "Next:"
echo "  - Build runners: bash model_profiling/scripts/build_runners.sh"
echo "  - Export model : source .venv/bin/activate && python model_profiling/export/export_model.py --model mobilenet_v3_small --dtype fp16 --outdir out_mobilenet/artifacts/"


