---
# User change
title: Write a reset handler

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
A real embedded system will need initialization before any other code is executed. You will create a minimal reset handler, putting all but one processor to sleep, and executing the application on just one processor.

## Write a reset handler

Create a new file, `startup_el3.s`, with the following contents:
#### startup_el3.s
```C
  .section  BOOT,"ax"   // Define an executable ELF section, BOOT
  .global el3_entry
  .type el3_entry, "function"

el3_entry:
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
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup_el3.s
```
{{% notice %}}
The compiler identifies `.s` files as assembler source.
{{% /notice %}}


### Understanding the reset handler

The [MPIDR_EL1](https://developer.arm.com/documentation/ddi0595/latest/AArch64-Registers/MPIDR-EL1--Multiprocessor-Affinity-Register) register provides a CPU identification mechanism. The `Aff0` and `Aff1` bitfields let us check which numbered processor in a cluster the code is running on. This startup code sends all but one processor to sleep.

Setting [CPTR_EL3](https://developer.arm.com/documentation/ddi0595/2021-12/AArch64-Registers/CPTR-EL3--Architectural-Feature-Trap-Register--EL3-) to zero disables various instruction traps which allows the C library init code to proceed.

## Link the application

Modify the scatter file so that the startup code goes into the root region `ROM_EXEC`. This must be located as the `FIRST` section in the region, so that it is at exactly `0x0`, and so is executed when the processors start.

#### scatter.txt
```console
  ROM_EXEC +0x0
  {
    startup_el3.o (BOOT, +FIRST)
    * (InRoot$$Sections)
    * (+RO)
  }
```
Link the objects, specifying the symbol `el3_entry` as the entry point.
```console
armlink --scatter=scatter.txt hello.o startup_el3.o -o hello.axf --entry=el3_entry
```
The entry point is used by the linker to determine which code is necessary to keep. It is also used by debuggers to know where to start execution from.

## Run the new application

You can now successfully execute on the FVP without the additional `pctl.startup` parameter from before.
```console
FVP_Base_AEMv8 -a hello.axf
```
A single "Hello World!" message is displayed.
```output
Hello World!
```
