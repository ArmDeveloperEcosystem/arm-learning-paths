---
title: (Optional) Use the Python API

description: Use the optional MLIA Python API to run compatibility checks, compare LiteRT models, and discover targets and backends programmatically.

weight: 7

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Use the API after the CLI

This section is optional. The MLIA CLI is the primary workflow for this Learning Path, and it is the best way to learn the tool, inspect output, and debug your environment.

Use the Python API when you want another product, dashboard, workflow runner, or CI system to integrate MLIA.

The `mlia` Python package exposes the same advisor functionality used by the CLI. If you continue, you use `run_advisor()` as the main API entry point, and helper functions such as `list_targets()`, `list_target_profiles()`, and `list_backends()` to discover what the installed environment supports.

## Run MLIA from Python and compare two models

This example shows using the API to analyze two LiteRT model variants, and then printing results and advice:

```bash
cat > compare_mlia_models.py <<'PY'
from pathlib import Path

from mlia import run_advisor


models = [
    Path("tflite/mv2_fp32.tflite"),
    Path("tflite/mv2_int8.tflite"),
]

for model in models:
    result = run_advisor(
        advice_category="compatibility",
        target_profile="ethos-u85-256",
        model=model,
        backends=["vela"],
    )

    print()
    print(model)

    for item in result["results"]:
        print(item["kind"], item["status"])

        for advice in item.get("advice", []):
            print("advice:", advice["severity"], advice["message"].splitlines()[0])
PY
```

Run the comparison script:

```bash
python compare_mlia_models.py
```

The expected result is that `mv2_fp32.tflite` reports `compatibility incompatible`, while `mv2_int8.tflite` reports `compatibility ok`. You might still see warning advice for both models. For example, MLIA can report that `SOFTMAX` is a suboptimal activation even when the quantized model is otherwise compatible with the NPU. Compatibility tells you whether the model can map to the target; advice can still point out ways to improve it.

You could take this further to:

- extract selected metrics into a dashboard
- compare performance between model revisions
- fail a CI job if a key metric regresses
- surface advice messages in an internal model review tool

## Discover capabilities from Python

MLIA also exposes helper functions for discovery. Depending on the installed MLIA version, useful helpers can include:

```bash
cat > discover_mlia.py <<'PY'
from mlia import list_backends, list_target_profiles, list_targets


print(list_targets())
print(list_target_profiles())
print(list_backends())
PY
```

Run the discovery script:

```bash
python discover_mlia.py
```

Use discovery in integrations so your product can report what the current environment supports.

## What you have learned

You have used the Python API to run the same kind of analysis you performed from the CLI. You have also seen how to compare model variants programmatically and why the API is useful for product integration or automation.
