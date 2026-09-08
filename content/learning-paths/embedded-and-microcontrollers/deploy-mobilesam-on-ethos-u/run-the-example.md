---
title: Build and run MobileSAM on the Corstone-320 FVP
description: Build the MobileSAM bare-metal application and run prompt segmentation on an Ethos-U85 Fixed Virtual Platform.
weight: 5

layout: "learningpathall"
---

## Build ExecuTorch for Arm

Run the remaining commands from the ExecuTorch repository root. Load the Arm tools installed during environment setup:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

Configure and install the bare-metal ExecuTorch libraries:

```bash
cmake --preset arm-baremetal -B cmake-out-arm
cmake --build cmake-out-arm --target install --parallel
```

The installed libraries provide the ExecuTorch runtime, Ethos-U backend, and kernels needed by the example application.

## Build the MobileSAM application

Configure the application with the Arm GNU bare-metal toolchain:

```bash
cmake \
  -S examples/arm/mobilesam_prompt_segmentation_example_ethos_u/runtime \
  -B arm_test/mobilesam_manual/runtime \
  -DCMAKE_TOOLCHAIN_FILE="$PWD/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake"
```

The example defaults select the `.pte`, metadata, and image produced by the export step. Mask output is enabled for later visualization.

Build the application Executable and Linkable Format (ELF) file:

```bash
cmake --build arm_test/mobilesam_manual/runtime \
  --target mobilesam_prompt_segmentation_example --parallel
```

The build writes `arm_test/mobilesam_manual/runtime/mobilesam_prompt_segmentation_example`.

## Run the application on the FVP

Enable pipeline failure reporting, then run the ELF on the Corstone-320 Fixed Virtual Platform (FVP):

```bash
set -o pipefail

backends/arm/scripts/run_fvp.sh \
  --elf=arm_test/mobilesam_manual/runtime/mobilesam_prompt_segmentation_example \
  --target=ethos-u85-256 \
  --timeout=300 \
  --semihosting-cwd=arm_test/mobilesam_manual/runtime \
  --fast 2>&1 | tee arm_test/mobilesam_manual/fvp.log
```

A successful run ends with `Model executed successfully.` and writes the complete target output to `arm_test/mobilesam_manual/fvp.log`.

## What you've accomplished

You have built the MobileSAM bare-metal application and run it on a virtual Cortex-M85 and Ethos-U85 system. Next, you will reconstruct the target mask and compare it with the host result.
