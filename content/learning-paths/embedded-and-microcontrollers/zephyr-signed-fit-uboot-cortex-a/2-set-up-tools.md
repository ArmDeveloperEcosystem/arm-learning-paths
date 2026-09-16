---
title: Set up the host tools and the board's SDK
description: Install the Ubuntu packages, get the board's U-Boot source, early firmware and cross compiler from the vendor SDK, download the vendor's SD card image, and create the environment file that every later page of this Learning Path loads.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you need

From your board vendor you need three things: the U-Boot source tree for the board, the prebuilt firmware that runs before U-Boot, and the cross compiler that builds U-Boot. On the example board, the TI [AM62L EVM](https://www.ti.com/tool/TMDS62LEVM), all three come in one installer, the TI Processor SDK.

You build Zephyr with [Workbench for Zephyr](https://z-workbench.com/), an open-source [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=Ac6.zephyr-workbench) by Ac6. Follow [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/) up to and including its section *Install the required host tools*, then come back here. Skip its toolchain and workspace steps; you add a Cortex-A toolchain and workspace when you [build the Zephyr image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).

## Install the host packages

U-Boot's build and the signing tools need a few packages beyond a normal Zephyr setup. Install them in one command:

```bash
sudo apt install -y build-essential bison flex swig python3-dev python3-setuptools libssl-dev libgnutls28-dev uuid-dev device-tree-compiler openssl mtools xz-utils curl picocom
```

## Create the working directory and environment file

Every path in this Learning Path lives under `$HOME/zephyr-secure-boot`, and every page reads the same variables from a file inside it.

Create the directory and write the environment file:

```bash
mkdir -p $HOME/zephyr-secure-boot
cat > $HOME/zephyr-secure-boot/env.sh <<'EOF'
export WORK=$HOME/zephyr-secure-boot

# Board values
export BOARD=am62l_evm/am62l3/a53             # Zephyr board identifier
export ZEPHYR_ADDR=0x82000000                 # Zephyr link address, FIT load and go target
export FIT_ADDR=0x90000000                    # where U-Boot loads the FIT, clear of ZEPHYR_ADDR
export BOOT_DEV="mmc 1:1"                     # U-Boot device and partition that hold the files
export UBOOT_DEFCONFIG=am62lx_evm_defconfig   # the board's U-Boot configuration

# Vendor SDK: U-Boot source, firmware that runs before U-Boot, cross compiler and its libraries
export SDK=$WORK/tisdk
export UBOOT_SRC=$SDK/board-support/ti-u-boot-2026.01+git
export PREBUILT=$SDK/board-support/prebuilt-images/am62lxx-evm
export CROSS=$SDK/linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-
export SYSROOT=$SDK/linux-devkit/sysroots/aarch64-oe-linux

# Your build outputs: U-Boot build, signing keys, signed FITs
export UBOOT_OUT=$WORK/uboot-build
export KEYS=$WORK/keys
export FIT=$WORK/fit
EOF
```

Load the file and create the directories the later pages write into:

```bash
source $HOME/zephyr-secure-boot/env.sh
mkdir -p $KEYS $FIT
```

Only the `# Board values` and `# Vendor SDK` blocks depend on the board; for another board, change those and leave the rest of the file as it is. [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) says where each value comes from. The variables live only in the shell that loaded them, so every later page starts with `source $HOME/zephyr-secure-boot/env.sh`.

## Install the vendor SDK

Any vendor's SDK or BSP (board support package) has to give you the three pieces named above; point `UBOOT_SRC`, `PREBUILT`, `CROSS` and `SYSROOT` at them.

### Install the TI Processor SDK for the AM62L EVM

On the AM62L EVM, the three pieces come from the TI Processor SDK Linux for AM62Lx; you use nothing from Linux itself. The installer is 4.5 GB and unpacks to 11 GB. Download it from the [TI download page](https://www.ti.com/tool/download/AM62L-LINUX-SDK/12.01.00.05.03):

```bash
curl -L -o $WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin
```

Make it executable and run it without the graphical wizard:

```bash
chmod +x $WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin
$WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin --mode unattended --prefix $SDK
```

`--mode unattended` accepts every default, and `--prefix` installs into `$SDK` without root.

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

## Download the vendor's SD card image

The vendor's own SD card image has a layout the boot ROM is known to accept, so this Learning Path uses it as a template. For another board, download your vendor's image instead of the file below.

### Download TI's card image for the AM62L EVM

On the AM62L EVM, the image is TI's `.wic.xz` file. You don't boot Linux from it: you keep its first partition and replace the files inside.

Download it into the working directory:

```bash
curl -L -o $WORK/tisdk-default-image.wic.xz https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/tisdk-default-image-am62lxx-evm-12.01.00.05.03.rootfs.wic.xz
```

The compressed file is about 1.3 GB. Leave it compressed: the SD card page reads the part it needs straight out of `xz`.

## What you've accomplished and what's next

Your host has the build packages, the board's SDK, the vendor's card image, and `env.sh` with every path. Next, you [build a small Zephyr application for the board](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).
