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

The reference run with Neural Technology `0.2.0`, LiteRT converter `0.1.2`, and the `neural-technology` profile produced an estimated `136,962` total cycles and about `0.09131 ms` per inference. The setup now uses Neural Technology `0.3.0` and LiteRT converter `0.1.3`; use your generated report for the current result. These figures are compiler estimates, rather than timings measured on a device.

## Locate and read the reports

With `--output-dir runs/baseline`, the following files are important:

| Path under `runs/baseline/mlia-output/` | Purpose |
| --- | --- |
| `mlia-output.json` | Standardized Arm ML Inference Advisor (MLIA) result, including model metadata, metrics, entities, breakdowns, and advice |
| `nx_performance_statistics.json` | Detailed chain and cascade performance statistics |
| `nx-performance-estimator/` | Estimator summaries and raw performance, timing, and debug databases |
| `ml-sdk-model-converter/` | Tensor Operator Set Architecture (TOSA) intermediates and `baseline.tosa.vgf`, produced automatically from the LiteRT model |
| `logs/mlia.log` | Analysis and diagnostic log |

By default, MLIA writes to `mlia-output` in the current directory, with the report in `mlia-output.json`.

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

The reference output is:

```output
total_cycles: 136962 cycles
compute_cycles: 34976 cycles
dram_cycles: 94396 cycles
inference_time: 0.091308 ms
inferences_per_second: 10951.9 inferences/s
```

The full report also includes `target_utilization`, memory traffic, and compiled size.

For the baseline, `dram_cycles` is `94,396`, compared with `34,976` compute cycles. This gives you a reason to investigate memory traffic.

Use `results[].breakdowns` and their `entity_id` links to `results[].entities` to inspect individual chains and cascades. These are compiler scheduling groups. They're not necessarily one framework layer each. Source-operator provenance helps you relate those groups to the original graph. Some metrics overlap or use non-additive aggregation policies, so don't sum every breakdown to recreate the model total.

## (Optional) Explore results in Model Explorer

After installing the compatible Model Explorer plugin in [Set up your MLIA environment](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/2-devenv/#optional-prepare-model-explorer-visualizations), rerun the check into a separate directory with visualization enabled:

```bash
mlia check models/baseline.tflite \
  --target-profile neural-technology \
  --performance \
  --output-dir runs/baseline-visualized \
  --model-explorer open
```

`--model-explorer open` creates a self-contained HTML visualization and opens it in your browser. Use `--model-explorer files` to generate the files without opening a browser. If the browser doesn't open, open `runs/baseline-visualized/mlia-output/model-explorer/bundle/index.html` manually.

Inspect the generated MLIA hierarchy alongside **Source Model**:

1. Select a cycle metric in the node-data controls to color the hierarchy by cost.
2. Expand the hierarchy and select a chain or cascade to read its reported values.
3. Follow its mapping to **Source Model**, where available, to find the related model operations.

Use these overlays to find scheduling groups worth investigating. A group can contain several operations, so its cost isn't a separate measurement for each operation. Keep using the model-level report for whole-model totals.

For the editor workflow, follow the [Ethos-U VS Code and Model Explorer walkthrough](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/7-vscode-plugin/). Its example uses Ethos-U and Vela; use the NX metrics from this analysis when exploring your results.

## (Optional) Compare a different built-in profile

Keep the model unchanged when exploring a different target configuration. For example, run the peak profile into its own directory:

```bash
mlia check models/baseline.tflite --target-profile NX-peak-12SC-8NX-600MHz --performance --output-dir runs/baseline-peak
```

Differences in performance reflect the system and compiler assumptions of the profile. The performance differences don't reflect a model optimization.

## What you've accomplished and what's next

You've collected baseline estimates and distinguished model metrics from scheduling breakdowns.

Next, you'll evaluate a smaller public model under the `neural-technology` profile and compare the results.
