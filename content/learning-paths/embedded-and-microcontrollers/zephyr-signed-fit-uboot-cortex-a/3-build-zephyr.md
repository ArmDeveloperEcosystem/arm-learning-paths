---
title: Build a Zephyr image that U-Boot can start
description: Write a small Zephyr application, build it with west for the Cortex-A53 on the TI AM62L EVM, and check that the binary starts with a branch instruction so U-Boot can jump to it with go.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a small Zephyr application

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

The application is a hello world that prints a banner. The banner names the image, so later, when U-Boot starts one of several images, the console tells you which program ran. That's the only reason the text is so loud.

Create the application directory:

```bash
mkdir -p $WORK/app/hello/src
```

Create `$WORK/app/hello/CMakeLists.txt` with the standard four lines of a Zephyr application:

```cmake
cmake_minimum_required(VERSION 3.20.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(hello)
target_sources(app PRIVATE src/main.c)
```

Create `$WORK/app/hello/src/main.c` with the following code:

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

Create `$WORK/app/hello/prj.conf` with the following four lines:

```text
CONFIG_ARMV8_A_NS=y
CONFIG_PRINTK=y
CONFIG_BOOT_BANNER=y
CONFIG_AARCH64_IMAGE_HEADER=y
```

`CONFIG_PRINTK` gives you `printk()` on the console. `CONFIG_BOOT_BANNER` prints the `*** Booting Zephyr OS build ... ***` line, which is the first sign that the jump from U-Boot landed. The other two options deserve their own section.

## Two settings that matter

`CONFIG_ARMV8_A_NS=y` tells Zephyr that it runs in the Non-secure world. An Armv8-A processor runs code in one of two worlds, Secure or Non-secure, and some hardware keeps a separate set of registers for each world. On the AM62L, TF-A owns the Secure world and starts U-Boot, and then Zephyr, in the Non-secure world. The Generic Interrupt Controller (GIC) is one such piece of hardware, and Zephyr's GICv3 driver programs its Non-secure registers only when this option is set. Without it, the timer interrupt never arrives, and Zephyr hangs right after its banner.

`CONFIG_AARCH64_IMAGE_HEADER=y` puts a 64-byte arm64 header at the start of `zephyr.bin`, in the same format as a Linux kernel image. The first instruction of that header is `b __start`, a branch to Zephyr's real entry point. U-Boot never parses this header in the flow you build here, and it doesn't need to. It jumps to the first byte of the image with `go 0x82000000`. The `go` command is only a jump to an address, and the branch takes it the rest of the way. Without the header, the first byte of the image is whatever the linker placed there, and `go` jumps into garbage.

The board configuration for `am62l_evm/am62l3/a53` already sets both options. Repeating them in `prj.conf` documents the intent, and protects you when you move the application to a board whose configuration doesn't set them.

## Build for the AM62L EVM

Run `west` from inside your Zephyr workspace, for example `cd ~/zephyrproject`, and activate its Python virtual environment if you use one. `west` finds Zephyr from the workspace, and the application can live anywhere.

Build the application for the Cortex-A53 cluster of the AM62L EVM:

```bash
west build -p always -b am62l_evm/am62l3/a53 -d $WORK/build/hello $WORK/app/hello
```

The options are:

- `-p always` forces a clean build, so nothing from a previous board leaks in.
- `-b am62l_evm/am62l3/a53` selects the board, the AM62L3 SoC variant, and the A53 cluster.
- `-d` sets the build directory, and the last argument is the application directory.

The result is `$WORK/build/hello/zephyr/zephyr.bin`, a raw binary linked to run at `0x82000000`. Check its size:

```bash
stat -c %s $WORK/build/hello/zephyr/zephyr.bin
```

The output is similar to:

```output
58340
```

That's about 58 KB. The link address comes from the board's device tree, whose `zephyr,sram` memory node starts at `0x82000000`. That's past the first 32 MB of DDR, the board's RAM, where TF-A and OP-TEE live. On another board, read the address from that board's device tree. The same address appears on every following page: as the FIT `load` and `entry` address, and as the `go` target.

