---
title: Analyze LiteRT artifacts with Vela

description: Run MLIA compatibility and Vela performance checks on LiteRT models and inspect JSON metrics, operator placement, and advice.

weight: 4

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Run a compatibility check

Start by asking MLIA whether a LiteRT model can map to the selected target profile.

LiteRT is a compact model format and runtime stack for deploying machine learning models on mobile, embedded, and edge devices. In embedded ML workflows, a `.tflite` file is often the artifact handed to backend tools for target-specific compatibility checks, compilation, or runtime deployment.

The model artifacts repository includes floating-point and quantized MobileNetV2 LiteRT variants:

```output
tflite/mv2_fp32.tflite
tflite/mv2_int8.tflite
```

From the `ml-model-artifacts` directory, run MLIA on the FP32 LiteRT artifact:

```bash
mlia check tflite/mv2_fp32.tflite \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

The `--json` option makes the output easier to inspect, compare, and automate.

You can also use the shorter `-t` and `-b` options instead of `--target-profile` and `--backend`. Note `--compatibility` and `vela` are both defaults that could be omitted:

```bash
mlia check tflite/mv2_fp32.tflite -t ethos-u85-256 --json
```

This report should show the FP32 LiteRT model as incompatible for Ethos-U acceleration, with `accelerator_operator_percentage` set to `0`. This is expected because Ethos-U acceleration requires supported quantized integer workloads. The failed checks explain that the input, output, and weight tensors are missing quantization parameters.

This does not mean LiteRT is the problem. It means this particular LiteRT artifact is not in the numeric form the selected Ethos-U target needs. Use a quantized model instead.

Now run the same compatibility check on the quantized INT8 model:

```bash
mlia check tflite/mv2_int8.tflite \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

You will generate a lengthy report, saved in the `mlia-output` directory in the root of the `mlia` execution directory. A small snippet is included below:

```output
{
  "target": {
    "configuration": {
      "target": "ethos-u85",
      "mac": 256
    }
  },
  "model": {
    "name": "mv2_int8.tflite",
    "format": "tflite"
  },
  "backends": [
    {
      "id": "vela",
      "name": "Vela Compiler",
      "version": "5.0.0"
    }
  ],
  "results": [
    {
      "kind": "compatibility",
      "status": "ok",
      "metrics": [
        {
          "name": "accelerator_operator_percentage",
          "value": 100.0
        }
      ]
    }
  ]
}
```

## What does this report tell us?

| Field | What it tells you |
| --- | --- |
| `schema_version`, `run_id`, `timestamp` | Which output schema was used, and how to identify this specific run later. |
| `tool` | The MLIA version that generated the report. |
| `target` | The selected target profile and its configuration, such as Ethos-U85 with 256 MACs. |
| `model` | The artifact name, format, and hash. |
| `context` | The CLI command that produced the report. |
| `backends` | The backend MLIA used, including the Vela version and compiler configuration. |
| `results` | The answer MLIA produced for the requested check. |
| `checks` | The individual operator support checks. |
| `entities` | The operators MLIA analyzed, including placement and operator type. |

For the INT8 LiteRT file, the important result is that `status` is `ok` and `accelerator_operator_percentage` is `100.0`. That means Vela found the operators in this quantized MobileNetV2 LiteRT artifact compatible with the selected `ethos-u85-256` target profile, and MLIA expects the operator work to map to the NPU path for this compatibility check. It does not prove runtime latency or application accuracy. It tells you the model is a good candidate for the next step: performance estimation and deeper deployment testing.

## Read operator placement

The summary result tells you that the model is compatible overall. To see how MLIA reached that result, look at the `entities` list. Each operator entity describes one analyzed operator and includes a `placement` field:

```json
{
  "scope": "operator",
  "name": "...",
  "placement": "npu",
  "attributes": {
    "op_type": "Conv2D"
  }
}
```

Names and attributes vary by input format and MLIA version. The important part is the placement: it tells you where MLIA and the backend analysis expect the operator to land for this target profile. If a future model has unsupported operators, this is where you start narrowing down the problem: find the operator whose placement or check status differs from the expected NPU path, then inspect that part of the model graph or change the model before deployment.

## Run a performance check

Next, ask MLIA for a target-aware performance estimate using the INT8 LiteRT model:

```bash
mlia check tflite/mv2_int8.tflite \
  --target-profile ethos-u85-256 \
  --performance \
  --backend vela \
  --json
```

Because this run uses Vela, the performance report uses the same top-level structure as the compatibility report, but the `results` object now contains estimated performance metrics, operator-level breakdowns, and advice:

```output
{
  "results": [
    {
      "kind": "performance",
      "status": "ok",
      "warnings": [
        "The performance figures above refer to NPU only"
      ],
      "metrics": [
        {
          "name": "npu_cycles",
          "value": 3623146
        },
        {
          "name": "total_cycles",
          "value": 5006357
        },
        {
          "name": "inference_time",
          "unit": "ms",
          "value": 5.006357
        },
        {
          "name": "inferences_per_second",
          "unit": "inferences/s",
          "value": 199.74604288108097
        },
        {
          "name": "target_utilization",
          "unit": "%",
          "value": 72.3709076280417
        }
      ],
      "advice": [
        {
          "category": "performance",
          "severity": "warning",
          "message": "The following layers make up the majority of operator cycles..."
        },
        {
          "category": "performance",
          "severity": "warning",
          "message": "Among the layers with the highest impact, 5 layers have been identified with low MAC utilization..."
        },
        {
          "category": "performance",
          "severity": "warning",
          "message": "Among the layers with the highest impact, 5 layers have been identified as possibly memory bound..."
        }
      ]
    }
  ]
}
```

## What does this report tell us?

| Field | What it tells you |
| --- | --- |
| `warnings` | Important scope limits for the result, such as the estimate referring to NPU work only. |
| `metrics` | Summary estimates for cycles, inference time, throughput, utilization, model size, and memory use. |
| `breakdowns` | Per-operator metrics, including operator cycles, memory access cycles, MAC count, and MAC utilization. |
| `advice` | MLIA's interpretation of the metrics, including which layers dominate cycles or may be inefficient. |
| `availability` and `reason` | Why a metric is not available from the selected backend, if MLIA cannot report it. |

For this INT8 LiteRT file, the Vela-backed estimate reports about `5.01M` total cycles, about `5.01 ms` inference time for batch size 1, about `199.7` inferences per second, and about `72.4%` target utilization. It also reports about `3.62M` NPU cycles, plus SRAM and DRAM access cycles. Treat these as target-aware estimates for the NPU portion of the model, not as final runtime measurements from hardware.

MLIA is now advising on where to investigate to improve target performance. In this report, the advice identifies the ten layers that make up most operator cycles, flags five high-impact layers with low MAC utilization, and flags five high-impact layers as possibly memory-bound. Low MAC utilization can be expected for layers with small channel counts, small spatial dimensions, or heavy memory movement, so these are the layers to consider adjusting.

## What you have learned

You have used MLIA to check compatibility and estimate performance with LiteRT and Vela. You have also learned how to read target metadata, backend metadata, metrics, operator placement, and advice.

Next, you will inspect the TOSA intermediate representation using MLIA.
