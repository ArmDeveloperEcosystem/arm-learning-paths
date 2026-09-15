---
title: Build a Zephyr image that U-Boot can start
description: Use Workbench for Zephyr in VS Code to build a small Zephyr 4.4 application for the Cortex-A53 on the TI AM62L EVM, then check that the binary starts with a branch instruction that U-Boot's go command can jump to.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open Workbench for Zephyr

You build Zephyr in Visual Studio Code with Workbench for Zephyr, which you installed with its host tools on the previous page. [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/) sets up a Cortex-M toolchain and workspace. This page does the same two steps with what the AM62L needs: the AArch64 toolchain and a Zephyr 4.4 workspace made from the Texas Instruments template.

Open VS Code on your working directory:

```bash
code $HOME/zephyr-secure-boot
```

Then select the **Workbench for Zephyr** icon in the Activity Bar. The panel has one view per thing you manage: **Applications**, **West workspaces**, **Toolchains** and **Host tools**.

{{% notice Note %}}
The screenshots on this page were taken on Windows, so the paths in them start with `C:\Users\`. On your Ubuntu host the same fields take paths that start with `/home/`. That machine also had the Zephyr SDK installed globally already, so its **Toolchains** view tags the SDK `[global]` and its build log finds the compiler under a `zephyr-sdk-1.0.1` directory in the user's home; yours shows the `tools` directory you choose. Everything else is identical.
{{% /notice %}}

## Import the AArch64 toolchain

The Cortex-A53 cores of the AM62L run AArch64 code, so you need the Zephyr SDK's `aarch64-zephyr-elf` compiler. The SDK's Minimal type lets you download only that one.

In the **Workbench for Zephyr** panel, select **Add Toolchain** and fill in the form:

- **Toolchain family**: **Zephyr SDK**
- **Source**: **Official**
- **Destination**: **Custom location**
- **SDK Type**: **Minimal**
- **Version**: v1.0.1
- **aarch64** checkbox selected, with the other architecture checkboxes left clear
- **Location**: a directory for the SDK, for example `/home/user/zephyr-secure-boot/tools`

![The Add Toolchain form in Workbench for Zephyr with red rectangles around the fields to set: Add Toolchain in the sidebar, the Zephyr SDK family, the Minimal SDK type, the version v1.0.1, the selected aarch64 architecture, the Location field and the Import button#center](images/wz-add-toolchain.webp "Add Toolchain, filled in for the AM62L")

Select **Import**. Workbench downloads the SDK and the AArch64 compiler, which takes a few minutes. When it finishes, the **Toolchains** view shows `Zephyr SDK 1.0.1` with a `GNU` entry and `aarch64-zephyr-elf` under it.

## Add a West workspace with Zephyr 4.4 or later

Board support for the AM62L EVM entered Zephyr in version 4.4, so the workspace needs Zephyr 4.4.0 or later. Select **Add West Workspace** and fill in the form:

- **Source location**: **From template**
- **Minimal**, not **Full**, in the pair of options under the **Path** field
- **Template**: **Texas Instruments**, which pulls the TI HAL module next to Zephyr
- **Revision**: v4.4.2, or a later 4.x release
- **Location**: `/home/user/zephyr-secure-boot`
- **Subfolder**: `zephyrproject`

![The Add West Workspace form in Workbench for Zephyr with red rectangles around the fields to set: Add West Workspace in the sidebar, the From template source, the Minimal option, the Texas Instruments template, the v4.4.2 revision, the Location field and the Import button#center](images/wz-add-west-workspace.webp "Add West Workspace, set to Zephyr 4.4.2 with the Texas Instruments template")

Select **Import**. Workbench clones Zephyr, the TI HAL and the other modules the template lists into `zephyrproject/deps`. This is the longest step on this page. When it finishes, `zephyrproject` appears in the **West workspaces** view.

## Create the application

Select **Add Application** and fill in the wizard:

- **Select West Workspace**: `zephyrproject`
- **Select Toolchain**: `zephyr-sdk-1.0.1`
- **SDK Variant**: **GNU GCC**
- **Select Board**: type `am62l` and select **TI AM62L Evaluation Module (EVM)**, Zephyr identifier `am62l_evm/am62l3/a53` (the AM62L EVM board, the AM62L3 SoC variant, the A53 cluster)
- **New or existing application?**: **Create new application**
- **Select template**: `hello_world`, the one under `deps/zephyr/samples/hello_world`
- **Project Name**: `hello`, replacing the sample name the wizard fills in
- **Application type**: **West workspace application**
- **Project Location**: filled in by the wizard as `zephyrproject/applications/hello` inside your working directory, the path the later pages use

![The Add Application wizard in Workbench for Zephyr with red rectangles around the fields to set: Add Application in the sidebar, the zephyrproject workspace, the zephyr-sdk-1.0.1 toolchain, the TI AM62L Evaluation Module board, the hello_world template, the project name hello, the project location under zephyrproject/applications and the Create button#center](images/wz-add-application.webp "Add Application, filled in for the AM62L EVM")

Select **Create**. The application `hello` appears in the **Applications** view, marked `[with zephyrproject]`, and Workbench creates `zephyrproject/applications/hello` with the sample's `CMakeLists.txt`, `prj.conf` and `src/main.c`.

## Replace the sample's files

Leave the sample's `CMakeLists.txt` as it is and replace the other two files.

Replace the contents of `prj.conf` with these four lines:

```text
CONFIG_ARMV8_A_NS=y
CONFIG_PRINTK=y
CONFIG_BOOT_BANNER=y
CONFIG_AARCH64_IMAGE_HEADER=y
```

`CONFIG_PRINTK` gives you `printk()` on the console. `CONFIG_BOOT_BANNER` prints the `*** Booting Zephyr OS build ... ***` line, which is the first sign that the jump from U-Boot landed. The other two options have their own section.

Replace the contents of `src/main.c` with the following code. The banner names the image and its key, so the console tells you which program ran; that matters on the optional [test page](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/), where U-Boot is offered a second image with a different banner. That's the only reason the text is so loud.

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

`CONFIG_ARMV8_A_NS=y` tells Zephyr that it runs in the Non-secure world, the one TF-A hands to U-Boot and U-Boot hands to Zephyr. The Generic Interrupt Controller (GIC) keeps a separate set of registers for each world, and Zephyr's GICv3 driver programs the Non-secure ones only when this option is set. Without it, the timer interrupt never arrives, and Zephyr hangs right after its banner.

`CONFIG_AARCH64_IMAGE_HEADER=y` puts a 64-byte arm64 header (arm64 is Linux's name for AArch64) at the start of `zephyr.bin`, in the same format as a Linux kernel image. The first instruction of that header is `b __start`, a branch to Zephyr's real entry point. U-Boot never parses this header in the flow you build here; it only needs the branch at offset 0. Without the header, the first byte of the image is whatever the linker placed there, and `go` jumps into garbage.

The board configuration for `am62l_evm/am62l3/a53` already sets both options. Repeating them in `prj.conf` documents the intent, and protects you when you move the application to a board whose configuration doesn't set them.

## Build the application

In the **Applications** view, right-click `hello` and select **Build**. Workbench runs `west build` for the board in the terminal, with the build directory `build/primary` inside the application; `primary` is the name of the default build configuration. Near the end of the build, the linker prints its memory report. The expected output is:

```output
Memory region         Used Size  Region Size  %age Used
           FLASH:           0 B          0 B
             RAM:       4168 KB      2016 MB      0.20%
        IDT_LIST:           0 B        32 KB      0.00%
