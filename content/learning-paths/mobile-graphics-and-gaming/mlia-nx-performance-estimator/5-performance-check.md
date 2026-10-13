---
title: Estimate performance and inspect configurations
description: Run the NX Performance Estimator, read standardized model and scheduling metrics, and compare built-in or custom target configurations.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Estimate baseline performance

Run a performance check with the same model and target profile, and open the results in Model Explorer:

```bash
mlia check models/baseline.tflite --target-profile neural-technology --performance --output-dir runs/baseline --model-explorer open
```

With the tested packages and `neural-technology` profile, expect `136,962` estimated total cycles and about `0.09131 ms` per inference. These are compiler estimates, not timings measured on a device.

`--model-explorer open` creates a standalone HTML visualization and opens it in your browser. Omit this option if you only want the CLI reports.

## Locate and read the reports

With `--output-dir runs/baseline`, the key files are:

| Path under `runs/baseline/mlia-output/` | Purpose |
| --- | --- |
| `mlia-output.json` | Standardized MLIA result, including model metadata, metrics, entities, breakdowns, and advice |
| `model-explorer/bundle/index.html` | Self-contained Model Explorer page with the graph and MLIA overlays |
| `nx_performance_statistics.json` | Detailed chain and cascade performance statistics |
| `nx-performance-estimator/` | Estimator summaries and raw performance, timing, and debug databases |
| `ml-sdk-model-converter/` | TOSA intermediates and `baseline.tosa.vgf`, produced automatically from the LiteRT model |
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

## (Optional) Explore results in VS Code and Model Explorer

In the Model Explorer page opened by the command, inspect the generated MLIA hierarchy alongside **Source Model**:

1. Select a cycle metric in the node-data controls to color the hierarchy by cost.
2. Expand the hierarchy and select a chain or cascade to read its reported values.
3. Follow its mapping to **Source Model**, where available, to find the related model operations.

Use the cycle overlays to find scheduling groups worth investigating. A group can contain several operations, so its cost isn't a separate measurement for each operation. Keep using the model-level report for whole-model totals.

If the browser doesn't open, open `runs/baseline/mlia-output/model-explorer/bundle/index.html` manually.

To run these checks from your editor, follow the [Ethos-U VS Code and Model Explorer walkthrough](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/7-vscode-plugin/). It introduces the MLIA VS Code extension and shows how to explore metrics and advice. Its example uses Ethos-U and Vela; use the NX metrics from this analysis rather than expecting the same metric names or graph groups.

## (Optional) Compare a different built-in profile

Keep the model unchanged when exploring a different target configuration. For example, run the peak profile into its own directory:

```bash
mlia check models/baseline.tflite --target-profile NX-peak-12SC-8NX-600MHz --performance --output-dir runs/baseline-peak
```

Differences here reflect the profile's system and compiler assumptions, not a model optimization. Return to `neural-technology` for the model comparison in the final section.

## What you've accomplished and what's next

You've collected baseline estimates and distinguished model metrics from scheduling breakdowns. Next, you'll evaluate a smaller public model under the original profile and compare the results.
