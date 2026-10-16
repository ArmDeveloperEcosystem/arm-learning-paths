---
title: Validate the virtual machines
description: Check the resources, network connectivity, time synchronization, and empty data disks required by Ceph.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the nodes for Ceph

You'll prepare all three virtual machines (VMs) with hostname resolution, synchronized clocks, and the tools cephadm needs to run storage services. Connect from the AGI host, then run the preparation commands inside each VM. Finish by identifying the empty data disks that Ceph will use.

### Check the virtual machines

You created three Ubuntu 26.04 VMs named `ceph1`, `ceph2`, and `ceph3`. 

Ensure that each VM has the following resources:

- 4 virtual CPUs
- 4 GB of memory
- A 20 GB operating-system disk 
- A separate unused data disk of at least 10 GB
- An interface connected to `agi-net`

For this Learning Path, the example unused disk is `/dev/vdb`. If you want to use a different disk, substitute `/dev/vdb` in the subsequent commands with your preferred device name.

{{% notice Warning %}}
Ceph consumes the complete object storage daemon (OSD) data disk. Don't use a disk that contains data that you need. Check the device name and contents before you create each OSD.
{{% /notice %}}

### Record the addresses

Start from a terminal on the AGI host with the `~/.ssh/agi_ceph` private key created that you created earlier. Connect to `ceph1` as the `ubuntu` user:

```bash
ssh -o ConnectTimeout=10 -i "${HOME}/.ssh/agi_ceph" ubuntu@192.168.100.11
```

After login, your shell is running inside `ceph1`. The prompt typically includes `ubuntu@ceph1`. 

Run the following commands in that SSH session to display the hostname, architecture, and IPv4 addresses of the VM:

```bash
hostname
uname -m
uname -r
ip -4 -brief address show scope global
```

Confirm that the architecture is `aarch64`. The tested Ubuntu 26.04 guest kernel is `7.0.0-34-generic`. RADOS Block Device (RBD) requires kernel support for `aes256k` credentials. Loading the RBD module alone doesn't prove authentication compatibility. Record one stable IP address for each VM. 

The examples use the following addresses:

| Hostname | Address |
| --- | --- |
| `ceph1` | `192.168.100.11` |
| `ceph2` | `192.168.100.12` |
| `ceph3` | `192.168.100.13` |

Run `exit` to leave the VM SSH session and return to the AGI host. 

Repeat the login and address checks for `ceph2` and `ceph3`, using `192.168.100.12` and `192.168.100.13` respectively in the SSH command. 

You can also open a separate AGI-host terminal for each SSH session.

### Configure the hosts file

After recording all three addresses, connect to each VM again and add all three nodes to the `/etc/hosts` of that VM. Run the following block once inside each VM SSH session, replacing the example addresses if needed:

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

### Install and confirm the Ceph prerequisites

Run the following commands on all three VMs:

```bash
sudo apt update
sudo apt install -y chrony lvm2 podman openssh-server curl
sudo systemctl enable --now chrony ssh
```

You need the following prerequisites for Cephadm:
- Python 3
- systemd
- A container runtime
- Time synchronization
- LVM2 

Confirm the remaining services and tools:

```bash
python3 --version
podman --version
systemctl is-active chrony
command -v lvm
```

The output is similar to:

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

### Validate the data disks

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

You've prepared three networked VMs and confirmed that each VM has an unused data disk. 

Next, you'll bootstrap Ceph on `ceph1` and add the first OSD.
