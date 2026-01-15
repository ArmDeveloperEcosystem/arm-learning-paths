---
title: Compiling Linux Kernels for Arm
additional_search_terms:
- linux kernel
- tuxmake
- fastpath
- Image.gz
- modules.tar.xz
minutes_to_complete: 60
author: Geremy Cohen
official_docs: https://tuxmake.org/
test_images:
- ubuntu:latest
test_maintenance: true
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

This guide walks you through building and installing Linux kernels on Arm cloud VM instances using utility scripts available at  [`arm_kernel_install_guide`](https://github.com/geremyCohen/arm_kernel_install_guide). 

## What do I need before building Arm kernels?

Before you begin, choose a cloud provider, and spin up an instance with the following characteristics:

### Cloud Provider ###  
This guide uses AWS as the example platform, but you can follow the same steps on any cloud provider that offers 64-bit Arm Ubuntu instances.

### Instance Type ### 
This guide uses an AWS `c8g.24xlarge` instance for demonstration. Any sufficiently large instance on your chosen provider will work, however, smaller instances may take longer or risk running out of memory during compilation.  If you choose to use a different instance type, the minimal requirements are an Arm instance running at least 24 vCPUs with 200 GB of free storage.

### Operating System ###
Ubuntu 24.04 LTS (64-bit Arm) is the recommended OS for this guide. Other distributions may work but are not officially supported (yet).  If you find a different distro that works well, or you'd like to request support for a different setup, please open an issue or pull request.

# Install and Clone

With your build instance running and accessible via SSH, install the required dependencies:

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv build-essential bc rsync dwarves flex bison libssl-dev libelf-dev btop yq jq

cd
git clone https://github.com/geremyCohen/arm_kernel_install_guide.git ~/arm_kernel_install_guide
cd ~/arm_kernel_install_guide
chmod +x scripts/*.sh
```

All commands in this guide assume you are inside this directory. The important script is `scripts/kernel_build_and_install.sh`, which orchestrates cloning the upstream kernel tree, configuring tuxmake, building artifacts, and optionally installing the kernel. The script now runs non-interactively—once invoked it proceeds without confirmation prompts, and any install operation automatically reboots the system when it finishes.

## How do I build Arm kernels?

The `kernel_build_and_install.sh` script is intentionally modular. Most users fall into two buckets:

1. **General Usage (non-fastpath)** – build kernels for direct install or downstream packaging.
2. **Fastpath Usage** – build kernels that add the *fastpath* headers/perf configuration needed by the *fastpath* validation tool. Aside from those extra configs, the workflow mirrors the general case.

The sections below start simple (demo flags) and progress toward advanced scenarios. Every flag referenced is shown in at least one example so you can mix and match confidently.

### Flag overview

#### General usage flags

| Flag | Description |
| --- | --- |
| `--demo-default-build` | Shortcut: builds `v6.18.1` with default configs and leaves *fastpath* disabled. |
| `--tag <tag>` / `--tags <list>` / `--tag-latest` | Select one or more kernel tags. Multiple tags build in parallel; the latest stable release can be added via `--tag-latest`. |
| `--install-from <dir>` / `--install-format <flat\|deb\|auto>` | Install an existing build (flat artifacts or `.deb` packages) without recompiling. |
| `--dry-run` | Generate a self-contained plan script (stored in `/tmp/kernel_plan_*.sh`) with the resolved arguments and exit without running the build. |
| `--kernel-install [tag\|bool]` | Install a kernel right after it finishes building. When multiple tags build, provide the specific tag to install. |
| `--change-to-64k <bool>` | Generate a 64 KB page-size kernel. Often combined with the install flags to test high-page builds. |
| `--config-file <path>` | Reuse a captured stock config instead of `/boot/config-$(uname -r)`. |
| `--include-bindeb-pkg` | Adds the `bindeb-pkg` target so `.deb` packages are produced alongside `Image.gz` and `modules.tar.xz`. |
| `--kernel-command-line <string>` | Override GRUB’s `GRUB_CMDLINE_LINUX` when installing a kernel. |
| `--append-to-kernel-version <text>` | Attach custom suffixes to `EXTRAVERSION` (e.g., `--append "-lab"`). |
| `--kernel-dir <path>` / `--venv-path <path>` | Control where the kernel git checkout lives and which Python venv hosts tuxmake. Build artifacts always land under `~/kernels/<tag>`. |

#### Fastpath usage flags

| Flag | Description |
| --- | --- |
| `--demo-fastpath-build` | Shortcut: builds `v6.18.1` and `v6.19-rc1` with *fastpath* configs enabled. |
| `--fastpath <bool>` | Manually enable/disable the *fastpath* configuration overlay (installs Docker as needed). |

Run `./scripts/kernel_build_and_install.sh --help` anytime for the exhaustive list.

---

## General Usage

### Worked examples (general usage)

#### 1. Quick sanity check (demo)
```bash
./scripts/kernel_build_and_install.sh --demo-default-build
```
This demo builds `v6.18.1`, populates `~/kernels/6.18.1`, and leaves Docker as well as *fastpath* configs untouched.

#### 2. Specify your own tag
```bash
./scripts/kernel_build_and_install.sh --tags v6.19-rc1
```
This behaves like the demo while targeting a release candidate instead of the pinned stable tag, and it still runs without any interactive prompts.

#### 3. Produce both flat artifacts and Debian packages
```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --include-bindeb-pkg
```
Running this command outputs `Image.gz`, `modules.tar.xz`, `perf.tar.xz`, and `.deb` files (headers, image, dbg) under `~/kernels/6.18.1`.

#### 4. Build and immediately install (single tag)
```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --kernel-install true
```
This command installs the freshly built kernel, regenerates initramfs, updates GRUB, and then reboots automatically.

#### 5. Multi-tag build + targeted install
```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1,v6.19-rc1 \
  --kernel-install v6.18.1
```
Both kernels build in parallel, but only `v6.18.1` is installed (followed by an automatic reboot), leaving the `v6.19-rc1` artifacts untouched under `~/kernels`.

#### 6. 64K page-size build and install
```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --change-to-64k true \
  --kernel-install true \
  --append-to-kernel-version "-64k"
```
This variation produces a 64 KB build, installs it, appends “-64k” to the reported kernel version, and reboots automatically so you can verify the new settings.

#### 7. Install-only workflow (reusing flat artifacts)
```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1 \
  --install-format flat
```
Instead of compiling, the script installs the saved `Image.gz`, `modules.tar.xz`, and `config` from a prior run, which is ideal when the directory contains flat artifacts rather than `.deb` packages.

#### 8. Install-only with Debian packages
```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1 \
  --install-format deb
```
Here the script installs the `.deb` artifacts produced earlier via `--include-bindeb-pkg`, expecting files such as `linux-image-*` and `linux-headers-*` to exist in the source directory.

#### 9. Install-only with auto-detection
```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1
```
This form lets the script auto-detect whether the directory contains flat artifacts or `.deb` files, which simplifies reuse when you are not sure which format is present.

#### 10. Generate a runnable plan without executing
```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --dry-run
```
Instead of performing the build, this command writes a self-contained plan such as `/tmp/kernel_plan_v6.18.1_<hash>.sh` that embeds the current script plus the resolved arguments (minus `--dry-run`). Running that plan file later—on the same host or another system with the required dependencies—replays the exact workflow.

---

## Fastpath Usage

*fastpath* builds use the same tuxmake pipelines but add a configuration fragment that exposes the interfaces needed by the *fastpath* testing framework (extra headers, perf tooling, and Docker so *fastpath* can drive the host). *fastpath* workflows are build-only: do not combine `--fastpath true` (or the demo shortcut) with `--kernel-install` or any `--install-from` commands. Instead, let the build finish, copy the flat artifacts (`Image.gz`, `modules.tar.xz`, and `config`) to the *fastpath* host, and let the *fastpath* tooling handle deployment to the SUT. Docker is still installed automatically whenever *fastpath* mode is enabled so the *fastpath* controller can manage the host.

*fastpath* runs can still take advantage of tuning flags such as `--change-to-64k`, alternate configs, or custom output directories. Even if you specify packaging flags such as `--include-bindeb-pkg`, *fastpath* tests consume the flat artifacts.

### Fastpath examples

#### 1. Demo (dual-tag baseline)
```bash
./scripts/kernel_build_and_install.sh --demo-fastpath-build
```
The demo builds `v6.18.1` and `v6.19-rc1` with *fastpath* configs enabled and installs Docker automatically if the host lacks it.

#### 2. Custom tags with Fastpath enabled
```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1,v6.19-rc1 \
  --fastpath true
```
This explicit version mirrors the demo while making it easy to swap tag sets or add additional flags.

#### 3. Fastpath build with additional tuning
```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1,v6.19-rc1 \
  --fastpath true \
  --change-to-64k true
```
This variation still produces build-only artifacts, but it proves that you can layer other build-time options (like a 64 KB page size) on top of *fastpath* runs before exporting the results to the *fastpath* host.

---

### Where are the artifacts stored?

Each kernel tag produces a directory under `~/kernels/<kernel_version>` containing:

- `Image.gz` – compressed kernel image.
- `modules.tar.xz` – modules tree (untar to `/lib/modules/<version>` when installing elsewhere).
- `perf.tar.xz`, `cpupower.tar.xz` – optional user-space tools.
- `config` – final merged configuration.
- `config.stock` – copy of the original base config used for the build.

The script also writes a copy of the base config to `~/kernels/stock-configs/`, named after the running host kernel. Preserve this directory if you want to reuse the stock configuration later (for example, pass it via `--config-file`).

### How do I verify the results?

After every run:

```bash
ls ~/kernels
ls ~/kernels/<version>
```

If you installed the kernel, the script reboots automatically when the install finishes. After it comes back up, confirm:

```bash
uname -r
getconf PAGE_SIZE        # expect 65536 for 64K builds, 4096 otherwise
```

When using build-only workflows, copy `Image.gz`, `modules.tar.xz`, and the corresponding `config` file to the downstream environment that will consume the kernel.
