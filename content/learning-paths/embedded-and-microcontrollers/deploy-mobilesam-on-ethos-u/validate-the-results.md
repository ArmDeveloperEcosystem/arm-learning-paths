---
title: Validate the MobileSAM segmentation result
description: Reconstruct the FVP mask, compare it with the host quantized mask, and inspect the MobileSAM result.
weight: 6

layout: "learningpathall"
---

## Reconstruct the target mask

Run the visualization tool from the ExecuTorch repository root. It decodes the mask from the FVP log and compares it with the host quantized mask:

```bash
python examples/arm/mobilesam_prompt_segmentation_example_ethos_u/runtime/visualize_fvp_output.py \
  --fvp-log=arm_test/mobilesam_manual/fvp.log \
  --input-image=examples/models/dinov2/dog.jpg \
  --metadata=arm_test/mobilesam_manual/export/mobilesam_point_ethos_u85_448.json \
  --reference-mask=arm_test/mobilesam_manual/export/debug/dog/quantized_mask.png \
  --minimum-iou=0.9 \
  --output-dir=arm_test/mobilesam_manual/fvp_visual
```

The command reports the number of foreground pixels and the agreement between the FVP and host masks. It exits with an error if the mask is empty, full, or below `0.9` IoU.

## Inspect the metrics

Display the target comparison metrics:

```bash
python -m json.tool arm_test/mobilesam_manual/fvp_visual/metrics.json
```

Confirm that `fvp_reference_iou` is at least `0.9`. The `fvp_reference_pixel_agreement` value reports the fraction of matching pixels.

The exporter already checked the floating-point and quantized host masks. Display that result if you want to inspect the earlier stage:

```bash
python -m json.tool \
  arm_test/mobilesam_manual/export/mobilesam_point_ethos_u85_448_metrics.json
```

The `fp32_quantized_iou` value must also be at least `0.9`.

## Confirm Ethos-U delegation

Display the delegation report written during export:

```bash
sed -n '1,120p' \
  arm_test/mobilesam_manual/export/mobilesam_point_ethos_u85_448_delegation.txt
```

Confirm that the graph is represented by one Ethos-U delegate and that no operators remain for CPU execution.

## Inspect the visual result

Open `arm_test/mobilesam_manual/fvp_visual/fvp_comparison.png` in an image viewer. The image contains three panels:

- The resized input image with the positive point prompt
- The host quantized segmentation overlay
- The FVP segmentation overlay

Compare the object boundaries in the two mask overlays. The FVP mask should select the dog at the positive point prompt and closely match the host quantized result.

## What you've accomplished

You have completed the MobileSAM deployment flow from PyTorch export to bare-metal execution on Ethos-U85. You also confirmed that the target produces a non-degenerate mask that agrees with the host quantized reference.
