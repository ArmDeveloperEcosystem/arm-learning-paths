---
title: Install prerequisites and download Gemma 4
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install prerequisites on macOS

Install Xcode Command Line Tools if they are not already available:

```bash
xcode-select --install
```

Install Bazelisk:

```bash
brew install bazelisk
```

Install the Hugging Face Hub CLI:

```bash
python3 -m pip install -U huggingface_hub
```

Confirm that LiteRT-LM pins Bazel `7.6.1`:

```bash
cd $HOME/gemma4-prefill-bench/LiteRT-LM
cat .bazelversion
bazelisk version
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
  --local-dir models/gemma-4-E2B-it-litert-lm
```

The model repository is public. If Hugging Face asks for credentials, run
`hf auth login` and repeat the download.

Verify the downloaded file:

```bash
shasum -a 256 \
  models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm
ls -lh models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm
```

The expected SHA-256 checksum is:

```output
181938105e0eefd105961417e8da75903eacda102c4fce9ce90f50b97139a63c  models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm
```

{{% notice Note %}}
The file is about 2.6 GB. LiteRT-LM requires the `.litertlm` artifact; a
Transformers repository containing only `safetensors` files is not a direct
replacement.
{{% /notice %}}

In the next section, you will build each XNNPACK variant and run the benchmark.
