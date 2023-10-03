---
# User change
title: Complete software stack

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Now that you understand the underlying concepts of how CCA works, we can move to a more realistic implementation, where isolated virtual machines are instantiated on the Arm `RD-Fremont` reference compute platform, available as a free-of-charge Fixed Virtual Platform (FVP).

Full documentation is available at [Arm Neoverse Reference Design Platform Software documentation](https://neoverse-reference-design.docs.arm.com/en/latest/index.html).

These instructions assume an AArch64 Ubuntu 22.04 Linux host, and was tested on a `m7g.metal` [AWS instance](../../../servers-and-cloud-computing/csp/aws/).

## Download and install the FVP

The FVP is available from the [Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) section of the Arm Developer website.

Locate the FVP under `Neoverse Infrastructure FVPs` > `Neoverse Fremont Reference Design FVP` > `Download RD-Fremont`, and click on `Download Linux - Arm Host`.

We shall be using the single chip system (`rdfremont`) for this example.

To install, accepting EULA and default settings, use:
```command
tar -xf FVP_RD_Fremont_11.22_16_Linux64_armv8l.tgz
./FVP_RD_Fremont.sh --no-interactive --i-agree-to-the-contained-eula
```

Further install instructions are available in the [Arm Ecosystem FVP](../../../../install-guides/fm_fvp/eco_fvp/) install guide.

Create an environment variable `MODEL` pointing to the FVP executable.
```command
export MODEL=/home/ubuntu/FVP_RD_Fremont/models/Linux64_armv8l_GCC-9.3/FVP_RD_Fremont
```

## Setup workspace

{{% notice Container based setup %}}
A Docker container based set up is also available.

Full instructions are given in the [documentation](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/common/setup-workspace.html).
{{% /notice %}}

Install necessary packages:
```command
sudo apt update
sudo apt install -y git repo
```

### Download the platform software

The entire software stack is available from the Arm Gitlab repository.

```command
mkdir rd-infra
cd rd-infra
repo init -u https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests.git -m pinned-rdfremont.xml -b refs/tags/RD-INFRA-2023.03.29
repo sync -c -j $(nproc) --fetch-submodules --force-sync
```

### Set up the build environment

A script is provided to install all necessary build dependencies.

```command
sudo ./build-scripts/rdinfra/install_prerequisites.sh
```

## Build the platform software

Build the necessary software packages to boot Linux on the single core FVP (`rdfremont`).

### Busybox

Building for Busybox is optional, but is a good way to verify that everything is set up correctly, as the build step is relatively fast.

To skip this step, proceed to [Buildroot boot](#buildroot).

#### Build

To build the stack, use:
```command
cd ~/rd-infra
./build-scripts/rdinfra/build-test-busybox.sh -p rdfremont all
```

#### Boot

To boot on the FVP use:
```command
cd model-scripts/rdinfra
./boot.sh -p rdfremont
```
{{% notice Note %}}
A number of `Info` and `Warning` messages will be emitted by the FVP. These can safely be ignored.

If you see an error of the form `xterm: Xt error: Can't open display:`, ensure that your terminal application (e.g. `PuTTY`) has `X11 forwarding` enabled.
{{% /notice %}}

The model will launch and after a short time a terminal window will open displaying output.
```output
[INF] Starting TF-M BL1_1
TP mode set complete, reset now.
Enabling secure provisioning mode
...
[INF] BL2 image validated successfully
[INF] Jumping to BL2
[INF] Starting bootloader
[INF] BL2: SCP pre load start
```
Use `Crtl+C` to shut down FVP.


### Buildroot boot {#buildroot}

`Buildroot boot` allows the use of `buildroot` as the filesystem and boot the software stack on the FVP.

#### Build

To build the stack use:
```command
cd ~/rd-infra
./build-scripts/rdinfra/build-test-buildroot.sh -p rdfremont all
```
{{% notice Note %}}
The build will take a significant time to complete.
{{% /notice %}}

#### Boot

To boot on the FVP use:
```command
cd model-scripts/rdinfra
./boot-buildroot.sh -p rdfremont
```

{{% notice Note %}}
A number of `Info` and `Warning` messages will be emitted by the FVP. These can safely be ignored.

If you see an error of the form `xterm: Xt error: Can't open display:`, ensure that your terminal application (e.g. `PuTTY`) has `X11 forwarding` enabled.
{{% /notice %}}

The model will launch and after a short time a terminal window will open displaying output.
```output
[INF] Starting TF-M BL1_1
TP mode set complete, reset now.
Enabling secure provisioning mode
...
[INF] BL2 image validated successfully
[INF] Jumping to BL2
[INF] Starting bootloader
[INF] BL2: SCP pre load start
```
{{% notice Note %}}
It will take a significant time to boot to the Linux log in prompt.

TO DO... I'm at 31 BILLION cycles and still nothing has happened...
{{% /notice %}}

## Realm KVM unit tests

See [here](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/rdfremont/docs/realm-test.html#rd-fremont-realm-test-label)