## Check the image starts with a branch

Before you sign anything, check that the header is really there. Print the first four bytes of the binary:

```bash
od -An -tx1 -N4 $WORK/build/hello/zephyr/zephyr.bin
```

The expected output is:

```output
 53 04 00 14
```

The `od` options are: `-An` drops the address column, `-tx1` prints hex bytes, and `-N4` reads four bytes.

Read as a little-endian 32-bit word, that's `0x14000453`. The top six bits of that word, `000101`, encode an AArch64 `b` (branch) instruction, which is why the last byte printed reads `14`. The remaining 26 bits, `0x453`, are the branch distance counted in 4-byte instructions: `0x453` times 4 is `0x114c` bytes. In the build used to write this page, Zephyr's ELF entry point is `0x8200114c`, which is `0x82000000 + 0x114c`. So a jump to offset 0 lands on the branch, and the branch lands on `__start`.

Now check the header's magic number, a fixed four-byte marker that identifies an arm64 image. It sits at offset `0x38`:

```bash
od -An -c -j 0x38 -N4 $WORK/build/hello/zephyr/zephyr.bin
```

The expected output is:

```output
   A   R   M   d
```

The magic is the four bytes `ARM\x64`. The `-c` option prints each byte as a character, and `0x64` is the ASCII code for `d`, so `A R M d` is the magic. `-j 0x38` skips to that offset.

That header is why U-Boot's boot command can use the fixed address `go 0x82000000`. The entry point of the ELF file moves whenever the code changes; offset 0 of the binary doesn't.

{{% notice Note %}}
If the last of the four bytes isn't `14`, or the magic isn't at `0x38`, then `CONFIG_AARCH64_IMAGE_HEADER` isn't set in the build. Check `$WORK/build/hello/zephyr/.config` for `CONFIG_AARCH64_IMAGE_HEADER=y`. The first three bytes can differ from `53 04 00` in your build, because they hold the branch distance; the `14` byte and the magic are what matter.
{{% /notice %}}

## Build a second image for the wrong-key test

The next page signs three images: a trusted one, one signed with a key U-Boot doesn't know, and a tampered copy. The wrong-key image is a different program on purpose. If U-Boot ever runs it, the console says so in capital letters, and you can't mistake it for the trusted image.

Copy the application and change the two banner lines:

```bash
cp -r $WORK/app/hello $WORK/app/hello_b
sed -i 's/ZEPHYR IMAGE A/ZEPHYR IMAGE B/; s/key-a  (TRUSTED by U-Boot)     #/key-b  (NOT trusted by U-Boot) #/' $WORK/app/hello_b/src/main.c
```

The replacement is the same length as the text it replaces, so the box stays aligned.

Check the edit:

```bash
grep -e 'IMAGE B' -e 'key-b' $WORK/app/hello_b/src/main.c
```

The expected output is:

```output
	printk("#   Hello from ZEPHYR IMAGE B                  #\n");
	printk("#   signed with key-b  (NOT trusted by U-Boot) #\n");
```

Build it into its own directory:

```bash
west build -p always -b am62l_evm/am62l3/a53 -d $WORK/build/hello_b $WORK/app/hello_b
```

The result is `$WORK/build/hello_b/zephyr/zephyr.bin`, again about 58 KB. Only the text differs. The next page signs it with `key-b`, a key U-Boot doesn't know.

## What you've accomplished and what's next

You've built two Zephyr images for the Cortex-A53 on the AM62L EVM, both linked at `0x82000000`. You've also checked that the trusted one starts with a branch instruction and carries the arm64 header. That's all U-Boot needs to start Zephyr with `go`, and all `mkimage` needs to wrap it in a FIT on the next page.

Next, you [create the signing keys and sign the trusted image into a FIT](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/), then make the two images that U-Boot must refuse.
