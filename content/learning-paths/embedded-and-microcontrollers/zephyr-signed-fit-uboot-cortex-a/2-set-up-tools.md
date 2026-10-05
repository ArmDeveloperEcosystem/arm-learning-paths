---
title: Set up the host tools for your target
description: Prepare an Ubuntu host with Zephyr build tools, U-Boot source, a cross compiler, and a shared environment file for QEMU or the TI AM62L EVM.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you need

You need Zephyr host tools, U-Boot source, and a cross compiler for your chosen target. For QEMU, you download U-Boot source and install the emulator and compiler from Ubuntu packages. For the AM62L EVM, the TI Processor SDK supplies U-Boot source, the cross compiler, and prebuilt early firmware.

## Install the Zephyr host tools

Open Visual Studio Code and select **Workbench for Zephyr** in the Activity Bar. In its panel, select **Install Host Tools** to install the dependencies used to build Zephyr: Python, CMake, Ninja, Git, Device Tree Compiler, and West.

When installation finishes, select **Verify Host Tools**. Resolve any missing-tool errors before continuing.

You’ll import the AArch64 toolchain and create the West workspace in the next lesson, before building Zephyr.

## Install the host packages

Install the additional packages used to build U-Boot, sign images, and prepare the boot media:

```bash
sudo apt install -y build-essential bison flex swig python3-dev python3-setuptools libssl-dev libgnutls28-dev uuid-dev device-tree-compiler openssl mtools dosfstools xz-utils curl picocom
```

If you chose QEMU, install the emulator and U-Boot cross compiler with this command. For the AM62L EVM, skip it; you’ll get the cross compiler from the TI SDK:

```bash
sudo apt install -y qemu-system-arm gcc-aarch64-linux-gnu
```

## Create the working directory and environment file

Keep your source, tools, and build outputs under `$HOME/zephyr-secure-boot`. An environment file stores the paths and target settings you’ll reuse throughout the workflow. Select your target’s tab, create and load its environment file, and create the signing-key and FIT directories:

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

The variables are available only in the shell where you load the environment file. Load it again whenever you open a new terminal; later lessons include a reminder. If you adapt the workflow to another board, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) explains how to choose its target values and paths.

{{% notice Note %}}
Example output shows paths under `/home/user/`, the home directory of the account that produced it. Your paths reflect your own username. On a standard Ubuntu cloud instance, for example, they appear under `/home/ubuntu/`. The commands use `$HOME` and `$WORK`, so they adapt to your account automatically, and only the printed paths differ.
{{% /notice %}}

## Get the U-Boot source and the cross compiler

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
Download U-Boot 2025.07 and unpack it into your working directory. The archive is about 32 MB:

```bash
curl -L -o $WORK/u-boot-2025.07.tar.bz2 https://ftp.denx.de/pub/u-boot/u-boot-2025.07.tar.bz2
tar -xf $WORK/u-boot-2025.07.tar.bz2 -C $WORK
ls -d $UBOOT_SRC
```

The expected output is:

```output
/home/user/zephyr-secure-boot/u-boot-2025.07
```

You’ll add the public key and boot command through build configuration, without patching U-Boot source. Check that the cross compiler runs:

```bash
${CROSS}gcc --version
```

The output is similar to:

```output
aarch64-linux-gnu-gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
...
```

Run `qemu-system-aarch64 --version` to check that the emulator is installed and report its version.

You’ll create a 64 MiB disk image when you prepare the boot media; you don’t need to download one for QEMU.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
The TI Processor SDK Linux for AM62Lx supplies U-Boot source, prebuilt early firmware, and the cross compiler. You use these components to boot Zephyr. The installer is 4.5 GB and unpacks to 11 GB. Download version 12.01.00.05.03 from the [TI Processor SDK download page](https://www.ti.com/tool/download/AM62L-LINUX-SDK/12.01.00.05.03):

```bash
curl -L -o $WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin
```

Make the installer executable and run it. `--mode unattended` uses the default settings without opening the graphical wizard. `--prefix` selects `$SDK` as the installation directory, without root privileges:

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

Download TI’s SD card image to preserve the boot partition layout expected by the AM62L boot ROM. The download is about 1.3 GB. Leave it compressed; when you prepare the boot media, you’ll extract the boot partition and replace its files:

```bash
curl -L -o $WORK/tisdk-default-image.wic.xz https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/tisdk-default-image-am62lxx-evm-12.01.00.05.03.rootfs.wic.xz
```
  {{< /tab >}}
{{< /tabpane-normal >}}

## What you've accomplished and what's next

You’ve installed the Zephyr host tools and U-Boot build packages, obtained your target’s U-Boot source and cross compiler, and created a reusable environment file. For the AM62L EVM, you also have the early firmware and SD card image. Next, you’ll import the AArch64 toolchain, create a West workspace, and build a small Zephyr application for your chosen target.