```

![The Applications view in Workbench for Zephyr and the build terminal, with red rectangles around the hello application, listed with its zephyrproject workspace, zephyr-sdk-1.0.1 toolchain and am62l_evm/am62l3/a53 board, and around the Memory region table near the end of a successful build#center](images/wz-build.webp "The hello application built for the AM62L EVM")

There is no flash on this board target, and `RAM` is the part of the DDR, the board's main memory, that Zephyr may use. The result is `$WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin`, a raw binary of about 58 KB, linked to run at `0x82000000`. The link address comes from the board's device tree, whose `zephyr,sram` memory node starts at `0x82000000`, past the first 32 MB of DDR where TF-A and OP-TEE live. On another board, read the address from that board's device tree. The same address appears on every following page: as the FIT `load` and `entry` address, and as the `go` target.

## Check the image starts with a branch

Before you sign anything, check that the header is really there. Open a terminal (**Terminal > New Terminal** in VS Code, or any shell) and load the environment: `source $HOME/zephyr-secure-boot/env.sh`. Then print the first four bytes of the binary:

```bash
od -An -tx1 -N4 $WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin
```

The expected output is:

```output
 53 04 00 14
```

The `od` options are: `-An` drops the address column, `-tx1` prints hex bytes, and `-N4` reads four bytes.

Read as a little-endian 32-bit word, those four bytes are one AArch64 `b` (branch) instruction. The last byte printed, `14`, holds the opcode; the other three hold the distance to `__start`, Zephyr's real entry point, so they can differ in your build.

Now check the header's magic number, a fixed four-byte marker that identifies an arm64 image. It sits at offset `0x38`:

```bash
od -An -c -j 0x38 -N4 $WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin
```

The expected output is:

```output
   A   R   M   d
```

The magic is the four bytes `ARM\x64`. The `-c` option prints each byte as a character, and `0x64` is the ASCII code for `d`, so `A R M d` is the magic. `-j 0x38` skips to that offset.

That header is why U-Boot's boot command can use the fixed address `go 0x82000000`. The entry point of the ELF file moves whenever the code changes; offset 0 of the binary doesn't.

{{% notice Note %}}
If the last of the four bytes isn't `14`, or the magic isn't at `0x38`, then `CONFIG_AARCH64_IMAGE_HEADER` isn't set in the build. Check `$WORK/zephyrproject/applications/hello/build/primary/zephyr/.config` for `CONFIG_AARCH64_IMAGE_HEADER=y`.
{{% /notice %}}

## What you've accomplished and what's next

You've set up Workbench for Zephyr with an AArch64 toolchain and a Zephyr 4.4 workspace, and built one Zephyr image for the Cortex-A53 on the AM62L EVM, linked at `0x82000000`. You've also checked that it starts with a branch instruction and carries the arm64 header. That's all U-Boot needs to start Zephyr with `go`, and all `mkimage` needs to wrap it in a FIT on the next page.

Next, you [create the signing keys and sign the image into a FIT](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/).
