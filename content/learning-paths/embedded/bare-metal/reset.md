---
# User change
title: Write a reset handler

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
A real embedded system will need initialization at startup. Often this initialization must occur before any other code is executed.

## Write a reset handler
We will create a minimal reset handler, putting all but one processor to sleep, and executing the application on just one processor.

Create a new file, `startup.s`, with the following contents:
```C
  .section  BOOT,"ax"   // Define an executable ELF section, BOOT
  
  .global start64
  .type start64, "function"

start64:
  MRS      x0, MPIDR_EL1      // Read Affinity register
  AND      x0, x0, #0xFFFF    // Mask off Aff0/Aff1 fields
  CBZ      x0, boot           // Branch to boot if Aff0/Aff1 are zero (Core 0 of Cluster 0)
sleep:                        // Else put processor to sleep
  WFI
  B        sleep

boot:
  MSR      CPTR_EL3, xzr       // Clear all trap bits

  // Branch to scatter loading and C library init code
  .global  __main
  B        __main
```
Build the startup code with:
```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup.s
```
Identifying the file as `.s` tells the compiler that this is in fact assembler source.

### Understanding the reset handler

The [MPIDR_EL1](https://developer.arm.com/documentation/ddi0595/latest/AArch64-Registers/MPIDR-EL1--Multiprocessor-Affinity-Register) register provides a CPU identification mechanism. The `Aff0` and `Aff1` bitfields let us check which numbered processor in a cluster the code is running on. This startup code sends all but one processor to sleep.

Setting [CPTR_EL3](https://developer.arm.com/documentation/ddi0595/2021-12/AArch64-Registers/CPTR-EL3--Architectural-Feature-Trap-Register--EL3-) to zero disables various instruction traps which allows the code to proceed.

## Link the application

Modify the scatter file so that the startup code goes into the root region `ROM_EXEC`. We need this to be located as the `FIRST` section in the region, so that it is at exactly 0x0, and so is executed when the processors start.
```console
  ROM_EXEC +0x0
  {
    startup.o(BOOT, +FIRST)
    * (InRoot$$Sections)
    * (+RO)
  }
```
Link the objects, specifying the symbol `start64` as the entry point.
```console
armlink --scatter=scatter.txt hello_world.o startup.o -o hello.axf --entry=start64
```
The entry point is used by the linker to determine which code is necessary to keep. It is also used by debuggers to know where to start execution from.

## Run the new application

We can now successfully execute on the FVP without the additional parameter from before.
```console
FVP_Base_Cortex-A73x2-A53x4 -a hello.axf
```
The "Hello World!" message appears on screen.
