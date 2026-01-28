---
title: Build and install custom Linux kernels
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Standard kernel workflows

Standard kernel builds produce general-purpose kernels suitable for production deployment, development testing, or distribution packaging. These workflows let you build specific versions, install them directly, or package them for later use.

This section covers standard kernel build workflows for direct installation or downstream packaging.

{{% notice Note on kernel build only %}}
The kernel versions given in the \--tags flag, such as `v6.18.1` in the first example below, are arbitrary (but valid) Linux kernel versions. If you prefer to use kernel versions different from the examples, you can replace them with your preferred versions.

Kernel.org hosts all official Linux kernel releases: https://www.kernel.org/. Browse and select any stable or mainline release version.
{{% /notice %}}


### Build a specific kernel version

To begin, start with a minimal argument example to build a specific kernel version.  In this example, `v6.18.1` is used:

```bash
./scripts/kernel_build_and_install.sh --tags v6.18.1
```

This builds kernel v6.18.1 in flat-file format, and writes the artifacts to ~/kernels/v6.18.1.  Because we don't specify the --kernel-install flag (which is default false), it will only build, and not automatically install this kernel to the system.


### Produce Debian packages

Use Debian packages when you need to:
- Deploy to multiple systems using package management
- Track kernel installations with dpkg
- Simplify dependency management for downstream users

This example builds both flat artifacts and Debian packages for easier distribution:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --include-bindeb-pkg
```

This command outputs `Image.gz`, `modules.tar.xz`, `perf.tar.xz`, and `.deb` files (headers, image, dbg) under `~/kernels/v6.18.1`.



### Generate a build plan without executing (dry-run)

Use dry-run mode to:
- Document your build configuration
- Share build recipes with team members
- Reproduce builds on different systems
- Test configuration changes before execution

This command writes a self-contained plan such as `/tmp/kernel_plan_v6.18.1_<hash>.sh` that embeds the current script plus the resolved arguments (minus `--dry-run`):

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --dry-run
```

Run the plan file later—on the same host or another system with the required dependencies—to replay the exact workflow. Replace `<hash>` with the actual hash value from your generated plan file:

```bash
bash /tmp/kernel_plan_v6.18.1_<hash>.sh
```

You can use tab completion or `ls /tmp/kernel_plan_*.sh` to find the exact filename.

## Install kernel

{{% notice Note %}}
The following sections demonstrate build and install scenarios.  

*Before and after* any install-related command, use the linux command `uname -r` to verify the current version of the kernel you are running so you can compare kernel versions (before and after) to confirm the new kernel is properly installed.

Also remember that installing a new kernel requires a system reboot to take effect.
{{% /notice %}}

### Build and install a kernel

Build a kernel and immediately install it:

First, take note of the current kernel version:

```bash
uname -r
```

Make a note of that value so you can compare it after the new kernel is installed and the system reboots.

Next, perform a build and install of kernel version `v6.18.1`:

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

The output shows the newly installed kernel version.  Compare it to the value gathered before the install to confirm the update was successful.

### Build multiple kernel versions

This approach is useful when you want to:
- Compare different kernel versions
- Prepare multiple kernels for testing
- Build a library of kernel versions for deployment

To build two kernel versions in parallel, run the following command (it will build both `v6.18.1` and `v6.19-rc1`, but only install `v6.18.1`):

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1,v6.19-rc1 \
  --kernel-install v6.18.1
```

Both kernels build in parallel, but only `v6.18.1` installs (followed by an automatic reboot), leaving the `v6.19-rc1` artifacts untouched under `~/kernels`.


### Build a 64 KB page-size kernel

{{% notice Note %}}
Memory page size affects how the operating system manages memory.  The default page size is typically 4 KB, but certain workloads can benefit from larger page sizes, such as 64 KB.  Make sure to test compatibility with your applications before changing memory page size.
{{% /notice %}}

In this example, you will create and install a kernel with 64 KB pages instead of the standard 4 KB.  This variation produces a 64 KB build, installs it, appends "-64k" to the reported kernel version, and reboots automatically:


```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1 \
  --change-to-64k true \
  --kernel-install true \
  --append-to-kernel-version "-64k"
```

After reboot, verify the page size:

```bash
getconf PAGE_SIZE
```

The expected output is `65536` for 64 KB builds, compared to `4096` for standard builds.

### Install previously built kernels

There are two input formats for kernel artifacts that match the build output formats: flat files and Debian packages. Choose the appropriate installation method based on your prior build format.

#### Flat-file installation

This installs the saved `Image.gz`, `modules.tar.xz`, and `config` from a prior build run. Use this when the directory contains flat artifacts rather than `.deb` packages.

To install flat-file kernel artifacts without recompiling:

```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1 \
  --install-format flat
```
Upon completion, the script installs the kernel, regenerates initramfs, updates GRUB, and reboots the system.

#### Debian package installation:

To install from previously built Debian packages (`.deb` files):

```bash
./scripts/kernel_build_and_install.sh \
  --install-from ~/kernels/6.18.1 \
  --install-format deb
```

This installs the `.deb` artifacts produced earlier via `--include-bindeb-pkg`, expecting files such as `linux-image-*` and `linux-headers-*` to exist in the source directory.

## What you've accomplished and what's next

In this section, you've learned how to:
- Build standard Linux kernels for Arm instances
- Create kernels with different page sizes
- Produce both flat artifacts and Debian packages
- Install kernels automatically with system reboots
- Build multiple kernel versions in parallel
- Reuse existing build artifacts

The next section covers Fastpath kernel builds, which add configuration overlays needed for validation testing.
