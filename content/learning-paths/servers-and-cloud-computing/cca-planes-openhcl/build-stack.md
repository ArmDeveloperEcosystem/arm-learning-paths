---
# User change
title: "Build the planes-enabled stack"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---

## Install host packages

Use Ubuntu 24.04 LTS for the host system. Install the packages needed by the CCA development platform, Shrinkwrap, Docker, and the prototype builds:

```console
sudo apt update
sudo apt upgrade
sudo apt install build-essential cmake ninja-build python3-venv ccache git \
    parted e2fsprogs docker.io netcat-openbsd telnet net-tools docker-buildx \
    flex libssl-dev gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
```

These commands require `sudo` access. If you are using a shared host where you do not have passwordless `sudo`, ask the administrator to install the packages or use a host where they are already
present.

Add your user to the `docker` group:

```console
sudo usermod -aG docker $USER
newgrp docker
```

Check that Docker is available:

```console
docker ps
```

## Clone and initialize the CCA development platform

Clone the CCA development platform repository:

```console
mkdir -p $HOME/cca-planes-workbook
cd $HOME/cca-planes-workbook
git clone --branch planes https://github.com/EllieRoe/CCA-dev-platform.git CCA-dev-platform
cd CCA-dev-platform
```

This command must complete without prompting for GitHub credentials before the Learning Path is ready for publication. If GitHub prompts for credentials, the repository is still unavailable through
public HTTPS access.

Set up the build environment:

```console
source setup.source_me
```

This command creates a Python virtual environment, installs the Python packages needed by Shrinkwrap, and sets the `SHRINKWRAP_*` environment variables. The package installation step needs network
access to Python package indexes unless the host already has a populated virtual environment.

## Create the planes Shrinkwrap overlays

The CCA development platform README describes the base Learning Path build with `cca-lp.yaml`. The OpenHCL prototype also needs a planes overlay. Create a Learning Path overlay that keeps the base
filesystem and tooling changes from `cca-lp.yaml`, while omitting the `kvmtool.yaml` layer that applies `config/lkvm.patch`:

```console
cat > config/cca-planes-lp.yaml <<'EOF'
# Copyright (c) 2026, Arm Limited.
# SPDX-License-Identifier: MIT

%YAML 1.2
---
description: >-
  Generates all blobs for the CCA planes Learning Path while avoiding the
  kvmtool patch layer used by the base CCA Learning Path overlay.

concrete: true

layers:
  - buildroot-cca.yaml
  - bootsync.yaml
  - cca-kata.yaml
  - edk2.yaml

build:

  linux:
    prebuild:
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_VIRT_DRIVERS
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_ARM_FFA_TRANSPORT
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_ARM_CCA_GUEST
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_TSM_REPORTS
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_TRACEPOINTS
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_TRACING
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_FTRACE
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_FUNCTION_TRACER
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_FUNCTION_GRAPH_TRACER
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_DYNAMIC_FTRACE
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_TRACE_EVENTS
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_BLOCK
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_BLK_DEV_IO_TRACE
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_EVENT_TRACING
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_BLOCK_HOLDER_TRACKING
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_BLK_DEV_BOUNCE
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_PERF_EVENTS
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_PERF_USE_VMALLOC
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_PRINTK
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_DEBUG_KERNEL
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_DEBUG_FS
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_DEBUG_INFO

  buildroot:
    repo:
      revision: 2026.02

    prebuild:
      - ./utils/config --file ${param:builddir}/.config --set-str BR2_ROOTFS_POST_BUILD_SCRIPT ${param:configdir}/../realm-post-build-lp.sh
      - ./utils/config --file ${param:builddir}/.config --set-str TARGET_GENERIC_HOSTNAME "realm"
      - ./utils/config --file ${param:builddir}/.config --set-str TARGET_GENERIC_ISSUE "Welcome to the CCA realm"
      - ./utils/config --file ${param:builddir}/.config --disable BR2_PACKAGE_OPTEE_EXAMPLES
      - ./utils/config --file ${param:builddir}/.config --disable BR2_PACKAGE_OPTEE_TEST
      - ./utils/config --file ${param:builddir}/.config --disable BR2_PACKAGE_OPTEE_CLIENT
      - ./utils/config --file ${param:builddir}/.config --disable BR2_PACKAGE_TRACE_CMD
      - ./utils/config --file ${param:builddir}/.config --enable BR2_PACKAGE_LIBOPENSSL_BIN
      - ./utils/config --file ${param:builddir}/.config --enable BR2_PACKAGE_LIBOPENSSL_ENGINES

  rmm:
    params:
      -DRMM_V1_1: 1
      -DRMM_MEM_SCRUB_METHOD: 2

  tfa:
    params:
      ENABLE_FEAT_MEC: 1

run:

  terminals:
    bp.terminal_0:
      type: telnet

    bp.terminal_1:
      type: telnet

    bp.terminal_2:
      type: telnet

    bp.terminal_3:
      type: telnet
EOF
```

