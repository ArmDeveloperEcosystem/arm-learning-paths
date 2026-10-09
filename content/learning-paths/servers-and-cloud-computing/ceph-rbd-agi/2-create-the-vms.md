---
title: Create three Arm64 virtual machines
description: Use KVM, libvirt, and cloud-init to create three networked Ubuntu 26.04 Arm64 virtual machines on one Arm AGI CPU host.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the VM environment

In this section, you will create three Ubuntu 26.04 Arm64 VMs with stable IP addresses, SSH access, and a separate data disk for Ceph. Run the commands on the physical AGI host. By the end, you will be able to connect to each VM and confirm that its initial setup has completed.

## Check the AGI host

This Learning Path uses KVM and libvirt to create the virtual machines. The commands in this section assume that the AGI CPU host runs Ubuntu 24.04 Arm64 and provides:

- At least 12 available CPU cores
- At least 12 GB of memory available to the VMs; 16 GB or more of total host memory is recommended
- At least 90 GB of available storage
- Hardware virtualization support through KVM
- Root or `sudo` access

The virtual disks use the QCOW2 format and grow as data is written, but the host must have enough capacity for the disks to reach their configured sizes.

Confirm that the host uses the Arm64 architecture:

```bash
uname -m
```

The command should print `aarch64`.

## Install the virtualization tools

Install KVM, libvirt, the Arm64 UEFI firmware, `virt-install`, and the cloud-image tools:

```bash
sudo apt update
sudo apt install -y \
  qemu-kvm \
  qemu-efi-aarch64 \
  libvirt-daemon-system \
  libvirt-clients \
  libvirt-daemon-config-network \
  virtinst \
  cloud-image-utils \
  curl
```

Start libvirt and configure it to start when the host boots:

```bash
sudo systemctl enable --now libvirtd
```

Check whether QEMU can use KVM on the host:

```bash
sudo virt-host-validate qemu
```

The expected output is:
```output
  QEMU: Checking if device /dev/kvm exists                                   : PASS
  QEMU: Checking if device /dev/kvm is accessible                            : PASS
  QEMU: Checking if device /dev/vhost-net exists                             : PASS
  QEMU: Checking if device /dev/net/tun exists                               : PASS
  QEMU: Checking for cgroup 'cpu' controller support                         : PASS
  QEMU: Checking for cgroup 'cpuacct' controller support                     : PASS
  QEMU: Checking for cgroup 'cpuset' controller support                      : PASS
  QEMU: Checking for cgroup 'memory' controller support                      : PASS
  QEMU: Checking for cgroup 'devices' controller support                     : PASS
  QEMU: Checking for cgroup 'blkio' controller support                       : PASS
  QEMU: Checking for device assignment IOMMU support                         : PASS
  QEMU: Checking if IOMMU is enabled by kernel                               : PASS
  QEMU: Checking for secure guest support                                    : WARN (Unknown if this platform has Secure Guest support)
```
Warnings for features that this example does not use, such as secure guests, can be ignored.

## Create the shared virtual network

Create a libvirt NAT network named `agi-net`. The network gives the VMs outbound access and lets them communicate with one another. It also assigns a fixed private address to each VM:

| Virtual machine | MAC address | IP address |
| --- | --- | --- |
| `ceph1` | `52:54:00:ce:00:01` | `192.168.100.11` |
| `ceph2` | `52:54:00:ce:00:02` | `192.168.100.12` |
| `ceph3` | `52:54:00:ce:00:03` | `192.168.100.13` |

If the AGI host already uses the `192.168.100.0/24` subnet, select an unused private subnet and update the addresses in this section.

Run this on the AGI host to check for an existing route:

```bash
ip -4 route show 192.168.100.0/24
```

If the command returns nothing, there is no matching route currently configured on the AGI host.

Create the network definition:

```bash
cat >/tmp/agi-net.xml <<'EOF'
<network>
  <name>agi-net</name>
  <forward mode="nat"/>
  <ip address="192.168.100.1" prefix="24">
    <dhcp>
      <range start="192.168.100.100" end="192.168.100.200"/>
      <host mac="52:54:00:ce:00:01" name="ceph1" ip="192.168.100.11"/>
      <host mac="52:54:00:ce:00:02" name="ceph2" ip="192.168.100.12"/>
      <host mac="52:54:00:ce:00:03" name="ceph3" ip="192.168.100.13"/>
    </dhcp>
  </ip>
</network>
EOF
```

Define, start, and enable the network:

