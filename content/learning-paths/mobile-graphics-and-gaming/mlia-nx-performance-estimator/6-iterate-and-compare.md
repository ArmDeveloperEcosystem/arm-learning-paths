---
title: Compare a smaller model under the same target profile
description: Download and analyze a smaller-input public MobileNet variant with MLIA, then compare its NX estimates with the baseline under the same target profile.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose a model change to investigate

The baseline report shows that memory traffic contributes substantially to estimated cycles. A smaller input reduces intermediate activation sizes and convolution work, so it's a useful candidate to evaluate.

Use the public `mobilenet_v1_0.25_128_quant.tflite` variant. It keeps the MobileNet V1 family and `0.25` width multiplier but uses `[1, 128, 128, 3]` input instead of `[1, 224, 224, 3]`. Both variants use batch size one and quantized eight-bit tensors.

## Download the smaller variant

From the same `mlia-demo` directory, download the versioned model archive and verify the extracted file:

```bash
curl -fL https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_128_quant.tgz -o models/smaller.tgz
tar -xzf models/smaller.tgz -C models ./mobilenet_v1_0.25_128_quant.tflite
mv models/mobilenet_v1_0.25_128_quant.tflite models/smaller.tflite
echo "3799e7cdb3ec44beacaf47ef5c884111c919e51bb50b34ac836244b08d4b953b  models/smaller.tflite" | sha256sum --check
```

The checksum check reports `models/smaller.tflite: OK`. Pass this file directly to MLIA, as you did for the baseline.

## Recheck compatibility and performance

Keep the `neural-technology` target profile for both checks. MLIA selects the same backend automatically:

```bash
mlia check models/smaller.tflite --target-profile neural-technology --compatibility --output-dir runs/smaller-compatibility
mlia check models/smaller.tflite --target-profile neural-technology --performance --output-dir runs/smaller
```

## Compare standardized metrics

Validate the compatibility and performance status of both variants, then calculate the changes from your own reports:

```bash
python - <<'PY'
import json
from pathlib import Path

def load_result(run, kind):
    path = Path("runs") / run / "mlia-output" / "mlia-output.json"
    report = json.loads(path.read_text())
    result = next(result for result in report["results"] if result["kind"] == kind)
    assert result["status"] == "ok", f"Review the {run} report."
    if kind == "compatibility":
        assert all(check["status"] == "pass" for check in result["checks"]), f"Review the {run} checks."
    return {metric["name"]: metric["value"] for metric in result["metrics"] if "value" in metric}

for run in ("baseline-compatibility", "smaller-compatibility"):
    load_result(run, "compatibility")
baseline = load_result("baseline", "performance")
smaller = load_result("smaller", "performance")
for name in ("total_cycles", "inference_time", "inferences_per_second", "dram_cycles"):
    before, after = baseline[name], smaller[name]
    change = (after / before - 1) * 100
    print(f"{name}: {before:.5f} -> {after:.5f} ({change:+.2f}%)")
PY
```
The following table includes example results:

| Metric | Baseline, 224 × 224 | Smaller, 128 × 128 | Change |
| --- | ---: | ---: | ---: |
| Total cycles | 136,962 | 79,824 | -41.72% |
| Inference time (ms) | 0.09131 | 0.05322 | -41.72% |
| Inferences per second | 10,951.94 | 18,791.34 | +71.58% |
| DRAM cycles | 94,396 | 45,981 | -51.29% |

Fewer cycles, shorter inference times, and higher throughput indicate better performance. However, these are separately trained public model variants, not the same weights with a resized input. Their weights and quantization parameters differ.

The TensorFlow model catalog reports lower ImageNet accuracy for the smaller variant, so don't choose a model on performance alone. Validate task accuracy, preprocessing, and runtime behavior on representative data before deployment to confirm that the model meets your requirements.

## What you've accomplished and what's next

You've analyzed two public LiteRT models directly with MLIA and compared their neural acceleration (NX) performance estimates under the same target profile. For your own model, keep that profile fixed while checking each change. Validate the accuracy and runtime behavior of the model before deployment.

If you have compatible hardware, continue to [(Optional) Run and profile the model on an NX device](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/7-run-on-nx-device/). Otherwise, you've completed the estimator workflow and can extend it to models and profiles of your choice.
