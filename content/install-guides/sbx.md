---
title: Docker Sandboxes (sbx)

description: Install Docker Sandboxes (sbx) on macOS with Apple Silicon or Arm Linux to run AI coding agents in isolated microVMs.

minutes_to_complete: 10

official_docs: https://docs.docker.com/ai/sandboxes/

additional_search_terms:
- docker
- sbx
- sandbox
- microvm
- containers

author: Jason Andrews

test_images:
test_maintenance: false

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

Docker Sandboxes (`sbx`) is a standalone CLI from Docker for running AI coding agents in isolated microVMs. Each sandbox gets its own filesystem, network, and Docker daemon, so agents can install packages, modify files, and run containers without touching your host system.

{{% notice Note %}}
Arm Linux support is available in `sbx` version 0.33 and later.
{{% /notice %}}

On macOS with Apple Silicon, `sbx` uses Apple's virtualization framework to launch Arm Linux (Ubuntu) microVMs. You don't need Docker Desktop.

On Arm Linux, `sbx` uses the KVM hypervisor to launch microVMs. KVM requires bare metal and does not work on virtual machines.

## Before you begin

### macOS prerequisites

You need:

- A Mac with Apple Silicon (M1 or later) running macOS Sonoma (version 14) or later.
- [Homebrew](https://brew.sh/) installed.
- A [Docker Hub](https://hub.docker.com/) account to authenticate `sbx`.

### Arm Linux prerequisites

You need:

- An Arm Linux system running Ubuntu 24.04 LTS or later on aarch64 architecture.
- Kernel-based Virtual Machine (KVM) enabled on bare metal hardware.
- A [Docker Hub](https://hub.docker.com/) account to authenticate `sbx`.

## Install the sbx CLI

### macOS installation

Install `sbx` using Homebrew:

```bash
brew install docker/tap/sbx
```

Homebrew installs the `sbx` binary at `/opt/homebrew/bin/sbx`.

### Arm Linux installation

On Arm Linux, `sbx` requires KVM acceleration. KVM does not typically work on virtual machines. It requires bare metal.

Install and run the `kvm-ok` command to confirm KVM is available.

Install `kvm-ok` on Debian-based Linux distributions:

```bash
sudo apt install cpu-checker -y
```

To check if KVM is available, run:

```console
sudo kvm-ok
```

If KVM is available, the output is similar to:

```output
INFO: /dev/kvm exists
KVM acceleration can be used
```

If KVM is not available, the output is similar to:

```output
INFO: /dev/kvm does not exist
HINT:   sudo modprobe kvm
INFO: For more detailed results, you should run this as root
HINT:   sudo /usr/sbin/kvm-ok
```

After KVM is available, install `sbx` using the appropriate .deb package for your Ubuntu version. First, check your Ubuntu version:

```bash
grep VERSION_ID /etc/os-release
```

{{% notice Note %}}
The following commands use Docker Sandboxes version 0.33.0. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest release and available Ubuntu versions, see the [sbx releases page](https://github.com/docker/sbx-releases/releases).
{{% /notice %}}

For Ubuntu 26.04, download and install the .deb package:

```bash
wget https://github.com/docker/sbx-releases/releases/download/v0.33.0/DockerSandboxes-linux-arm64-ubuntu2604.deb
sudo apt install ./DockerSandboxes-linux-arm64-ubuntu2604.deb
```

For Ubuntu 24.04, download and install the .deb package:

```bash
wget https://github.com/docker/sbx-releases/releases/download/v0.33.0/DockerSandboxes-linux-arm64-ubuntu2404.deb
sudo apt install ./DockerSandboxes-linux-arm64-ubuntu2404.deb
```

Verify the installation:

```bash
which sbx
```

The output is similar to:

```output
/usr/bin/sbx
```

## Verify the installation

After installing the CLI, verify that the installation was successful.

### Check the sbx CLI version

Start by checking what version of `sbx` is installed:

```bash
sbx version
```

{{% notice Note %}}
The following output shows the version at the time this guide was written. To find the latest release, see the [sbx releases page](https://github.com/docker/sbx-releases/releases).
{{% /notice %}}

The output is similar to:

```output
sbx version: v0.33.0 d7da69cb30eb3000c4d4ef0c848ffe84f32058bf
```

### Authenticate with Docker Hub

Sign in to your Docker account:

```bash
sbx login
```

This outputs a one-time code and a URL. Open the link in a browser, sign in with your Docker Hub credentials, and approve the activation.

### Start a shell sandbox

Navigate to your project directory and start an agentless sandbox for manual exploration:

```bash
sbx run shell
```

This launches a bare Arm Linux microVM with a shell prompt. No AI agent runs inside it.

On your first run, the CLI will ask you to select a network policy:

- `Open`: allows all network access from within the sandbox.
- `Balanced`: allows common development services while blocking everything else.
- `Locked Down`: blocks all outbound network traffic.

`Balanced` is a good starting point for most development workflows.

### Confirm the sandbox runs Arm Linux

To ensure the shell sandbox runs as expected, from within the sandbox, verify the operating system and architecture:

```bash
uname -a
```

The output is similar to:

```output
Linux shell-arm-learning-paths 7.0.8 #1 SMP PREEMPT Thu Jun  4 20:59:42 UTC 2026 aarch64 GNU/Linux
```

Check the Ubuntu release:

```bash
cat /etc/os-release
```

The output is similar to:

```output
PRETTY_NAME="Ubuntu 26.04 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04 (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo
```

This confirms that the shell sandbox is running Arm Linux (Ubuntu on aarch64) inside the microVM.

Keep the shell running to test management commands in another terminal.

### Verify sandbox management commands

In another terminal window, list all sandboxes with their agent and current status:

```bash
sbx ls
```

The output is similar to:

```output
SANDBOX                    AGENT   STATUS    PORTS    WORKSPACE
shell-arm-learning-paths   shell   stopped           ~/my-project
```

Copy a file from your host into the sandbox. For example:

```bash
sbx cp ./myfile.txt <SANDBOX>:/home/user/myfile.txt
```

Copy a file from a sandbox back to your host. For example:

```bash
sbx cp <SANDBOX>:/home/user/output.txt ./output.txt
```

## Clean up

Stop the running shell sandbox using its name:

```bash
sbx stop <SANDBOX>
```

The running shell sandbox in the first terminal window stops.

Remove the sandbox permanently:

```bash
sbx rm <SANDBOX>
```

You'll be prompted to confirm whether you want to remove the sandbox. Answer `y` and press Enter to delete the sandbox.

## Next steps

You're now ready to use Docker Sandboxes to run AI agents in isolated microVMs on macOS or Arm Linux.

To launch an agent sandbox, provide the name of the agent sandbox in the run command. For example, to launch a Claude sandbox:

```bash
sbx run claude
```

Other supported agent sandboxes include `copilot`, `codex`, and `kiro`. For the full list, see the [Docker Sandboxes agents documentation](https://docs.docker.com/ai/sandboxes/agents/).

You can use AI agents with the Arm MCP Server to build on or migrate to Arm. For more information, see the [Arm MCP Server](/learning-paths/servers-and-cloud-computing/arm-mcp-server/) Learning Path.