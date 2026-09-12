---
title: Export, lower and run the FP32 SmolVLA natively
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Convert the FP32 model

You will now progress through the model conversion pipeline and validate the converted model output.

The artifact will be placed in `artifacts/fp32`. You can override this with:

```bash
export SMOLVLA_ARTIFACTS_DIR=path/to/artifacts/dir
```

### Generate inputs
First, generate the tensor inputs that will be used. We will save them so that they can be re-used for comparisons later:
```bash
python scripts/generate_inputs.py \
    --synthetic-inputs \
    --checkpoint "$SMOLVLA_CHECKPOINT" \
    --output-dir "$SMOLVLA_INPUT_SUITE" \
    --image-size 512 \
    --language-length 48
```
`SMOLVLA_CHECKPOINT` and `SMOLVLA_INPUT_SUITE` are other variables with default paths that you can override.

### Export the model graph
The provided checkpoint uses BF16 for many of its weights, but our ExecuTorch-XNNPACK workflow primarily supports FP16 and FP32. We will convert the model uniformly to FP32 to ensure there is broad backend coverage.

Load the FP32 PyTorch model, split it into `vision`, `prefix` and `denoise`, and export the graphs with `torch.export`:
```bash
python scripts/export.py \
    --checkpoint "$SMOLVLA_CHECKPOINT" \
    --input-suite "$SMOLVLA_INPUT_SUITE" \
    --variant fp32
```

### Partition and lower the model
Convert each graph to ExecuTorch Edge IR, partition supported operators for XNNPACK, lower the graphs and convert them to an ExecuTorch runtime `.pte` format:
```bash
python scripts/lower.py
```

### Validate the export in the Python runtime
We'll quickly check that the model converted correctly using ExecuTorch's portable Python runtime binding.

Convert the input tensors into the serialised format used by the three exports, and check that they collectively reproduce the PyTorch reference output:
```bash
python scripts/prepare_inputs.py
python scripts/validate_pte.py
```

### Build the orchestrator
Our setup built the ExecuTorch runtime with XNNPACK backend and KleidiAI support.

ExecuTorch's generic runner is useful for executing a single `.pte` program. However, invoking it separately for each stage would require intermediate tensors to be written and transferred between processes. Repeatedly launching it for ten denoising steps would also reload the program each time, adding substantial overhead during runtime.

Instead, we'll build a small C++ orchestrator linked against our ExecuTorch runtime. It loads the three exported `.pte` programs, keeps intermediate tensors in memory, connects their I/O, and invokes `denoising_step` 10 times within the same process.
```bash
./scripts/build_runner.sh
```

### Run the model on the target CPU
Your program can now execute on the target using the native runner:
```bash
./scripts/run_runner.sh
```

Validate the native runner output against the original PyTorch reference:
```bash
python scripts/validate_runner.py
```

## What you've accomplished and what's next

You have exported the FP32 SmolVLA and built a native runner to execute it on the target Arm CPU, validating its output.

Next, you'll quantize part of the model to INT8, convert that model to ExecuTorch using this pipeline, and compare it to the FP32 variant through the same native runner.
