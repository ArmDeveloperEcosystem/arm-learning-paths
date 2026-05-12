---
title: Overview and benchmark workflow
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why this benchmark matters

This Learning Path gives you a reproducible process to evaluate Gemma prefill performance improvements when using SME2-optimized paths across LiteRT-LM, KleidiAI, and XNNPACK.

The flow in this guide is based on a pinned set of repository commits and a local benchmark command (`litert_lm_advanced_main --benchmark`) so your numbers are comparable across runs.

## What you will do

You will complete the workflow in this order:

1. Create a local workspace and clone LiteRT-LM, KleidiAI, and XNNPACK at tested commits.
2. Install macOS prerequisites and Bazelisk, then pin Bazel to version `7.6.1`.
3. Prepare a LiteRT-LM-compatible `.litertlm` model in `LiteRT-LM/models`.
4. Build LiteRT-LM and run benchmark and sample prompts.

In the next section, you will set up the workspace with pinned repository commits.

## Find out if your device supports SME2

Confirm your machine exposes SME/SME2 to user space:

```bash
uname -m
sysctl -a | grep -Ei 'sme2|sme'
```

Expected result:
- `uname -m` should report `arm64`
- `sysctl` output should include an SME/SME2 capability entry

If you do not see SME/SME2 in the `sysctl` output, this benchmark can still run, but XNNPACK/KleidiAI will dispatch non-SME2 kernels and your prefill throughput will likely be lower.

{{% notice Note %}}
For a deeper validation (compiler + runtime streaming mode checks), see the cross-platform Learning Path section [Test your SME2 development environment](./learning-paths/cross-platform/multiplying-matrices-with-sme2/2-check-your-environment).
{{% /notice %}}
