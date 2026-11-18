---
title: Export and inspect the live MobileSAM model
description: Freeze four independent prompts, export int8 model I/O, and inspect delegation and metadata before building firmware.
weight: 4
layout: learningpathall
---

## Prepare the pinned MobileSAM source

Keep the environment from the previous lesson active and run these commands from the patched ExecuTorch checkout. Its exporter has live-camera options that are absent from some later versions of the public FVP example.

```bash
cd "$EXECUTORCH_ROOT"
python examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/prepare_mobilesam.py \
  --source-dir "$MOBILE_SAM_SOURCE"
```

The preparation step uses MobileSAM revision `f706ad9c4eb7f219c00d9050e46328518ffb65d2` and applies the configurable-image-size patch. The exporter verifies the official checkpoint SHA256:

```output
6dbb90523a35330fedd7f1d3dfc66f995213d81b29a5ca8108dbcdd4e37d6c2f
```

## Select a calibration image

Use the public dog image from the Segment Anything example, pinned to a source revision. Download it and verify its SHA256 before export:

```bash
export MOBILE_SAM_CALIBRATION_IMAGE="$MOBILE_SAM_OUTPUT/sam-example-dog.jpg"
curl --fail --location \
  https://raw.githubusercontent.com/facebookresearch/segment-anything/dca509fe793f601edb92606367a655c15ac00fdf/notebooks/images/dog.jpg \
  --output "$MOBILE_SAM_CALIBRATION_IMAGE"
printf '%s  %s\n' \
  bf76876b90e3ebd521f9882b9177ba8f33e80cb7ec09c630f179b122edd125e1 \
  "$MOBILE_SAM_CALIBRATION_IMAGE" | shasum -a 256 -c
```

