---
title: Build and run MobileSAM on the Corstone-320 FVP
description: Build the standard Arm executor runner and run MobileSAM prompt segmentation on an Ethos-U85 Fixed Virtual Platform.
weight: 5

layout: "learningpathall"
---

## Build the Arm executor runner

Run the remaining commands from the ExecuTorch repository root.

Load the Arm tools installed during environment setup:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

Build the standard Arm executor runner with the exported MobileSAM program:

```bash
backends/arm/scripts/build_executor_runner.sh \
  --pte=arm_test/mobilesam/export/mobilesam.pte \
  --target=ethos-u85-256 \
  --output=arm_test/mobilesam/runner \
  '--extra_build_flags=-DSEMIHOSTING=ON -DET_COMPILED_PTE=ON'
```

The script builds the required ExecuTorch libraries and the runner for Corstone-320. `ET_COMPILED_PTE=ON` embeds `mobilesam.pte` in the Executable and Linkable Format (ELF) file named `arm_executor_runner`, under `arm_test/mobilesam/runner/`.

`SEMIHOSTING=ON` lets the simulated target read input tensors from host files and write its output tensors back to the host.

## Prepare the target input

Copy the preprocessed image tensor into the directory used for target input and output. Remove any output from an earlier run so that validation uses a fresh result:

```bash
mkdir -p arm_test/mobilesam/io
cp arm_test/mobilesam/export/input.bin arm_test/mobilesam/io/input.bin
rm -f arm_test/mobilesam/io/output-0.bin
```

The runner reads `input.bin` at runtime. The image is not compiled into the ELF.

## Run the application on the FVP

On macOS, the FVPs-on-Mac wrapper needs access to the repository files inside its container. Set its mount and working directories from the ExecuTorch repository root, preserving any existing configuration:

```bash
if [[ "$(uname -s)" == "Darwin" ]]; then
  export FVP_MOUNT_DIR="${FVP_MOUNT_DIR:-$PWD}"
  export FVP_WORKDIR="${FVP_WORKDIR:-$PWD}"
fi
```

Enable pipeline failure reporting, then run the ELF on the Corstone-320 Fixed Virtual Platform (FVP):

```bash
set -o pipefail

backends/arm/scripts/run_fvp.sh \
  --elf=arm_test/mobilesam/runner/arm_executor_runner \
  --target=ethos-u85-256 \
  --timeout=300 \
  --semihosting-cwd=arm_test/mobilesam/io \
  '--semihosting-cmd-line=executor_runner -i input.bin -o output' \
  --fast 2>&1 | tee arm_test/mobilesam/fvp.log
```

The runner reads the tensor specified by `-i input.bin` and writes its first output tensor to `output-0.bin` under `arm_test/mobilesam/io/`. The console transcript is saved to `arm_test/mobilesam/fvp.log`; validation reads the tensor file.

Confirm that the run created the output file before continuing:

```bash
test -s arm_test/mobilesam/io/output-0.bin
```

The check exits successfully without printing anything when the file exists and is not empty. The next page checks its shape and segmentation agreement.

## What you've accomplished and what's next

You've built the Arm executor runner with MobileSAM and run it on a virtual Cortex-M85 and Ethos-U85 system.

Next, you'll reconstruct the target mask and compare it with the host result.
