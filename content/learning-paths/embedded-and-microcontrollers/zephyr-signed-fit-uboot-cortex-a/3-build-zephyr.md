---
title: Build a Zephyr image that U-Boot can start
description: Use Workbench for Zephyr in VS Code to build a small Zephyr 4.4 application for a Cortex-A board, the TI AM62L EVM in this example, then check that the binary starts with a branch instruction that U-Boot's go command can jump to.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open Workbench for Zephyr

You build Zephyr with Workbench for Zephyr in VS Code, installed on the previous page. [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/) sets up a Cortex-M toolchain and workspace. This page does the same for a Cortex-A board: an AArch64 toolchain, and a Zephyr 4.4 workspace built from your board vendor's template, Texas Instruments here.

Open VS Code on your working directory:

```bash
code $HOME/zephyr-secure-boot
```

Then select the **Workbench for Zephyr** icon in the Activity Bar. The panel has one view each for **Applications**, **West workspaces**, **Toolchains** and **Host tools**.

{{% notice Note %}}
The screenshots were taken on Windows with the Zephyr SDK installed globally, so their paths start with `C:\Users\` and the SDK is tagged `[global]`; on your Ubuntu host the same fields take `/home/` paths and the `tools` directory you choose.
{{% /notice %}}

## Import the AArch64 toolchain

Cortex-A cores need the Zephyr SDK's `aarch64-zephyr-elf` compiler, and the Minimal SDK type downloads only that one.

In the **Workbench for Zephyr** panel, select **Add Toolchain** and fill in the form:

- **Toolchain family**: **Zephyr SDK**
- **Source**: **Official**
- **Destination**: **Custom location**
- **SDK Type**: **Minimal**
- **Version**: v1.0.1
- **aarch64** checkbox selected, the others clear
- **Location**: a directory for the SDK, for example `/home/user/zephyr-secure-boot/tools`

![The Add Toolchain form in Workbench for Zephyr with red rectangles around the fields to set: Add Toolchain in the sidebar, the Zephyr SDK family, the Minimal SDK type, the version v1.0.1, the selected aarch64 architecture, the Location field and the Import button#center](images/wz-add-toolchain.webp "Add Toolchain, filled in for the AM62L")

Select **Import**. The download takes a few minutes. When it finishes, the **Toolchains** view shows `Zephyr SDK 1.0.1` with a `GNU` entry and `aarch64-zephyr-elf` under it.

## Add a West workspace

The workspace needs a Zephyr release that supports your board. Board support for the AM62L EVM entered Zephyr in version 4.4, so this example uses 4.4.2. Select **Add West Workspace** and fill in the form:

- **Source location**: **From template**
- **Minimal**, not **Full**, under the **Path** field
- **Template**: your board vendor's, **Texas Instruments** for the AM62L EVM
- **Revision**: v4.4.2, or a later 4.x release
- **Location**: `/home/user/zephyr-secure-boot`
- **Subfolder**: `zephyrproject`

![The Add West Workspace form in Workbench for Zephyr with red rectangles around the fields to set: Add West Workspace in the sidebar, the From template source, the Minimal option, the Texas Instruments template, the v4.4.2 revision, the Location field and the Import button#center](images/wz-add-west-workspace.webp "Add West Workspace, set to Zephyr 4.4.2 with the Texas Instruments template")

Select **Import**. Workbench clones Zephyr, the vendor's HAL (hardware abstraction layer) and the other modules into `zephyrproject/deps`, the longest step on this page, and `zephyrproject` appears in the **West workspaces** view.

## Create the application

Select **Add Application** and fill in the wizard:

- **Select West Workspace**: `zephyrproject`
- **Select Toolchain**: `zephyr-sdk-1.0.1`
- **SDK Variant**: **GNU GCC**
- **Select Board**: type `am62l` and select **TI AM62L Evaluation Module (EVM)**
- **New or existing application?**: **Create new application**
- **Select template**: `hello_world`, under `deps/zephyr/samples/hello_world`
- **Project Name**: `hello`
- **Application type**: **West workspace application**
- **Project Location**: `zephyrproject/applications/hello`, filled in by the wizard

The board's Zephyr identifier, `am62l_evm/am62l3/a53`, is the `BOARD` value in `env.sh`; on another board, select the entry that matches your `BOARD`.

![The Add Application wizard in Workbench for Zephyr with red rectangles around the fields to set: Add Application in the sidebar, the zephyrproject workspace, the zephyr-sdk-1.0.1 toolchain, the TI AM62L Evaluation Module board, the hello_world template, the project name hello, the project location under zephyrproject/applications and the Create button#center](images/wz-add-application.webp "Add Application, filled in for the AM62L EVM")

Select **Create**. The application `hello` appears in the **Applications** view, marked `[with zephyrproject]`, and `zephyrproject/applications/hello` holds the sample's `CMakeLists.txt`, `prj.conf` and `src/main.c`.

## Replace the sample's files

Leave `CMakeLists.txt` as it is and replace the other two files.

Replace the contents of `prj.conf` with these four lines:

```text
CONFIG_ARMV8_A_NS=y
CONFIG_PRINTK=y
CONFIG_BOOT_BANNER=y
CONFIG_AARCH64_IMAGE_HEADER=y
```

`CONFIG_PRINTK` gives you `printk()` on the console, and `CONFIG_BOOT_BANNER` prints the `*** Booting Zephyr OS build ... ***` line, the first sign that the jump from U-Boot landed.

Replace the contents of `src/main.c` with the following code. The banner names the image and its key, so that on the optional page [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) the console tells you which of two images ran.

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

int main(void)
{
	printk("\n");
	printk("################################################\n");
	printk("#                                              #\n");
	printk("#   Hello from ZEPHYR IMAGE A                  #\n");
	printk("#   signed with key-a  (TRUSTED by U-Boot)     #\n");
	printk("#                                              #\n");
	printk("################################################\n");
	printk("\n");
	printk("board            : %s\n", CONFIG_BOARD_TARGET);
	printk("arch             : %s\n", CONFIG_ARCH);
	printk("started by       : U-Boot 'go' after FIT signature verification\n");
	printk("this image was verified by U-Boot before it ran.\n");
	return 0;
}
```

