---
title: Prepare the XNNPACK baseline
description: Prepare the XNNPACK baseline and apply four patches for a KleidiAI SME2 integration that you will inspect and validate.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll build

You'll integrate a KleidiAI matrix multiplication microkernel into the existing XNNPACK `qd8_f16_qc4w` fully connected operator.

The completed path uses a KleidiAI microkernel for Scalable Matrix Extension 2 (SME2) matrix outer product accumulate (MOPA) instructions:

```text
kai_matmul_clamp_f16_qai8dxp1vlx8_qsi4cxp4vlx8_1vlx4vl_sme2_mopa
```

The name identifies the output, operand formats, and instruction family:

- `f16`: The output is FP16.
- `qai8dxp`: The left-hand side (LHS) is asymmetric int8 quantized per row.
- `qsi4cxp`: The right-hand side (RHS) is signed int4 quantized per output channel.
- `sme2_mopa`: It uses SME2 matrix outer product accumulate instructions.

This is a framework-integration example. You won't write a new assembly microkernel. Instead, you'll learn how to select an existing kernel, adapt framework-owned tensors to its packed layouts, dispatch it safely, and verify correctness.

## Clone the tested XNNPACK revision

The patch series that you'll use was created and tested from the XNNPACK commit `119bb329762be10e63688256bb989a0007445b49`.

Other XNNPACK revisions can have different microkernel lists, packing helpers, or operator code. Use this exact revision when you clone and check out XNNPACK:

```bash
git clone https://github.com/google/XNNPACK.git
cd XNNPACK
git checkout 119bb329762be10e63688256bb989a0007445b49
```

## Download the patch series

The four patches supply the complete implementation. Download the patches into the XNNPACK checkout directory:

```bash
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0001-prepare-qd8-f16-qc4w-sme2-kernel.patch
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0002-support-transposed-kai-qc4w-weights.patch
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0003-pack-qd8-lhs-for-kai-sme2.patch
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/integrate-kleidiai-kernel-xnnpack-qd8-f16-qc4w/0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch
```

The patch files are named in numeric order. From the XNNPACK directory, apply the patches in order:

```bash
git am 0001-prepare-qd8-f16-qc4w-sme2-kernel.patch
git am 0002-support-transposed-kai-qc4w-weights.patch
git am 0003-pack-qd8-lhs-for-kai-sme2.patch
git am 0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch
```

You'll learn about the changes these patches have already applied. Use the snippets in the Learning Path to understand the implementation in your checkout. You don't need to add them again. After inspecting the patch snippets, you'll build and validate the integration.

## The complete data flow

XNNPACK owns the operator lifecycle. KleidiAI supplies optimized packing and matrix multiplication components:

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

## What you've accomplished and what's next

You've checked out the tested XNNPACK revision and applied the four integration patches. Your checkout is ready for the implementation walkthrough and subsequent build.

Next, you'll examine the operator inputs before reviewing the kernel selection.
