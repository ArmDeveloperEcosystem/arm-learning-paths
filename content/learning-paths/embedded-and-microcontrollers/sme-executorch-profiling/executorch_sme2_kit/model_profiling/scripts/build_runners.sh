#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
EXECUTORCH_DIR="${ROOT_DIR}/executorch"

on_err() {
  echo "ERROR: build_runners.sh failed at: ${BASH_COMMAND}" >&2
  echo "Run with 'bash -x' for detailed trace." >&2
}
trap on_err ERR

# Check prerequisites
if [[ -f "${ROOT_DIR}/model_profiling/scripts/check_prereqs.sh" ]]; then
  bash "${ROOT_DIR}/model_profiling/scripts/check_prereqs.sh"
fi

# Activate venv if available
if [[ -f "${ROOT_DIR}/.venv/bin/activate" ]]; then
  source "${ROOT_DIR}/.venv/bin/activate"
fi

# Validate environment
if [[ ! -d "${EXECUTORCH_DIR}" ]]; then
  echo "ERROR: executorch/ directory not found. Run setup_repo.sh first." >&2
  exit 1
fi

if ! command -v cmake >/dev/null 2>&1; then
  echo "ERROR: cmake not found. Install CMake and retry." >&2
  exit 1
fi

if ! command -v ninja >/dev/null 2>&1; then
  echo "ERROR: ninja not found. Install ninja and retry." >&2
  exit 1
fi

# Merge CMake presets
echo "Merging CMake presets..."
python3 "${ROOT_DIR}/model_profiling/scripts/merge_cmake_presets.py"

# Build Mac runners (runners stay in executorch/cmake-out/ for version tracking)
echo "Building mac-arm64 runner (SME2 ON)..."
cd "${EXECUTORCH_DIR}"
cmake --preset mac-arm64
cmake --build --preset build-mac-arm64 --target executor_runner

echo "Building mac-arm64-sme2-off runner (SME2 OFF)..."
cmake --preset mac-arm64-sme2-off
cmake --build --preset build-mac-arm64-sme2-off --target executor_runner

echo "Mac runners built:"
echo "  ${EXECUTORCH_DIR}/cmake-out/mac-arm64/executor_runner"
echo "  ${EXECUTORCH_DIR}/cmake-out/mac-arm64-sme2-off/executor_runner"

# Build Android runners (optional)
if [[ -z "${ANDROID_NDK:-}" && -z "${ANDROID_NDK_HOME:-}" ]]; then
  echo ""
  echo "Android runners skipped (ANDROID_NDK not set)"
  exit 0
fi

ANDROID_NDK="${ANDROID_NDK:-${ANDROID_NDK_HOME}}"
TOOLCHAIN="${ANDROID_NDK}/build/cmake/android.toolchain.cmake"
if [[ ! -f "${TOOLCHAIN}" ]]; then
  echo "ERROR: Android toolchain not found: ${TOOLCHAIN}" >&2
  exit 1
fi

export ANDROID_NDK

echo "Building android-arm64-v9a runner (SME2 ON)..."
cmake --preset android-arm64-v9a
cmake --build --preset build-android-arm64-v9a --target executor_runner

echo "Building android-arm64-v9a-sme2-off runner (SME2 OFF)..."
cmake --preset android-arm64-v9a-sme2-off
cmake --build --preset build-android-arm64-v9a-sme2-off --target executor_runner

# Copy libc++_shared.so if available (for Android device deployment)
PREBUILT_ROOT="${ANDROID_NDK}/toolchains/llvm/prebuilt"
HOST_PREBUILT="$(ls -d "${PREBUILT_ROOT}/"* 2>/dev/null | head -1 || true)"
if [[ -n "${HOST_PREBUILT}" ]]; then
  LIBCXX_SHARED="${HOST_PREBUILT}/sysroot/usr/lib/aarch64-linux-android/libc++_shared.so"
  if [[ -f "${LIBCXX_SHARED}" ]]; then
    cp -f "${LIBCXX_SHARED}" "${EXECUTORCH_DIR}/cmake-out/android-arm64-v9a/libc++_shared.so"
    cp -f "${LIBCXX_SHARED}" "${EXECUTORCH_DIR}/cmake-out/android-arm64-v9a-sme2-off/libc++_shared.so"
  fi
fi

echo "Android runners built:"
echo "  ${EXECUTORCH_DIR}/cmake-out/android-arm64-v9a/executor_runner"
echo "  ${EXECUTORCH_DIR}/cmake-out/android-arm64-v9a-sme2-off/executor_runner"
