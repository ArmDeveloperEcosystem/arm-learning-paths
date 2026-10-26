---
title: Set up the Gemma 4 benchmark workspace
description: Set up LiteRT-LM, KleidiAI, and baseline and optimized XNNPACK builds for the Gemma 4 benchmark.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll build

You'll benchmark Gemma 4 CPU inference with LiteRT-LM and KleidiAI on macOS. You'll compare
baseline and optimized XNNPACK builds to measure prefill and decode throughput.

The optimized build improves one-thread decode by 53.6% on Apple M4 Pro and
44.5% on the Android example. Prefill and thread scaling vary by device, so
compare both phases using the same model and settings.

## Confirm SME2 support on your device

Use an SME2-capable Mac, such as an M4-family Mac. For Mac and Android examples, see the
[devices with native SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices).

A macOS device is used as an example in this Learning Path.

Confirm the host architecture and SME feature flags:

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

If either feature reports `0`, XNNPACK can't dispatch the SME2 kernels and the
macOS performance comparison isn't valid.

## Create the workspace

Create a working directory outside the Learning Paths repository:

```bash
mkdir -p $HOME/gemma4-prefill-bench
cd $HOME/gemma4-prefill-bench
```

## Clone the sources

{{% notice Note %}}
The commands check out specific revisions so that you can reproduce the benchmark results.
{{% /notice %}}

Clone LiteRT-LM, KleidiAI, and XNNPACK:

```bash
git clone https://github.com/google-ai-edge/LiteRT-LM.git LiteRT-LM
git -C LiteRT-LM checkout 924e79c91542761242244e4f1651851f822e4cbb

git clone https://github.com/ARM-software/kleidiai.git kleidiai
git -C kleidiai checkout 02f7b3df98c39df1884eead7461c3269feca4ddc

git clone https://github.com/google/XNNPACK.git xnnpack
git -C xnnpack fetch origin 27199f7c0b5d0178a67f666d2ba85db56ec9858e
git -C xnnpack checkout --detach 27199f7c0b5d0178a67f666d2ba85db56ec9858e
```

## Create the baseline

Create a separate XNNPACK worktree for the baseline. It already includes earlier
SME2 support; the optimized build adds the static INT2 SME2 kernels.

```bash
git -C xnnpack worktree add --detach ../xnnpack-baseline \
  c6b52536d3f614793f21ab4a17ae1cde73cc0333
```
## What you've accomplished and what's next

You've prepared the sources and baseline.

Next, you'll install the build tools and
download the Gemma 4 model.
