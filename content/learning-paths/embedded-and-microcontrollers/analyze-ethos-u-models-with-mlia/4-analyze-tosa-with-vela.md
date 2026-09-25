---
title: Analyze TOSA IR artifacts with Vela

description: Analyze TOSA artifacts with MLIA and Vela to compare FP32 and INT8 compatibility, performance estimates, and NPU mapping.

weight: 5

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## What TOSA is

Tensor Operator Set Architecture (TOSA) is an intermediate representation for machine learning graphs. It's a stable set of tensor operators that can sit between a model framework and a target backend. The [TOSA specification](https://www.mlplatform.org/tosa/tosa_spec.html) defines the operator set and semantics.

Instead of asking every backend to understand every framework operator directly, a conversion flow can lower supported parts of a model into TOSA. Backend tools can then analyze or compile that TOSA graph for a target.

TOSA can appear in more than one kind of ML workflow. Some compiler flows for LiteRT models can use TOSA as an intermediate representation. Other LiteRT flows hand a `.tflite` file directly to a backend tool such as Vela. In the ExecuTorch Arm Ethos-U flow, supported PyTorch graph regions are lowered to TOSA before Vela compiles them for Ethos-U.

## Compare FP32 and INT8 TOSA artifacts

The model artifacts repository includes floating-point and quantized TOSA variants:

```output
tosa/mv2_fp32.tosa
tosa/mv2_int8.tosa
```

Start with the FP32 TOSA model:

```bash
mlia check tosa/mv2_fp32.tosa \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

The result is similar to the FP32 LiteRT check. The model can be expressed as an artifact, but it's not in the supported quantized integer form required for Ethos-U acceleration with this target profile. The important distinction is that TOSA describes an intermediate graph form rather than a complete runtime deployment.

Run the same compatibility check on the quantized INT8 TOSA model:

```bash
mlia check tosa/mv2_int8.tosa \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

The INT8 TOSA report shows `status` as `ok` and `accelerator_operator_percentage` as `100.0`. The model format is now TOSA, but the target profile and Vela backend configuration are the same as the LiteRT run.

The difference from the FP32 TOSA artifact is that the INT8 artifact has the quantized representation required for Ethos-U acceleration. The operator support checks pass, and MLIA expects the operator work to map to the NPU path.

You can also run a performance check using the INT8 `.tosa` model:

```bash
mlia check tosa/mv2_int8.tosa \
  --target-profile ethos-u85-256 \
  --performance \
  --backend vela \
  --json
```

The report is similar to the INT8 LiteRT performance result. The model maps to the NPU path. MLIA reports NPU-scoped estimated metrics, and the advice points you toward operators that dominate estimated cycles or have low utilization.

Whether TOSA with MLIA is useful depends on your workflow. Many developers will likely use ExecuTorch or LiteRT artifacts directly.

## What you've accomplished and what's next

You have seen how the same MLIA CLI pattern applies to TOSA, and how TOSA bridges model formats and backend compilation.

Next, you'll learn how packaged ExecuTorch `.pte` artifacts fit into the same MLIA workflow.
