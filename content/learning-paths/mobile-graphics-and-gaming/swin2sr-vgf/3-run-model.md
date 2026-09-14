---
title: Run Swin2SR on your image
description: Build the VGF host runner and use the exported Swin2SR program to save a 128 × 128 image.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the host runner

ExecuTorch's `executor_runner` loads your `.pte` program and executes it. Continue from the same terminal in your `executorch` directory.

If you opened a new terminal, restore the environment first:

```bash
source .venv/bin/activate
source examples/arm/arm-scratch/setup_path.sh
```

Use the repository's build script to enable VGF and the runtime libraries it needs:

```bash
bash backends/arm/scripts/build_executor_runner_vkml.sh \
  --output=swin2sr-work/build
```

This builds a Release executable at `swin2sr-work/build/executor_runner`. You only need to build it once for this walkthrough.

## Upscale the image

Run the image helper with your exported program, the host runner, and the 64 × 64 input:

```bash
python examples/arm/super_resolution_example_vgf/runtime/run_super_resolution.py \
  --model-path swin2sr-work/swin2sr.pte \
  --runner swin2sr-work/build/executor_runner \
  --input-image swin2sr-work/runtime/demo_lr_64.png \
  --output-image swin2sr-work/runtime/demo_sr_128.png
```

The helper converts the image into a tensor, runs the model, and saves the output tensor as a PNG. A successful run ends with `Saved super-resolved image to` followed by the full path to `demo_sr_128.png`.

Your input must be exactly 64 × 64 pixels. If you see an `expected (1, 3, 64, 64)` error, check that you used `demo_lr_64.png`, not the larger reference image.

## What you've accomplished and what's next

You have executed the exported program and saved its 128 × 128 output. Next, open the result and compare it with the input and high-resolution reference.
