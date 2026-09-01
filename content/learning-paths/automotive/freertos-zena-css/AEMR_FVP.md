---
title: Build the Cortex-R82  FreeRTOS demo
description: Build and run the existing FreeRTOS SMP MPU demo on the Cortex-R82 AEM FVP before adapting it for Cortex-R82AE.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Run the existing FreeRTOS demo on the Cortex-R82 AEM FVP

## Objective

Porting an operating system to a new platform involves changes to startup code, memory maps, interrupts, timers, and peripherals. Before making those changes, reproduce a known-good example on its supported platform. This separates tool installation problems from problems introduced during the port.

You will build the existing FreeRTOS symmetric multiprocessing (SMP) and Memory Protection Unit (MPU) demo for Cortex-R82. You will then run it on `FVP_BaseR_AEMv8R` and confirm that the compiler, CMake, FreeRTOS sources, and FVP work together.

After completing this section, you will have verified that:

- The FreeRTOS distribution and all required submodules are available
- The selected Arm toolchain can build the Cortex-R82 port
- The Cortex-R82 AEM FVP can load and run the generated executable
- FreeRTOS SMP scheduling and MPU-protected task communication operate correctly
- The existing example provides a working baseline for the Cortex-R82AE port

## Before you begin

The upstream example is tested with these tools:

- Arm GNU Toolchain 15.2
- Arm Compiler for Embedded 6.24
- CMake
- `FVP_BaseR_AEMv8R` from Fast Models 11.28.23

Use either the GNU toolchain or Arm Compiler for Embedded. Building with both is useful if you plan to support both compilers during the port.

