---
title: Build and install custom Linux kernels
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section covers standard kernel build workflows for direct installation or downstream packaging.

## Quick sanity check build

Start with a simple demo build to verify your environment:

```bash
./scripts/kernel_build_and_install.sh --demo-default-build
```

This demo builds `v6.18.1`, populates `~/kernels/6.18.1`, and leaves Docker and Fastpath configs untouched. The build takes approximately 30-45 minutes on a `m6g.12xlarge` instance.

The expected output shows:
- Kernel source cloning progress
- Configuration generation
- Compilation progress with CPU usage
- Final artifact locations

## Build a specific kernel version

Specify your own kernel tag:

```bash
./scripts/kernel_build_and_install.sh --tags v6.19-rc1
```

This behaves like the demo while targeting a release candidate instead of the pinned stable tag, and it runs without any interactive prompts.

## Produce Debian packages

Build both flat artifacts and Debian packages for easier distribution:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --include-bindeb-pkg
```

This command outputs `Image.gz`, `modules.tar.xz`, `perf.tar.xz`, and `.deb` files (headers, image, dbg) under `~/kernels/6.18.1`.

Use Debian packages when you need to:
- Deploy to multiple systems using package management
- Track kernel installations with dpkg
- Simplify dependency management for downstream users

## Build and install a kernel

Build a kernel and immediately install it:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --kernel-install true
```

This command installs the freshly built kernel, regenerates initramfs, updates GRUB, and then reboots automatically.

After the system comes back up, verify the new kernel:

```bash
uname -r
```

The output shows the newly installed kernel version.

## Build multiple kernel versions

Build several kernel versions in parallel:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1,v6.19-rc1 \
  --kernel-install v6.18.1
```

Both kernels build in parallel, but only `v6.18.1` installs (followed by an automatic reboot), leaving the `v6.19-rc1` artifacts untouched under `~/kernels`.

This approach is useful when you want to:
- Compare different kernel versions
- Prepare multiple kernels for testing
- Build a library of kernel versions for deployment

## Build a 64 KB page-size kernel

Create a kernel with 64 KB pages instead of the standard 4 KB:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --change-to-64k true \
  --kernel-install true \
  --append-to-kernel-version "-64k"
```

This variation produces a 64 KB build, installs it, appends "-64k" to the reported kernel version, and reboots automatically.

After reboot, verify the page size:

```bash
getconf PAGE_SIZE
```

The expected output is `65536` for 64 KB builds, compared to `4096` for standard builds.

Use 64 KB page sizes when:
- Working with large memory workloads
- Optimizing database performance
- Reducing TLB pressure on systems with large working sets

## Install a previously built kernel

Install kernel artifacts without recompiling:

```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1 \
  --install-format flat
```

This installs the saved `Image.gz`, `modules.tar.xz`, and `config` from a prior run. Use this when the directory contains flat artifacts rather than `.deb` packages.

For Debian package installation:

```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1 \
  --install-format deb
```

This installs the `.deb` artifacts produced earlier via `--include-bindeb-pkg`, expecting files such as `linux-image-*` and `linux-headers-*` to exist in the source directory.

For automatic format detection:

```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1
```

This lets the script auto-detect whether the directory contains flat artifacts or `.deb` files.

## Generate a build plan without executing

Create a reusable build plan without running the build:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --dry-run
```

This command writes a self-contained plan such as `/tmp/kernel_plan_v6.18.1_<hash>.sh` that embeds the current script plus the resolved arguments (minus `--dry-run`). 

Run the plan file later—on the same host or another system with the required dependencies—to replay the exact workflow:

```bash
bash /tmp/kernel_plan_v6.18.1_<hash>.sh
```

Use dry-run mode to:
- Document your build configuration
- Share build recipes with team members
- Reproduce builds on different systems
- Test configuration changes before execution

## Locate build artifacts

Each kernel tag produces a directory under `~/kernels/<kernel_version>` containing:

```bash
ls ~/kernels/6.18.1
```

The directory contains:
- `Image.gz` - Compressed kernel image
- `modules.tar.xz` - Modules tree (untar to `/lib/modules/<version>` when installing elsewhere)
- `perf.tar.xz`, `cpupower.tar.xz` - Optional user-space tools
- `config` - Final merged configuration
- `config.stock` - Copy of the original base config used for the build

The script also writes a copy of the base config to `~/kernels/stock-configs/`, named after the running host kernel. Preserve this directory if you want to reuse the stock configuration later (for example, pass it via `--config-file`).

## What you've accomplished and what's next

In this section, you've learned how to:
- Build standard Linux kernels for Arm instances
- Create kernels with different page sizes
- Produce both flat artifacts and Debian packages
- Install kernels automatically with system reboots
- Build multiple kernel versions in parallel
- Reuse existing build artifacts

The next section covers Fastpath kernel builds, which add configuration overlays needed for validation testing.
