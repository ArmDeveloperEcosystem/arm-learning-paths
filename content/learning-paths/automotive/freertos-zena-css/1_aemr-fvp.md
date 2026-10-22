---
title: Build the Cortex-R82 FreeRTOS demo
description: Build and run the existing FreeRTOS SMP MPU demo on the Cortex-R82 AEM FVP before adapting it for Cortex-R82AE.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the existing FreeRTOS demo on the Cortex-R82 AEM FVP

Porting an operating system to a new platform involves changes to startup code, memory maps, interrupts, timers, and peripherals. Before making those changes, reproduce a known-good example on its supported platform. This separates tool installation problems from problems introduced during the port.

You'll build the existing FreeRTOS symmetric multiprocessing (SMP) and Memory Protection Unit (MPU) demo for Cortex-R82. You'll then run it on `FVP_BaseR_AEMv8R` and confirm that the compiler, CMake, FreeRTOS sources, and Fixed Virtual Platform (FVP) work together.

### Before you begin

Ensure that you've installed the following tools and added their executable directories to your `PATH`:

- CMake 3.22.1
- [Arm GNU Toolchain 15.3](https://gitlab.arm.com/tooling/gnu-toolchains-for-arm/-/tree/releases/15.3.rel1?ref_type=heads#linux) or [Arm Compiler for Embedded 6.24](https://support.arm.com/downloads/view/ACOMPE?sortBy=availableBy&revision=r6p24-00rel0)
- [`FVP_BaseR_AEMv8R` from Fast Models 11.32](https://support.arm.com/tools-and-software/fixed-virtual-platforms/arm-architecture-fvps)

You need only one of Arm GNU Toolchain or Arm Compiler for Embedded.

Verify your setup with the following commands, omitting the command for the compiler that you're not using:

```bash
cmake --version
FVP_BaseR_AEMv8R --version
aarch64-none-elf-gcc --version  # GNU build
armclang --version              # Arm Compiler build
```

### Clone the FreeRTOS sources

Clone the FreeRTOS distribution with its submodules:

```bash
git clone --recurse-submodules \
  https://github.com/FreeRTOS/FreeRTOS.git \
  freertos-r82-baseline
cd freertos-r82-baseline
```

The Cortex-R82 demo is supplied by the partner-supported demos submodule. The portable kernel code is supplied by the kernel submodule.

### Review the Cortex-R82 kernel port

The recursive clone initializes the official FreeRTOS Kernel under `FreeRTOS/Source`. The demo selects the portable layer in `FreeRTOS/Source/portable/GCC/ARM_CR82` through the `GCC_ARM_CR82` CMake port name.

Confirm that the Cortex-R82 port files are present:

```bash
ls FreeRTOS/Source/portable/GCC/ARM_CR82
```

The directory contains `port.c`, `portASM.S`, `portmacro.h`, and the MPU wrapper implementation. Together, these files provide the Cortex-R82-specific scheduler, context-switching, interrupt, and MPU support.

<!-- See the [Cortex-R82 portable layer on the `R82AE-demo` branch](https://github.com/JulienJayat-Arm/FreeRTOS-Kernel/tree/R82AE-demo/portable/GCC/ARM_CR82) to review the implementation. Use the complete port directory supplied by the kernel submodule instead of copying an individual file. This keeps the C and assembly implementations synchronized with the rest of the selected kernel revision. -->

### Understand the existing demo

You'll start with a demo that runs FreeRTOS in SMP mode on up to four Cortex-R82 cores. This demo implements a ping/pong-style exchange with three tasks:

- An unprivileged sender places counter values in a shared queue.
- An unprivileged receiver reads the values from the queue.
- A privileged logger prints messages received from both tasks.

The sender and receiver are created with `xTaskCreateRestricted()`. Their MPU configuration grants access only to their stacks and a small shared region containing the queue handles. Kernel data remains accessible only to privileged code.

Unlike the application that you'll use later, the demo doesn't provide an interactive `ping` command. It starts exchanging messages automatically after FreeRTOS starts.

#### Understand the baseline limitations

This initial demo is a useful starting point, but its startup and core-identification code depend on behavior provided by `FVP_BaseR_AEMv8R` configured for `aarch64`. This behavior doesn't strictly follow the Cortex-R82 and Cortex-R82AE specifications.

1. The demo supports entry at Exception Level 1 (EL1) only. Its `fvp_config.txt` file sets `cluster0.has_pl2=0`, so the AEM FVP starts the demo without EL2. The boot code reads `CurrentEL` and enters an error loop unless the value indicates EL1. A platform that starts the cores at EL2 therefore cannot use this startup path unchanged.

2. The demo assumes that the core number is stored in the `Aff0` field of `MPIDR_EL1`. The AEM FVP uses this layout by default through `cluster0.mpidr_layout=0`. The startup code consequently extracts bits `[7:0]` to select the primary core, allocate a per-core stack, and index the secondary-core state.

The Cortex-R82 affinity layout is different:

| `MPIDR_EL1` field | AEM demo assumption | Cortex-R82 definition |
| --- | --- | --- |
| `Aff0`, bits `[7:0]` | Core number | `0`, because each core has one thread |
| `Aff1`, bits `[15:8]` | Not used as the core number | Core number from `0` to `7` |

For the affinity-field definitions, see the [Cortex-R82 MPIDR_EL1 register description](https://support.arm.com/documentation/102670/0002/AArch64-registers/AArch64-register-descriptions/AArch64-Identification-register-description/MPIDR-EL1--Multiprocessor-Affinity-Register).

If the original `MPIDR_EL1 & 0xFF` calculation is used with this layout, every core appears to be core 0. Multiple cores can then perform primary-core initialization, select the same stack, and use incorrect scheduler or interrupt-routing indexes. The Cortex-R82AE port must derive its logical core index from `Aff1` and preserve the complete affinity value when targeting a core with a software-generated interrupt.

3. The demo doesn't use the PL011 UART interface. Instead, it sets `semihosting-enable=1` to print output to the console through semihosting.

### Build the example

Enter the demo directory and build the example with either GCC or Arm Compiler for Embedded. Each compiler uses a separate build directory, which prevents CMake from reusing settings from the other toolchain.

{{< tabpane code=true >}}
  {{< tab header="GCC" language="bash" >}}
cd FreeRTOS/Demo/ThirdParty/Partner-Supported-Demos/CORTEX_R82_SMP_MPU_FVP_GCC_ARMCLANG
cmake -S . -B build_AEMR \
  -DCMAKE_TOOLCHAIN_FILE=gnu_toolchain.cmake
cmake --build build_AEMR --parallel
  {{< /tab >}}
  {{< tab header="Arm Compiler for Embedded" language="bash" >}}
cd FreeRTOS/Demo/ThirdParty/Partner-Supported-Demos/CORTEX_R82_SMP_MPU_FVP_GCC_ARMCLANG
cmake -S . -B build_AEMR_armclang \
  -DCMAKE_TOOLCHAIN_FILE=armclang_toolchain.cmake
cmake --build build_AEMR_armclang --parallel
  {{< /tab >}}
{{< /tabpane >}}

The generated executable is in `build_AEMR` for GCC or `build_AEMR_armclang` for Arm Compiler for Embedded.

### Launch the demo on the AEM FVP

The upstream `run.sh` script expects its default output-directory name. You'll use different build-directory names so that you can launch the executable directly:

{{< tabpane code=true >}}
  {{< tab header="GCC" language="bash" >}}
FVP_BaseR_AEMv8R \
  --application build_AEMR/cortex_r82_smp_mpu_fvp_example.axf \
  --config fvp_config.txt
  {{< /tab >}}
  {{< tab header="Arm Compiler for Embedded" language="bash" >}}
FVP_BaseR_AEMv8R \
  --application build_AEMR_armclang/cortex_r82_smp_mpu_fvp_example.axf \
  --config fvp_config.txt
  {{< /tab >}}
{{< /tabpane >}}

The FVP starts the application and displays sender and receiver activity in the semihosting console. The core numbers depend on how the SMP scheduler assigns the tasks. 

The output is similar to:

```output
[Core: x] Sender: Sent message 0
[Core: y] Receiver: Received message 0
[Core: x] Sender: Sent message 1
[Core: z] Receiver: Received message 1
... (continues) ...
```

Confirm that the message number received by the receiver matches the number sent by the sender. 

Continued output demonstrates that the following components are working together:

- Scheduler
- Timer interrupt
- Interprocessor coordination
- Queues
- MPU-protected shared region 

## What you've accomplished and what's next

You've reproduced the existing Cortex-R82 FreeRTOS example without modifying its platform code. This confirms that your selected compiler, CMake, FreeRTOS source tree, Cortex-R82 portable layer, and AEM FVP are working.

Keep this build as a known-good reference. Next, you'll adapt the example for `FVP_BaseR_Cortex-R82AE`, where you'll address Cortex-R82AE startup behavior. You'll also address platform-specific memory, timer, interrupt, and UART configuration independently of the toolchain setup.
