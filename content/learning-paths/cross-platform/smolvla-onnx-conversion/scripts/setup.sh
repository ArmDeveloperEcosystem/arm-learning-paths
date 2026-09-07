#!/usr/bin/env bash
set -euo pipefail

if (( $# != 0 )); then
  echo "Usage: setup.sh" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LP_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WORK_ROOT="${SMOLVLA_LP_WORK_ROOT:-$LP_ROOT/work}"
PYTHON_BIN="${SMOLVLA_LP_PYTHON:-python3}"
LEROBOT_ROOT="$WORK_ROOT/lerobot"
VENV_ROOT="$WORK_ROOT/venv"
ARTIFACT_ROOT="$WORK_ROOT/artifacts"

LEROBOT_REVISION="30da8e687a6dfc617fcd94afc367ac7071c376ce"
MODEL_REPO="HuggingFaceVLA/smolvla_libero"
MODEL_REVISION="6721902bc4d61e50a3bfdb11dfb4cb626f05d102"
BASE_MODEL_REPO="HuggingFaceTB/SmolVLM2-500M-Instruct"
BASE_MODEL_REVISION="7b375e1b73b11138ff12fe22c8f2822d8fe03467"

if ! "$PYTHON_BIN" -c 'import sys; raise SystemExit(sys.version_info[:2] != (3, 12))'; then
  echo "Python 3.12 is required." >&2
  exit 1
fi

mkdir -p "$ARTIFACT_ROOT" "$WORK_ROOT/cache/huggingface" \
  "$WORK_ROOT/cache/pip" "$WORK_ROOT/tmp"

export HF_HOME="${HF_HOME:-$WORK_ROOT/cache/huggingface}"
export PIP_CACHE_DIR="${PIP_CACHE_DIR:-$WORK_ROOT/cache/pip}"
export TMPDIR="${TMPDIR:-$WORK_ROOT/tmp}"

if [[ ! -d "$LEROBOT_ROOT/.git" ]]; then
  git clone https://github.com/huggingface/lerobot.git "$LEROBOT_ROOT"
fi
git -C "$LEROBOT_ROOT" fetch origin "$LEROBOT_REVISION"
git -C "$LEROBOT_ROOT" checkout --detach "$LEROBOT_REVISION"
if [[ -n "$(git -C "$LEROBOT_ROOT" status --porcelain)" ]]; then
  echo "LeRobot worktree has local changes: $LEROBOT_ROOT" >&2
  exit 1
fi

if [[ ! -x "$VENV_ROOT/bin/python" ]]; then
  "$PYTHON_BIN" -m venv "$VENV_ROOT"
fi
if ! "$VENV_ROOT/bin/python" -c 'import sys; raise SystemExit(sys.version_info[:2] != (3, 12))'; then
  echo "Python 3.12 is required in the virtual environment: $VENV_ROOT" >&2
  exit 1
fi

"$VENV_ROOT/bin/python" -m pip install --upgrade \
  pip wheel 'setuptools>=71.0.0,<81.0.0'
"$VENV_ROOT/bin/python" -m pip install \
  --index-url https://download.pytorch.org/whl/cpu \
  'torch==2.11.0+cpu' 'torchvision==0.26.0+cpu'
"$VENV_ROOT/bin/python" -m pip install \
  'torchao==0.18.0' 'transformers==5.5.4' \
  'onnx==1.22.0' 'onnxruntime==1.29.0' \
  'matplotlib>=3.10.3,<4.0.0'
"$VENV_ROOT/bin/python" -m pip install -e "$LEROBOT_ROOT[smolvla]"

"$VENV_ROOT/bin/hf" download "$MODEL_REPO" \
  --revision "$MODEL_REVISION" \
  --exclude 'onnx/**' \
  --local-dir "$ARTIFACT_ROOT/smolvla_libero"
"$VENV_ROOT/bin/hf" download "$BASE_MODEL_REPO" \
  --revision "$BASE_MODEL_REVISION" \
  --exclude 'onnx/**' \
  --local-dir "$ARTIFACT_ROOT/smolvlm_base"

"$VENV_ROOT/bin/python" -m pip list --format=freeze > "$WORK_ROOT/environment.freeze.txt"
"$VENV_ROOT/bin/python" - "$WORK_ROOT/revisions.json" <<'PY'
import json
from pathlib import Path
import sys

payload = {
    "lerobot": "30da8e687a6dfc617fcd94afc367ac7071c376ce",
    "model_repo": "HuggingFaceVLA/smolvla_libero",
    "model_revision": "6721902bc4d61e50a3bfdb11dfb4cb626f05d102",
    "base_model_repo": "HuggingFaceTB/SmolVLM2-500M-Instruct",
    "base_model_revision": "7b375e1b73b11138ff12fe22c8f2822d8fe03467",
}
Path(sys.argv[1]).write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

echo "Environment: $VENV_ROOT"
echo "Model:       $ARTIFACT_ROOT/smolvla_libero"
