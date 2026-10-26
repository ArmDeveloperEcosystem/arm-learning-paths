---
title: Export MobileSAM for Ethos-U85
description: Prepare MobileSAM, quantize the model, and export a fixed-prompt ExecuTorch program for Ethos-U85.
weight: 4

layout: "learningpathall"
---

## Prepare the MobileSAM source and checkpoint

Run all commands from the ExecuTorch repository root. Confirm that your Python environment is active and that you've sourced the Arm tools' `setup_path.sh` file in the current shell, as shown during environment setup.

Prepare the pinned MobileSAM source and checkpoint:

```bash
python3 examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/prepare_mobilesam.py
```

The script downloads the [pinned MobileSAM revision](https://github.com/ChaoningZhang/MobileSAM/tree/f706ad9c4eb7f219c00d9050e46328518ffb65d2), applies the patch needed for a configurable image size, and verifies the checkpoint's SHA-256 checksum. It stores the source in `source/` and the checkpoint in `mobile_sam.pt`, outside the ExecuTorch repository. The cache directory is:

```text
~/.cache/executorch/mobilesam/f706ad9c4eb7f219c00d9050e46328518ffb65d2/
```

## Export the ExecuTorch program

Export the example image and positive point prompt for the `ethos-u85-256` target:

```bash
python3 examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/export_mobilesam.py
```

The exporter loads the prepared checkpoint, calibrates post-training quantization with the example image, checks the quantized mask against the floating-point mask, and lowers the graph to Ethos-U85.

This script uses one fixed configuration: `examples/models/dinov2/dog.jpg`, positive point `(219, 193)`, input size `448`, target `ethos-u85-256`, and memory mode `Dedicated_Sram_384KB`. These values are set in the Python source rather than through command-line arguments.

Export requires a host mask intersection over union (IoU) of at least `0.9` and exactly one Ethos-U delegated subgraph. It writes `mobilesam.pte` to `arm_test/mobilesam/export/`.

## Verify the export artifacts

The files under `arm_test/mobilesam/export/` support the remaining steps:

| Artifact | Path |
|---|---|
| ExecuTorch program | `mobilesam.pte` |
| Preprocessed float32 input tensor | `input.bin` |
| Resized and padded input image | `input.png` |
| Floating-point host mask | `fp32_mask.png` |
| Quantized host mask | `quantized_mask.png` |
| Host mask metrics | `metrics.json` |
| Delegation report | `delegation.txt` |
| TOSA and Vela artifacts | `artifacts/` |

Check that these artifacts exist before building the runner:

```bash
export_dir=arm_test/mobilesam/export

for artifact in \
  mobilesam.pte \
  input.bin \
  input.png \
  fp32_mask.png \
  quantized_mask.png \
  metrics.json \
  delegation.txt; do
  test -s "$export_dir/$artifact" || {
    echo "Missing export artifact: $export_dir/$artifact" >&2
    exit 1
  }
done

test -n "$(find "$export_dir/artifacts" -type f -print -quit)" || {
  echo "No TOSA or Vela artifacts found in $export_dir/artifacts" >&2
  exit 1
}
```

The checks complete without output when the artifacts are present. The point prompt is embedded in the `.pte`, which is compiled into the runner. The image remains a runtime input: the runner reads `input.bin` through semihosting, which lets the FVP access files on the host.

## What you've accomplished and what's next

You've prepared MobileSAM and exported a quantized ExecuTorch program for Ethos-U85.

Next, you'll build the bare-metal application and run it on the Corstone-320 FVP.
