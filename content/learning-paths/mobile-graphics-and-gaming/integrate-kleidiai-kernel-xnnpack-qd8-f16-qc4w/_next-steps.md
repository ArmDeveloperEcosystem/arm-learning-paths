---
title: Next steps
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Continue learning

You have integrated a KleidiAI SME2 microkernel into an XNNPACK quantized fully connected operator.

Use these Learning Paths to go further:

- [Understand KleidiAI SME2 matmul microkernels](/learning-paths/mobile-graphics-and-gaming/kai_sme2_matmul_ukernel_explained/) explains SME2 MOPA packing and kernel execution in more detail.
- [KleidiAI on Android with MediaPipe and XNNPACK](/learning-paths/mobile-graphics-and-gaming/kleidiai-on-android-with-mediapipe-and-xnnpack/) shows an end-to-end Android inference workflow.

## Improve the integration

The correctness-first adapter packs a qd8 LHS tile immediately before the KAI call. For workloads that split a single activation matrix across many N tiles, consider a workspace-based LHS pre-pack stage:

```text
Pack LHS once per run
  -> reuse packed LHS across all RHS N tiles
```

Keep the same rules when optimizing:

- Preserve the qd8 per-row zero point and scale.
- Pad K with the quantized zero point.
- Query KAI tile dimensions instead of hard-coding vector-length-dependent values.
- Keep the non-SME2 XNNPACK fallback.
