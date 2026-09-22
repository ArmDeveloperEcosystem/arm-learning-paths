---
title: Set up the Gemma 4 benchmark workspace
description: Prepare a reproducible macOS workspace for comparing Gemma 4 LiteRT-LM performance with baseline and SME2-optimized XNNPACK variants.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll build

You'll build a workflow for comparing Gemma 4 CPU performance with the upstream XNNPACK SME2 Int4 and Int2 paths used through LiteRT-LM and KleidiAI.

The workflow records the repository revisions and uses the
`litert_lm_advanced_main --benchmark` command so that you can compare results
across XNNPACK variants.

## Confirm SME2 support on your device

Confirm the architecture and SME feature flags:

```bash
uname -m
sysctl hw.optional.arm.FEAT_SME
sysctl hw.optional.arm.FEAT_SME2
```

The output on a supported Apple M4 system is similar to:

```output
arm64
hw.optional.arm.FEAT_SME: 1
hw.optional.arm.FEAT_SME2: 1
```

If either feature reports `0`, XNNPACK can't dispatch the SME2 kernels, and the
performance comparison isn't valid.

For a deeper validation, see [Test your SME2 development
environment](/learning-paths/cross-platform/multiplying-matrices-with-sme2/2-check-your-environment).

After confirming SME2 support on your device, create a workspace. Then, clone LiteRT-LM `v0.16.1`, KleidiAI `v1.30.0`, and upstream XNNPACK with SME2 Int4 and Int2 support.

## Create a workspace directory

Create a working directory outside the Learning Paths repository and navigate to it:

```bash
mkdir -p $HOME/gemma4-prefill-bench
cd $HOME/gemma4-prefill-bench
```

## Clone the tested LiteRT-LM and KleidiAI versions

Clone LiteRT-LM and check out the tested `v0.16.1` commit:

```bash
git clone https://github.com/google-ai-edge/LiteRT-LM.git LiteRT-LM
git -C LiteRT-LM checkout 924e79c91542761242244e4f1651851f822e4cbb
```

Clone KleidiAI and check out `v1.30.0`, which the upstream XNNPACK SME2 paths
require:

```bash
git clone https://github.com/ARM-software/kleidiai.git kleidiai
git -C kleidiai checkout 74b1a12d3620c89dae4766de640e064952000f4d
```

## Create the XNNPACK variants

Clone upstream XNNPACK using the default XNNPACK branch:

```bash
git clone https://github.com/google/XNNPACK.git xnnpack
git -C xnnpack log -1 --oneline
```
The default XNNPACK branch contains the merged SME2 Int4 and Int2 support, and is the optimized tree.

Record the commit printed by the command so that you can identify the exact upstream
revision used for your results.

Create a historical baseline worktree from the common XNNPACK revision before
the SME2 Int4 and Int2 support:

```bash
git -C xnnpack worktree add --detach ../xnnpack-baseline \
  eb452a766d8f1075b5491f22309e8f09bd31d828
```

Verify the repository revisions:

```bash
git -C LiteRT-LM rev-parse HEAD
git -C kleidiai rev-parse HEAD
git -C xnnpack rev-parse HEAD
git -C xnnpack-baseline rev-parse HEAD
```

The baseline command should print
`eb452a766d8f1075b5491f22309e8f09bd31d828`.

The workspace layout is now:

```output
gemma4-prefill-bench/
├── kleidiai/
├── LiteRT-LM/
├── xnnpack/
└── xnnpack-baseline/
```

## What you've accomplished and what's next

You now have a workspace for the Gemma 4 benchmark.

Next, you'll install the prerequisites and download the Gemma 4 model.
