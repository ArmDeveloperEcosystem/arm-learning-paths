---
title: Port FreeRTOS on the Cortex-R82AE FVP
description: Build the FreeRTOS SMP port with GCC or ArmClang and validate four-core task execution on the Cortex-R82AE FVP.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start from the Cortex-R82 SMP port

Begin with the partner-supported Cortex-R82 SMP demo. It provides the Armv8-R FreeRTOS port, Generic Interrupt Controller (GIC) setup, Memory Protection Unit (MPU) configuration, and SMP scheduler support needed for Cortex-R82.

The Zena CSS FVP provides a clonfigurationthat adds a second cluster of R82AE with 4 cores. 
The objective is to run FreeRTOS on this R82AE cluster.

The first step will to port FreeRTOS on the R82AE cores. To make it easier, we can start by porting on a standalone `FVP_BaseR_Cortex-R82AE` FVP. It can be configured to be as close as possible to the R82AE from the Zena CSS FVP.
To do that, we can start by adding a board support package for `FVP_BaseR_Cortex-R82AE` and a four-task command-line application. Each task has a fixed core affinity, which makes scheduler and coherency problems visible during bring-up.

{{% notice Note %}}
This Learning Path remains in draft until the Cortex-R82AE port repository has a public URL. Obtain the repository URL from the project owner before continuing.
{{% /notice %}}

Clone the port and initialize its FreeRTOS Kernel submodule. Set `PORT_REPOSITORY_URL` to the repository URL supplied to you:

```bash
PORT_REPOSITORY_URL="REPLACE_WITH_PORT_REPOSITORY_URL"
git clone "$PORT_REPOSITORY_URL" fvp-r82ae-freertos
cd fvp-r82ae-freertos
./scripts/setup-freertos-kernel.sh
```

The setup script initializes the pinned kernel and applies the port's kernel patches. The current patch series adjusts Cortex-R82 MPU validation and Cortex-R82AE affinity handling.

## Understand the Cortex-R82AE changes

### FVP configuration

The Zena CSS SW documentation https://arm-zena-css.docs.arm.com/en/v2.2/design/boot_process.html#boot-flow indicate that  SI CL1 boot from LLRAM.

```RSE BL2:
    If CFG2, copies the encrypted SI CL1 image from the RSE flash to SI LLRAM, decrypts and authenticates the image
```

The specifc configuration should be retrived from the Zephyr example implemtation: SRAM is 8MB at 0x140000000
https://gitlab.arm.com/automotive-and-industrial/arm-auto-solutions/arm-zena-css/-/blob/release-v2.2/components/safety_island/zephyr/src/boards/arm/fvp_rd_aspen_safety_island/fvp_rd_aspen_safety_island_c1.dts?ref_type=heads#L109 

The FVP_BaseR_Cortex-R82AE can be configured to expose the same amount of LLRAM at the same base address. The Reset vector Address (RVBAR) can be configured to boot from this address. 

```
cluster0.memory.has_llram=1
cluster0.memory.llram_base=0x140000000
cluster0.memory.llram_enable_at_reset=1
cluster0.memory.llram_shared=1
cluster0.memory.llram_size=0x00800000
cluster0.cpu0.RVBAR=0x140000000
cluster0.cpu1.RVBAR=0x140000000
cluster0.cpu2.RVBAR=0x140000000
cluster0.cpu3.RVBAR=0x140000000
```
Other configurations:
- Use MPU mode for the Cortex R82AE,
- Configure 4 cores, 
- Enable the automatically starts refcounter
- Model architectural cache state
- Disable semihosting

```
cluster0.VMSA_supported=0
cluster0.NUM_CORES=4
bp.refcounter.non_arch_start_at_default=1
cache_state_modelled=1
semihosting-enable=0
```

### Code adaptation 

The generic demo isn't sufficient for the Cortex-R82AE FVP. Check that the port handles these platform differences:

