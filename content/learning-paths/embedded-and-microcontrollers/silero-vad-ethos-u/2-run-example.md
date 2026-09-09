---
title: Export Silero VAD for Ethos-U85
description: Quantize Silero VAD and export a stateful ExecuTorch program for the Ethos-U85 NPU.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Export the model

You prepared the model and two audio clips on the previous page. Now use the calibration clip to quantize Silero VAD and the validation clip to create a host reference.

From the ExecuTorch repository root, activate the environment:

```bash
source .venv/bin/activate
source examples/arm/arm-scratch/setup_path.sh
```

## Build the host quantized operators

The exporter requires the host shared library that registers the quantized operator out variants. Build it before exporting the model:

```bash
cmake \
  -S . \
  -B silero-vad-work/quantized_ops_aot \
  -DCMAKE_BUILD_TYPE=Release \
  -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
  -DEXECUTORCH_BUILD_KERNELS_QUANTIZED_AOT=ON \
  -DEXECUTORCH_BUILD_XNNPACK=OFF \
  -DPYTHON_EXECUTABLE="$(command -v python)"

cmake --build silero-vad-work/quantized_ops_aot \
  --target quantized_ops_aot_lib --parallel

export EXECUTORCH_QUANTIZED_OPS_AOT_LIBRARY="$(find \
  silero-vad-work/quantized_ops_aot/kernels/quantized \
  -name 'libquantized_ops_aot_lib.*' -type f -print -quit)"
test -s "$EXECUTORCH_QUANTIZED_OPS_AOT_LIBRARY"
```

## Export the model

Run the exporter and save its output for the delegation check:

```bash
set -o pipefail

python3 examples/arm/silero_vad_example_ethos_u/model_export/export_silero_vad_ethos_u.py \
  --jit-model silero-vad-work/assets/silero_vad.jit \
  --calibration-audio silero-vad-work/assets/calibration.wav \
  --validation-audio silero-vad-work/assets/validation.wav \
  --output-path silero-vad-work/export/silero_vad_ethos_u.pte \
  --expected-output-path silero-vad-work/export/expected_probs.bin \
  --num-calibration-frames 32 \
  --num-validation-frames 0 2>&1 | \
  tee silero-vad-work/export/export.log
```

The final messages are similar to:

```output
Wrote expected probabilities to silero-vad-work/export/expected_probs.bin
Lowering to Ethos-U85...
Exported model saved to silero-vad-work/export/silero_vad_ethos_u.pte
```

Verify the generated outputs and the number of reference probabilities:

```bash
for artifact in \
  silero-vad-work/export/silero_vad_ethos_u.pte \
  silero-vad-work/export/expected_probs.bin \
  silero-vad-work/export/export.log; do
  test -s "$artifact" || {
    echo "Missing export artifact: $artifact" >&2
    exit 1
  }
done

test "$(wc -c < silero-vad-work/export/expected_probs.bin)" -eq $((79 * 4)) || {
  echo "Expected 79 float32 reference probabilities" >&2
  exit 1
}

test "$(grep -c 'CPU operators = 0' silero-vad-work/export/export.log)" -eq 2 || {
  echo "Expected both Vela subgraphs to contain no CPU operators" >&2
  exit 1
}

echo "Export artifacts and Ethos-U lowering verified."
```

## Understand the streaming model

The application supplies one 512-sample audio frame at a time. The exported program keeps the LSTM hidden and cell state between calls and produces one speech probability every 32 ms.

![Runtime diagram showing 64 context samples and a 512-sample frame entering the ExecuTorch program, model operations delegated to Ethos-U85, an internal int8 hidden and cell state reused between calls, and one speech probability emitted every 32 ms.#center](silero-vad-streaming-delegation.svg "Silero VAD streaming state and Ethos-U delegation boundary")

The Vela output contains two subgraphs with no CPU operators: the main VAD network and a smaller state-quantization subgraph. Only small boundary conversions and the state update remain as portable ExecuTorch operations.

## What you've accomplished and what's next

You have exported Silero VAD as a stateful ExecuTorch program and saved the host reference output.

Next, build the bare-metal application and run it on the Corstone-320 FVP.
