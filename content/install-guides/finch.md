---
title: Finch on Arm Linux
author: Jason Andrews

minutes_to_complete: 10

official_docs: https://runfinch.com/docs/

additional_search_terms:
- containerd
- Docker
- Finch

test_images:
- ubuntu:latest
test_maintenance: false

tool_install: true
layout: installtoolsall
multi_install: false
multitool_install_part: false
weight: 1
---

[Finch](https://runfinch.com) is an open-source container development tool from AWS. It offers a simple, Docker-compatible CLI powered by containerd and nerdctl. Designed for Linux, macOS, and Windows, Finch is especially useful on Arm-based systems for efficient container workflows.

This guide explains how to install Finch on Arm Linux distributions, specifically Amazon Linux 2023 and Ubuntu 24.04.

To get started, make sure you're using a system running Arm Linux. You can use a physical Arm device, a cloud instance from AWS, Azure, GCP, or OCI, or an Arm-based virtual machine. 

To confirm the architecture, run:

```bash
uname -m
```

The output should be `aarch64` for 64-bit Arm systems.

## How do I install Finch on Amazon Linux 2023 for Arm?

Finch is available as an RPM package in the standard Amazon Linux 2023 repositories, making installation simple.

Install Finch using the package manager:

```console
sudo yum install runfinch-finch -y
```

Enable and start the containerd service:

```console
sudo systemctl start containerd
```

Check that the containerd service is running:

```console
sudo systemctl status containerd
```

You should see something like:

```output
● containerd.service - containerd container runtime
     Loaded: loaded (/usr/lib/systemd/system/containerd.service; disabled; preset: disabled)
     Active: active (running) since Wed 2025-05-21 19:49:50 UTC; 40s ago
       Docs: https://containerd.io
    Process: 25839 ExecStartPre=/sbin/modprobe overlay (code=exited, status=0/SUCCESS)
   Main PID: 25841 (containerd)
      Tasks: 10
     Memory: 160.5M
        CPU: 1.771s
     CGroup: /system.slice/containerd.service
             └─25841 /usr/bin/containerd
```

The `finch` command is now available in your PATH. You can now skip to the section on [verifying the Finch installation](#how-do-i-verify-the-finch-installation).


## How do I install Finch on Ubuntu 24.04 for Arm?

Finch doesn't currently provide a Debian package for Ubuntu, but you can install it manually, using the three steps outlined below.

### Step 1: Install Finch dependencies

Install Nerdctl by following the instructions in the [Nerdctl install guide](/install-guides/nerdctl/). Then install the required tools:

```console
sudo apt install -y \
  golang \
  make \
  build-essential
```

### Step 2: Build and install Finch

Clone the Finch repository and build the binary:

```console
git clone https://github.com/runfinch/finch.git
cd finch
git submodule update --init --recursive
make
sudo make install
```

### Step 3: Configure Finch

Create the Finch configuration directories:

```bash
sudo mkdir -p /etc/finch
sudo mkdir -p /usr/libexec/finch
```

Create the Finch configuration file:

```bash
cat << EOF | sudo tee /etc/finch/finch.yaml > /dev/null
# cpus: the amount of vCPU to dedicate to the virtual machine. (required)
cpus: 2

# memory: the amount of memory to dedicate to the virtual machine. (required)
memory: 2GiB

# snapshotters: the snapshotters a user wants to use (the first snapshotter will be set as the default snapshotter)
snapshotters: 
    - overlayfs

# dockercompat: a configuration parameter to activate finch functionality to accept Docker-like commands and arguments.
dockercompat: true
EOF
```

Configure Nerdctl:

```bash
sudo ln -sf $(which nerdctl) /usr/libexec/finch/nerdctl
```

After these steps, the `finch` command is available in your PATH.

## How do I verify the Finch installation?

You can check the Finch version:

```bash
sudo finch --version
```

The version is printed:

```output
finch version v1.8.2
```

Run a container to confirm functionality:

```bash
sudo finch run --rm armswdev/uname
```

If you see the architecture printed, then Finch is working correctly. 

The expected output is:

```output
Architecture is aarch64
```

Print your local container images:

```bash
sudo finch images
```

The output is similar to:

```output
REPOSITORY        TAG       IMAGE ID        CREATED           PLATFORM       SIZE       BLOB SIZE
armswdev/uname    latest    82762f30a4a3    43 seconds ago    linux/arm64    110.4MB    28.89MB
```

Use `sudo finch help` to explore available commands.

You are ready to use Finch to run containers on your Arm Linux system.
