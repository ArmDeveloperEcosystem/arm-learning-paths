---
title: Docker Sandboxes (sbx)

description: Install Docker Sandboxes (sbx) on macOS with Apple Silicon to run AI coding agents in isolated Arm Linux microVMs using Apple's virtualization framework.

minutes_to_complete: 10

official_docs: https://docs.docker.com/ai/sandboxes/

additional_search_terms:
- docker
- sbx
- sandbox
- microvm
- containers
- apple silicon

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
`sbx` is not available on Arm Linux. 
{{% /notice %}}

On macOS with Apple Silicon, `sbx` uses Apple's virtualization framework to launch Arm Linux (Ubuntu) microVMs. You don't need Docker Desktop.

## Before you begin

You need:

- A Mac with Apple Silicon (M1 or later) running macOS Sonoma (version 14) or later.
- A [Docker Hub](https://hub.docker.com/) account to authenticate `sbx`.
- [Homebrew](https://brew.sh/) installed.

## Install the sbx CLI

Install `sbx` using Homebrew:

```bash
brew install docker/tap/sbx
```

Homebrew installs the `sbx` binary at `/opt/homebrew/bin/sbx`.

## Verify the installation

After installing the CLI, verify that the installation was successful.

### Check the sbx CLI version

Start by checking what version of `sbx` is installed:

```bash
sbx version
```

{{% notice Note %}}
The following output shows the version at the time this guide was written. Homebrew installs the latest available version. To find the latest release, see the [sbx releases page](https://github.com/docker/sbx-releases/releases).
{{% /notice %}}

The output is similar to:

```output
sbx version: v0.32.0 55580366449bcfebfc1787b9944284cf64c856d7
```

### Authenticate with Docker Hub

Sign in to your Docker account:

```bash
sbx login
```

This outputs a one-time code and a URL. Open the link in a browser, sign in with your Docker Hub credentials, and approve the activation.

### Run a sandbox

Navigate to your project directory and start an agentless sandbox for manual exploration.

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

To exit the sandbox, enter `exit`.

### Verify sandbox management commands

After exiting the sandbox, list all sandboxes, including their names and current status:

```bash
sbx ls
```

The output is similar to:

```output
SANDBOX                    AGENT   STATUS    PORTS    WORKSPACE
shell-arm-learning-paths   shell   stopped           /Users/arm-learning-paths
```

Copy a file from your Mac into the sandbox:

```bash
sbx cp ./myfile.txt <SANDBOX>:/home/user/myfile.txt
```

Copy a file from a sandbox back to your Mac:

```bash
sbx cp <SANDBOX>:/home/user/output.txt ./output.txt
```

## Clean up 

Stop the running shell sandbox using its name:

```bash
sbx stop <SANDBOX>
```

Remove the sandbox permanently:

```bash
sbx rm <SANDBOX>
```

## Next steps

You're now ready to use Docker Sandboxes to run AI agents in isolated microVMs on macOS. 

To launch an agent sandbox, provide the name of the agent sandbox in the run command. For example, `claude`:

```bash
sbx run claude
```

Other supported agent sandboxes include `copilot`, `codex`, and `kiro`. For the full list, see the [Docker Sandboxes agents documentation](https://docs.docker.com/ai/sandboxes/agents/).

You can use AI agents with the Arm MCP Server to build on or migrate to Arm. For more information, see the [Arm MCP Server](/learning-paths/servers-and-cloud-computing/arm-mcp-server/) Learning Path.