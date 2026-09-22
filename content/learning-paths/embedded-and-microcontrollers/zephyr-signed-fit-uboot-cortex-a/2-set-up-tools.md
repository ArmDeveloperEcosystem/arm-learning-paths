---
title: Set up the host tools for your target
description: Install the Ubuntu packages, get the U-Boot source and cross compiler for your target, from the U-Boot project for QEMU or from the vendor SDK for the AM62L EVM, and create the environment file that every later page of this Learning Path loads.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you need

Whichever target you chose, you need a U-Boot source tree that supports it and a cross compiler that builds U-Boot. For QEMU, the U-Boot release and two Ubuntu packages are everything. On the TI [AM62L EVM](https://www.ti.com/tool/TMDS62LEVM) you also need the prebuilt firmware that runs before U-Boot, and all three come in one installer, the TI Processor SDK.

You build Zephyr with [Workbench for Zephyr](https://z-workbench.com/), an open-source [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=Ac6.zephyr-workbench) by Ac6. Follow [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/) up to and including its section *Install the required host tools*, then come back here. Skip its toolchain and workspace steps; you add a Cortex-A toolchain and workspace when you [build the Zephyr image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).

## Install the host packages

U-Boot's build and the signing tools need a few packages beyond a normal Zephyr setup. Install them in one command:

```bash
sudo apt install -y build-essential bison flex swig python3-dev python3-setuptools libssl-dev libgnutls28-dev uuid-dev device-tree-compiler openssl mtools dosfstools xz-utils curl picocom
```

On QEMU, add the emulator and a cross compiler; the AM62L EVM gets both from the TI SDK instead, so skip this command if you are on the board:

```bash
sudo apt install -y qemu-system-arm gcc-aarch64-linux-gnu
```

## Create the working directory and environment file

Every path in this Learning Path lives under `$HOME/zephyr-secure-boot`, and every page reads the same variables from a file inside it. Write the file for your target, then load it and create the directories the later pages write into:

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
```bash
mkdir -p $HOME/zephyr-secure-boot
cat > $HOME/zephyr-secure-boot/env-qemu.sh <<'EOF'
export WORK=$HOME/zephyr-secure-boot

# Target values
export BOARD=qemu_cortex_a53                  # Zephyr board identifier
export ZEPHYR_ADDR=0x40000000                 # Zephyr link address, FIT load and go target
export FIT_ADDR=0x48000000                    # where U-Boot loads the FIT, clear of ZEPHYR_ADDR
export BOOT_DEV="virtio 0:1"                  # U-Boot device and partition that hold the files
export UBOOT_DEFCONFIG=qemu_arm64_defconfig   # the target's U-Boot configuration

# No vendor SDK: U-Boot from the U-Boot project, cross compiler from Ubuntu
export UBOOT_SRC=$WORK/u-boot-2025.07
export CROSS=aarch64-linux-gnu-
export UBOOT_CC="${CROSS}gcc"

# Your build outputs: U-Boot build, signing keys, signed FITs, and the boot volume
export UBOOT_OUT=$WORK/uboot-build
export KEYS=$WORK/keys
export FIT=$WORK/fit
export BOOT_IMG=$WORK/disk.img@@1048576
EOF
source $HOME/zephyr-secure-boot/env-qemu.sh
mkdir -p $KEYS $FIT
```
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
```bash
mkdir -p $HOME/zephyr-secure-boot
cat > $HOME/zephyr-secure-boot/env-am62l.sh <<'EOF'
export WORK=$HOME/zephyr-secure-boot

# Target values
export BOARD=am62l_evm/am62l3/a53             # Zephyr board identifier
export ZEPHYR_ADDR=0x82000000                 # Zephyr link address, FIT load and go target
export FIT_ADDR=0x90000000                    # where U-Boot loads the FIT, clear of ZEPHYR_ADDR
export BOOT_DEV="mmc 1:1"                     # U-Boot device and partition that hold the files
export UBOOT_DEFCONFIG=am62lx_evm_defconfig   # the target's U-Boot configuration

# Vendor SDK: U-Boot source, firmware that runs before U-Boot, cross compiler and its libraries
export SDK=$WORK/tisdk
export UBOOT_SRC=$SDK/board-support/ti-u-boot-2026.01+git
export PREBUILT=$SDK/board-support/prebuilt-images/am62lxx-evm
export CROSS=$SDK/linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-
export SYSROOT=$SDK/linux-devkit/sysroots/aarch64-oe-linux
export UBOOT_CC="${CROSS}gcc --sysroot=$SYSROOT"

# Your build outputs: U-Boot build, signing keys, signed FITs, and the boot volume
export UBOOT_OUT=$WORK/uboot-build
export KEYS=$WORK/keys
export FIT=$WORK/fit
export BOOT_IMG=$WORK/sdcard.img@@1048576
EOF
source $HOME/zephyr-secure-boot/env-am62l.sh
mkdir -p $KEYS $FIT
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Only the `# Target values` block and the paths under it depend on the target; for another board, copy `env-am62l.sh`, change those, and leave the rest as it is. [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) says where each value comes from. The variables live only in the shell that loaded them, so every later page starts by loading your file again.

## Get the U-Boot source and the cross compiler

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
There is no vendor SDK. Download the U-Boot release from the U-Boot project and unpack it into your working directory; the archive is about 32 MB:

```bash
curl -L -o $WORK/u-boot-2025.07.tar.bz2 https://ftp.denx.de/pub/u-boot/u-boot-2025.07.tar.bz2
tar -xf $WORK/u-boot-2025.07.tar.bz2 -C $WORK
ls -d $UBOOT_SRC
```

The expected output is:

```output
/home/user/zephyr-secure-boot/u-boot-2025.07
```

The source stays unpatched: the key and the boot command are configuration. Check that the compiler you installed above runs:

```bash
${CROSS}gcc --version
```

The output is similar to:

```output
aarch64-linux-gnu-gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
...
```

`qemu-system-aarch64 --version` prints the emulator's version; this Learning Path uses only long-standing QEMU options, so any recent version works.

There is no card image to download: you build a 64 MiB disk image from nothing when you [boot the target](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-target/).
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
The U-Boot source, the firmware that runs before U-Boot and the cross compiler all come from the TI Processor SDK Linux for AM62Lx; you use nothing from Linux itself. The installer is 4.5 GB and unpacks to 11 GB. Download it from the [TI download page](https://www.ti.com/tool/download/AM62L-LINUX-SDK/12.01.00.05.03):

```bash
curl -L -o $WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin
```

Make it executable and run it without the graphical wizard. `--mode unattended` accepts every default, and `--prefix` installs into `$SDK` without root:

```bash
chmod +x $WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin
$WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin --mode unattended --prefix $SDK
```

Check that the three paths exist and the compiler runs:

```bash
ls -d $UBOOT_SRC $PREBUILT $SYSROOT
${CROSS}gcc --version
```

The output is similar to:

```output
/home/user/zephyr-secure-boot/tisdk/board-support/prebuilt-images/am62lxx-evm
/home/user/zephyr-secure-boot/tisdk/board-support/ti-u-boot-2026.01+git
/home/user/zephyr-secure-boot/tisdk/linux-devkit/sysroots/aarch64-oe-linux
aarch64-oe-linux-gcc (GCC) 15.3.0
...
```

The boot ROM only accepts a card laid out the way it expects, so you start from TI's own SD card image and replace the files inside. Download it; it is about 1.3 GB and stays compressed, because the boot page reads the part it needs straight out of `xz`:

```bash
curl -L -o $WORK/tisdk-default-image.wic.xz https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/tisdk-default-image-am62lxx-evm-12.01.00.05.03.rootfs.wic.xz
```
  {{< /tab >}}
{{< /tabpane-normal >}}

## What you've accomplished and what's next

Your host has the build packages, the U-Boot source for your target, its cross compiler, and an environment file with every path. Next, you [build a small Zephyr application for your target](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).
