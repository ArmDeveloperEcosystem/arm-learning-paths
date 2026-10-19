---
title: Estimate baseline performance and inspect reports
description: Estimate baseline NX performance with MLIA, inspect report metrics and breakdowns, and optionally compare a built-in target profile.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Estimate baseline performance

Run a performance check with the same model and target profile:

```bash
mlia check models/baseline.tflite --target-profile neural-technology --performance --output-dir runs/baseline
```

With the tested packages and `neural-technology` profile, expect `136,962` estimated total cycles and about `0.09131 ms` per inference. These are compiler estimates, not timings measured on a device.

## Locate and read the reports

With `--output-dir runs/baseline`, the following files are important:

| Path under `runs/baseline/mlia-output/` | Purpose |
| --- | --- |
| `mlia-output.json` | Standardized Arm ML Inference Advisor (MLIA) result, including model metadata, metrics, entities, breakdowns, and advice |
| `nx_performance_statistics.json` | Detailed chain and cascade performance statistics |
| `nx-performance-estimator/` | Estimator summaries and raw performance, timing, and debug databases |
| `ml-sdk-model-converter/` | Tensor Operator Set Architecture (TOSA) intermediates and `baseline.tosa.vgf`, produced automatically from the LiteRT model |
| `logs/mlia.log` | Analysis and diagnostic log |

By default MLIA writes to `mlia-output` in the current directory, with the report in `mlia-output.json`.

Read the main cycle and inference estimates:

```bash
python - <<'PY'
import json
from pathlib import Path

report = json.loads(Path("runs/baseline/mlia-output/mlia-output.json").read_text())
result = next(result for result in report["results"] if result["kind"] == "performance")
assert result["status"] == "ok", "Review the performance report for errors."
metrics = {metric["name"]: metric for metric in result["metrics"]}
for name in ("total_cycles", "compute_cycles", "dram_cycles", "inference_time", "inferences_per_second"):
    metric = metrics[name]
    print(f"{name}: {metric['value']:.6g} {metric['unit']}")
PY
```

The expected output is:

```output
total_cycles: 136962 cycles
compute_cycles: 34976 cycles
dram_cycles: 94396 cycles
inference_time: 0.091308 ms
inferences_per_second: 10951.9 inferences/s
```

The full report also includes `target_utilization`, memory traffic, and compiled size.

For the baseline, `dram_cycles` is `94,396`, compared with `34,976` compute cycles. This gives you a reason to investigate memory traffic.

Use `results[].breakdowns` and their `entity_id` links to `results[].entities` to inspect individual chains and cascades. These are compiler scheduling groups, not necessarily one framework layer each. Source-operator provenance helps you relate those groups to the original graph. Some metrics overlap or use non-additive aggregation policies, so don't sum every breakdown to recreate the model total.

## (Optional) Compare a different built-in profile

Keep the model unchanged when exploring a different target configuration. For example, run the peak profile into its own directory:

```bash
mlia check models/baseline.tflite --target-profile NX-peak-12SC-8NX-600MHz --performance --output-dir runs/baseline-peak
```

Differences in performance reflect the system and compiler assumptions of the profile, not a model optimization.

## What you've accomplished and what's next

You've collected baseline estimates and distinguished model metrics from scheduling breakdowns.

Next, you'll evaluate a smaller public model under the `neural-technology` profile and compare the results.
