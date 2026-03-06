---
title: Install prerequisites and download the model
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you install the macOS dependencies required to build LiteRT-LM and prepare a Gemma model in LiteRT-LM `.litertlm` format.

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

## Prepare a LiteRT-LM-compatible model

LiteRT-LM benchmark commands in this Learning Path use `litert_lm_advanced_main`, which expects a LiteRT-LM model artifact (`.litertlm`) for `--model_path`.

The `google/gemma-3-4b-it` repository on Hugging Face follows the Transformers layout (multiple `safetensors` files), so it is not directly consumable by `litert_lm_advanced_main`.

Use a prebuilt LiteRT-LM model artifact instead:

```bash
cd $HOME/gemma4-prefill-bench/LiteRT-LM/models
hf auth login
hf download google/gemma-3n-E4B-it-litert-lm \
  --include "gemma-3n-E4B-it-int4.litertlm" \
  --local-dir ./gemma-3n-E4B-it-litert-lm

cp ./gemma-3n-E4B-it-litert-lm/gemma-3n-E4B-it-int4.litertlm \
   ./gemma-3n-E4B-it-int4.litertlm

ls -lh ./gemma-3n-E4B-it-int4.litertlm
```

{{% notice Note %}}
The model repository is gated. Make sure your Hugging Face account has accepted the model terms before downloading.
{{% /notice %}}

Expected layout:

```text
LiteRT-LM/models/
├── gemma-3n-E4B-it-int4.litertlm
└── gemma-3n-E4B-it-litert-lm/
    └── gemma-3n-E4B-it-int4.litertlm
```

## What you've accomplished and what's next

In this section:
- You installed macOS prerequisites and pinned Bazel for LiteRT-LM
- You created the local model directory and prepared a LiteRT-LM-compatible `.litertlm` Gemma model

In the next section, you will build and run the benchmark workflow.