The example and its tested tool versions are documented in the [Cortex-R82 SMP MPU demo README](https://github.com/JulienJayat-Arm/FreeRTOS-Partner-Supported-Demos/blob/R82AE-demo/CORTEX_R82_SMP_MPU_FVP_GCC_ARMCLANG/README.md).

Verify that CMake and the FVP are available:

```bash
cmake --version
FVP_BaseR_AEMv8R --version
```

For a GNU build, also verify the cross-compiler:

```bash
aarch64-none-elf-gcc --version
```

For an Arm Compiler build, verify `armclang` instead:

```bash
armclang --version
```

If a command isn't found, install the missing tool and add its executable directory to your `PATH` before continuing.

## Get the FreeRTOS sources

Clone the FreeRTOS distribution with its submodules. The Cortex-R82 demo is supplied by the partner-supported demos submodule, while the portable kernel code is supplied by the kernel submodule.

```bash
git clone --recurse-submodules \
  https://github.com/FreeRTOS/FreeRTOS.git \
  freertos-r82-baseline
cd freertos-r82-baseline
```

Downloading the repository as a ZIP file does not include its submodules. If you already cloned the repository without `--recurse-submodules`, initialize them now:

```bash
git submodule update --init --recursive
```

## Review the Cortex-R82 kernel port

The recursive clone initializes the official FreeRTOS Kernel under `FreeRTOS/Source`. The demo selects the portable layer in `FreeRTOS/Source/portable/GCC/ARM_CR82` through the `GCC_ARM_CR82` CMake port name.

Confirm that the Cortex-R82 port files are present:

```bash
ls FreeRTOS/Source/portable/GCC/ARM_CR82
```

The directory contains `port.c`, `portASM.S`, `portmacro.h`, and the MPU wrapper implementation. Together, these files provide the Cortex-R82-specific scheduler, context-switching, interrupt, and MPU support.

See the [Cortex-R82 portable layer on the `R82AE-demo` branch](https://github.com/JulienJayat-Arm/FreeRTOS-Kernel/tree/R82AE-demo/portable/GCC/ARM_CR82) to review the implementation. Use the complete port directory supplied by the kernel submodule instead of copying an individual file. This keeps the C and assembly implementations synchronized with the rest of the selected kernel revision.

## Understand the existing demo

The example runs FreeRTOS in SMP mode on up to four Cortex-R82 cores. The current upstream example implements a ping/pong-style exchange with three tasks:

- An unprivileged sender places counter values in a shared queue
- An unprivileged receiver reads the values from the queue
- A privileged logger prints messages received from both tasks

The sender and receiver are created with `xTaskCreateRestricted()`. Their MPU configuration grants access only to their stacks and a small shared region containing the queue handles. Kernel data remains accessible only to privileged code.

Unlike the application used later in this Learning Path, this example does not provide an interactive `ping` command. It starts exchanging messages automatically after FreeRTOS starts.

### Understand the baseline limitations

The example is a useful starting point, but its startup and core-identification code depend on behavior provided by `FVP_BaseR_AEMv8R` configured for `aarch64` but is not strictly following the Cortex-R82 and Cortex-R82AE specification.

First, the example supports entry at Exception Level 1 (EL1) only. Its `fvp_config.txt` file sets `cluster0.has_pl2=0`, so the AEM FVP starts the application without EL2. The boot code reads `CurrentEL` and enters an error loop unless the value indicates EL1. A platform that starts the cores at EL2 therefore cannot use this startup path unchanged. 

Second, the example assumes that the core number is stored in the `Aff0` field of `MPIDR_EL1`. The AEM FVP uses this layout by default through `cluster0.mpidr_layout=0`. The startup code consequently extracts bits `[7:0]` to select the primary core, allocate a per-core stack, and index the secondary-core state.

The Cortex-R82 affinity layout is different:

| `MPIDR_EL1` field | AEM demo assumption | Cortex-R82 definition |
| --- | --- | --- |
| `Aff0`, bits `[7:0]` | Core number | `0`, because each core has one thread |
| `Aff1`, bits `[15:8]` | Not used as the core number | Core number from `0` to `7` |

See the [Cortex-R82 `MPIDR_EL1` register description](https://support.arm.com/documentation/102670/0002/AArch64-registers/AArch64-register-descriptions/AArch64-Identification-register-description/MPIDR-EL1--Multiprocessor-Affinity-Register) for the affinity-field definitions.

If the original `MPIDR_EL1 & 0xFF` calculation is used with this layout, every core appears to be core 0. Multiple cores can then perform primary-core initialization, select the same stack, and use incorrect scheduler or interrupt-routing indexes. The Cortex-R82AE port must derive its logical core index from `Aff1` and preserve the complete affinity value when targeting a core with a software-generated interrupt.


## Build with the GNU toolchain

Enter the demo directory:

```bash
cd FreeRTOS/Demo/ThirdParty/Partner-Supported-Demos/CORTEX_R82_SMP_MPU_FVP_GCC_ARMCLANG
```

Configure a GNU build. The supplied toolchain file selects `aarch64-none-elf-gcc` and enables Cortex-R82 code generation:

```bash
cmake -S . -B build_AEMR \
  -DCMAKE_TOOLCHAIN_FILE=gnu_toolchain.cmake
```

Build the executable:

```bash
cmake --build build_AEMR --parallel
```

The generated executable is:

```output
build_AEMR/cortex_r82_smp_mpu_fvp_example.axf
```

## Build with Arm Compiler for Embedded

If you want to validate the Arm Compiler toolchain as well, configure a separate build directory. Keeping separate directories prevents CMake from reusing settings from another compiler.

```bash
cmake -S . -B build_AEMR_armclang \
  -DCMAKE_TOOLCHAIN_FILE=armclang_toolchain.cmake
cmake --build build_AEMR_armclang --parallel
```

The Arm Compiler build creates:

```output
build_AEMR_armclang/cortex_r82_smp_mpu_fvp_example.axf
```

## Run the demo on the AEM FVP

The upstream `run.sh` script expects its default output-directory name. Because this Learning Path uses `build_AEMR`, launch the GNU executable directly:

```bash
FVP_BaseR_AEMv8R \
  --application build_AEMR/cortex_r82_smp_mpu_fvp_example.axf \
  --config fvp_config.txt
```

To run the Arm Compiler build, specify its executable directly:

```bash
FVP_BaseR_AEMv8R \
  --application build_AEMR_armclang/cortex_r82_smp_mpu_fvp_example.axf \
  --config fvp_config.txt
```

The FVP starts the application and displays sender and receiver activity. The core numbers depend on how the SMP scheduler assigns the tasks. The output is similar to:

```output
[Core: x] Sender: Sent message 0
[Core: y] Receiver: Received message 0
[Core: x] Sender: Sent message 1
[Core: z] Receiver: Received message 1
... (continues) ...
```

Confirm that the message number received by the receiver matches the number sent by the sender. Continued output demonstrates that the scheduler, timer interrupt, interprocessor coordination, queues, and MPU-protected shared region are working together.

{{% notice Note %}}
The example assumes that `FVP_BaseR_AEMv8R` provides fully coherent caches. A target without full cache coherency needs suitable memory attributes or explicit cache maintenance for shared data.
{{% /notice %}}

## What you've accomplished and what's next

You've reproduced the existing Cortex-R82 FreeRTOS example without modifying its platform code. This confirms that your selected compiler, CMake, FreeRTOS source tree, Cortex-R82 portable layer, and AEM FVP are working.

Keep this build as a known-good reference. Next, you will adapt the example for `FVP_BaseR_Cortex-R82AE`, where you can address Cortex-R82AE startup behavior and platform-specific memory, timer, interrupt, and UART configuration independently of the toolchain setup.
