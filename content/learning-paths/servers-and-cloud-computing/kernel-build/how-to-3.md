---
title: Build kernels for Fastpath validation
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Fastpath builds use the same TuxMake pipelines but add a configuration fragment that exposes the interfaces needed by the Fastpath testing framework. This includes extra headers, Linux Perf for performance profiling, and Docker so Fastpath can control and automate testing.

## Understand Fastpath workflows

Fastpath workflows are build-only: don't combine `--fastpath true` (or the demo shortcut) with `--kernel-install` or any `--install-from` commands. 

The proper workflow is:
- Build the kernel with Fastpath configuration enabled
- Copy the flat artifacts (`Image.gz`, `modules.tar.xz`, and `config`) to the Fastpath host
- Let the Fastpath tooling handle deployment to the SUT (System Under Test)

### Install Docker for Fastpath

Docker is required for Fastpath builds. The build script installs Docker automatically when you enable Fastpath mode, but you can also install it manually beforehand.

To install Docker manually, follow the [Docker Engine install guide](/install-guides/docker/docker-engine/).

After Docker is installed, the Fastpath controller can manage the host system.

Fastpath runs can still take advantage of tuning flags such as `--change-to-64k`, alternate configs, or custom output directories. Even if you specify packaging flags such as `--include-bindeb-pkg`, Fastpath tests consume the flat artifacts.

## Build with the Fastpath demo

Run the Fastpath demo to build two kernel versions:

```bash
./scripts/kernel_build_and_install.sh --demo-fastpath-build
```

This demo builds `v6.18.1` and `v6.19-rc1` with Fastpath configs enabled and installs Docker automatically if the host lacks it.

The build process:
- Clones both kernel versions
- Applies the Fastpath configuration overlay
- Compiles both versions in parallel
- Stores artifacts in separate directories under `~/kernels/`

## Build custom tags with Fastpath enabled

Specify your own kernel versions for Fastpath builds:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1,v6.19-rc1 \
  --fastpath true
```

This explicit version mirrors the demo while making it easy to swap tag sets or add additional flags.

## Combine Fastpath with other configurations

Layer additional build-time options on top of Fastpath runs:

```bash
./scripts/kernel_build_and_install.sh \
  --tags v6.18.1,v6.19-rc1 \
  --fastpath true \
  --change-to-64k true
```

This variation produces build-only artifacts with both Fastpath configuration and 64 KB page size enabled. Export the results to the Fastpath host for testing with large page configurations.

## Verify Docker installation

Check that Docker was installed as part of the Fastpath build:

```bash
docker --version
```

The expected output shows the Docker version installed on your system.

Fastpath requires Docker because:
- The Fastpath controller runs in containers
- Test workloads are containerized for isolation
- Docker provides consistent environments across test runs

## Copy artifacts to the Fastpath host

After the build completes, copy the required files to your Fastpath testing system:

```bash
scp ~/kernels/6.18.1/Image.gz user@fastpath-host:/path/to/kernels/
scp ~/kernels/6.18.1/modules.tar.xz user@fastpath-host:/path/to/kernels/
scp ~/kernels/6.18.1/config user@fastpath-host:/path/to/kernels/
```

Replace `user@fastpath-host` with your actual Fastpath host credentials and adjust the destination path as needed.

The Fastpath tooling on the remote host uses these artifacts to:
- Deploy the kernel to test systems
- Configure the test environment
- Execute validation test suites
- Collect performance metrics

## What you've accomplished

In this section, you've learned how to:
- Build kernels with Fastpath configuration enabled
- Combine Fastpath builds with other kernel options like 64 KB pages
- Prepare kernel artifacts for Fastpath validation testing
- Transfer build artifacts to Fastpath testing systems

You now have the skills to build custom Linux kernels for both general deployment and specialized validation workflows on Arm cloud instances.
