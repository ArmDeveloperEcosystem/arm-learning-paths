#!/usr/bin/env bash
# Install host-side prerequisites and Firecracker on Ubuntu 24.04 Arm64.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00-common.sh
source "$SCRIPT_DIR/00-common.sh"

require_root
require_arm64
ensure_dirs

if [[ ! -e /dev/kvm ]]; then
    echo "ERROR: /dev/kvm is not present. Firecracker requires KVM access." >&2
    echo "Use an Arm64 host with hardware virtualization exposed (bare metal is simplest)." >&2
    exit 1
fi

if [[ -r /etc/os-release ]]; then
    # shellcheck disable=SC1091
    source /etc/os-release
    if [[ "${ID:-}" != "ubuntu" ]]; then
        echo "WARNING: this package was prepared for Ubuntu 24.04; detected ${PRETTY_NAME:-unknown}." >&2
    elif [[ "${VERSION_ID:-}" != "24.04" ]]; then
        echo "WARNING: Ubuntu 24.04 is the reference host; detected ${PRETTY_NAME:-unknown}." >&2
    fi
fi

echo "[1/3] Installing host packages..."
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y --no-install-recommends \
    curl ca-certificates iproute2 iptables openssh-client \
    e2fsprogs squashfs-tools util-linux mount

echo "[2/3] Installing Firecracker v${FC_VERSION}..."
ARCH="$(uname -m)"
TARBALL="firecracker-v${FC_VERSION}-${ARCH}.tgz"
URL="https://github.com/firecracker-microvm/firecracker/releases/download/v${FC_VERSION}/${TARBALL}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
curl -fL "$URL" -o "$TMP/$TARBALL"
tar -xzf "$TMP/$TARBALL" -C "$TMP"
install -m 0755 \
    "$TMP/release-v${FC_VERSION}-${ARCH}/firecracker-v${FC_VERSION}-${ARCH}" \
    /usr/local/bin/firecracker
if [[ -f "$TMP/release-v${FC_VERSION}-${ARCH}/jailer-v${FC_VERSION}-${ARCH}" ]]; then
    install -m 0755 \
        "$TMP/release-v${FC_VERSION}-${ARCH}/jailer-v${FC_VERSION}-${ARCH}" \
        /usr/local/bin/jailer
fi

echo "[3/3] Verifying installation..."
firecracker --version
[[ -r /dev/kvm && -w /dev/kvm ]] || echo "NOTE: /dev/kvm exists but current permissions may require root."

echo
printf 'Host setup complete. Next: sudo %q\n' "$SCRIPT_DIR/02-prepare-guest.sh"