Require the checksum result `OK`. The image comes from the [Segment Anything repository](https://github.com/facebookresearch/segment-anything/tree/dca509fe793f601edb92606367a655c15ac00fdf/notebooks/images), which provides its [license](https://github.com/facebookresearch/segment-anything/blob/dca509fe793f601edb92606367a655c15ac00fdf/LICENSE).

With the released dependencies and the configuration below, this image passed the unchanged host quality gate with selected-mask IoU `0.9756` and pixel agreement `0.9919`. The gate selected zero-based prompt indices 2 and 3 (the third and fourth prompts); the later section explains this selection rule. This image is different from `examples/models/dinov2/dog.jpg`.

The exporter uses this image for both quantization calibration and its host comparison. You can replace it with an RGB image representative of your camera scenes, but require your export to pass the unchanged quality gate before continuing. Calibration input affects both the result and the generated model. A passing comparison on the calibration image does not measure accuracy on new scenes.

## Export four independent prompts

Use the live-camera configuration:

```bash
python examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/export_mobilesam.py \
  --output-path "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.pte" \
  --mobile-sam-source "$MOBILE_SAM_SOURCE" \
  --image "$MOBILE_SAM_CALIBRATION_IMAGE" \
  --input-size 384 \
  --point 96 96 \
  --point 288 96 \
  --point 96 288 \
  --point 288 288 \
  --multimask-output \
  --quantized-io
```

The points sample the four image quadrants. In this multimask mode they are independent prompt batches, giving three candidate masks and associated quality scores per point. This is different from asking SAM for one mask constrained jointly by all four points.

The image encoder and decoder run on the NPU. The prompt encoder runs during export, and its fixed embeddings are stored in the model. Re-export when you change prompt coordinates, input size, or the output contract.

This model contract is the same for the default camera-and-UART firmware and optional dashboard. Enabling a display does not require a different export.

The export applies A8W8 globally and A16W8 to TinyViT attention, then lowers through the Arm backend and Vela for `ethos-u85-256`. The compiled configuration uses `Ethos_U85_SYS_DRAM_Mid` and `Dedicated_Sram_384KB`. Those are compiler settings; actual firmware storage and scratch placement still need to match the E8 memory map.

## Inspect artifacts before continuing

The exporter writes the `.pte` and matching `.json` metadata beside it, together with mask-agreement metrics, a delegation summary, and TOSA/Vela debug artifacts. Inspect them:

```bash
ls -lh "$MOBILE_SAM_OUTPUT"
python -m json.tool "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.json"
cat "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask_metrics.json"
cat "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask_delegation.txt"
```

Require successful export and inspect the generated masks and both quality metrics. This exporter accepts selected-mask IoU at least `0.9` **or** pixel agreement at least `0.96`. It compares selected candidates at prompts whose predicted quantized quality reaches `0.9`, using all prompts as fallback when none reaches that threshold. This does not require `0.9` IoU for every candidate or every prompt. The device's later mask-selection threshold is `0.8`.

Using the same image for calibration and evaluation does not measure segmentation accuracy on new scenes. Inspect the generated masks, then validate the programmed model on representative camera scenes. Your calibration image and released dependencies can produce a different artifact from the retained board binary; record your own model and metadata hashes.

The live application expects this tensor interface:

| Tensor | Shape | Type |
| --- | --- | --- |
| Image input | `[1,3,384,384]` | int8 |
| Mask output | `[4,3,96,96]` | int8 |
| Quality output | `[4,3]` | int8 |

CMake rejects known CPU operators, while the runtime checks input type/byte count and some output dimensions. The metadata-only header generator does not validate `output_shape`. Check the actual PTE tensor interface against the JSON and this configuration before building:

```bash
python - <<'PY'
import hashlib
import json
import math
import os
from pathlib import Path

from executorch.exir._serialize._program import deserialize_pte_binary
from executorch.exir.scalar_type import ScalarType
from executorch.exir.schema import Tensor

pte_path = Path(os.environ["MOBILE_SAM_OUTPUT"]) / "mobilesam_live_384_grid4_multimask.pte"
json_path = pte_path.with_suffix(".json")
metadata = json.loads(json_path.read_text())
program = deserialize_pte_binary(pte_path.read_bytes()).program
plan, = [p for p in program.execution_plan if p.name == "forward"]
shapes = [[1, 3, 384, 384], [4, 3, 96, 96], [4, 3]]
assert len(plan.inputs) == 1 and len(plan.outputs) == 2
for index, shape in zip(plan.inputs + plan.outputs, shapes):
    tensor = plan.values[index].val
    assert isinstance(tensor, Tensor) and tensor.scalar_type == ScalarType.CHAR
    assert tensor.sizes == shape, (tensor.sizes, shape)
assert metadata["input_shape"] == shapes[0]
assert metadata["output_shape"] == shapes[1]
assert metadata["input_size"] == 384 and metadata["multimask_output"] is True
assert metadata["point_prompts_xy"] == [[96, 96], [288, 96], [96, 288], [288, 288]]
preprocessing = metadata["preprocessing"]
assert preprocessing["resize"] == "longest_side_then_zero_pad"
for key, expected in (("pixel_mean", [123.675, 116.28, 103.53]),
                      ("pixel_std", [58.395, 57.12, 57.375])):
    values = preprocessing[key]
    assert len(values) == 3 and all(
        math.isclose(value, reference, rel_tol=0, abs_tol=0.0001)
        for value, reference in zip(values, expected)
    )
for name in ("input", "output", "quality"):
    qparams = metadata["io_quantization"][name]
    assert qparams["dtype"] == "int8"
    assert math.isfinite(qparams["scale"]) and qparams["scale"] > 0
    assert isinstance(qparams["zero_point"], int) and -128 <= qparams["zero_point"] <= 127
print("PTE tensor interface and JSON configuration checks passed")
for path in (pte_path, json_path):
    print(hashlib.sha256(path.read_bytes()).hexdigest(), path.name)
PY
```

Require the success message and retain both printed hashes with your export. An assertion failure means the files do not satisfy this configuration; resolve it before continuing. The PTE's tensor schema does not store quantization parameters, so this check cannot prove that the JSON scales and zero points belong to that PTE. Keep the matching PTE and JSON from the same export, alongside their hashes, and check target output during execution.

An old `[1,1,112,112]` floating-point FVP result belongs to the earlier 448×448 single-mask configuration. It is not the output contract of this 384×384 live model.

## Prepare an identical model file for programming

J-Link and the recovery writer consume a raw `.bin` file. This is an unchanged copy of the PTE, without a new container or header:

```bash
cp "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.pte" \
  "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.bin"
cmp "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.pte" \
  "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.bin"
```

The fresh released-dependency export using this public image is 13,317,584 bytes, with SHA256 `a908bca09a74bac884895fa72b650d15e944cdfc7b0351b99e40ee63b6b3a7b5`. Its metadata JSON has SHA256 `36884d2ffafa1b9ee46c71c0a855b9b83b01da57e3e87a3a99fdb56f547770f7`. Its extracted scratch requirement is 5,898,256 bytes with a 393,216-byte fast scratch requirement. These identify the fresh host export; firmware and hardware checks follow in later lessons. Generated JSON records local paths, so its hash also depends on your workspace. Record the size and hashes of your own matching pair.

Before proceeding, explain why `--quantized-io` matters: it removes the host-style floating-point I/O boundary from the device program, while the application performs camera normalization, quantization, and mask post-processing.

## What you've accomplished

You've exported the four-prompt model, checked delegation and quantized tensor metadata, and prepared an identical binary for programming. Next, build firmware with this PTE and JSON and check its memory use.
