---
title: Set up workspace and pinned repositories
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you prepare a local workspace and clone the exact LiteRT-LM, KleidiAI, and XNNPACK commits used for this benchmark flow.

Create a working directory and move into it:

```bash
mkdir -p $HOME/gemma4-prefill-bench
cd $HOME/gemma4-prefill-bench
```

## Clone tested commits

Clone the repositories and check out pinned commits:

```bash
git clone https://github.com/google-ai-edge/LiteRT-LM.git LiteRT-LM
git -C LiteRT-LM checkout 41d6b964c21f225af9dad7088231b024c369adc1

git clone https://github.com/ARM-software/kleidiai.git kleidiai
git -C kleidiai checkout 72a6a50c1dba714ff27a908e8dd54be3628794b0

git clone https://github.com/google/xnnpack.git xnnpack
git -C xnnpack checkout deb87c027acd2cca4e59fd1f227e523a1640d24c
```

Expected layout:

```text
gemma4-prefill-bench/
├── kleidiai/
├── LiteRT-LM/
└── xnnpack/
```

In the next section, you will install prerequisites and download the model.
