---
title: Overview and prerequisites
description: Prepare the XNNPACK baseline and apply four patches for a KleidiAI SME2 integration that you will inspect and validate.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you will build

You integrate a KleidiAI matrix multiplication microkernel into the existing XNNPACK `qd8_f16_qc4w` fully connected operator.

The completed path uses a KleidiAI microkernel for Scalable Matrix Extension 2 (SME2) matrix outer product accumulate (MOPA) instructions:

```text
kai_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa
```

The name identifies the output, operand formats, and instruction family:

- `f16`: The output is FP16.
- `qai8dxp`: The left-hand side (LHS) is asymmetric int8 quantized per row.
- `qsi4cxp`: The right-hand side (RHS) is signed int4 quantized per output channel.
- `sme2_mopa`: It uses SME2 matrix outer product accumulate instructions.

The following pages use KAI as shorthand for KleidiAI interfaces, matching the `kai_` prefix in function names.

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

The four patches supply the complete implementation. Download them into the XNNPACK checkout directory you entered in the previous step:

```bash
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0001-prepare-qd8-f16-qc4w-sme2-kernel.patch
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0002-support-transposed-kai-qc4w-weights.patch
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0003-pack-qd8-lhs-for-kai-sme2.patch
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch
```

From that directory, apply the patches once in numeric order:

```bash
git am 0001-prepare-qd8-f16-qc4w-sme2-kernel.patch
git am 0002-support-transposed-kai-qc4w-weights.patch
git am 0003-pack-qd8-lhs-for-kai-sme2.patch
git am 0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch
```

The following pages walk through the changes these patches have already applied. Use the snippets to understand the implementation in your checkout; you do not need to add them again. After the walkthrough, build and validate the integration.

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

Follow the applied implementation through these steps:

1. Inspect the matrix and quantization formats used by `qd8_f16_qc4w`.
2. Examine why the selected KleidiAI microkernel matches the operator.
3. Trace how static QC4W weights are packed during operator creation.
4. Trace how dynamic QD8 activations are packed at execution time without changing their quantization.
5. Inspect SME2 runtime dispatch and the KleidiAI kernel call.
6. Build for Android and validate the completed integration on an SME2 device.

## What you've accomplished

You have checked out the tested XNNPACK revision and applied the four integration patches. Your checkout is ready for the implementation walkthrough and subsequent build.

Next, examine the operator inputs before reviewing the kernel selection.
