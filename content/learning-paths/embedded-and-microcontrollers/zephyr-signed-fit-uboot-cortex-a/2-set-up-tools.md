---
title: Set up the host tools and the TI SDK
description: Install the Ubuntu packages, the TI Processor SDK and TI's SD card image on your host, and create the environment file that every later page of this Learning Path loads.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you need

The board is the TI [AM62L EVM](https://www.ti.com/tool/TMDS62LEVM). It boots from a micro-SD card, so you need one and a way to write it from your host. The micro-USB connector **J7** is the serial console. It shows up on the host as four serial ports, and the console is the one named SoC UART0, which is usually, but not always, the first. You open it when you boot the board. Power comes from a USB-C supply that supports Power Delivery (PD), on **J17** or **J19**.

The host is an x86_64 PC running Ubuntu 22.04 or 24.04 with at least 20 GB of free disk space. TI ships the SDK installer and its cross compiler as x86_64 binaries, so an Arm host doesn't work here. The TI SDK download alone is 4.5 GB, and it unpacks to 11 GB of U-Boot source, Linux toolchain and prebuilt images. You can delete the installer after the install.

You also need a Zephyr workspace with Zephyr 4.4 or later and the Zephyr SDK. Set both up as described in the [Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html). This page doesn't repeat those steps.

From inside your Zephyr workspace (for example `cd ~/zephyrproject`, with its Python virtual environment active if you use one), check that the tree knows the board:

```bash
west boards | grep am62l
```

The expected output is:

```output
am62l_evm
```

If nothing prints, your Zephyr checkout doesn't have the board yet. Update it to 4.4 or later before you continue, because the board files set the address Zephyr is built to run at, and every later page uses that address.

## Install the host packages

U-Boot's build and the signing tools need a few packages beyond a normal Zephyr setup. Install them in one command:

```bash
sudo apt install -y build-essential bison flex swig python3-dev python3-setuptools libssl-dev libgnutls28-dev uuid-dev device-tree-compiler openssl mtools u-boot-tools xz-utils curl picocom
```

Six of them are for U-Boot and signing. `swig` and `python3-dev` let U-Boot build `pylibfdt`, the Python device tree library its build scripts import. `libssl-dev` gives `mkimage` the RSA code it signs with. `libgnutls28-dev` and `uuid-dev` are for `mkeficapsule`, a host tool TI's configuration builds next to `mkimage`; you don't use it, but the build stops without them. `device-tree-compiler` provides `dtc`, which converts device tree blobs to source and back; you use it to read the public key node out of a blob when you build U-Boot.

The rest are for the card and the console. `mtools` edits the SD card image without root, and `xz-utils` unpacks TI's card image. `openssl` creates the keys, `curl` downloads the two TI files, and `picocom` is the serial terminal.

`u-boot-tools` is optional. It installs Ubuntu's own `mkimage` as a fallback. You build `mkimage` from TI's U-Boot tree when you [create the signing keys and sign the image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/), so the tool that signs and the code that verifies come from the same source.

## Create the working directory and environment file

Every path in this Learning Path lives under one directory, `$HOME/zephyr-secure-boot`, and every page reads the same variables from a file inside it. That keeps the commands short, and you can paste them as they are.

Create the directory and write the environment file. The heredoc is quoted, so `$HOME` and `$WORK` stay as text in the file and expand when you load it:

```bash
mkdir -p $HOME/zephyr-secure-boot
cat > $HOME/zephyr-secure-boot/env.sh <<'EOF'
export WORK=$HOME/zephyr-secure-boot
export TISDK=$WORK/tisdk
export UBOOT_SRC=$TISDK/board-support/ti-u-boot-2026.01+git
export PREBUILT=$TISDK/board-support/prebuilt-images/am62lxx-evm
export CROSS=$TISDK/linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-
export SYSROOT=$TISDK/linux-devkit/sysroots/aarch64-oe-linux
export UBOOT_OUT=$WORK/uboot-build
export KEYS=$WORK/keys
export FIT=$WORK/fit
export ZEPHYR_ADDR=0x82000000
export FIT_ADDR=0x90000000
EOF
```

Load the file and create the directories the later pages write into:

```bash
source $HOME/zephyr-secure-boot/env.sh
mkdir -p $KEYS $FIT $WORK/app
```

The first group of variables points into the TI SDK, which you install next. `UBOOT_SRC` is the U-Boot source, `PREBUILT` holds the firmware that runs before U-Boot, and `CROSS` is the cross compiler prefix. `SYSROOT` is there because the SDK's compiler can't find its own libraries without `--sysroot`; the U-Boot pages pass it through the `CC` variable of `make`. `UBOOT_OUT` receives the U-Boot build, `KEYS` holds the signing keys, and `FIT` holds the signed images.

The two addresses come from the AM62L memory map. `ZEPHYR_ADDR` is where Zephyr is built to run, and `FIT_ADDR` is where U-Boot puts the signed image while it checks it. They must not overlap, because U-Boot copies Zephyr from one to the other. The later pages write the numbers out where they are used, in the FIT source and the boot command, and explain each use there. The variables keep them in one place to read.

The variables live only in the shell that loaded them. Every later page starts with `source $HOME/zephyr-secure-boot/env.sh`, and you need to run it again in each new terminal.

## Install the TI Processor SDK

The TI Processor SDK Linux for AM62Lx is TI's Linux distribution kit for the board. You use three things from it and nothing from Linux itself: the U-Boot source tree `ti-u-boot-2026.01+git`, the prebuilt firmware that runs before U-Boot, and the aarch64 GCC toolchain (GCC 15.3.0).

The prebuilt firmware is TF-A as `bl1.bin` and `bl31.bin`, OP-TEE 4.10 as `bl32.bin`, and TI's system firmware in the `ti-sysfw` directory. You met TF-A and OP-TEE on the previous page. `bl1.bin` is the first TF-A stage, and the U-Boot build packs it into `tiboot3.bin`; `bl31.bin` is the runtime part that hands over to U-Boot, and it goes into `tispl.bin`. You can build both from source, but these binaries are the ones inside TI's own image, so using them removes two builds and two places to get wrong.

Download the installer from the [TI download page](https://www.ti.com/tool/download/AM62L-LINUX-SDK/12.01.00.05.03). The direct link is the one in this command:

```bash
curl -L -o $WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin
```

The download takes a while. Then make it executable and run it without the graphical wizard:

```bash
chmod +x $WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin
$WORK/ti-processor-sdk-linux-am62lxx-evm-12.01.00.05.03-Linux-x86-Install.bin --mode unattended --prefix $TISDK
```

`--mode unattended` answers every prompt with its default, and `--prefix` sets the install directory to `$TISDK`, which is inside your working directory. The installer writes only there, so it doesn't need root.

Check that the three paths the later pages use exist, and that the compiler runs:

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

## Download TI's SD card image

The `.wic.xz` file is TI's complete SD card image: a boot partition and a Linux root filesystem, compressed with `xz`. You don't boot Linux from it. When you [prepare the SD card and boot the board](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/), you keep its first partition as a template and replace only the files inside. The AM62L boot ROM is picky about that partition's layout, and TI's layout is known to work.

Download it into the working directory:

```bash
curl -L -o $WORK/tisdk-default-image.wic.xz https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.01.00.05.03/tisdk-default-image-am62lxx-evm-12.01.00.05.03.rootfs.wic.xz
```

The compressed file is about 1.3 GB. Leave it compressed. That page reads the part it needs straight out of `xz`, so the full image never has to exist on disk.

## What you've accomplished and what's next

Your host now has the build packages and the TI SDK: U-Boot source, prebuilt firmware and toolchain. `$WORK/env.sh` holds every path, and every later page loads it with one `source` command. TI's card image is on disk, ready to serve as the boot partition template.

Next, you [build a small Zephyr application for the AM62L EVM](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/) and check that its binary starts with a branch instruction, so U-Boot's `go` command can start it.
