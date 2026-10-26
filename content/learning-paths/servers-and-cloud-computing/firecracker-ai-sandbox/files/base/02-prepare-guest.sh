#!/usr/bin/env bash
# Download an Arm64 Firecracker CI kernel/rootfs, create a writable ext4 guest,
# and provision SSH + simple static guest networking.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00-common.sh
source "$SCRIPT_DIR/00-common.sh"

require_root
require_arm64
ensure_dirs

for cmd in curl unsquashfs mkfs.ext4 mount umount chroot ssh-keygen e2fsck; do
    have "$cmd" || { echo "ERROR: missing required tool: $cmd. Run 01-setup-host.sh first." >&2; exit 1; }
done

S3="https://s3.amazonaws.com/spec.ccfc.min"
ARCH="$(uname -m)"

latest_ci_prefix() {
    if [[ -n "${FC_CI_PREFIX:-}" ]]; then
        printf '%s\n' "${FC_CI_PREFIX#/}"
        return
    fi
    curl -fsSL "${S3}?list-type=2&prefix=firecracker-ci/&delimiter=/" \
      | grep -oE 'firecracker-ci/[0-9]{8}-[^<]+/' \
      | sort -u \
      | tail -n 1 \
      | sed 's:/$::'
}

PREFIX="$(latest_ci_prefix)"
if [[ -z "$PREFIX" ]]; then
    echo "ERROR: unable to resolve Firecracker CI artifact prefix." >&2
    exit 1
fi
KERNEL_URL="${FC_KERNEL_URL:-$S3/$PREFIX/$ARCH/vmlinux-$FC_KERNEL_VERSION}"
ROOTFS_URL="${FC_ROOTFS_URL:-$S3/$PREFIX/$ARCH/ubuntu-$FC_ROOTFS_RELEASE.squashfs}"

echo "Using Firecracker CI artifacts: $PREFIX"

if [[ ! -f "$FC_KERNEL" ]]; then
    echo "[1/4] Downloading Arm64 guest kernel ${FC_KERNEL_VERSION}..."
    curl -fL "$KERNEL_URL" -o "$FC_KERNEL"
else
    echo "[1/4] Kernel already present: $FC_KERNEL"
fi

if [[ ! -f "$FC_SQUASHFS" ]]; then
    echo "[2/4] Downloading Ubuntu ${FC_ROOTFS_RELEASE} guest rootfs..."
    curl -fL "$ROOTFS_URL" -o "$FC_SQUASHFS"
else
    echo "[2/4] SquashFS already present: $FC_SQUASHFS"
fi

if [[ ! -f "$FC_ROOTFS" || "${FC_REBUILD_ROOTFS:-0}" == "1" ]]; then
    echo "[3/4] Building writable ext4 rootfs (${FC_ROOTFS_SIZE})..."
    rm -f "$FC_ROOTFS" "$FC_ARTIFACT_DIR"/.guest-provisioned-*
    WORK="$(mktemp -d)"
    trap 'rm -rf "$WORK"' EXIT
    unsquashfs -f -d "$WORK/root" "$FC_SQUASHFS" >/dev/null
    chown -R root:root "$WORK/root"
    truncate -s "$FC_ROOTFS_SIZE" "$FC_ROOTFS"
    mkfs.ext4 -F -q -d "$WORK/root" "$FC_ROOTFS"
    rm -rf "$WORK"
    trap - EXIT
else
    echo "[3/4] Writable rootfs already present: $FC_ROOTFS"
fi

if [[ ! -f "$FC_SSH_KEY" ]]; then
    ssh-keygen -q -t ed25519 -N '' -f "$FC_SSH_KEY"
fi

PROVISION_MARKER="$FC_ARTIFACT_DIR/.guest-provisioned-v1"
if [[ ! -f "$PROVISION_MARKER" || "${FC_REPROVISION:-0}" == "1" ]]; then
    echo "[4/4] Provisioning SSH and guest networking..."
    MNT="$(mktemp -d)"
    cleanup_mounts() {
        umount "$MNT/proc" 2>/dev/null || true
        umount "$MNT/sys" 2>/dev/null || true
        umount "$MNT/dev" 2>/dev/null || true
        umount "$MNT" 2>/dev/null || true
        rmdir "$MNT" 2>/dev/null || true
    }
    trap cleanup_mounts EXIT

    mount -o loop,rw "$FC_ROOTFS" "$MNT"
    mkdir -p "$MNT/proc" "$MNT/sys" "$MNT/dev"
    mount --bind /proc "$MNT/proc"
    mount --bind /sys "$MNT/sys"
    mount --bind /dev "$MNT/dev"

    PUBKEY="$(cat "$FC_SSH_KEY.pub")"
    cat > "$MNT/tmp/fc-lp-provision.sh" <<PROVISION