Save both files.

## Two settings that matter

`CONFIG_ARMV8_A_NS=y` tells Zephyr that it runs in the Non-secure world, the one U-Boot hands it. Without it, the driver of the GICv3 (Generic Interrupt Controller) never programs the Non-secure registers, the timer interrupt never arrives, and Zephyr hangs right after its banner.

`CONFIG_AARCH64_IMAGE_HEADER=y` puts a 64-byte arm64 header at the start of `zephyr.bin`, in the same format as a Linux kernel image. The header's first instruction is `b __start`, a branch to Zephyr's real entry point. U-Boot only needs that branch at offset 0: without the header, `go` jumps into whatever the linker placed there.

The board configuration for `am62l_evm/am62l3/a53` already sets both options; repeating them in `prj.conf` protects you on a board whose configuration doesn't.

## Build the application

In the **Applications** view, right-click `hello` and select **Build**. Workbench runs `west build` in the terminal with the build directory `build/primary` inside the application, and the linker prints its memory report near the end. The output is similar to:

```output
Memory region         Used Size  Region Size  %age Used
           FLASH:           0 B          0 B
             RAM:       4168 KB      2016 MB      0.20%
        IDT_LIST:           0 B        32 KB      0.00%
```

![The Applications view in Workbench for Zephyr and the build terminal, with red rectangles around the hello application, listed with its zephyrproject workspace, zephyr-sdk-1.0.1 toolchain and am62l_evm/am62l3/a53 board, and around the Memory region table near the end of a successful build#center](images/wz-build.webp "The hello application built for the AM62L EVM")

There is no flash on this board target; `RAM` is the part of the DDR that Zephyr may use. The result is `$WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin`, a raw binary of about 58 KB. It is linked at `0x82000000`, the `ZEPHYR_ADDR` value in `env.sh`. That address is the start of the memory node the board device tree selects as `zephyr,sram`; on the AM62L it sits past the first 32 MB of DDR, where TF-A and OP-TEE live. Every following page uses that address as the FIT `load` and `entry` address and as the `go` target.

## Check the image starts with a branch

Open a terminal (**Terminal > New Terminal** in VS Code, or any shell), load the environment with `source $HOME/zephyr-secure-boot/env.sh`, and print the first four bytes of the binary:

```bash
od -An -tx1 -N4 $WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin
```

The output is similar to:

```output
 53 04 00 14
```

Those four bytes, read as a little-endian 32-bit word, are one AArch64 `b` (branch) instruction: the top six bits of the last byte (`14` here) are the opcode and the remaining 26 bits hold the distance to `__start`, so the first three bytes can differ in your build.

Now check the header's magic number at offset `0x38`:

```bash
od -An -c -j 0x38 -N4 $WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin
```

The expected output is:

```output
   A   R   M   d
```

`0x64` is the ASCII code for `d`, so `A R M d` is the magic `ARM\x64`.

{{% notice Note %}}
If the last of the four bytes isn't in the range `14` to `17`, or the magic isn't at `0x38`, then `CONFIG_AARCH64_IMAGE_HEADER` isn't set in the build. Check `$WORK/zephyrproject/applications/hello/build/primary/zephyr/.config` for `CONFIG_AARCH64_IMAGE_HEADER=y`.
{{% /notice %}}

## What you've accomplished and what's next

You've built one Zephyr image for the Cortex-A53 on the AM62L EVM with Workbench for Zephyr, linked at `0x82000000`, starting with a branch instruction and carrying the arm64 header. That's all U-Boot needs to start it with `go`, and all `mkimage` needs to wrap it in a FIT on the next page.

Next, you [create the signing keys and sign the image into a FIT](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/).
