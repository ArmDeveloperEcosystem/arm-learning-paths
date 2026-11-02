---
title: Build and run the Corstone-320 application
description: Build the bare-metal ExecuTorch application and run Silero VAD on the Corstone-320 Fixed Virtual Platform.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build ExecuTorch for Cortex-M85

You already have the exported model and validation audio. You'll package both the model and audio into a bare-metal application and run the application on a virtual Cortex-M85 and Ethos-U85 system.

Start by building ExecuTorch for Cortex-M85.

Continue from the ExecuTorch repository root. Activate the environment and build the target libraries:

```bash
source .venv/bin/activate
source examples/arm/arm-scratch/setup_path.sh
if [ "$(uname -s)" = Darwin ]; then
  export PATH="$PWD/examples/arm/arm-scratch/FVPs-on-Mac/bin:$PATH"
  export FVP_MOUNT_DIR="$PWD"
fi

cmake --preset arm-baremetal \
  -DCMAKE_BUILD_TYPE=Release \
  -DTARGET_CPU=cortex-m85 \
  -B cmake-out-arm -S .
cmake --build cmake-out-arm --target install --parallel 2
```

The installed libraries provide the ExecuTorch runtime, portable operators, and Ethos-U backend used by the application.

## Build the Silero VAD application

Configure the application with the exported model, validation audio, and the default speech threshold of `0.5`. The command selects the UART address required by FVPs-on-Mac:

```bash
runtime_cmake_args=()
if [ "$(uname -s)" = Darwin ]; then
  runtime_cmake_args+=(-DUART0_BASE=0x49303000)
fi

cmake \
  "${runtime_cmake_args[@]}" \
  -DCMAKE_TOOLCHAIN_FILE="$PWD/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
  -DCMAKE_BUILD_TYPE=Release \
  -DTARGET_CPU=cortex-m85 \
  -DET_PTE_FILE_PATH="$PWD/silero_vad_ethos_u.pte" \
  -DAUDIO_PATH="$PWD/silero-vad/validation.wav" \
  -B examples/arm/silero_vad_ethos_u \
  -S examples/arm/silero_vad_example_ethos_u/runtime
```

Build the configured application:

```bash
cmake --build examples/arm/silero_vad_ethos_u \
  --target silero_vad_ethos_u --parallel 2
```

The build creates `examples/arm/silero_vad_ethos_u/silero_vad_ethos_u`. This ELF image contains both the `.pte` model and the 2.5-second validation clip.

## Run Silero VAD on the FVP

Run the application and save its simulated UART output to `fvp.log`:

```bash
set -o pipefail
bash backends/arm/scripts/run_fvp.sh \
  --elf=examples/arm/silero_vad_ethos_u/silero_vad_ethos_u \
  --target=ethos-u85-256 \
  --timeout=300 2>&1 | tee fvp.log
```

The application processes one audio frame every 32 ms of recording time, then prints the probabilities and a summary. The output is similar to:

```output
2 segments, 79 frames, 2.5s
Speech: 56/79 frames (70.9%)
Model executed successfully.
Simulation complete, 0
No problems found!
```

## Check the target artifacts

Confirm that the application and its serial log exist:

```bash
for artifact in \
  examples/arm/silero_vad_ethos_u/silero_vad_ethos_u \
  fvp.log; do
  test -s "$artifact" || {
    echo "Missing target artifact: $artifact" >&2
    exit 1
  }
done

echo "Target artifacts verified."
```

## What you've accomplished and what's next

You've run the stateful Silero VAD model on a virtual Cortex-M85 and Ethos-U85 target.

Next, you'll inspect the speech decisions and compare them with the host reference.
