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

These commands require `sudo` access. If you are using a shared host where you do not have passwordless `sudo`, ask the administrator to install the packages or use a host where they are already present.

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
git clone <CCA-dev-platform-public-repository> CCA-dev-platform
cd CCA-dev-platform
```

Set up the build environment:

```console
source setup.source_me
```

This command creates a Python virtual environment, installs the Python packages needed by Shrinkwrap, and sets the `SHRINKWRAP_*` environment variables. The package installation step needs network access to Python package indexes unless the host already has a populated virtual environment.

## Add the planes Shrinkwrap overlays

Before you build the stack, make sure that the planes overlays are available. The rest of this Learning Path depends on the published `cca-planes-lp.yaml` and `planes.yaml` files:

```console
test -f config/cca-planes-lp.yaml
test -f config/planes.yaml
```

The `cca-planes-lp.yaml` overlay must contain the base CCA Learning Path filesystem and tooling changes from `cca-lp.yaml`, without the `kvmtool.yaml` layer. The `kvmtool.yaml` layer applies `config/lkvm.patch` before building `kvmtool`. That patch is incompatible with the planes-enabled `kvmtool` branch that this prototype uses.

The planes overlay must configure the stack to:

- Build RMM with CCA v1.1 experimental features enabled.
- Build a Linux host with virtualization support needed by CCA.
- Build a `kvmtool` version that can create a Realm with at least one auxiliary plane.
- Enable Permission Indirection and Permission Overlay support in the FVP run parameters.

{{% notice Note %}}
This draft assumes that `cca-planes-lp.yaml` and `planes.yaml` are published with the demo repository before the Learning Path is published. If either `test` command fails, stop here and see the publication readiness page.
{{% /notice %}}

If the overlay uses shell command substitution in a Shrinkwrap command, escape the dollar sign as `$$`. For example, use `$$(stat -c '%Y' ${param:sourcedir})` instead of `$(stat -c '%Y' ${param:sourcedir})`.

{{% notice Warning %}}
Testing on Ubuntu 24.04 showed that `--overlay cca-lp.yaml --overlay planes.yaml` fails while applying `config/lkvm.patch` to `net/uip/tcp.c` in the planes-enabled `kvmtool` branch. Shrinkwrap appends list values from later overlays, so adding another `kvmtool.prebuild` list in `planes.yaml` does not remove the inherited patch command. Use a planes-specific Learning Path overlay that excludes the `kvmtool.yaml` layer, or update the CCA development platform so the patch is skipped for the planes branch.
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

Clone the public OpenHCL Linux source and check out the branch used by the planes demo:

```console
cd $HOME/cca-planes-workbook
git clone <OpenHCL-Linux-public-repository> openhcl-linux
cd openhcl-linux
git checkout <planes-demo-branch>
```

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

Clone the public OpenVMM/OpenHCL source and check out the branch used by the planes demo:

```console
cd $HOME/cca-planes-workbook
git clone <OpenVMM-public-repository> openvmm
cd openvmm
git checkout <planes-demo-branch>
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
