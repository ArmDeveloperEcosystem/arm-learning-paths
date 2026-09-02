---
title: Build and run the Corstone-320 application
description: Build the bare-metal ExecuTorch application and run Silero VAD on the Corstone-320 Fixed Virtual Platform.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand this stage

You already have the exported model and validation audio. This stage packages both into a bare-metal application and runs it on a virtual Cortex-M85 and Ethos-U85 system.

## 1. Build ExecuTorch for Cortex-M85

Continue from the ExecuTorch repository root. Activate the environment and build the target libraries:

```bash
source .venv/bin/activate
source examples/arm/arm-scratch/setup_path.sh

cmake --preset arm-baremetal -B cmake-out-arm
cmake --build cmake-out-arm --target install --parallel
```

The installed libraries provide the ExecuTorch runtime, portable operators, and Ethos-U backend used by the application.

## 2. Build the Silero VAD application

Configure the application with the exported model, validation audio, and a speech threshold of `0.55`. Select your host operating system:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="shell" >}}
cmake \
  -S examples/arm/silero_vad_example_ethos_u/runtime \
  -B silero-vad-work/app \
  -DCMAKE_TOOLCHAIN_FILE="$PWD/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
  -DTARGET_CPU=cortex-m85 \
  -DET_PTE_FILE_PATH="$PWD/silero-vad-work/export/silero_vad_ethos_u.pte" \
  -DAUDIO_PATH="$PWD/silero-vad-work/assets/validation.wav" \
  -DVAD_THRESHOLD=0.55
  {{< /tab >}}
  {{< tab header="macOS" language="shell" >}}
cmake \
  -S examples/arm/silero_vad_example_ethos_u/runtime \
  -B silero-vad-work/app \
  -DCMAKE_TOOLCHAIN_FILE="$PWD/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
  -DTARGET_CPU=cortex-m85 \
  -DET_PTE_FILE_PATH="$PWD/silero-vad-work/export/silero_vad_ethos_u.pte" \
  -DAUDIO_PATH="$PWD/silero-vad-work/assets/validation.wav" \
  -DVAD_THRESHOLD=0.55 \
  -DUART0_BASE=0x49303000
  {{< /tab >}}
{{< /tabpane >}}

Build the configured application:

```bash
cmake --build silero-vad-work/app \
  --target silero_vad_ethos_u --parallel
```

The build creates `silero-vad-work/app/silero_vad_ethos_u`. This ELF image contains both the `.pte` model and the 2.5-second validation clip.

## 3. Run Silero VAD on the FVP

Run the application and save its simulated UART output to `fvp.log`:

```bash
mkdir -p silero-vad-work/fvp
bash backends/arm/scripts/run_fvp.sh \
  --elf=silero-vad-work/app/silero_vad_ethos_u \
  --target=ethos-u85-256 \
  --timeout=300 2>&1 | tee silero-vad-work/fvp/fvp.log
```

The application prints one speech probability every 32 ms. Near the end, it reports a summary and stops the simulation:

```output
1 segments, 79 frames, 2.5s
Speech: 57/79 frames (72.2%)
Simulation complete, 0
No problems found!
```

## Check the target artifacts

Confirm that the application and its serial log exist:

```bash
ls -lh \
  silero-vad-work/app/silero_vad_ethos_u \
  silero-vad-work/fvp/fvp.log
```

## What you've accomplished and what's next

You have run the stateful Silero VAD model on a virtual Cortex-M85 and Ethos-U85 target.

Next, inspect the speech decisions and compare them with the host reference.
