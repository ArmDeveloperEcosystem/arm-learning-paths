---
title: Validate the MobileSAM segmentation result
description: Reconstruct the FVP mask, compare it with the host quantized mask, and inspect the MobileSAM result.
weight: 6

layout: "learningpathall"
---

## Reconstruct the target mask

Run the visualization tool from the ExecuTorch repository root without arguments. It reads the Fixed Virtual Platform (FVP) output tensor from `output-0.bin` under `arm_test/mobilesam/io/` and thresholds its mask logits at zero. It compares the mask with `quantized_mask.png` under `arm_test/mobilesam/export/`:

```bash
python3 examples/arm/mobilesam_prompt_segmentation_example_ethos_u/runtime/visualize_fvp_output.py
```

The tool requires `112 × 112` float32 logits and exits with an error if the FVP and host masks have an intersection over union (IoU) below `0.9`. The threshold is fixed in the script.

On success, it prints `FVP/reference mask IoU:` with the measured score and a `Saved` line with the comparison image path. It writes `fvp_mask.png`, `fvp_comparison.png`, and `metrics.json` under `arm_test/mobilesam/result/`.

## Inspect the metrics

Display the target comparison metrics:

```bash
python3 -m json.tool arm_test/mobilesam/result/metrics.json
```

Confirm that `fvp_reference_iou` is at least `0.9`.

The exporter already checked the floating-point and quantized host masks. Display that result if you want to inspect the earlier stage:

```bash
python3 -m json.tool arm_test/mobilesam/export/metrics.json
```

The `fp32_quantized_iou` value must also be at least `0.9`.

A reference run at the pinned commit produced these scores:

| Comparison | IoU |
| --- | --- |
| Floating-point and quantized host masks | 0.9550 |
| FVP and quantized host masks | 0.9809 |

This run used Python 3.12.13, PyTorch 2.14.0, Vela 5.1.0, and Corstone-320 FVP 11.31.28 on macOS 26.6.2 with Apple silicon. Treat these scores as examples; use the two `0.9` thresholds to check your own run.

## Confirm Ethos-U delegation

Display the delegation report written during export:

```bash
sed -n '1,120p' arm_test/mobilesam/export/delegation.txt
```

Confirm that `Total delegated subgraphs` is `1`. The exporter checks this before writing the `.pte`. The reference run above produced:

```output
Total delegated subgraphs: 1
Number of delegated nodes: 5076
Number of non-delegated nodes: 3
```

Node counts can vary with dependency versions. Use the values from your export when reporting delegation.

## Inspect the visual result

Open `fvp_comparison.png` under `arm_test/mobilesam/result/` in an image viewer. The image contains three panels:

- The resized input image with the positive point prompt
- The host quantized segmentation overlay
- The FVP segmentation overlay

Compare the object boundaries in the two mask overlays. The FVP mask should select the dog at the positive point prompt and closely match the host quantized result.

## What you've accomplished

You've completed the MobileSAM deployment flow from PyTorch export to bare-metal execution on Ethos-U85. You also checked that both the host quantization comparison and the FVP mask comparison meet the `0.9` IoU threshold.
