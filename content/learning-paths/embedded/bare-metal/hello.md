---
# User change
title: Create and build a Hello World example project

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Prerequisites

It is assumed you have installed Arm Development Studio and configured your license. For full instructions see [here](/install-tools/armds/).

Alternatively you can install [Arm Compiler for Embedded](/install-tools/armclang/) and [Arm Fixed Virtual Platforms (FVP)](/install-tools/fm#fvp) individually.

See [Prepare Docker image for Arm embedded development](/learning-paths/cross-platform/docker/) for an example Docker image containing all these tools.

We shall use the `FVP_Base_Cortex-A73x2-A53x4` platform, which is a complex FVP system, containing two processor clusters.

## "Hello World!"

Let's start with a simple C program, and use the `armclang` compiler and `armlink` linker tools to compile and generate an executable image.

Use your favorite editor to create a new source file called `hello.c` with the following contents:
```C
#include <stdio.h>

int main(void) {
  printf("Hello World!\n");
  return 0;
}
```
## Build the example

This command invokes the compiler to compile `hello.c` for the [Armv8-A architecture](https://developer.arm.com/Architectures/A-Profile%20Architecture) and generate an ELF object file `hello.o`:
```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a hello.c
```

The options used in this command are:
- `-c` tells the compiler to stop after compiling to object code. We will perform the link step to create the final executable in the next step.
- `-g` tells the compiler to include debug information in the image.
- `--target=aarch64-arm-none-eabi` tells the compiler to target the Armv8-A AArch64 ABI.
- `-march=armv8-a` explicitly selects the architecture version. Alternatively you can specify a particular processor with `-mcpu`.

Create an executable image by linking the object using armlink. This generates an ELF image file named `hello.axf`:
```console
armlink hello.o -o hello.axf
```
We have not yet specified an entry point, and so the entry point defaults to` __main()` in the Arm libraries. These libraries perform a number of setup activities, including:

- Copying all the code and data from the image into memory.
- Setting up an area of memory for the application stack and heap.
- Branching to the main() function to run the application.

## Specify the memory map

If you tried to execute the image that you created in the last step on the `FVP_Base_Cortex-A73x2-A53x4 model`, it would not run. This is because the default memory map used by `armlink` does not match the memory map used by the model.

We must specify a memory map that matches the target and allows the image to run successfully. To do this, we will create a [scatter file](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features).

Create a file `scatter.txt` with the following contents:
```console
ROM_LOAD 0x00000000 0x00010000
{
    ROM_EXEC +0x0 0x10000
    {
      * (InRoot$$Sections)
      * (+RO)
    }

    RAM_EXEC 0x04000000 0x10000
    {
      * (+RW, +ZI)
    }
    ARM_LIB_STACKHEAP 0x04010000 ALIGN 64 EMPTY 0x10000
    {}
}
```
and link the image using the scatter file.
```console
armlink --scatter=scatter.txt hello.o -o hello.axf
```
### Understanding the scatter file

The statements in the scatter file define the different regions of memory and their purpose. The following defines a `load region`, starting at address 0x0, and of size 0x10000 bytes. A `load region` is an area of memory that contains the image file at reset before execution starts (typically defining the Flash memory addresses of a real system).
```
ROM_LOAD 0x00000000 0x00010000
{...}
```

Within the `load region` we define `execution region(s)`, where the code/data will be located at run-time:
```
  ROM_EXEC +0x0 0x10000
  {
    * (InRoot$$Sections)
    * (+RO)
  }
```
An execution region is called a `root region` if it has the same load-time and execute-time address. The initial entry point of an image must be in a root region, as this is executed before scatterloading can occur to relocate that code. You can use the `InRoot$$Sections` section name to ensure the appropriate C library code for scatterloading is in this section (useful when there are multiple code regions).

In our scatter file, all read-only (`RO`) code/data (including the entry point `__main()`) is placed in the `ROM_EXEC` root region.

```
  RAM_EXEC 0x04000000 0x10000
  {
    * (+RW, +ZI)
  }
```
`RAM_EXEC` contains any read-write (`RW`) or zero-initialised (`ZI`) data. Because this has been located at a different address (0x04000000, in SRAM), it is not a root region.

`ARM_LIB_STACKHEAP` and `EMPTY` are syntactically significant for the linker.

Region names (such as `ROM_LOAD`, `ROM_EXEC`, and `RAM_EXEC` above) are arbitrary. However there are reserved names for the Stack and Heap regions. We use a single region (`ARM_LIB_STACKHEAP`) for both.
```
ARM_LIB_STACKHEAP 0x04010000 EMPTY 0x10000
{}
```
* The heap will start at `0x04010000` and grows upwards.
* The stack will start at `0x04020000` (`0x04010000 + 0x10000`) and grows downwards.

The use of `EMPTY` is used as there are no explicit sections to locate therein.

## Run the image on the FVP

You can now run the executable image `hello.axf` from the command line using the `FVP_Base_Cortex-A73x2-A53x4 model`:
```console
FVP_Base_Cortex-A73x2-A53x4 -a hello.axf -C pctl.startup=0.0.1.0
```
When the model is running, the message "Hello World!" appears on screen.

By default, this model starts all processors in the model running. To avoid this, use the `-C pctl.startup=0.0.1.0` option to specify that only a single core should be used (we will address this in the next section).

At reset, the code and data will be in the `ROM_LOAD` section. The library function `__main()` is responsible for copying the RW and ZI data, and `__rt_entry()` sets up the stack and heap.
