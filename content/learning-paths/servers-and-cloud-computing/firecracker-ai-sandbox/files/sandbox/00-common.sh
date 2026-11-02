#!/usr/bin/env bash
set -euo pipefail

AI_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Reuse the kernel, root filesystem, and SSH key produced by ../02-prepare-guest.sh.
FC_BASE_DIR="${FC_BASE_DIR:-/opt/firecracker-lp}"
FC_KERNEL="${FC_KERNEL:-$FC_BASE_DIR/artifacts/vmlinux}"
FC_BASE_ROOTFS="${FC_BASE_ROOTFS:-$FC_BASE_DIR/artifacts/rootfs.ext4}"
FC_SSH_KEY="${FC_SSH_KEY:-$FC_BASE_DIR/artifacts/id_rsa}"

FC_AI_DIR="${FC_AI_DIR:-/opt/firecracker-ai}"
FC_RUNTIME_ROOT="${FC_RUNTIME_ROOT:-$FC_AI_DIR/runtime}"
FC_RESULTS_DIR="${FC_RESULTS_DIR:-$FC_AI_DIR/results}"

# This first example runs one job at a time and uses the static guest network
# already provisioned by ../02-prepare-guest.sh.
FC_TAP="${FC_TAP:-fc-ai0}"
FC_HOST_IP="${FC_HOST_IP:-172.16.0.1}"
FC_GUEST_IP="${FC_GUEST_IP:-172.16.0.2}"
FC_NET_PREFIX="${FC_NET_PREFIX:-30}"
FC_GUEST_MAC="${FC_GUEST_MAC:-06:00:AC:10:00:02}"

FC_VCPUS="${FC_VCPUS:-1}"
FC_MEM_MIB="${FC_MEM_MIB:-512}"
FC_BOOT_TIMEOUT="${FC_BOOT_TIMEOUT:-45}"
FC_JOB_TIMEOUT="${FC_JOB_TIMEOUT:-15}"

fail() {
    echo "ERROR: $*" >&2
    exit 1
}

require_root() {
    [[ ${EUID:-$(id -u)} -eq 0 ]] || fail "run this script with sudo/root"
}

require_arm64() {
    [[ "$(uname -m)" == "aarch64" ]] || fail "this example requires an Arm64/aarch64 host"
}

require_command() {
    command -v "$1" >/dev/null 2>&1 || fail "missing required command: $1"
}

