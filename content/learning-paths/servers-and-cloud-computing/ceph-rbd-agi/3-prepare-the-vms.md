---
title: Validate the Arm64 virtual machines
description: Check the resources, network connectivity, time synchronization, and empty data disks required by Ceph.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the nodes for Ceph

In this section, you will prepare all three VMs with hostname resolution, synchronized clocks, and the tools cephadm needs to run storage services. Connect from the AGI host, then run the preparation commands inside each VM. Finish by identifying the empty data disks that Ceph will use.

## Check the virtual machines

The previous section created three Ubuntu 26.04 Arm64 virtual machines named `ceph1`, `ceph2`, and `ceph3`. Each VM should have:

- 4 virtual CPUs
- 4 GB of memory
- A 20 GB operating-system disk
- A separate unused data disk of at least 10 GB
- An interface connected to `agi-net`

This Learning Path assumes that the unused disk is `/dev/vdb`. Substitute your device name if it differs.

{{% notice Warning %}}
Ceph consumes the complete OSD data disk. Do not use a disk that contains data you need. Check the device name and contents before you create each OSD.
{{% /notice %}}

## Record the addresses

Start from a terminal on the AGI host, using the host account that holds the `~/.ssh/agi_ceph` private key created in the previous section. Connect to `ceph1` as the `ubuntu` user:

```bash
ssh -o ConnectTimeout=10 -i "${HOME}/.ssh/agi_ceph" ubuntu@192.168.100.11
```

After login, your shell is running inside `ceph1`. The prompt typically includes `ubuntu@ceph1`. Run the following commands in that SSH session to display the VM's hostname, architecture, and IPv4 addresses:

```bash
hostname
uname -m
uname -r
ip -4 -brief address show scope global
```

Confirm that the architecture is `aarch64`. The tested Ubuntu 26.04 guest kernel is `7.0.0-34-generic`. The RBD section requires kernel support for `aes256k` credentials; loading the RBD module alone does not prove authentication compatibility. Record one stable IP address for each VM. The examples use the following addresses:

| Hostname | Address |
| --- | --- |
| `ceph1` | `192.168.100.11` |
| `ceph2` | `192.168.100.12` |
| `ceph3` | `192.168.100.13` |

If you changed the `agi-net` subnet or supplied your own VMs, replace these addresses with the addresses you recorded.

Run `exit` to leave the VM's SSH session and return to the AGI host. Repeat the login and address checks for `ceph2` and `ceph3`, using `192.168.100.12` and `192.168.100.13` respectively in the SSH command. You can also open a separate AGI-host terminal for each SSH session. Keep the private key on the AGI host; each connection starts there.

Use SSH for these checks. The VMs have SSH-key access configured for `ubuntu`, with no console login password set.

After recording all three addresses, connect to each VM again and add all three nodes to that VM's `/etc/hosts`. Run the following block once inside each VM's SSH session, replacing the example addresses if needed:

```bash
cat <<'EOF' | sudo tee -a /etc/hosts
192.168.100.11 ceph1
192.168.100.12 ceph2
192.168.100.13 ceph3
EOF
```

In the SSH session connected to `ceph1`, confirm that the other nodes resolve and respond:

```bash
getent hosts ceph2 ceph3
ping -c 2 ceph2
ping -c 2 ceph3
```

## Check the Ceph prerequisites

Run the following commands on all three virtual machines:

```bash
sudo apt update
sudo apt install -y chrony lvm2 podman openssh-server curl
sudo systemctl enable --now chrony ssh
```

Cephadm requires Python 3, systemd, a container runtime, time synchronization, and LVM2. Ubuntu 26.04 includes Python 3 and systemd. Confirm the remaining services and tools:

```bash
python3 --version
podman --version
systemctl is-active chrony
command -v lvm
```
The expected output is similar to:
```output
Python 3.14.4
podman version 5.7.0
active
/usr/sbin/lvm
```

Check time synchronization on each VM:

```bash
chronyc tracking
```

Wait for a valid reference source and `Leap status: Normal`.

## Validate the data disks

On each node, inspect the candidate disk:

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS /dev/vdb
sudo wipefs --no-act /dev/vdb
```

The expected output is:

```output
NAME SIZE TYPE FSTYPE MOUNTPOINTS
vdb   10G disk
```
The disk should have no partitions, file system, or mount point. `wipefs --no-act` must not report any signatures. Resolve any unexpected output before continuing.

## What you've accomplished and what's next

You've prepared three networked Arm64 virtual machines and confirmed that each has an unused data disk. Next, you'll bootstrap Ceph on `ceph1` and add its first OSD.
