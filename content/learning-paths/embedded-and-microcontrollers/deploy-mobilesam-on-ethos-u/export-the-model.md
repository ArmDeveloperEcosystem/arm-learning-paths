---
title: Export MobileSAM for Ethos-U85
description: Prepare MobileSAM, quantize the model, and export a fixed-prompt ExecuTorch program for Ethos-U85.
weight: 4

layout: "learningpathall"
---

## Prepare the MobileSAM source

Run all commands from the ExecuTorch repository root. Confirm that your Python environment is active and that you've sourced `examples/arm/arm-scratch/setup_path.sh` in the current shell.

Prepare the pinned MobileSAM source in a separate working directory:

```bash
python examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/prepare_mobilesam.py \
  --source-dir arm_test/mobilesam_manual/mobile_sam/source
```

The script downloads the pinned MobileSAM revision and applies the patch needed for a configurable image size. It keeps the external source separate from the example source.

## Build the host quantized operators

The exporter requires the host shared library that registers the quantized operator out variants. Build the operators before exporting the model:

```bash
cmake \
  -S . \
  -B arm_test/mobilesam_manual/quantized_ops_aot \
  -DCMAKE_BUILD_TYPE=Release \
  -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
  -DEXECUTORCH_BUILD_KERNELS_QUANTIZED_AOT=ON \
  -DEXECUTORCH_BUILD_XNNPACK=OFF \
  -DPYTHON_EXECUTABLE="$(command -v python)"

cmake --build arm_test/mobilesam_manual/quantized_ops_aot \
  --target quantized_ops_aot_lib --parallel
```

Set the library path for the export command. The `find` command handles the `.so` extension on Linux and `.dylib` on macOS:

```bash
export EXECUTORCH_QUANTIZED_OPS_AOT_LIBRARY="$(find \
  arm_test/mobilesam_manual/quantized_ops_aot/kernels/quantized \
  -name 'libquantized_ops_aot_lib.*' -type f -print -quit)"
test -f "$EXECUTORCH_QUANTIZED_OPS_AOT_LIBRARY"
```

## Export the ExecuTorch program

Export the example image and positive point prompt for the `ethos-u85-256` target:

```bash
python examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/export_mobilesam.py \
  --output-path arm_test/mobilesam_manual/export/mobilesam_point_ethos_u85_448.pte \
  --calibration-image examples/models/dinov2/dog.jpg \
  --eval-image examples/models/dinov2/dog.jpg \
  --point 219 193 \
  --mobile-sam-source arm_test/mobilesam_manual/mobile_sam/source \
  --num-calibration-samples 1 \
  --num-eval-samples 1 \
  --num-debug-samples 1 \
  --minimum-fp32-quantized-iou 0.9 \
  --artifact-dir arm_test/mobilesam_manual/export/artifacts \
  --debug-output-dir arm_test/mobilesam_manual/export/debug
```

The first export downloads the pinned MobileSAM checkpoint. The exporter calibrates post-training quantization with the example image. It checks the quantized mask against the floating-point mask, and lowers the graph to Ethos-U85.

Export succeeds when the host mask intersection over union (IoU) is at least `0.9` and the `.pte` is written to `arm_test/mobilesam_manual/export/`.

## Verify the export artifacts

Check that the exporter created the files needed for the remaining steps:

```bash
export_dir=arm_test/mobilesam_manual/export

for artifact in \
  mobilesam_point_ethos_u85_448.pte \
  mobilesam_point_ethos_u85_448.json \
  mobilesam_point_ethos_u85_448_metrics.json \
  mobilesam_point_ethos_u85_448_delegation.txt \
  debug/dog/quantized_mask.png; do
  test -s "$export_dir/$artifact" || {
    echo "Missing export artifact: $export_dir/$artifact" >&2
    exit 1
  }
done

find "$export_dir/artifacts" -type f -print -quit | grep -q . || {
  echo "No TOSA or Vela artifacts found in $export_dir/artifacts" >&2
  exit 1
}
```

The point prompt is embedded in the `.pte`. The image remains a runtime input and is compiled into the bare-metal application.

## What you've accomplished and what's next

You've prepared MobileSAM and exported a quantized ExecuTorch program for Ethos-U85.

Next, you'll build the bare-metal application and run it on the Corstone-320 FVP.
