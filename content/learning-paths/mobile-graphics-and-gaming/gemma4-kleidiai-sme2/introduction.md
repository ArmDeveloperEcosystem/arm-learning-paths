---
title: Overview and benchmark workflow
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why this benchmark matters

This Learning Path gives you a reproducible process to evaluate Gemma 4 CPU
performance with the upstream XNNPACK SME2 Int4 and Int2 paths used through
LiteRT-LM and KleidiAI.

The workflow records the repository revisions and uses the
`litert_lm_advanced_main --benchmark` command so that you can compare results
across XNNPACK variants.

## What you will do

You will complete the workflow in this order:

1. Create a workspace and clone LiteRT-LM `v0.16.1`, KleidiAI `v1.30.0`, and
   upstream XNNPACK with the SME2 Int4 and Int2 support.
2. Create a historical XNNPACK baseline worktree from before the SME2 support.
3. Download the Gemma 4 E2B `.litertlm` model from Hugging Face.
4. Build and benchmark the baseline and upstream-optimized variants with
   identical settings.
5. Compare steady-state prefill and decode throughput.

## Find out if your device supports SME2

Confirm the architecture and macOS SME feature flags:

```bash
uname -m
sysctl hw.optional.arm.FEAT_SME
sysctl hw.optional.arm.FEAT_SME2
```

The expected output on a supported Apple M4 system is:

```output
arm64
hw.optional.arm.FEAT_SME: 1
hw.optional.arm.FEAT_SME2: 1
```

If either feature reports `0`, XNNPACK cannot dispatch the SME2 kernels and the
performance comparison is not valid.

For a deeper validation, see [Test your SME2 development
environment](./learning-paths/cross-platform/multiplying-matrices-with-sme2/2-check-your-environment).

In the next section, you will set up the benchmark workspace.
