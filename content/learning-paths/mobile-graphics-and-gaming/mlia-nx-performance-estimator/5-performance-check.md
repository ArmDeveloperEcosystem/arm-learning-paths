---
title: Estimate performance and inspect configurations
description: Run the NX Performance Estimator, read standardized model and scheduling metrics, and compare built-in or custom target configurations.
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

With `--output-dir runs/baseline`, the key files are:

| Path under `runs/baseline/mlia-output/` | Purpose |
| --- | --- |
| `mlia-output.json` | Standardized MLIA result, including model metadata, metrics, entities, breakdowns, and advice |
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

You can also run MLIA in your editor and explore its results visually. Follow the [Ethos-U VS Code and Model Explorer walkthrough](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/7-vscode-plugin/) to set up and use two complementary tools:

- **MLIA VS Code extension**: configure compatibility and performance checks in your editor, run an analysis, and inspect model-level results
- **MLIA Model Explorer plugin**: overlay MLIA metrics and advice on the model graph, select operations, and compare costs within graph groups

The walkthrough shows how to select a cycle or memory-access metric in **Overlay** and locate operations that dominate the estimate. Selecting **advice** highlights operations to investigate. This helps you connect a report's numbers to the model structure rather than inspecting JSON alone.

The example uses Ethos-U and Vela metrics. For NX, use the metrics and chain-and-cascade breakdowns described here; don't assume that Ethos-U metric names or graph groupings apply unchanged. Graph-group summaries also aren't necessarily whole-model totals.

For graph inspection without MLIA overlays, follow [Explore model artifacts with Model Explorer](/learning-paths/cross-platform/explore-model-artifacts-with-model-explorer/). Use its VGF adapter to inspect the compiled graph produced here. The adapter visualizes graph structure; it isn't the MLIA metrics-and-advice overlay plugin. Continue using `mlia-output.json` for the analysis results.

## (Optional) Compare a different built-in profile

Keep the model unchanged when exploring a different target configuration. For example, run the peak profile into its own directory:

```bash
mlia check models/baseline.tflite --target-profile NX-peak-12SC-8NX-600MHz --performance --output-dir runs/baseline-peak
```

Differences here reflect the profile's system and compiler assumptions, not a model optimization. Return to `neural-technology` for the model comparison in the final section.

## What you've accomplished and what's next

You've collected baseline estimates and distinguished model metrics from scheduling breakdowns. Next, you'll evaluate a smaller public model under the original profile and compare the results.