- The processors start at Exception Level 2 (EL2), while the FreeRTOS port runs at EL1
- The Cortex-R82AE affinity layout differs from the layout assumed by the original interprocessor interrupt code
- The GIC uses the architectural affinity layout and must be configured separately from task affinity
- MPU programming needs the required data and instruction synchronization barriers
- The application uses a PL011 UART instead of semihosting
- The FVP protected MPU and shared low-latency RAM (LLRAM) need explicit configuration

The reference FVP configuration uses four cores and an 8 MiB LLRAM window. It divides that window into code and data regions:

| Region | Address | Size |
| --- | ---: | ---: |
| Code | `0x140000000` | 4 MiB |
| Data | `0x140400000` | 4 MiB |

All four reset vector base address registers (RVBARs) point to `0x140000000`. Keep the linker scripts, binary load address, and FVP configuration consistent.


```



## Build the port

Configure GCC in your current shell:

```bash
source scripts/sourceme.sh gcc
```

Build a debug image:

```bash
./scripts/build-r82ae.sh gcc debug
```

You can also build with ArmClang:

```bash
source scripts/sourceme.sh armclang
./scripts/build-r82ae.sh armclang debug
```

Both commands create the same three image formats in `build/fvp_r82ae/`:

```output
r82ae_smp_ping_pong_fvp_gcc_armclang.axf
r82ae_smp_ping_pong_fvp_gcc_armclang.elf
r82ae_smp_ping_pong_fvp_gcc_armclang.bin
```

Use the `.bin` file for direct FVP memory loading and the `.axf` or `.elf` file for symbols in a debugger.

## Run and validate the SMP application

Run the image on `FVP_BaseR_Cortex-R82AE`:

```bash
./scripts/run-r82ae.sh
```

At the application prompt, enter `ping`. The four tasks exchange a message in a cycle across the four cores. The expected output is:

```output
> ping
Ping from Core 0
Pong response from Core 1
Pang response from Core 2
Pung response from Core 3
>
```

This output validates UART access, SMP scheduling, core affinity, interprocessor interrupts, and visibility of shared task state.

## Debug early port failures

### Using the ARMDS debugger
Start the FVP with its debug server enabled when the application doesn't reach the prompt:

```bash
./scripts/run-r82ae.sh -I -p
```

Load the debug image symbols in Arm Development Studio, then set breakpoints on `main`, `FreeRTOS_Abort`, and `App_Fault_Handler`. Load symbols in the EL1 Secure address space if the debugger doesn't resolve the running code automatically.

```text
add-symbol-file FreeRtos_r82ae/build/fvp_r82ae/r82ae_smp_ping_pong_fvp_gcc_armclang.axf
add-symbol-file FreeRtos_r82ae/build/fvp_r82ae/r82ae_smp_ping_pong_fvp_gcc_armclang.axf EL1S:0
delete breakpoints
b main
b FreeRTOS_Abort
b App_Fault_Handler
```

### Using the Tarmac Trace
Tarmac Trace can identify the instruction that caused an exception. Pass the trace plugin to the run script, then search the resulting log for a synchronous exception event:

```bash
./scripts/run-r82ae.sh \
  --plugin=/opt/arm/developmentstudio_platinum-2025.a/sw/models/bin/TarmacTrace.so \
  -C TRACE.TarmacTrace.trace-file=tarmac.log
grep -B 8 -A 4 'CoreEvent_CURRENT_SPx_SYNC' tarmac.log
```

Inspect the instructions before the event together with `ELR_EL1`, `SPSR_EL1`, and `ESR_EL1`. For coherency failures, enable per-component trace files and MPU events so that you can compare activity across all four cores.

## What you've accomplished and what's next

You've built and validated the FreeRTOS SMP port on a standalone Cortex-R82AE FVP. You also have a raw binary for direct memory loading and an ELF image for source-level debugging.

Next, you'll adapt this known-good port to the Zena CSS Safety Island memory and peripheral map.
