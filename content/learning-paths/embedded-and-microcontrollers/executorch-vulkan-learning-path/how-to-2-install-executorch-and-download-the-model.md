---
title: Install ExecuTorch and download the model
description: Clone the ExecuTorch release branch, create the Python environment, and fetch the gated Llama 3.2 model files.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clone ExecuTorch 1.4

Keep a source checkout because you will cross-compile the Android runtime and the standalone Llama runner:

```bash
cd $HOME
git clone --branch release/1.4 --recursive https://github.com/pytorch/executorch.git
cd executorch
git submodule update --init --recursive
```

Create and activate a Python virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
```

To reduce memory pressure during builds:

```bash
export CMAKE_BUILD_PARALLEL_LEVEL=2
```

## Fix the PyTorch version mismatch

On the tested `release/1.4` branch, a host environment with PyTorch `2.14.0+cpu` broke the build with:

```text
ATen/core/Tensor.h:70:37: error: 'C10_LIFETIMEBOUND' does not name a type
```

Pin the expected version explicitly:

```bash
python -m pip uninstall -y torch
python -m pip install "torch==2.13.0+cpu" --index-url https://download.pytorch.org/whl/cpu
python -c "import torch; print(torch.__version__)"
```

Expected output:

```text
2.13.0+cpu
```

Then clean and rebuild the host package:

```bash
python install_executorch.py --clean
export CMAKE_BUILD_PARALLEL_LEVEL=2
./install_executorch.sh --use-pt-pinned-commit
```

The important lesson is to verify `torch.__version__` before you start a long native build.

## Request access to Llama 3.2 1B Instruct

The model used in this workflow comes from the gated Hugging Face repository [`meta-llama/Llama-3.2-1B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct).

To request access:

1. Sign in to your Hugging Face account.
2. Open the Llama 3.2 1B Instruct model page.
3. Review and accept the Meta Llama license, then submit the access request.
4. Wait until Hugging Face confirms that your account can access the repository before continuing.

Access approval is associated with the Hugging Face account that submitted the request. Authenticate the CLI with the same account.

## Install and authenticate the Hugging Face CLI

Install the Hugging Face Hub CLI in the active Python virtual environment:

```bash
python -m pip install --upgrade huggingface_hub
hf version
```

Sign in. The command prompts you to authenticate through a browser or with a Hugging Face user access token:

```bash
hf auth login
hf auth whoami
```

Confirm that `hf auth whoami` displays the account that has access to the gated model.

## Download Llama 3.2 1B Instruct

Keep the model outside the source tree:

```bash
hf download \
  meta-llama/Llama-3.2-1B-Instruct \
  --include "original/*" \
  --local-dir ~/Llama-3.2-1B-Instruct
```

Verify that the three files required by the export are present:

```bash
test -f ~/Llama-3.2-1B-Instruct/original/consolidated.00.pth && echo "Checkpoint OK"
test -f ~/Llama-3.2-1B-Instruct/original/params.json && echo "Parameters OK"
test -f ~/Llama-3.2-1B-Instruct/original/tokenizer.model && echo "Tokenizer OK"
```

The measured run used:

- `consolidated.00.pth` at about 2.4 GB
- `params.json`
- `tokenizer.model` at about 2.1 MB

{{% notice Access errors %}}
If the download returns `401 Unauthorized` or `403 Forbidden`, run `hf auth whoami` and confirm that you authenticated with the account approved for the gated repository. If access is still pending, return to the model page and check the request status.
{{% /notice %}}
