---
title: Incus

description: Install Incus on Arm Linux and run an unprivileged Ubuntu system container with managed storage and network access.

minutes_to_complete: 15
official_docs: https://linuxcontainers.org/incus/docs/main/

author: Pareena Verma

test_images:
test_maintenance: false

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

Incus is an open-source system container and virtual machine manager. It provides image-based instance management and storage, as well as networking, profiles, and a command-line interface.

Incus system containers share the host Linux kernel. By default, containers are unprivileged and map container user IDs to non-root user IDs on the host. 

You'll install Incus and verify an unprivileged container.

Incus is useful for agentic tasks that need a disposable Linux filesystem for generated commands, scripts, builds, and tests. You can apply CPU, memory, and process limits while keeping agent filesystem changes separate from the host.

The Incus daemon runs on Linux. You'll install Incus using the Ubuntu package on Ubuntu 24.04 long-term support (LTS) on `aarch64`. Incus is also packaged for other Linux distributions. For platform-specific installation options, see the [Incus installation documentation](https://linuxcontainers.org/incus/docs/main/installing/).

## Before you begin

You need an Arm Linux system running Ubuntu 24.04 LTS on `aarch64`. The system needs to have sudo access and internet access to the Ubuntu package repositories and the Incus image server. Ensure that your network allows the container to obtain a DHCP address with its own MAC address.

Check the host architecture and operating system:

```bash
uname -m
cat /etc/os-release
```

Confirm that the architecture is `aarch64` and the operating system is Ubuntu 24.04 LTS.

Check that the host uses the unified control group version 2 hierarchy:

```bash
stat -fc %T /sys/fs/cgroup
```

The expected output is:

```output
cgroup2fs
```

## Install Incus

Update the package index:

```bash
sudo apt update
```

