---
title: Nerdctl
author: Jason Andrews

minutes_to_complete: 10

official_docs: https://github.com/containerd/nerdctl/blob/main/docs/command-reference.md 

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

[Nerdctl](https://github.com/containerd/nerdctl) is an open-source command-line interface (CLI) designed to be compatible with the Docker CLI, but specifically for interacting with [containerd](https://containerd.io/). It provides a familiar user experience for developers who are familiar with Docker, while leveraging the capabilities of containerd as the underlying container runtime.

Using `containerd` and `nerdctl` provides similar functionality to Docker but with a smaller memory footprint, making it ideal for IoT and edge solutions, especially on Arm devices that balance energy efficiency and performance. 

Nerdctl also supports running containers in rootless mode, which helps enhance security by not requiring elevated privileges. Rootless mode is not covered below but you can refer to the [documentation](https://rootlesscontaine.rs/getting-started/containerd/) for information about how to run `containerd-rootless-setuptool.sh install`. 

This guide explains how to install and use `containerd` and `nerdctl` on Arm Linux, and how to run commands with `sudo`. 

## Before you begin

This guide assumes you are using a Debian-based Arm Linux distribution, including Ubuntu and Raspberry Pi OS. You can use a local Arm Linux computer or an Arm instance in the cloud.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

Ensure `wget` and `tar` are installed. Most distributions will include them, but if not, run:

```bash
sudo apt-get update
sudo apt-get install -y wget tar
```

## Install containerd

Install the `containerd` runtime:

```bash 
sudo apt-get install containerd -y
```

Start and enable the `containerd` service:

```bash 
sudo systemctl start containerd
sudo systemctl enable containerd
```

Confirm the service is running:

```console
systemctl status containerd.service
```

When `containerd` is running, the output is similar to:

```output
● containerd.service - containerd container runtime
     Loaded: loaded (/usr/lib/systemd/system/containerd.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-04-22 20:12:03 UTC; 2min 20s ago
       Docs: https://containerd.io
   Main PID: 8428 (containerd)
      Tasks: 9
     Memory: 13.0M (peak: 13.7M)
        CPU: 401ms
     CGroup: /system.slice/containerd.service
             └─8428 /usr/bin/containerd
```

## Install nerdctl and CNI plugins

Install `nerdctl` and the necessary CNI (Container Network Interface) plugins: 

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
The commands above attempt to fetch the latest versions automatically. If required, you can replace `${NERDCTL_VERSION}` and `${CNI_VERSION}` with specific versions.
{{% /notice %}}

## Install BuildKit

If you want to build container images with `nerdctl`, you need to install [BuildKit](https://github.com/moby/buildkit). 

If you only plan to run container images (not build them), you can skip this step. 

```bash
BUILDKIT_VERSION=$(curl -s https://api.github.com/repos/moby/buildkit/releases/latest | grep tag_name | cut -d '"' -f 4 | sed 's/v//')
wget https://github.com/moby/buildkit/releases/download/v${BUILDKIT_VERSION}/buildkit-v${BUILDKIT_VERSION}.linux-arm64.tar.gz
sudo tar -xzvf buildkit-v${BUILDKIT_VERSION}.linux-arm64.tar.gz -C /usr
rm buildkit-v${BUILDKIT_VERSION}.linux-arm64.tar.gz
```

Create a systemd service for BuildKit:

```bash
sudo tee /etc/systemd/system/buildkit.service > /dev/null << EOF
[Unit]
Description=BuildKit
Documentation=https://github.com/moby/buildkit

[Service]
ExecStart=/usr/bin/buildkitd --oci-worker=false --containerd-worker=true

[Install]
WantedBy=multi-user.target
EOF
```

Start and enable the BuildKit service:

```bash
sudo systemctl daemon-reload
sudo systemctl start buildkit
sudo systemctl enable buildkit
```

Verify BuildKit is running:

```console
sudo systemctl status buildkit
```

When running, the output is similar to:

```output
ubuntu@m1u:~$ sudo systemctl status buildkit
● buildkit.service - BuildKit
     Loaded: loaded (/etc/systemd/system/buildkit.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-04-22 22:55:39 CDT; 18min ago
       Docs: https://github.com/moby/buildkit
   Main PID: 22280 (buildkitd)
      Tasks: 10 (limit: 4598)
     Memory: 14.6M (peak: 42.0M)
        CPU: 1.144s
     CGroup: /system.slice/buildkit.service
             └─22280 /usr/bin/buildkitd --oci-worker=false --containerd-worker=true
```

Check that buildctl can communicate with the daemon:

```console
sudo buildctl debug workers
```

If BuildKit is properly installed, you should see output similar to:

```output
ID				            PLATFORMS
jz1h9gb0xq39ob6868cr3ev6r	linux/arm64
```

## Verify the installation

You can check the `nerdctl` version:

```console
sudo nerdctl version
```

Test your installation by running a simple container that prints the processor architecture:

```console 
sudo nerdctl run --name uname armswdev/uname
```

Wait a few seconds for the container to start. It will print the system architecture:

```output
Architecture is aarch64
```

Clean up the test container:

```console
sudo nerdctl rm uname
```

To build a container image, save the following lines to a file named `Dockerfile`.

```console
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

Build the container image:

```console
sudo nerdctl build -t uname -f Dockerfile .
```

Run the new container image:

```console
sudo nerdctl run uname
```

The output is the architecture:

```output
Architecture is aarch64
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

View container logs:

```console
sudo nerdctl logs <container_name_or_id>
```

Execute a command in a running container:

```console
sudo nerdctl exec -it <container_name_or_id> <command>
```

You are now ready to use `nerdctl` and `containerd` to manage containers on Arm Linux.
