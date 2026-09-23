---
title: Overview and prerequisites
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you will build

In this Learning Path, you integrate a KleidiAI matrix multiplication microkernel into the existing XNNPACK `qd8_f16_qc4w` fully connected operator.

The completed path uses the following KleidiAI SME2 MOPA microkernel:

```text
kai_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa
```

The name is long, but its important properties are straightforward:

- `f16`: the output is FP16.
- `qai8dxp`: the left-hand side is asymmetric int8 quantized per row.
- `qsi4cxp`: the right-hand side is signed int4 quantized per output channel.
- `sme2_mopa`: it uses SME2 matrix outer product accumulate instructions.

This is a framework-integration example. The aim is not to write a new assembly microkernel. Instead, you learn how to select an existing kernel, adapt framework-owned tensors to its packed layouts, dispatch it safely, and verify correctness.

## Start from the tested XNNPACK revision

The patch series in this Learning Path was created and tested from XNNPACK commit:

```text
119bb329762be10e63688256bb989a0007445b49
```

Use this exact revision when following the steps. Other XNNPACK revisions can have different microkernel lists, packing helpers, or operator code.

```bash
git clone https://github.com/google/XNNPACK.git
cd XNNPACK
git checkout 119bb329762be10e63688256bb989a0007445b49
```

## Download the patch series

The implementation is split into four small patches. Apply them in numeric order after checking out the baseline revision:

```bash
git am 0001-prepare-qd8-f16-qc4w-sme2-kernel.patch
git am 0002-support-transposed-kai-qc4w-weights.patch
git am 0003-pack-qd8-lhs-for-kai-sme2.patch
git am 0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch
```

Download links:

1. [Prepare the SME2 wrapper](../0001-prepare-qd8-f16-qc4w-sme2-kernel.patch)
2. [Support transposed QC4W weights](../0002-support-transposed-kai-qc4w-weights.patch)
3. [Pack the QD8 LHS](../0003-pack-qd8-lhs-for-kai-sme2.patch)
4. [Dispatch through KAI SME2](../0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch)


## The completed data flow

XNNPACK owns the operator lifecycle. KleidiAI supplies optimized packing and matrix multiplication components.

```text
Create operator
  Raw QC4W weights and FP32 bias
      -> pack RHS once for KleidiAI
      -> optionally store packed RHS in the XNNPACK weights cache

Run operator
  QD8 activation values and per-row quantization parameters
      -> pack LHS for KleidiAI without requantizing
      -> run the SME2 MOPA microkernel
      -> write FP16 output
```

On a CPU without SME2 support, XNNPACK continues to use its existing native microkernels. This fallback is essential for portability and correctness.

## What you will do

You will complete these steps:

1. Inspect the matrix and quantization formats used by `qd8_f16_qc4w`.
2. Select a compatible KleidiAI microkernel.
3. Pack the static QC4W right-hand side during operator creation.
4. Pack the dynamic QD8 left-hand side at execution time without changing its quantization.
5. Add SME2 runtime dispatch and call the KleidiAI kernel.
6. Build for Android and validate the completed integration on an SME2 device.


Next, examine the operator inputs before selecting a kernel.
