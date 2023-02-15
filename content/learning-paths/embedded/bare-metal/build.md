---
# User change
title: "Import and build example project"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Prerequisites

It is assumed you have installed Arm Development Studio and configured your license. For full instructions see [here](/install-tools/armds/).

Alternatively you can install [Arm Compiler for Embedded](/install-tools/armclang/) and [Arm Fixed Virtual Platforms (FVP)](/install-tools/fm#fvp) individually.

See [Prepare Docker image for Arm embedded development](/learning-paths/cross-platform/docker/) for an example Docker image.

We shall use the `FVP_Base_Cortex-A73x2-A53x4` platform, which is a complex FVP system, containing two processor clusters.

## "Hello World!"

Let's start with a simple C program, and use the `armclang` compiler and `armlink` linker tools to compile and generate an executable image.

In your command-line terminal, use your favorite editor to create a new file called `hello_world.c` with the following contents:
```C
#include <stdio.h>

int main(void) {
  printf("Hello World!\n");
  return 0;
}
```
## Build the example

This command invokes the compiler to compile `hello_world.c` for the [Armv8-A architecture](https://developer.arm.com/Architectures/A-Profile%20Architecture) and generate an ELF object file `hello_world.o`:
```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a hello_world.c
```

The options used in this command are:
- `-c` tells the compiler to stop after compiling to object code. We will perform the link step to create the final executable in the next step.
- `-g` tells the compiler to include debug information in the image.
- `--target=aarch64-arm-none-eabi` tells the compiler to target the Armv8-A AArch64 ABI.
- `-march=armv8-a` explicitly selects the architecture version.

Create an executable image by linking the object using armlink. This generates an ELF image file named `hello.axf`:
```console
armlink hello_world.o -o hello.axf
```
We have not yet specified an entry point, and so the entry point defaults to` __main()` in the Arm libraries. These libraries perform a number of setup activities, including:

- Copying all the code and data from the image into memory.
- Setting up an area of memory for the application stack and heap.
- Branching to the main() function to run the application.

## Specify the memory map

If you tried to execute the image that you created in the last step on the `FVP_Base_Cortex-A73x2-A53x4 model`, it would not run. This is because the default memory map used by armlink does not match the memory map used by the model.

We will specify a new memory map that matches the model and allows the image to run successfully. To do this, you will create a [scatter file](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features) that tells the linker the structure of the memory map.

The memory map describes the different regions of target memory, and what they can be used for. For example, ROM can hold read-only code and data but cannot store read-write data.

Create a file `scatter.txt` in the same directory as `hello_world.c` with the following contents:
```console
ROM_LOAD 0x00000000 0x00010000
{
    ROM_EXEC +0x0
    {
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
armlink --scatter=scatter.txt hello_world.o -o hello.axf
```
## Understanding the scatter file

The statements in the scatter file define the different regions of memory and their purpose.

Let's look at them sequentially. The following defines a `load region`.
```
ROM_LOAD 0x00000000 0x00010000
{...}
```
A load region is an area of memory that contains the image file at reset before execution starts. The first value specified gives the starting address of the region, and the second number gives the size of the region.

The following defines an `execution region`:
```
  ROM_EXEC +0x0
  {
    * (+RO)
  }
```
Execution regions define the memory locations in which different parts of the image will be placed at run-time.

An execution region is called a `root region` if it has the same load-time and execute-time address. `ROM_EXEC` qualifies as a root region because its execute-time is located at an offset of `+0x0` from the start of the load region (that is, the region has the same load-time and execute-time addresses).

The initial entry point of an image must be in a root region. In our scatter file, all read-only (`RO`) code including the entry point `__main()` is placed in the `ROM_EXEC` root region.
```
  RAM_EXEC 0x04000000 0x10000
  {
    * (+RW, +ZI)
  }
```
`RAM_EXEC` contains any read-write (RW) or zero-initialised (ZI) data. Because this has been placed at a different address (in SRAM), it is not a root region.

This instruction specifies the placement of the heap and stack:
```
ARM_LIB_STACKHEAP 0x04010000 EMPTY 0x10000
{}
```
- The heap will start at `0x04010000` and grows upward.
- The stack will start at `0x0401FFFF` and grows downwards.

The `EMPTY` declaration reserves `0x10000` of uninitialized memory, starting at `0x04010000`.

`ARM_LIB_STACKHEAP` and `EMPTY` are syntactically significant for the linker. However, `ROM_LOAD`, `ROM_EXEC`, and `RAM_EXEC` are not syntactically significant and could be renamed if you like.

## Run the image on the FVP

You can now run the executable image `hello.axf` from the command line using the `FVP_Base_Cortex-A73x2-A53x4 model`:
```console
FVP_Base_Cortex-A73x2-A53x4 -a hello.axf -C pctl.startup=0.0.1.0
```
When the model is running, the message "Hello World!" appears on screen.

By default, this model boots up multiple cores. This could lead to strange or inconsistent behavior. To avoid this type of result, we use the `-C pctl.startup=0.0.1.0` option to specify that only a single core should be used.

Another method to avoid strange or inconsistent results is to write some startup code that shuts down all but one core. We will discuss writing startup code later.

At reset, the code and data will be in the `ROM_LOAD` section. The library function `__main()` is responsible for copying the RW and ZI data, and `__rt_entry()` sets up the stack and heap.

## Write a reset handler

Typically, an embedded system needs some low-level initialization at startup.

Often this initialization must occur before any other code is executed. This means that you must define and change the entry point for the system in a way that reflects the execution flow that is shown in the following diagram:

Create a new file, `startup.s`, with the following contents:
```C
  .section  BOOT,"ax" // Define an executable ELF section, BOOT
  .align 3                     // Align to 2^3 byte boundary

  .global start64
  .type start64, "function"

start64:

  // Which core am I
  // ----------------
  MRS      x0, MPIDR_EL1
  AND      x0, x0, #0xFFFF     // Mask off to leave Aff0 and Aff1
  CBZ      x0, boot            // If not *.*.0.0, then go to sleep
sleep:
  WFI
  B        sleep

boot:
  // Disable trapping of CPTR_EL3 accesses or use of Adv.SIMD/FPU
  // -------------------------------------------------------------
  MSR      CPTR_EL3, xzr       // Clear all trap bits

  // Branch to scatter loading and C library init code
  .global  __main
  B        __main
```
The `MPIDR_EL1` register provides a CPU identification mechanism. The `Aff0` and `Aff1` bitfields let us check which numbered CPU in a cluster the code is running on. This startup code sends all but one CPU to sleep. The status of the Floating Point Unit (FPU) in the model is unknown. The Architectural Feature Trap Register, `CPTR_EL3`, has no defined reset value. Setting `CPTR_EL3` to zero disables trapping of SIMD, FPU, and a few other instructions.

Build the startup code with:
```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup.s
```

## Link the application
Modify the scatter file so that the startup code goes into the root region `ROM_EXEC`:
```console
  ROM_EXEC +0x0
  {
    startup.o(BOOT, +FIRST)
    * (+RO)
  }
```
Adding the line `startup.o(BOOT, +FIRST)` ensures that the `BOOT` section is placed first in the `ROM_EXEC` region.

Link the objects, specifying `start64` as the entry point. Execution starts from this label on reset:
```console
armlink --scatter=scatter.txt --entry=start64 hello_world.o startup.o -o hello.axf
```

## Run the new application
We can now successfully execute on the FVP without the additional parameter.
```console
FVP_Base_Cortex-A73x2-A53x4 -a hello.axf
```
The "Hello World!" message appears on screen.
