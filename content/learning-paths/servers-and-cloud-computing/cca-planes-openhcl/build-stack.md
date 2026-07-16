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
    curl flex libssl-dev gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
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

## Verify the planes Shrinkwrap overlays

The `planes` branch provides the two overlays used by this Learning Path:

- `config/cca-planes-lp.yaml` keeps the base CCA Learning Path filesystem and
  tooling changes, while excluding the `kvmtool.yaml` layer that applies
  `config/lkvm.patch`.
- `config/planes.yaml` selects the prototype RMM, host Linux, and `kvmtool`
  branches, and enables Permission Indirection and Permission Overlay in the FVP
  parameters.

Check that both overlays are present:

```console
test -f config/cca-planes-lp.yaml
test -f config/planes.yaml
```

If either command fails, update the CCA development platform checkout to a
`planes` branch commit that includes both overlay files.

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

Install Rust 1.85.0 with `rustup`. The OpenVMM prototype branch is validated
with this Rust toolchain:

```console
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | \
    sh -s -- --default-toolchain=1.85.0 -y
source "$HOME/.cargo/env"
```

Install the Rust source component and the targets used by the test microkernel
and the VMM:

```console
rustup component add rust-src --toolchain 1.85.0
rustup target add aarch64-unknown-linux-gnu --toolchain 1.85.0
rustup target add aarch64-unknown-none --toolchain 1.85.0
```

Build the binaries:

```console
unset ARCH
unset CROSS_COMPILE
RUSTC_BOOTSTRAP=1 cargo +1.85.0 build -p simple_tmk \
    --config openhcl/minimal_rt/aarch64-config.toml
RUSTC_BOOTSTRAP=1 cargo +1.85.0 build -p tmk_vmm \
    --target aarch64-unknown-linux-gnu
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

Create `/cca` in the root filesystem image:

```console
$TOOLS_PATH/debugfs -w -R "mkdir /cca" rootfs.ext2
```

Copy the files needed by plane 0:

```console
$TOOLS_PATH/debugfs -w -R "write guest-disk.img /cca/guest-disk.img" rootfs.ext2
$TOOLS_PATH/debugfs -w -R "write KVMTOOL_EFI.fd /cca/KVMTOOL_EFI.fd" rootfs.ext2
$TOOLS_PATH/debugfs -w -R "write Image /cca/Image" rootfs.ext2
$TOOLS_PATH/debugfs -w -R "write lkvm /cca/lkvm" rootfs.ext2
$TOOLS_PATH/debugfs -w -R "write $PLANE0_IMAGE /cca/Image_ohcl" rootfs.ext2
$TOOLS_PATH/debugfs -w -R "write $SIMPLE_TMK /cca/simple_tmk" rootfs.ext2
$TOOLS_PATH/debugfs -w -R "write $TMK_VMM /cca/tmk_vmm" rootfs.ext2
```

Check that the files were copied and that the root filesystem is consistent:

```console
$TOOLS_PATH/debugfs -R "ls -l /cca" rootfs.ext2
$TOOLS_PATH/e2fsck -fn rootfs.ext2
```

## What you've accomplished

You have built the planes-enabled CCA stack, the plane 0 Linux kernel, and the TMK test binaries. Next, boot the FVP and start the Realm.
