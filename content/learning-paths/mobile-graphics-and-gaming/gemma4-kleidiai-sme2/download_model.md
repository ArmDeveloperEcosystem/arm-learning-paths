---
title: Install prerequisites on macOS and download Gemma 4
description: Install the macOS build tools and verify the Gemma 4 E2B LiteRT-LM model used for both XNNPACK variants.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install prerequisites on macOS

Install Xcode Command Line Tools if they're not already available:

```bash
xcode-select --install
```

Install Bazelisk:

```bash
brew install bazelisk
```

Install the Hugging Face Hub CLI in a virtual environment:

```bash
python3 -m venv "$HOME/gemma4-prefill-bench/.venv"
source "$HOME/gemma4-prefill-bench/.venv/bin/activate"
python3 -m pip install -U huggingface_hub
```

## Download Gemma 4 from Hugging Face

Create a shared model directory in the workspace:

```bash
mkdir -p $HOME/gemma4-prefill-bench/models
cd $HOME/gemma4-prefill-bench
```

Download the CPU-compatible Gemma 4 E2B LiteRT-LM artifact:

```bash
hf download litert-community/gemma-4-E2B-it-litert-lm \
  gemma-4-E2B-it.litertlm \
  --revision 6b78abd019e61a1ca4cbe3b212d2c9ce8ff38a94 \
  --local-dir models/gemma-4-E2B-it-litert-lm
```

If Hugging Face asks for credentials, run `hf auth login` and repeat the download.

Verify the downloaded file:

```bash
shasum -a 256 \
  models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm
```

The expected SHA-256 checksum is:

```output
181938105e0eefd105961417e8da75903eacda102c4fce9ce90f50b97139a63c  models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm
```

{{% notice Note %}}
Download the `.litertlm` artifact used by LiteRT-LM. The file is about 2.6 GB.
{{% /notice %}}

## What you've accomplished and what's next 

You've installed the build tools and verified the shared model artifact.
Next, you'll build each XNNPACK variant and run the benchmark.