Create the planes feature overlay. This overlay selects the prototype RMM, host Linux, and `kvmtool` branches, and enables Permission Indirection and Permission Overlay in the FVP parameters:

```console
cat > config/planes.yaml <<'EOF'
# Copyright (c) 2026, Arm Limited.
# SPDX-License-Identifier: MIT

%YAML 1.2
---
description: >-
  Overlay for the CCA planes OpenHCL prototype.

buildex:
  btvars:
    RMM_LOG_LEVEL:
      type: string
      value: '10'

    RMM_CONFIG:
      type: string
      value: 'fvp_defcfg'

    TFA_REVISION:
      type: string
      value: master

build:

  rmm:
    repo:
      remote: https://github.com/TF-RMM/tf-rmm.git
      revision: 9a98e8fcb1645b9917b2abd79212e6e3062e09fd

    params:
      -DLOG_LEVEL: ${btvar:RMM_LOG_LEVEL}
      -DRMM_CONFIG: ${btvar:RMM_CONFIG}
      -DRMM_V1_1: 1
      -DPLAT_CMN_CTX_MAX_XLAT_TABLES: 13

  tfa:
    repo:
      revision: ${btvar:TFA_REVISION}

    params:
      GIC_ENABLE_V4_EXTN: 1

  linux:
    repo:
      remote: https://gitlab.arm.com/linux-arm/linux-cca.git
      revision: cca/planes/rfc-v1

    prebuild:
      - export KBUILD_BUILD_TIMESTAMP="@$$(stat -c '%Y' ${param:sourcedir})"
      - ./scripts/config --file ${param:builddir}/.config --enable CONFIG_VIRT_DRIVERS
      - ./scripts/config --file ${param:builddir}/.config --disable CONFIG_HZ_250 --enable CONFIG_HZ_100
      - ./scripts/config --file ${param:builddir}/.config --disable CONFIG_RANDOMIZE_BASE

  kvmtool:
    repo:
      kvmtool:
        remote: https://gitlab.arm.com/linux-arm/kvmtool-cca.git
        revision: cca/planes/rfc-v1

run:
  params:
    -C cluster0.has_permission_indirection_s1: 2
    -C cluster1.has_permission_indirection_s1: 2
    -C cluster0.has_permission_indirection_s2: 2
    -C cluster1.has_permission_indirection_s2: 2
    -C cluster0.has_permission_overlay_s1: 2
    -C cluster1.has_permission_overlay_s1: 2
    -C cluster0.has_permission_overlay_s2: 2
    -C cluster1.has_permission_overlay_s2: 2
EOF
```

The `$$` in `$$(stat -c '%Y' ${param:sourcedir})` passes command substitution through Shrinkwrap so that the generated build script evaluates it.

{{% notice Warning %}}
Testing on Ubuntu 24.04 showed that `--overlay cca-lp.yaml --overlay planes.yaml` fails while applying `config/lkvm.patch` to `net/uip/tcp.c` in the planes-enabled `kvmtool` branch. Shrinkwrap appends
list values from later overlays, so adding another `kvmtool.prebuild` list in `planes.yaml` does not remove the inherited patch command. Use a planes-specific Learning Path overlay that excludes the
`kvmtool.yaml` layer, or update the CCA development platform so the patch is skipped for the planes branch.
{{% /notice %}}

Validate the merged Shrinkwrap configuration before starting the full build:

```console
shrinkwrap build cca-3world.yaml --overlay cca-planes-lp.yaml --overlay planes.yaml \
    --btvar GUEST_ROOTFS='${artifact:BUILDROOT}' --dry-run
```

The dry run prints the generated build script. If it reports a missing overlay, a malformed macro, or an unresolved repository setting, fix the overlay before you continue.

