---
title: Prepare the Arm KVM host
description: Install Firecracker and create the Arm64 kernel, root filesystem, network configuration, and SSH credentials used by disposable jobs.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Confirm the host environment

The Learning Path was validated on an [Arm AGI CPU](https://www.arm.com/products/cloud-datacenter/arm-agi-cpu) platform running Ubuntu 24.04.

You can also run the steps on another Arm-based bare-metal server with KVM available as `/dev/kvm`. For example, you can use an [AWS Graviton4-based Amazon EC2 R8g bare-metal instance](https://aws.amazon.com/blogs/aws/aws-graviton4-based-amazon-ec2-r8g-instances-best-price-performance-in-amazon-ec2/), such as `r8g.metal-24xl` or `r8g.metal-48xl`. Select an Ubuntu 24.04 Arm64 image when provisioning the instance.

A virtual machine (VM) works only when its platform exposes nested virtualization and `/dev/kvm` to the guest. Confirm kernel-based VM (KVM) access before continuing.

Ensure the following:

- Run all commands in a Bash shell on this host. You need `sudo` access and `wget` for the initial downloads.
- Use a dedicated test machine because setup scripts install packages. Each job temporarily changes the host's networking and firewall rules.
- Make sure that the sandbox subnet, `172.16.0.0/30`, doesn't overlap with any network used by the host or its VPN.

Check that you're running on an Arm-based Linux machine:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

Confirm that the KVM device exists and is accessible to a privileged process:

```bash
sudo test -r /dev/kvm && sudo test -w /dev/kvm && echo "KVM is available"
```

The expected output is:

```output
KVM is available
```

If the command produces no output, check that the host kernel enables KVM and that `/dev/kvm` is accessible through `sudo`. On a VM, also check whether the platform supports nested virtualization.

## Download the host preparation scripts

Create a working directory for the sandbox and navigate to it:

```bash
mkdir -p ~/firecracker-ai-sandbox
cd ~/firecracker-ai-sandbox
```

Run all subsequent commands for preparing the host in the `~/firecracker-ai-sandbox` directory.

Start by creating a child directory called `base/` and downloading scripts that install Firecracker and prepare the guest. `00-common.sh` holds their shared paths and version settings:

```bash
mkdir base
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/firecracker-ai-sandbox

for FILE in 00-common.sh 01-setup-host.sh 02-prepare-guest.sh; do
  wget -q "$BASE_URL/files/base/$FILE" -O "base/$FILE"
done
chmod +x base/*.sh
```

Verify that the downloads completed successfully before running the scripts as root. The command lists the files in the `base/` directory:

```bash
find "$PWD/base" -maxdepth 1 -type f -name "*.sh" -printf "%f\n" | sort
```

The expected output is:

```output
00-common.sh
01-setup-host.sh
02-prepare-guest.sh
```

## Install Firecracker

Run the host setup script:

```bash
sudo ./base/01-setup-host.sh
```

The script performs the following tasks:

- Confirms that the host uses `aarch64` and exposes `/dev/kvm`
- Installs the Ubuntu packages needed for Firecracker, guest preparation, networking, and SSH
- Downloads the pinned `aarch64` Firecracker release
- Installs `firecracker` and `jailer` under `/usr/local/bin`

Confirm the installed version:

```bash
firecracker --version
```

The output is similar to:

```output
Firecracker v1.15.1
```

## Prepare the reusable guest image

Create the Arm guest artifacts:

```bash
sudo ./base/02-prepare-guest.sh
```

The script downloads an Arm64 Linux kernel and Ubuntu 24.04 root filesystem from the Firecracker continuous integration (CI) artifacts. It converts the compressed, read-only SquashFS image into a 5 GB writable `ext4` image, then configures SSH and a static private network.

Preparation uses `chroot` to run Arm64 guest provisioning commands on your Arm host. It installs guest packages using the host's network access; the job firewall rules aren't active during this step. Allow disk space for the downloaded image, temporary extracted files, the base disk, and one disposable job disk.

Firecracker and the guest kernel version are pinned in `base/00-common.sh`, but the script selects a dated CI artifact directory dynamically. Those artifacts can change independently of the Firecracker release.

List the resulting artifacts:

```bash
sudo ls -lh /opt/firecracker-lp/artifacts
```

Confirm that the artifacts directory contains the following key files:

- `vmlinux`: the uncompressed Arm guest kernel
- `rootfs.ext4`: the reusable base root filesystem
- `id_rsa`: the host-side private SSH key
- `id_rsa.pub`: the public key installed in the guest

Despite the file name `id_rsa`, the script generates an Ed25519 key. Keep the private key on the host. The runner uses the key to copy and execute programs over SSH. You don't need to open a public SSH port for the microVM.

{{% notice Note %}}
Treat `/opt/firecracker-lp/artifacts/rootfs.ext4` as a clean baseline. The job runner copies it before every execution and never boots the baseline directly.
{{% /notice %}}

## What you've accomplished and what's next

You've installed Firecracker and created the guest artifacts shared by all jobs.

Next, you'll download the runner and execute a shell program inside a disposable microVM.
