---
title: Build and run MobileSAM on the Corstone-320 FVP
description: Build the MobileSAM bare-metal application and run prompt segmentation on an Ethos-U85 Fixed Virtual Platform.
weight: 5

layout: "learningpathall"
---

## Build ExecuTorch for Arm

Run the remaining commands from the ExecuTorch repository root.

Load the Arm tools installed during environment setup:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

Configure and install the bare-metal ExecuTorch libraries:

```bash
cmake --preset arm-baremetal \
  -DCMAKE_BUILD_TYPE=Release \
  -B cmake-out-arm
cmake --build cmake-out-arm --target install --parallel
```

The installed libraries provide the ExecuTorch runtime, Ethos-U backend, and kernels needed by the example application.

## Build the MobileSAM application

Configure the application with the Arm GNU bare-metal toolchain:

```bash
cmake \
  -S examples/arm/mobilesam_prompt_segmentation_example_ethos_u/runtime \
  -B arm_test/mobilesam_manual/runtime \
  -DCMAKE_TOOLCHAIN_FILE="$PWD/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
  -DET_BUILD_DIR_PATH="$PWD/cmake-out-arm" \
  -DET_PTE_FILE_PATH="$PWD/arm_test/mobilesam_manual/export/mobilesam_point_ethos_u85_448.pte" \
  -DMODEL_METADATA_PATH="$PWD/arm_test/mobilesam_manual/export/mobilesam_point_ethos_u85_448.json" \
  -DIMAGE_PATH="$PWD/examples/models/dinov2/dog.jpg" \
  -DMASK_THRESHOLD=0.0 \
  -DET_SEGMENTATION_DUMP_MASK=ON \
  -DPYTHON_EXECUTABLE="$(command -v python)"
```

The configuration embeds the `.pte` and image in the bare-metal application. Mask output is enabled for later visualization.

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

A successful run ends with `Model executed successfully.`, followed by `No problems found!`. The run writes the complete target output to `arm_test/mobilesam_manual/fvp.log`.

## What you've accomplished and what's next

You've built the MobileSAM bare-metal application and run it on a virtual Cortex-M85 and Ethos-U85 system.

Next, you'll reconstruct the target mask and compare it with the host result.
