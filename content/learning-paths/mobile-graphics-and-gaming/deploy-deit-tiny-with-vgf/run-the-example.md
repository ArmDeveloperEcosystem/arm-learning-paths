---
title: Classify a pet image and verify VGF execution
description: Run a pet image through your VGF-backed ExecuTorch program, inspect the predicted breed, and confirm successful host execution.
weight: 6
layout: "learningpathall"
aliases:
    - /learning-paths/mobile-graphics-and-gaming/deploy-deit-tiny-with-vgf/validate-the-results/
---

## Prepare a pet image

Keep your Python environment active and `setup_path.sh` sourced. Use the Learning Path helper to prepare the first image in the dataset's test split:

```bash
python arm_test/deit_vgf/deit_vgf_helper.py prepare
```

The helper uses the same pinned image processor as the exporter. It saves `input.bin`, `input.jpg`, and `reference.json` under `arm_test/deit_vgf/`.

`input.bin` contains the normalized float32 tensor in `[1, 3, 224, 224]` batch, channel, height, width order. The runner reads this tensor, not the JPEG. Open `input.jpg` in an image viewer to inspect the pet you will classify.

## Run inference through VGF

Execute the exported program with your input file and save the output scores:

```bash
set -o pipefail
./cmake-out-deit-vgf/executor_runner \
  --model_path=arm_test/deit_vgf/deit_quantized_vgf.pte \
  --inputs=arm_test/deit_vgf/input.bin \
  --output_file=arm_test/deit_vgf/prediction \
  2>&1 | tee arm_test/deit_vgf/runtime.log
```

A successful run reports `Model executed successfully` and writes `arm_test/deit_vgf/prediction-0.bin`. The runner appends `-0.bin` for the first output tensor.

Keep `--inputs`: without it, the generic runner fills the input tensor with ones instead of classifying your pet image.

## Inspect the breed prediction

Decode the saved scores and verify VGF execution:

```bash
python arm_test/deit_vgf/deit_vgf_helper.py inspect
```

The helper checks for 37 finite output scores, then maps the largest score to a breed. It prints `Expected breed`, `VGF prediction`, and `Matches dataset label`. It also checks the runtime log for `Entered VGF init` and `Model executed successfully` before reporting `VGF execution: confirmed`.

A valid prediction and confirmed VGF execution complete the deployment workflow. A matching dataset label means the model recognizes this image; a mismatch does not by itself indicate a deployment failure.

{{% notice Note %}}
One image does not measure dataset accuracy. The export log reports quantized PyTorch accuracy, not VGF accuracy across the test set. This host emulation run also does not establish performance on an Arm GPU.
{{% /notice %}}

## Optional: compare with the floating-point model

Run the original fine-tuned model on the same input and compare its winning class with the VGF result:

```bash
python arm_test/deit_vgf/deit_vgf_helper.py inspect --compare-fp32
```

The helper adds the floating-point prediction and whether the two predictions match. Quantization can change the winning class. Compare more images before drawing conclusions about accuracy or numerical equivalence.

To classify another test image, repeat `prepare` with `--sample-index 1`, then rerun inference and inspection. Each preparation replaces the previous input artifacts. The helper rejects predictions and logs that predate the prepared image, so you must rerun `executor_runner` before inspecting a new image.

## What you've accomplished

You have fine-tuned DeiT-Tiny, exported a VGF-backed program, and classified a pet image with the host runtime. Your model, input, prediction, and logs are in `arm_test/deit_vgf/`. You can now reuse the `.pte` to classify other test images.
