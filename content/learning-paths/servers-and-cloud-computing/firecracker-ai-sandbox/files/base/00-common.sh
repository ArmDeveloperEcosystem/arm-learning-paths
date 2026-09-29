#!/usr/bin/env bash
# Shared settings for the Firecracker-on-Arm Learning Path scripts.
set -euo pipefail

FC_LP_DIR="${FC_LP_DIR:-/opt/firecracker-lp}"
FC_ARTIFACT_DIR="${FC_ARTIFACT_DIR:-$FC_LP_DIR/artifacts}"
FC_RUNTIME_DIR="${FC_RUNTIME_DIR:-$FC_LP_DIR/runtime}"

FC_VERSION="${FC_VERSION:-1.15.1}"
FC_KERNEL_VERSION="${FC_KERNEL_VERSION:-6.1.186}"
FC_ROOTFS_RELEASE="${FC_ROOTFS_RELEASE:-24.04}"
FC_ROOTFS_SIZE="${FC_ROOTFS_SIZE:-5G}"

FC_KERNEL="$FC_ARTIFACT_DIR/vmlinux"
FC_ROOTFS="$FC_ARTIFACT_DIR/rootfs.ext4"
FC_SSH_KEY="$FC_ARTIFACT_DIR/id_rsa"
FC_SQUASHFS="$FC_ARTIFACT_DIR/ubuntu-${FC_ROOTFS_RELEASE}.squashfs"

FC_TAP="${FC_TAP:-fc-tap0}"
FC_HOST_IP="${FC_HOST_IP:-172.16.0.1}"
FC_GUEST_IP="${FC_GUEST_IP:-172.16.0.2}"
FC_NET_PREFIX="${FC_NET_PREFIX:-30}"
FC_GUEST_MAC="${FC_GUEST_MAC:-06:00:AC:10:00:02}"

FC_VCPUS="${FC_VCPUS:-2}"
FC_MEM_MIB="${FC_MEM_MIB:-2048}"

FC_API_SOCK="$FC_RUNTIME_DIR/firecracker.socket"
FC_CONFIG="$FC_RUNTIME_DIR/vm-config.json"
FC_PID_FILE="$FC_RUNTIME_DIR/firecracker.pid"
FC_SERIAL_LOG="$FC_RUNTIME_DIR/serial.log"
FC_NET_STATE="$FC_RUNTIME_DIR/network.state"

require_root() {
    if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
        echo "ERROR: run this script with sudo/root." >&2
        exit 1
    fi
}

require_arm64() {
    local arch
    arch="$(uname -m)"
    if [[ "$arch" != "aarch64" ]]; then
        echo "ERROR: this Learning Path package targets Arm64/aarch64; detected: $arch" >&2
        exit 1
    fi
}

ensure_dirs() {
    mkdir -p "$FC_ARTIFACT_DIR" "$FC_RUNTIME_DIR"
}

have() { command -v "$1" >/dev/null 2>&1; }

wait_for_file() {
    local path="$1" timeout_s="${2:-10}" i
    for ((i=0; i<timeout_s*10; i++)); do
        [[ -e "$path" ]] && return 0
        sleep 0.1
    done
    return 1
}
