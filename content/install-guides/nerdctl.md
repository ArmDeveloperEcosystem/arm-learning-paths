---
title: Nerdctl
author: Jason Andrews

draft: true

minutes_to_complete: 10

official_docs: https://github.com/containerd/nerdctl

additional_search_terms:
- container
- containerd
- docker
- Linux

test_images:
- ubuntu:latest
test_maintenance: false

tool_install: true
layout: installtoolsall
multi_install: false
multitool_install_part: false
weight: 1
---

Nerdctl is an open-source command-line interface (CLI) designed to be compatible with the popular Docker CLI, but specifically for interacting with [containerd](https://containerd.io/). It provides a familiar user experience for developers operators who are familiar with Docker, while leveraging the capabilities of containerd as the underlying container runtime.

Using containerd and nerdctl provides similar functionality to Docker but with a smaller memory and CPU footprint, making it ideal for IoT or edge solutions, especially on Arm devices which balance energy efficiency and performance. Nerdctl also supports running containers in a rootless mode, enhancing security by not requiring elevated privileges.

This guide focuses on installing containerd and Nerdctl on Arm Linux. 

## Before you begin

This guide assumes you are using Ubuntu 22.04 or later on an Arm-based system (like a Raspberry Pi or an Arm instance in the cloud).

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

Ensure `wget` and `tar` are installed:

```bash
sudo apt-get update
sudo apt-get install -y wget tar
```

## Install containerd

Install the containerd runtime:

```bash 
sudo apt-get update
sudo apt-get install -y containerd
```

Start and enable the containerd service:

```bash 
sudo systemctl start containerd
sudo systemctl enable containerd
```

## Install nerdctl and CNI plugins

Install nerdctl and the necessary CNI (Container Network Interface) plugins. Replace version numbers if needed.

```bash
NERDCTL_VERSION=$(curl -s https://api.github.com/repos/containerd/nerdctl/releases/latest | grep tag_name | cut -d '"' -f 4 | sed 's/v//')
wget https://github.com/containerd/nerdctl/releases/download/v${NERDCTL_VERSION}/nerdctl-${NERDCTL_VERSION}-linux-arm64.tar.gz
sudo tar -xzvf nerdctl-${NERDCTL_VERSION}-linux-arm64.tar.gz -C /usr/local/bin
```

Install the CNI plugins:

```bash
CNI_VERSION=$(curl -s https://api.github.com/repos/containernetworking/plugins/releases/latest | grep tag_name | cut -d '"' -f 4 | sed 's/v//')
wget https://github.com/containernetworking/plugins/releases/download/v${CNI_VERSION}/cni-plugins-linux-arm64-v${CNI_VERSION}.tgz
sudo mkdir -p /opt/cni/bin
sudo tar -xzvf cni-plugins-linux-arm64-v${CNI_VERSION}.tgz -C /opt/cni/bin
```

Clean up the downloaded files:

```bash
rm nerdctl-${NERDCTL_VERSION}-linux-arm64.tar.gz cni-plugins-linux-arm64-v${CNI_VERSION}.tgz
```


{{% notice Note %}}
The commands above attempt to fetch the latest versions automatically. You can replace `${NERDCTL_VERSION}` and `${CNI_VERSION}` with specific versions if required.*
{{% /notice %}

## Verify the installation

Test your installation by running a simple NGINX container:

```console 
sudo nerdctl run --name uname armswdev/uname
```

Wait a few seconds for the container to run, and the Architecture is printed: 

```output
Architecture is aarch64
```


Clean up the test container:

```console
sudo nerdctl rm uname
```

You can also check the nerdctl version:
```console
sudo nerdctl version
```

## Basic nerdctl commands

Here are some common commands to get you started:

List running containers:

```console
sudo nerdctl ps
```

List all containers (including stopped):

```console
sudo nerdctl ps -a
```

List images:

```console
sudo nerdctl images
```

Pull an image:

```console
sudo nerdctl pull <image_name>:<tag>
```

Build an image from Dockerfile in current directory:

```console
sudo nerdctl build -t <image_name>:<tag> .
```

Remove an image:

```console
sudo nerdctl rmi <image_name>:<tag>
```

Stop a container:

```console
sudo nerdctl stop <container_name_or_id>
```

Remove a container:

```console
sudo nerdctl rm <container_name_or_id>
```

You are now ready to use nerdctl and containerd.
