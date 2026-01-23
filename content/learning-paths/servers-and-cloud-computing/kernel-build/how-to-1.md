---
title: Set up your Arm instance for kernel building
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure an Arm Linux cloud instance for kernel building

Before you begin, you need an Arm cloud instance with SSH access. 

This Learning Path uses AWS as the example platform, but you can follow the same steps on any cloud provider that offers 64-bit Arm Ubuntu instances.

For demonstration purposes, you can use an AWS `m6g.12xlarge` instance. Any sufficiently large instance on your chosen provider works, however, smaller instances take longer or risk running out of memory during compilation. If you use a different instance type, the minimum requirements are an Arm instance running at least 24 vCPUs with 200 GB of free storage.

Ubuntu 24.04 LTS is the operating system. Other Linux distributions may work. If you find a different distribution that works well, or you'd like to request support for a different distribution, open an issue or a pull request in the [project repository](https://github.com/geremyCohen/arm_kernel_install_guide).

## Install required dependencies

With your build instance running and accessible via SSH, install the required dependencies:

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv python-is-python3 build-essential bc rsync dwarves flex bison libssl-dev libelf-dev btop yq jq
```

This command installs the compilation toolchain, kernel build tools, and utilities needed for the build scripts.

## Clone the kernel build repository

Clone the GitHub repository in your home directory:

```bash
git clone https://github.com/geremyCohen/arm_kernel_install_guide.git ~/arm_kernel_install_guide
cd ~/arm_kernel_install_guide
chmod +x scripts/*.sh
```

The repository contains:
- A build orchestration script
- Configuration templates for various kernel build scenarios
- Helper utilities for managing kernel artifacts

All commands in this Learning Path assume you're in the project directory at `$HOME/arm_kernel_install_guide`. 

The important script is `scripts/kernel_build_and_install.sh`, which orchestrates cloning the upstream kernel tree, configuring TuxMake, building artifacts, and optionally installing the kernel. The script runs non-interactively—once invoked it proceeds without confirmation prompts, and any install operation automatically reboots the system when it finishes.

## Understand the script flags

The `kernel_build_and_install.sh` script supports two main workflows:

1. **General usage** - Build kernels for direct installation or downstream packaging
2. **Fastpath usage** - Build kernels with additional headers and perf configuration needed by the Fastpath validation tool

### About Fastpath

Fastpath is a command-line tool designed for monitoring Linux kernel performance by executing structured performance benchmarks on various hardware platforms. It automates the collection, storage, and analysis of performance data to assess how Linux kernel modifications impact different workloads. Fastpath enables developers and performance engineers to detect regressions, validate optimizations, and track long-term performance trends.

Key use cases include:
- Kernel performance tracking across updates
- Hardware comparison between different systems
- Automated CI/CD benchmarking

If you need only general kernel building, use the first workflow. If you want to use Fastpath for kernel performance validation, use the second workflow. For more information, see the [Fastpath documentation](https://fastpath.docs.arm.com).

### General usage flags

| Flag | Description |
| --- | --- |
| `--demo-default-build` | Shortcut: builds `v6.18.1` with default configs and leaves Fastpath disabled |
| `--tag <tag>` / `--tags <list>` / `--tag-latest` | Select one or more kernel tags. Multiple tags build in parallel; the latest stable release can be added via `--tag-latest` |
| `--install-from <dir>` / `--install-format <flat\|deb\|auto>` | Install an existing build (flat artifacts or `.deb` packages) without recompiling |
| `--dry-run` | Generate a self-contained plan script (stored in `/tmp/kernel_plan_*.sh`) with the resolved arguments and exit without running the build |
| `--kernel-install [tag\|bool]` | Install a kernel right after it finishes building. When multiple tags build, provide the specific tag to install |
| `--change-to-64k <bool>` | Generate a 64 KB page-size kernel. Often combined with the install flags to test high-page builds |
| `--config-file <path>` | Reuse a captured stock config instead of `/boot/config-$(uname -r)` |
| `--include-bindeb-pkg` | Adds the `bindeb-pkg` target so `.deb` packages are produced alongside `Image.gz` and `modules.tar.xz` |
| `--kernel-command-line <string>` | Override GRUB's `GRUB_CMDLINE_LINUX` when installing a kernel |
| `--append-to-kernel-version <text>` | Attach custom suffixes to `EXTRAVERSION` (for example, `--append "-lab"`) |
| `--kernel-dir <path>` / `--venv-path <path>` | Control where the kernel git checkout lives and which Python venv hosts TuxMake. Build artifacts always land under `~/kernels/<tag>` |

### Fastpath usage flags

| Flag | Description |
| --- | --- |
| `--demo-fastpath-build` | Shortcut: builds `v6.18.1` and `v6.19-rc1` with Fastpath configs enabled |
| `--fastpath <bool>` | Manually enable/disable the Fastpath configuration overlay (installs Docker as needed) |


## Verify the setup

Check that the script is executable and displays help information:

```bash
./scripts/kernel_build_and_install.sh --help
```

The expected output shows all available flags and usage examples.

You're now ready to build Linux kernels on your Arm instance. The next section covers standard kernel build workflows.
