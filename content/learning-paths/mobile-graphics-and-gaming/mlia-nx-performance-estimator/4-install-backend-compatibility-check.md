---
title: Check baseline operator compatibility
description: Analyze the public MobileNet LiteRT model directly with MLIA, let it install the bundled NX backend if needed, and check operator compatibility.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the baseline operators

Pass `models/baseline.tflite` to Arm ML Inference Advisor (MLIA). It converts the model automatically and selects the backend for the `neural-technology` target profile.

{{% notice License %}}
On your first check, MLIA offers to install the bundled neural acceleration (NX) Performance Estimator. Confirm installation when prompted, then read its Arm license and continue only if you agree. If the backend is already installed, MLIA skips this setup.
{{% /notice %}}

Run the compatibility check:

```bash
mlia check models/baseline.tflite --target-profile neural-technology --compatibility --output-dir runs/baseline-compatibility
```

Each check writes to its own directory under `runs`, created during the model download.

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

## Interpret the compatibility result

The compatibility result includes `checks`, source-operator `entities`, and metrics. For this model, `accelerator_operator_percentage` is `100.0`. MLIA reports `ml-sdk-model-converter` as the compatibility producer because operator support is checked during conversion.

A passing result means that this graph can proceed through the supported conversion flow. It doesn't establish classification accuracy, guarantee a deployable application, or measure device performance.

If a check fails, inspect the non-passing checks and linked entities of the report. Verify that you're analyzing `models/baseline.tflite` and that both plugins from the environment setup are installed.

## What you've accomplished and what's next

You've checked the baseline's operator compatibility without a manual conversion step.

Next, you'll collect performance estimates and inspect their breakdowns.
