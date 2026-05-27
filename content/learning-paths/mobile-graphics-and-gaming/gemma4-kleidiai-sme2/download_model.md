---
title: Install prerequisites and download the model
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you install the macOS dependencies required to build LiteRT-LM and prepare a Gemma 4 model in LiteRT-LM `.litertlm` format.

## Install prerequisites on macOS

Install Xcode Command Line Tools (if needed):

```bash
xcode-select --install
```

Install Bazelisk:

```bash
brew install bazelisk
```

Install the Hugging Face Hub CLI:

```bash
python3 -m pip install -U "huggingface_hub[cli]"
```

Pin Bazel version `7.6.1` from the LiteRT-LM root:

```bash
cd $HOME/gemma4-prefill-bench/LiteRT-LM
echo "7.6.1" > .bazelversion
bazelisk version
```

## Create model directory

```bash
mkdir -p $HOME/gemma4-prefill-bench/LiteRT-LM/models
```

{{% notice Note %}}
The benchmark commands in this Learning Path assume your model directory is under `LiteRT-LM/models/`.
{{% /notice %}}

## Prepare a LiteRT-LM-compatible Gemma 4 model

LiteRT-LM benchmark commands in this Learning Path use `litert_lm_advanced_main`, which expects a LiteRT-LM model artifact (`.litertlm`) for `--model_path`.

The base Gemma model repositories on Hugging Face follow the Transformers layout, so they are not directly consumable by `litert_lm_advanced_main`.

Use a prebuilt LiteRT-LM model artifact instead:

```bash
cd $HOME/gemma4-prefill-bench/LiteRT-LM/models
hf download litert-community/gemma-4-E4B-it-litert-lm \
  gemma-4-E4B-it.litertlm \
  --local-dir ./gemma-4-E4B-it-litert-lm

cp ./gemma-4-E4B-it-litert-lm/gemma-4-E4B-it.litertlm \
   ./gemma-4-E4B-it.litertlm

ls -lh ./gemma-4-E4B-it.litertlm
```

{{% notice Note %}}
If the download is denied, run `hf auth login`, accept the model terms in Hugging Face, and repeat the download command.
{{% /notice %}}

Expected layout:

```text
LiteRT-LM/models/
├── gemma-4-E4B-it.litertlm
└── gemma-4-E4B-it-litert-lm/
    └── gemma-4-E4B-it.litertlm
```

## What you've accomplished and what's next

In this section:
- You installed macOS prerequisites and pinned Bazel for LiteRT-LM
- You created the local model directory and prepared a LiteRT-LM-compatible `.litertlm` Gemma 4 model

In the next section, you will build and run the benchmark workflow.
