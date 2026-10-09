---
title: Compare a smaller model under the same target profile
description: Convert a smaller-input public MobileNet variant, recheck compatibility, and compare NX estimates without confusing lower cost with preserved accuracy.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose a model change to investigate

The baseline report shows that memory traffic contributes substantially to estimated cycles. A smaller input reduces intermediate activation sizes and convolution work, so it's a useful candidate to evaluate.

Use the public `mobilenet_v1_0.25_128_quant.tflite` variant. It keeps the MobileNet V1 family and `0.25` width multiplier but uses `[1, 128, 128, 3]` input instead of `[1, 224, 224, 3]`. Both variants use batch size one and quantized eight-bit tensors.

{{% notice Accuracy tradeoff %}}
These are separately trained public model variants, not the same weights with a resized input. Their weights and quantization parameters differ. The TensorFlow model catalog reports lower ImageNet accuracy for the smaller variant. This exercise compares estimated workload cost; it doesn't prove that the smaller model is an acceptable replacement for your application. Validate task accuracy, preprocessing, and runtime behavior before deployment.
{{% /notice %}}

## Download and convert the smaller variant

From the same `mlia-demo` directory, download the versioned model archive and verify the extracted file:

```bash
curl --fail --location \
  https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_128_quant.tgz \
  --output mlia-demo-models/mobilenet_v1_0.25_128_quant.tgz
tar -xzf mlia-demo-models/mobilenet_v1_0.25_128_quant.tgz \
  -C mlia-demo-models ./mobilenet_v1_0.25_128_quant.tflite
printf '%s  %s\n' \
  3799e7cdb3ec44beacaf47ef5c884111c919e51bb50b34ac836244b08d4b953b \
  mlia-demo-models/mobilenet_v1_0.25_128_quant.tflite \
  | sha256sum --check
tosa-converter-for-tflite \
  mlia-demo-models/mobilenet_v1_0.25_128_quant.tflite \
  --text --emit-debug-info \
  -o mlia-demo-models/smaller.tosamlir
test -s mlia-demo-models/smaller.tosamlir
```

The checksum check reports `OK`, and the converter writes `mlia-demo-models/smaller.tosamlir`.

## Recheck compatibility and performance

Keep the original target profile and backend for both checks:

```bash
mlia check mlia-demo-models/smaller.tosamlir \
  --target-profile neural-technology \
  --backend nx-performance-estimator \
  --compatibility \
  --output-dir runs/smaller-compatibility

mlia check mlia-demo-models/smaller.tosamlir \
  --target-profile neural-technology \
  --backend nx-performance-estimator \
  --performance \
  --output-dir runs/smaller
```

## Compare standardized metrics

Validate both variants' compatibility and performance status, then calculate the changes from your own reports:

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

Your results should be similar to those shown in the following table:

| Metric | Baseline, 224 × 224 | Smaller, 128 × 128 | Change |
| --- | ---: | ---: | ---: |
| Total cycles | 136,962 | 79,824 | -41.72% |
| Inference time (ms) | 0.09131 | 0.05322 | -41.72% |
| Inferences per second | 10,951.94 | 18,791.34 | +71.58% |
| DRAM cycles | 94,396 | 45,981 | -51.29% |

Fewer cycles, shorter inference times, and higher throughput indicate better performance. However, a smaller model may be less accurate, so don't choose it on performance alone: check its outputs and evaluate accuracy on representative data to confirm that it still meets your application's requirements.

## What you've accomplished and what's next

You've installed MLIA from public PyPI packages, converted public pretrained models, validated operator compatibility, and compared NX performance estimates under a consistent target configuration. You can now apply the workflow to your own model: establish a baseline, inspect the breakdowns, make a focused change, recheck compatibility and estimates, then validate accuracy and performance on your deployment runtime.

If you have compatible hardware, continue to [(Optional) Run and profile the model on an NX device](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/7-run-on-nx-device/). Otherwise, you've completed the estimator workflow.
