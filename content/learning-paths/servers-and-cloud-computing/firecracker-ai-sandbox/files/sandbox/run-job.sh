#!/usr/bin/env bash
# Run one shell program in a fresh, disposable Firecracker microVM.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00-common.sh
source "$SCRIPT_DIR/00-common.sh"

usage() {
    cat <<'USAGE'
Usage: sudo ./run-job.sh PATH_TO_SCRIPT

The script is copied into a fresh microVM, executed as the unprivileged
ubuntu user, and discarded with the microVM's writable root filesystem.
USAGE
}

[[ $# -eq 1 ]] || { usage >&2; exit 2; }
JOB_SOURCE="$1"
[[ -f "$JOB_SOURCE" && -r "$JOB_SOURCE" ]] || fail "job is not a readable file: $JOB_SOURCE"

require_root
require_arm64
for cmd in firecracker ip iptables ssh scp timeout cp flock sha256sum; do
    require_command "$cmd"
done
[[ -e /dev/kvm ]] || fail "/dev/kvm is not available"
[[ -f "$FC_KERNEL" ]] || fail "kernel not found at $FC_KERNEL; run ../02-prepare-guest.sh"
[[ -f "$FC_BASE_ROOTFS" ]] || fail "base rootfs not found at $FC_BASE_ROOTFS; run ../02-prepare-guest.sh"
[[ -f "$FC_SSH_KEY" ]] || fail "SSH key not found at $FC_SSH_KEY; run ../02-prepare-guest.sh"
[[ "$FC_VCPUS" =~ ^[1-9][0-9]*$ ]] || fail "FC_VCPUS must be a positive integer"
[[ "$FC_MEM_MIB" =~ ^[1-9][0-9]*$ ]] || fail "FC_MEM_MIB must be a positive integer"
[[ "$FC_BOOT_TIMEOUT" =~ ^[1-9][0-9]*$ ]] || fail "FC_BOOT_TIMEOUT must be a positive integer"
[[ "$FC_JOB_TIMEOUT" =~ ^[1-9][0-9]*$ ]] || fail "FC_JOB_TIMEOUT must be a positive integer"

mkdir -p "$FC_RUNTIME_ROOT" "$FC_RESULTS_DIR"
chmod 0700 "$FC_RUNTIME_ROOT"

# The static /30 network permits one concurrent job. Refuse a second runner
# instead of letting two jobs accidentally share addressing or host state.
exec 9>"$FC_RUNTIME_ROOT/runner.lock"
flock -n 9 || fail "another sandbox job is already running"

JOB_ID="$(date -u +%Y%m%dT%H%M%SZ)-$$"
JOB_DIR="$FC_RUNTIME_ROOT/$JOB_ID"
RESULT_DIR="$FC_RESULTS_DIR/$JOB_ID"
ROOTFS="$JOB_DIR/rootfs.ext4"
API_SOCK="$JOB_DIR/firecracker.socket"
CONFIG="$JOB_DIR/vm-config.json"
SERIAL_LOG="$RESULT_DIR/serial.log"
STDOUT_FILE="$RESULT_DIR/stdout"
STDERR_FILE="$RESULT_DIR/stderr"
RESULT_FILE="$RESULT_DIR/result.env"
PID=""
TAP_CREATED=0
EGRESS_RULE_CREATED=0
HOST_INPUT_RULE_CREATED=0

mkdir -p "$JOB_DIR" "$RESULT_DIR"
chmod 0700 "$JOB_DIR" "$RESULT_DIR"

cleanup() {
    local cleanup_status=$?
    trap - EXIT INT TERM
    if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
        kill "$PID" 2>/dev/null || true
        for _ in $(seq 1 20); do
            kill -0 "$PID" 2>/dev/null || break
            sleep 0.1
        done
        kill -9 "$PID" 2>/dev/null || true
    fi
    if [[ "$EGRESS_RULE_CREATED" -eq 1 ]]; then
        iptables -D FORWARD -i "$FC_TAP" -j DROP 2>/dev/null || true
    fi
    if [[ "$HOST_INPUT_RULE_CREATED" -eq 1 ]]; then
        iptables -D INPUT -i "$FC_TAP" -m conntrack --ctstate NEW -j DROP 2>/dev/null || true
    fi
    if [[ "$TAP_CREATED" -eq 1 ]]; then
        ip link del "$FC_TAP" 2>/dev/null || true
    fi
    rm -rf -- "$JOB_DIR"
    exit "$cleanup_status"
}
trap cleanup EXIT INT TERM

ip link show "$FC_TAP" >/dev/null 2>&1 && fail "TAP device already exists: $FC_TAP"

echo "Job:       $JOB_ID"
echo "Resources: ${FC_VCPUS} vCPU, ${FC_MEM_MIB} MiB, ${FC_JOB_TIMEOUT}s timeout"
echo "Cloning a disposable root filesystem..."
cp --reflink=auto --sparse=always "$FC_BASE_ROOTFS" "$ROOTFS"

ip tuntap add dev "$FC_TAP" mode tap
TAP_CREATED=1
ip addr add "${FC_HOST_IP}/${FC_NET_PREFIX}" dev "$FC_TAP"
ip link set "$FC_TAP" up
# Insert at the front so a permissive host FORWARD rule cannot grant egress.
iptables -I FORWARD 1 -i "$FC_TAP" -j DROP
EGRESS_RULE_CREATED=1
# Permit replies to host-initiated SSH/SCP, but reject connections initiated
# by untrusted guest code toward services listening on the host.
iptables -I INPUT 1 -i "$FC_TAP" -m conntrack --ctstate NEW -j DROP
HOST_INPUT_RULE_CREATED=1

cat > "$CONFIG" <<JSON
{
  "boot-source": {
    "kernel_image_path": "$FC_KERNEL",
    "boot_args": "console=ttyS0 reboot=k panic=1 pci=off root=/dev/vda rw"
  },
  "drives": [{
    "drive_id": "rootfs",
    "path_on_host": "$ROOTFS",
    "is_root_device": true,
    "is_read_only": false
  }],
  "machine-config": {
    "vcpu_count": $FC_VCPUS,
    "mem_size_mib": $FC_MEM_MIB
  },
  "entropy": {},
  "network-interfaces": [{
    "iface_id": "eth0",
    "guest_mac": "$FC_GUEST_MAC",
    "host_dev_name": "$FC_TAP"
  }]
}
JSON

firecracker --api-sock "$API_SOCK" --config-file "$CONFIG" >"$SERIAL_LOG" 2>&1 &
PID=$!

SSH_OPTIONS=(
    -i "$FC_SSH_KEY"
    -o StrictHostKeyChecking=no
    -o UserKnownHostsFile=/dev/null
    -o ConnectTimeout=2
    -o LogLevel=ERROR
)

echo "Booting the microVM..."
READY=0
for _ in $(seq 1 "$FC_BOOT_TIMEOUT"); do
    if ssh "${SSH_OPTIONS[@]}" "ubuntu@$FC_GUEST_IP" true 2>/dev/null; then
        READY=1
        break
    fi
    kill -0 "$PID" 2>/dev/null || fail "Firecracker exited during boot; see $SERIAL_LOG"
    sleep 1
done
[[ "$READY" -eq 1 ]] || fail "guest SSH was not ready within ${FC_BOOT_TIMEOUT}s; see $SERIAL_LOG"

scp "${SSH_OPTIONS[@]}" "$JOB_SOURCE" "ubuntu@$FC_GUEST_IP:/tmp/ai-job.sh"

echo "Executing inside the microVM..."
START_NS="$(date +%s%N)"
set +e
timeout --signal=TERM --kill-after=2 "${FC_JOB_TIMEOUT}s" \
    ssh "${SSH_OPTIONS[@]}" "ubuntu@$FC_GUEST_IP" \
    'chmod 0700 /tmp/ai-job.sh && /bin/bash /tmp/ai-job.sh' \
    >"$STDOUT_FILE" 2>"$STDERR_FILE"
JOB_STATUS=$?
set -e
END_NS="$(date +%s%N)"
DURATION_MS=$(( (END_NS - START_NS) / 1000000 ))

if [[ "$JOB_STATUS" -eq 124 || "$JOB_STATUS" -eq 137 ]]; then
    OUTCOME="timed_out"
elif [[ "$JOB_STATUS" -eq 0 ]]; then
    OUTCOME="succeeded"
else
    OUTCOME="failed"
fi

SOURCE_SHA256="$(sha256sum "$JOB_SOURCE" | awk '{print $1}')"
cat > "$RESULT_FILE" <<RESULT
job_id=$JOB_ID
outcome=$OUTCOME
exit_code=$JOB_STATUS
duration_ms=$DURATION_MS
source_sha256=$SOURCE_SHA256
vcpus=$FC_VCPUS
memory_mib=$FC_MEM_MIB
timeout_seconds=$FC_JOB_TIMEOUT
RESULT

echo
echo "--- stdout ---"
cat "$STDOUT_FILE"
echo "--- stderr ---" >&2
cat "$STDERR_FILE" >&2
echo "--- result ---"
cat "$RESULT_FILE"
echo "Artifacts: $RESULT_DIR"
echo "The microVM and its writable disk are now being destroyed."

exit "$JOB_STATUS"