Build the CCA stack with the planes Learning Path overlay and the planes feature overlay:

```console
shrinkwrap build cca-3world.yaml --overlay cca-planes-lp.yaml --overlay planes.yaml \
    --btvar GUEST_ROOTFS='${artifact:BUILDROOT}'
```

## Build the plane 0 Linux kernel

Clone the OpenHCL Linux source and check out the branch used by the planes demo:

```console
cd $HOME/cca-planes-workbook
git clone --branch planes \
    http://atg-devlab-chimera.cambridge.arm.com:8080/fenimore-prototyping/openhcl-linux.git \
    openhcl-linux
cd openhcl-linux
```

The OpenHCL prototype notes recommend Arm GNU Toolchain 13.3.Rel1 for consistent results. The package installation step above installs Ubuntu's `aarch64-linux-gnu` GCC 13.3 cross compiler, which is
the compiler used by the commands below.

Configure the kernel for a Realm guest, 9P file sharing, and OpenHCL support:

```console
export ARCH=arm64
export CROSS_COMPILE=aarch64-linux-gnu-
make defconfig
./scripts/config --file .config --enable CONFIG_VIRT_DRIVERS --enable CONFIG_ARM_CCA_GUEST
./scripts/config --file .config --enable CONFIG_NET_9P --enable CONFIG_NET_9P_FD
./scripts/config --file .config --enable CONFIG_NET_9P_VIRTIO --enable CONFIG_NET_9P_FS
./scripts/config --file .config --enable CONFIG_HYPERV --enable CONFIG_HYPERV_MSHV
./scripts/config --file .config --enable CONFIG_MSHV --enable CONFIG_MSHV_VTL
./scripts/config --file .config --enable CONFIG_HYPERV_VTL_MODE
make olddefconfig
make Image -j$(nproc)
```

## Build the test microkernel and VMM

Clone the OpenVMM/OpenHCL source and check out the branch used by the planes demo:

```console
cd $HOME/cca-planes-workbook
git clone --branch cca-support \
    http://atg-devlab-chimera.cambridge.arm.com:8080/fenimore-prototyping/openhcl.git \
    openvmm
cd openvmm
```

Install the Rust targets used by the test microkernel and the VMM:

```console
rustup target add aarch64-unknown-linux-gnu
rustup target add aarch64-unknown-none
```

Build the binaries:

```console
unset ARCH
unset CROSS_COMPILE
RUSTC_BOOTSTRAP=1 cargo build -p simple_tmk --config openhcl/minimal_rt/aarch64-config.toml
RUSTC_BOOTSTRAP=1 cargo build -p tmk_vmm --target aarch64-unknown-linux-gnu
```

## Add the plane 0 kernel and test binaries to the root filesystem

Resize the root filesystem to make room for the prototype binaries:

```console
export CCA_PLANES_WORKDIR=$HOME/cca-planes-workbook
export PLANE0_IMAGE=$CCA_PLANES_WORKDIR/openhcl-linux/arch/arm64/boot/Image
export SIMPLE_TMK=$CCA_PLANES_WORKDIR/openvmm/target/aarch64-minimal_rt-none/debug/simple_tmk
export TMK_VMM=$CCA_PLANES_WORKDIR/openvmm/target/aarch64-unknown-linux-gnu/debug/tmk_vmm

cd $CCA_PLANES_WORKDIR/CCA-dev-platform
cd "$SHRINKWRAP_PACKAGE/cca-3world"
TOOLS_PATH="$SHRINKWRAP_BUILD/build/cca-3world/buildroot/host/sbin"
$TOOLS_PATH/e2fsck -fp rootfs.ext2
$TOOLS_PATH/resize2fs rootfs.ext2 1G
```

Mount the root filesystem:

```console
sudo mkdir -p mnt
sudo mount rootfs.ext2 mnt
sudo mkdir -p mnt/cca
```

Copy the files needed by plane 0:

```console
sudo cp guest-disk.img KVMTOOL_EFI.fd Image lkvm mnt/cca/
sudo cp "$PLANE0_IMAGE" mnt/cca/Image_ohcl
sudo cp "$SIMPLE_TMK" mnt/cca/
sudo cp "$TMK_VMM" mnt/cca/
sudo umount mnt
```

## What you've accomplished

You have built the planes-enabled CCA stack, the plane 0 Linux kernel, and the TMK test binaries. Next, boot the FVP and start the Realm.
