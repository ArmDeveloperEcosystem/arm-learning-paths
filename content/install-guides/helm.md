---
title: Helm

author_primary: Jason Andrews
minutes_to_complete: 10

official_docs: https://helm.sh/docs/

additional_search_terms:
- kubernetes
- helm

layout: installtoolsall
multi_install: false
multitool_install_part: false
test_images:
- ubuntu:latest
test_link: false
test_maintenance: false
tool_install: true
weight: 1
---

[Helm](https://helm.sh/) is a package manager for Kubernetes. It helps you manage Kubernetes applications.

Helm is available for Windows, macOS, and Linux and supports the Arm architecture.

## Before you begin

[General installation information](https://helm.sh/docs/intro/install/) is available which covers all supported operating systems.

This article provides a quick solution to install Helm for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:
```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

You may need to install `curl` and `wget` if you don't have them installed.

```bash
sudo apt install -y curl wget
```

## How do I download and install Helm?

There are multiple ways to install Helm for Ubuntu on Arm, pick the one you like most.

### Option 1: Install using the release tar file

Download and install the latest version. 

There is just one executable to copy to the desired location.

```bash
HELM_VER=`curl -s https://api.github.com/repos/helm/helm/releases/latest | grep tag_name | cut -d: -f2 | tr -d \"\,\v | awk '{$1=$1};1'`
wget https://get.helm.sh/helm-v${HELM_VER}-linux-arm64.tar.gz
tar -zxvf helm-v${HELM_VER}-linux-arm64.tar.gz
sudo cp linux-arm64/helm /usr/local/bin/
```

### Option 2: Install using the apt package manager

You can also install Helm using the apt package manager.

```bash
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

### Option 3: Install using Snap

Helm can also be installed using Snap.

```bash
sudo snap install helm --classic
```

### How do I confirm Helm is installed?

Regardless of which option you use, confirm the executable is available.

```bash
helm version
```

You see the version information printed:

```output
version.BuildInfo{Version:"v3.16.3", GitCommit:"cfd07493f46efc9debd9cc1b02a0961186df7fdf", GitTreeState:"clean", GoVersion:"go1.22.7"}
```

You are now ready to use Helm for your Kubernetes projects.