```bash
sudo virsh net-define /tmp/agi-net.xml
sudo virsh net-start agi-net
sudo virsh net-autostart agi-net
```

The expected output is:
```output
Network agi-net defined from /tmp/agi-net.xml
Network agi-net started
Network agi-net marked as autostarted
```

Confirm that `agi-net` is active:

```bash
sudo virsh net-list
```
The expected output is:

```output
Name      State    Autostart   Persistent
--------------------------------------------
 agi-net   active   yes         yes
 default   active   yes         yes
```

## Create an SSH key for the VMs

Create a dedicated SSH key on the AGI host. The command preserves the key if it already exists:

```bash
if [ ! -f "${HOME}/.ssh/agi_ceph" ]; then
  ssh-keygen -t ed25519 -f "${HOME}/.ssh/agi_ceph" -N ""
fi
```

Cloud-init adds the public key to each VM. You will use the matching private key to connect as the `ubuntu` user.

No password is set for `ubuntu`, so use SSH key authentication rather than a password at the VM console.

## Download the Ubuntu Arm64 cloud image

Create a directory for the VM images and download the Ubuntu 26.04 Arm64 release cloud image:

```bash
VM_DIRECTORY=/var/lib/libvirt/images/agi-ceph
BASE_IMAGE="${VM_DIRECTORY}/ubuntu-26.04-arm64-base.img"

sudo mkdir -p "$VM_DIRECTORY"
sudo curl --fail --location \
  https://cloud-images.ubuntu.com/releases/resolute/release/ubuntu-26.04-server-cloudimg-arm64.img \
  --output "$BASE_IMAGE"
```

Do not download over an existing base image that backs VM disks. The release URL can change as Ubuntu publishes updates; the tested guest image reported Ubuntu 26.04.1 and kernel `7.0.0-34-generic`.

The base image remains unchanged. Each VM uses a separate copy-on-write operating-system disk backed by this image.

## Create and start the VMs

The following loop creates `ceph1`, `ceph2`, and `ceph3`. Each VM receives four virtual CPUs, 4 GB of memory, a 20 GB operating-system disk, a separate empty 10 GB data disk, and an interface on `agi-net`.

Use `--cpu host-passthrough` to expose the host CPU to the Arm64 KVM guests. The `host-model` CPU mode is not supported by the hypervisor used here.

Each VM also receives a persistent NoCloud seed ISO containing its hostname, SSH public key, and network configuration. The network configuration enables IPv4 DHCP on the interface matching the VM's MAC address. The DHCP reservation in `agi-net` supplies the fixed IP address.

Run the loop on the AGI host for the initial VM creation. It checks that the VM disk and seed files do not already exist before creating them.

```bash
(
set -e
VM_DIRECTORY=/var/lib/libvirt/images/agi-ceph
BASE_IMAGE="${VM_DIRECTORY}/ubuntu-26.04-arm64-base.img"
SSH_PUBLIC_KEY="$(cat "${HOME}/.ssh/agi_ceph.pub")"
SEED_DIRECTORY=$(mktemp -d)

for VM_NUMBER in 1 2 3; do
  VM_NAME="ceph${VM_NUMBER}"
  VM_MAC="52:54:00:ce:00:0${VM_NUMBER}"
  OS_DISK="${VM_DIRECTORY}/${VM_NAME}-os.qcow2"
  DATA_DISK="${VM_DIRECTORY}/${VM_NAME}-data.qcow2"
  USER_DATA="${SEED_DIRECTORY}/${VM_NAME}-user-data.yaml"
  META_DATA="${SEED_DIRECTORY}/${VM_NAME}-meta-data.yaml"
  NETWORK_CONFIG="${SEED_DIRECTORY}/${VM_NAME}-network-config.yaml"
  SEED_IMAGE="${VM_DIRECTORY}/${VM_NAME}-seed.iso"

  test ! -e "$OS_DISK"
  test ! -e "$DATA_DISK"
  test ! -e "$SEED_IMAGE"

  sudo qemu-img create \
    -f qcow2 \
    -F qcow2 \
    -b "$BASE_IMAGE" \
    "$OS_DISK" \
    20G

  sudo qemu-img create \
    -f qcow2 \
    "$DATA_DISK" \
    10G

  cat >"$USER_DATA" <<EOF
#cloud-config
hostname: ${VM_NAME}
manage_etc_hosts: true
ssh_pwauth: false
users:
  - name: ubuntu
    groups:
      - adm
      - sudo
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    lock_passwd: true
    ssh_authorized_keys:
      - ${SSH_PUBLIC_KEY}
EOF

  cat >"$META_DATA" <<EOF
instance-id: ${VM_NAME}
local-hostname: ${VM_NAME}
EOF

  cat >"$NETWORK_CONFIG" <<EOF
version: 2
ethernets:
  cephnic:
    match:
      macaddress: "${VM_MAC}"
    dhcp4: true
EOF

  sudo cloud-localds \
    --network-config="$NETWORK_CONFIG" \
    "$SEED_IMAGE" \
    "$USER_DATA" \
    "$META_DATA"

  sudo virt-install \
    --connect qemu:///system \
    --name "$VM_NAME" \
    --virt-type kvm \
    --arch aarch64 \
    --machine virt \
    --cpu host-passthrough \
    --vcpus 4 \
    --memory 4096 \
    --import \
    --osinfo generic \
    --boot uefi \
    --disk "path=${OS_DISK},format=qcow2,bus=virtio" \
    --disk "path=${DATA_DISK},format=qcow2,bus=virtio" \
    --disk "path=${SEED_IMAGE},device=cdrom,format=raw" \
    --network "network=agi-net,model=virtio,mac=${VM_MAC}" \
    --graphics none \
    --noautoconsole

  rm -f "$USER_DATA" "$META_DATA" "$NETWORK_CONFIG"
done
rmdir "$SEED_DIRECTORY"
)
```