{{% notice Note %}}
The following commands use the Incus 6.0 LTS release from the Ubuntu 24.04 repositories. The Ubuntu package revision can change as updates are published. The same commands work with updated Incus 6.0 packages. To learn about the available release branches, see [Choose your release](https://linuxcontainers.org/incus/docs/main/installing/#choose-your-release) in the Incus documentation.
{{% /notice %}}

Install the Incus daemon and command-line client:

```bash
sudo apt install -y incus
```

The package supplies everything needed to run system containers.

Add your user to the `incus-admin` group:

```bash
sudo adduser "$USER" incus-admin
```

Membership in `incus-admin` grants full control of the local Incus daemon. Give this access only to users that you trust with root-level control of the host.

Activate the new group in your current terminal:

```bash
newgrp incus-admin
```

The command opens a new shell with the group active. Keep this shell open to complete initialization and verification. If you need to open another shell, log out and back in before continuing.

Confirm that the client can connect to the local daemon:

```bash
incus version
```

The output is similar to:

```output
Client version: 6.0.0
Server version: 6.0.0
```

The package revision can change without changing the displayed upstream version.

## Initialize Incus

Initialize Incus with a `dir` storage pool and a default profile that doesn't attach a network interface:

{{% notice Note %}}
Run the preseed command only for a new Incus installation. If the host already has Incus storage, networks, profiles, or instances, inspect the existing configuration instead of replacing it.
{{% /notice %}}

```bash
cat <<'EOF' | incus admin init --preseed
config: {}
networks: []
storage_pools:
- name: default
  driver: dir
profiles:
- name: default
  description: Default Incus profile
  config: {}
  devices:
    root:
      path: /
      pool: default
      type: disk
EOF
```

This creates a `dir`-backed storage pool named `default` and attaches it to new instances through the default profile. The `dir` storage driver is suitable for this installation check. However, it doesn't provide the snapshot, quota, and optimized-copy features of storage drivers such as ZFS or Btrfs.

List the storage pools:

```bash
incus storage list
```

Confirm that the output contains a storage pool named `default` with the `dir` driver.

The output is similar to:

```output
+---------+--------+--------------------------------------+-------------+---------+---------+
|  NAME   | DRIVER |                SOURCE                | DESCRIPTION | USED BY |  STATE  |
+---------+--------+--------------------------------------+-------------+---------+---------+
| default | dir    | /var/lib/incus/storage-pools/default |             | 1       | CREATED |
+---------+--------+--------------------------------------+-------------+---------+---------+
```

Confirm that no Incus managed bridge was created:

```bash
incus network list
```

Confirm that `incusbr0` doesn't appear. Existing host interfaces might appear as unmanaged networks.

## Verify the installation

You'll connect the test container directly to the default network interface of the host with a `macvlan` device.

{{% notice Note %}}
A `macvlan` device gives the container direct access to the physical network without an Incus managed bridge or outbound NAT. The network has to permit an additional MAC address on the host connection. The host and container can't communicate directly over this interface, but `incus exec` continues to work.
{{% /notice %}}

Find the host interface that carries the default IPv4 route:

```bash
parent_interface="$(
    ip -4 route show default |
    awk 'NR == 1 {print $5}'
)"

echo "$parent_interface"
```

The output is the interface name, and is similar to:

```output
enP11p1s0
```

Initialize an Ubuntu 24.04 system container with privileged mode disabled and resource limits suitable for an installation check.

On an `aarch64` host, the image server selects the Arm64 image:

```bash
incus init images:ubuntu/24.04 arm-install-check \
    --config security.privileged=false \
    --config limits.cpu=1 \
    --config limits.memory=1GiB \
    --config limits.processes=256
```

The output is similar to:
```output
Creating arm-install-check
                                           
The instance you are starting doesn't have any network attached to it.
  To create a new network, use: incus network create
  To attach a network to an instance, use: incus network attach
```

The first initialization downloads the image. Incus reports that the instance has no attached network. This is expected because the next command adds the network device before the container starts.

Add a `macvlan` device that uses the host interface, then start the container:

```bash
incus config device add arm-install-check eth0 nic \
    nictype=macvlan \
    parent="$parent_interface" \
    name=eth0

incus start arm-install-check
```

The device command reports:

```output
Device eth0 added to arm-install-check
```

### Check the container status

List the test container:

```bash
incus list arm-install-check
```

The output is similar to:

```output
+-------------------+---------+--------------------+------+-----------+-----------+
|       NAME        |  STATE  |        IPV4        | IPV6 |   TYPE    | SNAPSHOTS |
+-------------------+---------+--------------------+------+-----------+-----------+
| arm-install-check | RUNNING | 10.104.1.52 (eth0) |      | CONTAINER | 0         |
+-------------------+---------+--------------------+------+-----------+-----------+
```

The assigned address varies by network. Confirm that `arm-install-check` has state `RUNNING`, type `CONTAINER`, and an IPv4 address on `eth0`.

### Test network access

Inspect the container interface, routing table, and DNS resolution:

```bash
incus exec arm-install-check -- sh -c \
    'ip -brief address show eth0; ip route; getent hosts images.linuxcontainers.org'
```

The output is similar to:

```output
eth0@if4         UP             10.104.1.52/22 metric 100 fe80::216:3eff:fed5:5b22/64
default via 10.104.0.1 dev eth0 proto dhcp src 10.104.1.52 metric 100
10.104.0.0/22 dev eth0 proto kernel scope link src 10.104.1.52 metric 100
2602:fc62:a:1::8 images.linuxcontainers.org
```

The addresses and routes vary by network. Confirm that `eth0` is `UP`, a default route is present, and the hostname resolves.

Update the package index inside the container to verify outbound access:

```bash
incus exec arm-install-check -- apt-get update
```

A successful command downloads the Ubuntu repository metadata and finishes with:

```output
Reading package lists... Done
```

### Run a command in the container

Check the architecture and virtualization environment, then create a test file inside the container:

```bash
incus exec arm-install-check -- sh -c \
    'uname -m; systemd-detect-virt; printf "Incus container command succeeded\n" > /root/install-check.txt; cat /root/install-check.txt'
```

The expected output is:

```output
aarch64
lxc
Incus container command succeeded
```

The `aarch64` output confirms the container userspace architecture. The `lxc` output identifies the container environment but doesn't indicate a separate guest kernel.

### Verify the unprivileged container

Check the explicit privileged-mode setting:

```bash
incus config get arm-install-check security.privileged
```

The output is similar to:

```output
false
```

Inspect the user ID map from inside the container:

```bash
incus exec arm-install-check -- cat /proc/self/uid_map
```

The output is similar to:

```output
         0    1000000 1000000000
```

The values vary by host configuration. Confirm that container user ID `0` maps to a nonzero host user ID in the second column. This mapping shows that root inside the container isn't root on the host.

## Delete the test container

Stop and remove the container:

```bash
incus delete arm-install-check --force
incus list
```

Confirm that `arm-install-check` no longer appears. If you have other instances, `incus list` continues to show them.

The downloaded image and `default` storage pool remain available for future containers.

## Next steps

You can now use Incus to create and manage unprivileged system containers on Arm Linux. To use an Incus managed bridge with outbound NAT, use a kernel that enables `CONFIG_NFT_NAT` and `CONFIG_NFT_MASQ`.

To learn about features such as storage drivers, managed networks, profiles, and snapshots, see the [Incus documentation](https://linuxcontainers.org/incus/docs/main/).
