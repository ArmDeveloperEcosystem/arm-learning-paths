#!/usr/bin/env bash
set -euo pipefail

# scripts/check_prereqs.sh
# Fail fast with clear messages before long builds / pipelines.
#
# Usage:
#   bash scripts/check_prereqs.sh
#   bash scripts/check_prereqs.sh --android-run   # also checks adb presence

fail() {
  echo "❌ $*" >&2
  exit 1
}

ok() { echo "✅ $*"; }
warn() { echo "⚠️  $*"; }

need_cmd() {
  local c="$1"
  local help="$2"
  command -v "${c}" >/dev/null 2>&1 || fail "Missing '${c}'. ${help}"
  ok "Found ${c}"
}

ver_ge() {
  # ver_ge <have> <need>  (both x.y.z)
  local have="$1"
  local need="$2"
  python3 - <<PY
import sys
def parse(v): return tuple(int(x) for x in v.split("."))
have=parse("${have}")
need=parse("${need}")
sys.exit(0 if have>=need else 1)
PY
}

ANDROID_RUN=0
if [[ "${1:-}" == "--android-run" ]]; then
  ANDROID_RUN=1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "[sme2-profiling] Prerequisites check: ${ROOT_DIR}"

need_cmd python3 "Install Python 3.9+."
need_cmd git "Install git."
need_cmd cmake "Install CMake (3.29+ recommended)."
need_cmd ninja "Install ninja (macOS: 'brew install ninja')."

python_ver="$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"
ver_ge "${python_ver}" "3.9.0" || fail "Python ${python_ver} found, but Python 3.9+ is required."
ok "Python version: ${python_ver}"

cmake_ver="$(cmake --version | head -1 | awk '{print $3}')"
ver_ge "${cmake_ver}" "3.29.0" || warn "CMake ${cmake_ver} found; recommended 3.29+ for best compatibility."
ok "CMake version: ${cmake_ver}"

if command -v clang >/dev/null 2>&1; then
  ok "Found clang"
else
  warn "clang not found. On macOS install Xcode command line tools: xcode-select --install"
fi

if [[ "$(uname -s)" == "Darwin" ]]; then
  if command -v xcode-select >/dev/null 2>&1; then
    if xcode_path="$(xcode-select -p 2>/dev/null)"; then
      ok "Xcode CLT path: ${xcode_path}"
    else
      fail "Xcode Command Line Tools missing. Run: xcode-select --install"
    fi
  fi
fi

if [[ "${ANDROID_RUN}" == "1" ]]; then
  need_cmd adb "Install Android platform-tools (adb)."
fi

if [[ -n "${ANDROID_NDK:-}" || -n "${ANDROID_NDK_HOME:-}" ]]; then
  ndk="${ANDROID_NDK:-${ANDROID_NDK_HOME}}"
  [[ -f "${ndk}/build/cmake/android.toolchain.cmake" ]] || fail "ANDROID_NDK set but toolchain not found under: ${ndk}"
  ok "ANDROID_NDK OK: ${ndk}"
else
  warn "ANDROID_NDK not set (Android optional). Android runner builds will be skipped."
fi

echo "[sme2-profiling] Prerequisites OK"