#!/usr/bin/env bash
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
rm -f /etc/resolv.conf
echo 'nameserver 1.1.1.1' > /etc/resolv.conf
# Map localhost and the guest's own hostname so tools like sudo can resolve it.
GUEST_HOSTNAME="\$(cat /etc/hostname 2>/dev/null | tr -d '[:space:]')"
GUEST_HOSTNAME="\${GUEST_HOSTNAME:-ubuntu-fc-uvm}"
printf '127.0.0.1 localhost\n127.0.1.1 %s\n' "\$GUEST_HOSTNAME" > /etc/hosts
mkdir -p /tmp && chmod 1777 /tmp
mkdir -p /var/cache/apt/archives/partial /var/lib/apt/lists/partial
mkdir -p /var/log/apt
: > /var/log/dpkg.log
apt-get -o APT::Sandbox::User=root update
apt-get -o APT::Sandbox::User=root \
  -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold \
  install -y --no-install-recommends \
  openssh-server iproute2 ca-certificates procps sudo
rm -rf /var/lib/apt/lists/*
mkdir -p /root/.ssh
chmod 700 /root/.ssh
cat > /root/.ssh/authorized_keys <<'KEY'
$PUBKEY
KEY
chmod 600 /root/.ssh/authorized_keys

# EC2-like default user: ensure 'ubuntu' owns its home, can SSH in, and has passwordless sudo.
# The Firecracker CI Ubuntu image ships /home/ubuntu owned by root, which locks the user out.
if id -u ubuntu >/dev/null 2>&1; then
  UBUNTU_HOME="\$(getent passwd ubuntu | cut -d: -f6)"
  UBUNTU_HOME="\${UBUNTU_HOME:-/home/ubuntu}"
  mkdir -p "\$UBUNTU_HOME/.ssh"
  chmod 700 "\$UBUNTU_HOME/.ssh"
  cat > "\$UBUNTU_HOME/.ssh/authorized_keys" <<'KEY'
$PUBKEY
KEY
  chmod 600 "\$UBUNTU_HOME/.ssh/authorized_keys"
  chown -R ubuntu:ubuntu "\$UBUNTU_HOME"
  # Passwordless sudo, like an EC2 default user.
  mkdir -p /etc/sudoers.d
  echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/90-ubuntu
  chmod 440 /etc/sudoers.d/90-ubuntu
fi
ssh-keygen -A
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin prohibit-password/' /etc/ssh/sshd_config
systemctl enable ssh.service 2>/dev/null || true
cat > /usr/local/sbin/fc-lp-network.sh <<'NET'
#!/usr/bin/env bash
set -e
TARGET_MAC='${FC_GUEST_MAC,,}'
for p in /sys/class/net/*; do
  dev="\$(basename "\$p")"
  [[ "\$dev" == lo ]] && continue
  mac="\$(cat "\$p/address" 2>/dev/null || true)"
  if [[ "\$mac" == "\$TARGET_MAC" ]]; then
    ip addr flush dev "\$dev" || true
    ip addr add ${FC_GUEST_IP}/${FC_NET_PREFIX} dev "\$dev"
    ip link set "\$dev" up
    ip route replace default via ${FC_HOST_IP} dev "\$dev"
    exit 0
  fi
done
echo 'Firecracker network interface not found' >&2
exit 1
NET
chmod 0755 /usr/local/sbin/fc-lp-network.sh
cat > /etc/systemd/system/fc-lp-network.service <<'UNIT'
[Unit]
Description=Configure Firecracker Learning Path network
DefaultDependencies=no
After=local-fs.target
Before=ssh.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/local/sbin/fc-lp-network.sh

[Install]
WantedBy=multi-user.target
UNIT
mkdir -p /etc/systemd/system/multi-user.target.wants
ln -sf ../fc-lp-network.service /etc/systemd/system/multi-user.target.wants/fc-lp-network.service
echo '/dev/vda / ext4 defaults 0 1' > /etc/fstab
rm -f /tmp/fc-lp-provision.sh
PROVISION
    chmod +x "$MNT/tmp/fc-lp-provision.sh"
    chroot "$MNT" /bin/bash /tmp/fc-lp-provision.sh

    cleanup_mounts
    trap - EXIT
    e2fsck -fp "$FC_ROOTFS" || [[ $? -le 1 ]]
    touch "$PROVISION_MARKER"
else
    echo "[4/4] Guest already provisioned. Set FC_REPROVISION=1 to repeat."
fi

echo
printf 'Guest preparation complete.\n'
