---
title: Install the NX backend and check operator compatibility
description: Install the bundled NX Performance Estimator after reviewing its license, then check the public MobileNet baseline and validate the compatibility report.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install the bundled estimator

Install the backend from the public wheel's bundled payload:

```bash
mlia backend install nx-performance-estimator
mlia backend list
```

{{% notice License %}}
The installer presents the Arm license for the bundled NX Performance Estimator and asks whether you accept it. Read the terms and continue only if you agree.
{{% /notice %}}

After installation, the backend list shows `nx-performance-estimator` as installed.

## Check the baseline operators

Run a compatibility check on the converted model. Use a dedicated output directory to keep this report separate from performance results:

```bash
mlia check mlia-demo-models/baseline.tosamlir \
  --target-profile neural-technology \
  --backend nx-performance-estimator \
  --compatibility \
  --output-dir runs/baseline-compatibility
```

The `runs` parent directory was created during model preparation. MLIA version `0.12.3` creates the per-run directory, but needs its parent to exist.

The standardized report is written to `runs/baseline-compatibility/mlia-output/mlia-output.json`. Read the compatibility result and validate its status:

```bash
python - <<'PY'
import json
from pathlib import Path

report = json.loads(Path("runs/baseline-compatibility/mlia-output/mlia-output.json").read_text())
result = next(result for result in report["results"] if result["kind"] == "compatibility")
failed_checks = [check for check in result.get("checks", []) if check["status"] != "pass"]
print(f"Compatibility status: {result['status']}")
print(f"Non-passing checks: {len(failed_checks)}")
assert result["status"] == "ok", "Review the compatibility report before estimating performance."
assert not failed_checks, "Review the non-passing operator checks."
PY
```

The expected output for the pinned packages and baseline is:

```output
Compatibility status: ok
Non-passing checks: 0
```

## Interpret compatibility correctly

The compatibility result includes `checks`, source-operator `entities`, and metrics. For this model, `accelerator_operator_percentage` is `100.0`. The compatibility producer is `ml-sdk-model-converter`, even though you selected the NX analysis backend: operator support is checked during conversion.

A passing result means that this graph can proceed through the supported conversion flow. It doesn't establish classification accuracy, guarantee a deployable application, or measure device performance.

If a check fails, inspect the report's non-passing checks and linked entities. Verify that you're analyzing the intended TOSA file and that the package versions match the setup. For direct `.tflite` inputs, confirm that `mlia-converters-litert` is installed. PyTorch `.pt2` and ExecuTorch `.pte` inputs need a different converter plugin and aren't part of this example.

## What you've accomplished and what's next

You've installed the estimator and validated the baseline's operator compatibility. Next, you'll collect performance estimates and inspect the metrics and scheduling breakdowns.
