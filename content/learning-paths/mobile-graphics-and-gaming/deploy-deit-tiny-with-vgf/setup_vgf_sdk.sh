#!/usr/bin/env bash
# SDK setup for this Learning Path, using the pinned ExecuTorch release helpers.
set -euo pipefail

if [[ "$(uname -s)" != Linux || -z "${VIRTUAL_ENV:-}" ]]; then
    echo "Run this script on Linux with the Learning Path virtual environment active." >&2
    exit 1
fi

repo_dir="$(pwd)"
if [[ "${repo_dir}" =~ [[:space:]] ]]; then
    echo "Use a checkout path without spaces for the upstream SDK helpers." >&2
    exit 1
fi
if [[ "$(git rev-parse HEAD)" != 3b60683923245cf472b7323426920e15623ba361 ||
      ! -f "${repo_dir}/backends/arm/scripts/vulkan_utils.sh" ]]; then
    echo "Run this script from the ExecuTorch v1.5.1 repository root." >&2
    exit 1
fi

OS="$(uname -s)"
ARCH="$(uname -m)"
root_dir="${repo_dir}/arm_test/deit_vgf/sdk"
setup_path_script="${root_dir}/setup_path"
mkdir -p "${root_dir}"

source "${repo_dir}/backends/arm/scripts/vulkan_utils.sh"
setup_vulkan_sdk
clear_setup_path
setup_path_vulkan
source "${repo_dir}/backends/arm/scripts/mlsdk_utils.sh"
pkg_dir="$(find_emulation_layer_pkg_dir)"
if [[ -z "${pkg_dir}" ]] || ! apply_emulation_layer_deploy_dir "${pkg_dir}/deploy"; then
    echo "Install the Learning Path's released VGF Python packages first." >&2
    exit 1
fi
printf 'SDK environment ready. Run: source %s.sh\n' "${setup_path_script}"
