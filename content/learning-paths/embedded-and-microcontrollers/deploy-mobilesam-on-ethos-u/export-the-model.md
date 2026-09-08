---
title: Export MobileSAM for Ethos-U85
description: Prepare MobileSAM, quantize the model, and export a fixed-prompt ExecuTorch program for Ethos-U85.
weight: 4

layout: "learningpathall"
---

## Prepare the MobileSAM source

Run all commands from the ExecuTorch repository root. Confirm that your Python environment is active and that you have sourced `examples/arm/arm-scratch/setup_path.sh` in the current shell.

Prepare the pinned MobileSAM source in a separate working directory:

```bash
python examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/prepare_mobilesam.py \
  --source-dir arm_test/mobilesam_manual/mobile_sam/source
```

The script downloads the pinned MobileSAM revision and applies the patch needed for a configurable image size. It keeps the external source outside the ExecuTorch tree.

## Export the ExecuTorch program

Export the example image and positive point prompt for the `ethos-u85-256` target:

```bash
python examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/export_mobilesam.py \
  --output-path arm_test/mobilesam_manual/export/mobilesam_point_ethos_u85_448.pte \
  --image examples/models/dinov2/dog.jpg \
  --point 219 193 \
  --mobile-sam-source arm_test/mobilesam_manual/mobile_sam/source
```

The first export downloads the pinned MobileSAM checkpoint. The exporter calibrates post-training quantization with the example image, checks the quantized mask against the floating-point mask, and lowers the graph to Ethos-U85.

Export succeeds when the host mask intersection over union (IoU) is at least `0.9` and the `.pte` is written to `arm_test/mobilesam_manual/export/`.

## Locate the export artifacts

The export directory contains the evidence needed for the remaining steps:

| Artifact | Path |
|---|---|
| ExecuTorch program | `mobilesam_point_ethos_u85_448.pte` |
| Model metadata | `mobilesam_point_ethos_u85_448.json` |
| Host mask metrics | `mobilesam_point_ethos_u85_448_metrics.json` |
| Delegation report | `mobilesam_point_ethos_u85_448_delegation.txt` |
| Host quantized mask | `debug/dog/quantized_mask.png` |
| TOSA and Vela artifacts | `artifacts/` |

The point prompt is embedded in the `.pte`. The image remains a runtime input and is compiled into the bare-metal application in the next step.

## What you've accomplished

You have prepared MobileSAM and exported a quantized ExecuTorch program for Ethos-U85. Next, you will build the bare-metal application and run it on the Corstone-320 FVP.
