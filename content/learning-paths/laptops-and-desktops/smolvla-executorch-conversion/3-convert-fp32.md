---
title: Export, lower, and run the FP32 SmolVLA
description: Export, lower, and validate the FP32 SmolVLA components with ExecuTorch, then run them through a native Arm CPU orchestrator.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Convert the FP32 model

You'll now work through the model conversion pipeline and validate the converted model output.

The scripts place the artifacts in `artifacts/fp32` by default. To use a different location, set `SMOLVLA_ARTIFACTS_DIR` to an absolute path:

```bash
export SMOLVLA_ARTIFACTS_DIR="/path/to/artifacts/dir"
```

If you override the path, use the same location in the FP32 benchmark command later.

### Generate inputs

First, generate and save deterministic tensor inputs. You'll reuse the inputs when you compare the FP32 and INT8 models:

```bash
python scripts/generate_inputs.py \
    --synthetic-inputs \
    --checkpoint "$SMOLVLA_CHECKPOINT" \
    --output-dir "$SMOLVLA_INPUT_SUITE" \
    --image-size 512 \
    --language-length 48
```

The `env.sh` file sets default paths for `SMOLVLA_CHECKPOINT` and `SMOLVLA_INPUT_SUITE`. You can override the paths in the same way.

### Export the model graph

The checkpoint stores many weights in BF16, but this ExecuTorch and XNNPACK workflow primarily supports FP16 and FP32. Convert the model to FP32 to provide broad backend coverage.

Load the FP32 PyTorch model, split it into `vision`, `prefix` and `denoise`, and export the graphs with `torch.export`:

```bash
python scripts/export.py \
    --checkpoint "$SMOLVLA_CHECKPOINT" \
    --input-suite "$SMOLVLA_INPUT_SUITE" \
    --variant fp32
```

### Partition and lower the model

Convert each graph to ExecuTorch Edge IR, partition supported operators for XNNPACK, lower the graphs, and convert them to an ExecuTorch runtime `.pte` format:

```bash
python scripts/lower.py
```

### Validate the export in the Python runtime

Check that the model converted correctly with ExecuTorch's portable Python runtime binding.

Convert the input tensors into the serialized format used by the three exports:

```bash
python scripts/prepare_inputs.py
python scripts/validate_pte.py
```

After conversion, check that the exports collectively reproduce the PyTorch reference output.

The expected output is similar to:

```output
Accuracy gate passed; report: /path/to/artifacts/fp32/validation.json
```

### Build the orchestrator

The setup built the ExecuTorch runtime with the XNNPACK backend and KleidiAI support.

ExecuTorch's generic runner executes a single `.pte` program. Invoking the program separately for each stage would write and transfer intermediate tensors between processes. Repeatedly launching the program for ten denoising steps would also reload it each time, adding runtime overhead.

Build the provided C++ orchestrator and link it against the ExecuTorch runtime:

```bash
./scripts/build_runner.sh
```
The orchestrator loads the three exported `.pte` programs and keeps intermediate tensors in memory. It connects their inputs and outputs, then invokes `denoising_step` ten times in the same process.

## Run the model on the target CPU

Run the model on the target Arm CPU with the native runner:

```bash
./scripts/run_runner.sh
```

Validate the native runner output against the original PyTorch reference:

```bash
python scripts/validate_runner.py
```

The expected output ends with:

```output
Native split orchestrator output matches the full PyTorch reference.
```

## What you've accomplished and what's next

You've exported the FP32 SmolVLA, built a native runner for the target Arm CPU, and validated its output.

Next, you'll quantize part of the model to INT8 and convert that model to ExecuTorch using the pipeline. You'll then compare it to the FP32 variant through the same native runner.