The first boot can take a few minutes while cloud-init configures each VM. Keep the seed ISOs attached so they remain available on subsequent boots. The subshell stops the loop if a command fails.

## Verify access to the VMs

Confirm that all three VMs are running:

```bash
sudo virsh list --all
```

The expected output is similar to:
```output
 Id   Name    State
-----------------------
 1    ceph1   running
 2    ceph2   running
 3    ceph3   running
 ```

If a VM is listed as `shut off`, start that existing VM with `sudo vi
rsh start ceph1`, replacing `ceph1` with its name.

Check that libvirt assigned `192.168.100.11`, `192.168.100.12`, and `192.168.100.13` to the three VMs:

```bash
sudo virsh net-dhcp-leases agi-net
```
The expected output is similar to:
```output
Expiry Time           MAC address         Protocol   IP address          Hostname   Client ID or DUID
-----------------------------------------------------------------------------------------------------------------------------------------------
 2026-10-07 15:03:31   52:54:00:ce:00:01   ipv4       192.168.100.11/24   ceph1      ff:cb:39:0a:c7:00:02:00:00:ab:11:11:3d:ef:1d:a1:60:28:a1
 2026-10-07 15:05:06   52:54:00:ce:00:02   ipv4       192.168.100.12/24   ceph2      ff:cb:39:0a:c7:00:02:00:00:ab:11:fe:6b:dd:98:1d:91:16:4b
 2026-10-07 14:58:52   52:54:00:ce:00:03   ipv4       192.168.100.13/24   ceph3      ff:cb:39:0a:c7:00:02:00:00:ab:11:bb:14:a0:3e:17:e0:f4:e8
```

If the lease list is empty immediately after boot, wait a few minutes and check again. If a lease remains missing, run `sudo virsh domblklist ceph1 --details` for the affected VM and confirm that its seed ISO is attached to the CD-ROM. Use `sudo virsh console ceph1` to inspect boot and cloud-init messages; press **Ctrl+]** to leave the console.

After the leases appear, connect to each VM and display its hostname, architecture, and cloud-init status:

```bash
for VM_NUMBER in 1 2 3; do
  VM_IP="192.168.100.$((10 + VM_NUMBER))"
  echo "Checking ceph${VM_NUMBER} (${VM_IP})"
  ssh -o ConnectTimeout=10 \
    -o ConnectionAttempts=1 \
    -o ServerAliveInterval=10 \
    -o ServerAliveCountMax=2 \
    -i "${HOME}/.ssh/agi_ceph" "ubuntu@${VM_IP}" \
    'hostname; uname -m; cloud-init status --long'
done
```

Accept each SSH host key when prompted. Each connection should report the corresponding hostname, `ceph1`, `ceph2`, or `ceph3`, followed by `aarch64`. Before continuing, confirm that cloud-init reports `status: done` with no errors. Its datasource should be `DataSourceNoCloud` using the attached seed media. If SSH reports `Connection refused`, wait for cloud-init to finish and try again.

## What you've accomplished and what's next

You've created three Ubuntu 26.04 Arm64 virtual machines with fixed private addresses and separate empty data disks. Next, you'll validate their resources, networking, time synchronization, and storage before installing Ceph.
