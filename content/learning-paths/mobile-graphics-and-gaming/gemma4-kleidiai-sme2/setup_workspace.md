---
title: Set up the benchmark workspace
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the workspace

Create a working directory outside the Learning Paths repository:

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

Clone upstream XNNPACK. Its default branch contains the merged SME2 Int4 and
Int2 support and is the optimized tree:

```bash
git clone https://github.com/google/XNNPACK.git xnnpack
git -C xnnpack log -1 --oneline
```

Record the commit printed by the command so you can identify the exact upstream
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

In the next section, you will install the prerequisites and download the
Gemma 4 model.
