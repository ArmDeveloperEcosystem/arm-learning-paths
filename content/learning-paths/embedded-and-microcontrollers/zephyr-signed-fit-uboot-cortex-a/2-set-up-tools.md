---
title: Set up the host tools and the board's SDK
description: Install the Ubuntu packages, get the board's U-Boot source, early firmware and cross compiler from the vendor SDK, download the vendor's SD card image, and create the environment file that every later page of this Learning Path loads.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you need

From your board vendor you need three things: the U-Boot source tree for the board, the prebuilt firmware that runs before U-Boot, and the cross compiler that builds U-Boot. On the example board, the TI [AM62L EVM](https://www.ti.com/tool/TMDS62LEVM), all three come in one installer, the TI Processor SDK.

The AM62L EVM boots from a micro-SD card, so you need one and a way to write it. The micro-USB connector **J7** is the serial console. It shows up on the host as four serial ports, and the console is the one named SoC UART0, usually the first. Power comes from a USB-C supply that supports Power Delivery (PD), on **J17** or **J19**.

The host is an x86_64 PC running Ubuntu 22.04 or 24.04 with about 20 GB of free disk space. TI ships the SDK installer and its cross compiler as x86_64 binaries, so an Arm host doesn't work here. The SDK download is 4.5 GB and unpacks to 11 GB.

You build Zephyr with Workbench for Zephyr, an open-source Visual Studio Code extension by Ac6. Follow [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/) up to and including its section *Install the required host tools*, then come back here. Skip its toolchain and workspace steps: a Cortex-A board needs an AArch64 toolchain, and the AM62L needs Zephyr 4.4 or later; you add both from Workbench when you [build the Zephyr image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).

## Install the host packages

U-Boot's build and the signing tools need a few packages beyond a normal Zephyr setup. Install them in one command:

```bash
sudo apt install -y build-essential bison flex swig python3-dev python3-setuptools libssl-dev libgnutls28-dev uuid-dev device-tree-compiler openssl mtools u-boot-tools xz-utils curl picocom
```

`swig` and `python3-dev` are for U-Boot's Python device tree bindings, `libssl-dev` gives `mkimage` its RSA code, `libgnutls28-dev` and `uuid-dev` are for a tool the AM62L configuration builds but you never use, and `device-tree-compiler` provides `dtc`. `mtools` edits the SD card image without root, `xz-utils` unpacks the vendor's card image, `openssl` creates the keys, `curl` downloads the SDK and the card image, and `picocom` is the serial terminal.

`u-boot-tools` is optional: it installs Ubuntu's own `mkimage` as a fallback, but you build `mkimage` from the board's U-Boot tree when you [create the signing keys and sign the image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/).

## Create the working directory and environment file

Every path in this Learning Path lives under `$HOME/zephyr-secure-boot`, and every page reads the same variables from a file inside it.

Create the directory and write the environment file. The heredoc (the `cat > ... <<'EOF'` block) is quoted, so `$HOME` and `$WORK` stay as text in the file and expand when you load it:

```bash
mkdir -p $HOME/zephyr-secure-boot
cat > $HOME/zephyr-secure-boot/env.sh <<'EOF'
export WORK=$HOME/zephyr-secure-boot

# Board values
export BOARD=am62l_evm/am62l3/a53
export ZEPHYR_ADDR=0x82000000
export FIT_ADDR=0x90000000
export BOOT_DEV="mmc 1:1"
export UBOOT_DEFCONFIG=am62lx_evm_defconfig

# Vendor SDK: U-Boot source, prebuilt early firmware, cross compiler
export SDK=$WORK/tisdk
export UBOOT_SRC=$SDK/board-support/ti-u-boot-2026.01+git
export PREBUILT=$SDK/board-support/prebuilt-images/am62lxx-evm
export CROSS=$SDK/linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-
export SYSROOT=$SDK/linux-devkit/sysroots/aarch64-oe-linux

# Your build outputs
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

The first block holds the board values. `BOARD` is the Zephyr board identifier. `ZEPHYR_ADDR` is where Zephyr is built to run, and `FIT_ADDR` is where U-Boot puts the signed image while it checks it; they must not overlap, because U-Boot copies Zephyr from one to the other. `BOOT_DEV` is the U-Boot device and partition that hold the files, and `UBOOT_DEFCONFIG` is the board's U-Boot configuration. To take this Learning Path to another board, you change this block and the vendor SDK block after it, and nothing else in the file; [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) says where each value comes from.

The second block points into the vendor SDK, which you install next. `UBOOT_SRC` is the U-Boot source, `PREBUILT` holds the firmware that runs before U-Boot, `CROSS` is the cross compiler prefix, and `SYSROOT` is the library path the SDK's compiler needs through `--sysroot`. The last block is yours: `UBOOT_OUT` receives the U-Boot build, `KEYS` holds the signing keys, and `FIT` holds the signed images.

The variables live only in the shell that loaded them, so every later page starts with `source $HOME/zephyr-secure-boot/env.sh`.

## Install the vendor SDK

Any vendor's SDK or BSP (board support package) has to give you the three pieces named above; point `UBOOT_SRC`, `PREBUILT`, `CROSS` and `SYSROOT` at them.

### Install the TI Processor SDK for the AM62L EVM

On the AM62L EVM, the three pieces come from the TI Processor SDK Linux for AM62Lx: the U-Boot source tree `ti-u-boot-2026.01+git`, the prebuilt firmware that runs before U-Boot, and the aarch64 GCC toolchain (GCC 15.3.0). You use nothing from Linux itself.

The prebuilt firmware is TF-A as `bl1.bin` and `bl31.bin`, OP-TEE 4.10 as `bl32.bin`, and TIFS, the SoC's security firmware from the boot chain page, in the `ti-sysfw` directory. These binaries are the ones inside TI's own image, so you don't build them.

Download the installer from the [TI download page](https://www.ti.com/tool/download/AM62L-LINUX-SDK/12.01.00.05.03):

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

{{% notice Note %}}
`prebuilt-images` also contains a directory named `am62lxx-evm-jailhouse`. Don't use it. Its firmware is built for the Jailhouse hypervisor memory layout, not for the one Zephyr and this Learning Path use. `PREBUILT` in `env.sh` already points at the right one.
{{% /notice %}}

## Download the vendor's SD card image

What a boot ROM reads from the card is vendor-specific: a file on a FAT partition on some SoCs, raw sectors at a fixed offset on others. The vendor's own SD card image is the one layout known to work, so this Learning Path uses it as a template. For another board, download the vendor's own SD card image instead of the file below.

### Download TI's card image for the AM62L EVM

On the AM62L EVM, that image is the `.wic.xz` file, TI's complete SD card image compressed with `xz`. You don't boot Linux from it. When you [prepare the SD card and boot the board](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/), you keep its first partition as a template and replace only the files inside.

Download it into the working directory:

```bash
curl -L -o $WORK/tisdk-default-image.wic.xz https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/tisdk-default-image-am62lxx-evm-12.01.00.05.03.rootfs.wic.xz
```

The compressed file is about 1.3 GB. Leave it compressed: the SD card page reads the part it needs straight out of `xz`.

## What you've accomplished and what's next

Your host now has the build packages and the board's SDK: U-Boot source, prebuilt firmware and toolchain. `$WORK/env.sh` holds the board values and every path, and the vendor's card image is on disk as the boot partition template.

Next, you [build a small Zephyr application for the board](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/) and check that its binary starts with a branch instruction, so U-Boot's `go` command can start it.
