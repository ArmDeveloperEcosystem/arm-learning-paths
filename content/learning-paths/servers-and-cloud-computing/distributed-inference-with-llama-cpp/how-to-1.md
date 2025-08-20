---
title: Convert model to GGUF and quantize
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This example runs on three AWS Graviton4 `c8g.4xlarge` instances. Each instance has 16 cores, 32 GB of RAM, and 200 GB of disk storage to store the downloaded and quantized model weights.

In this Learning Path, you will:

- Download Meta's [Llama 3.1 70B parameter model](https://huggingface.co/meta-llama/Llama-3.1-70B).
- Download and build `llama.cpp`, a C++ library for efficient CPU inference of LLaMA and similar large language models on CPUs, optimized for local and embedded environments.
- Convert Meta's `safetensors` files to a single GGUF file.
- Quantize the 16-bit GGUF weights file to 4-bit weights.
- Load and run the model.

{{% notice Note %}}
The **Reading time** shown on the **Introduction** page does not include downloading, converting, and quantizing the model. These steps can take 1-2 hours. If you already have a quantized GGUF file, you can skip the download and quantization.
{{% /notice %}}

## Set up dependencies

Before you start, make sure you have permission to access Meta's [Llama 3.1 70B parameter model](https://huggingface.co/meta-llama/Llama-3.1-70B).

{{% notice Note %}}
You must repeat the install steps on each device. However, only run the download and quantization steps once as `llama.cpp` caches the tensors for reuse across devices.
{{% /notice %}}

## Create a virtual environment

```bash
apt update
apt install -y python3.12-venv
python3 -m venv myenv
source myenv/bin/activate
```

## Clone the llama.cpp repo and build dependencies

```bash
git clone https://github.com/ggerganov/llama.cpp
apt install -y cmake build-essential
apt install -y g++
apt install -y libcurl4-openssl-dev
cd llama.cpp
mkdir -p build-rpc
cd build-rpc
cmake .. -DGGML_RPC=ON -DLLAMA_BUILD_SERVER=ON
cmake --build . --config Release
```

The build output is placed in the `build-rpc/bin` directory.

Verify that the build succeeded by running the help command:

```bash
bin/llama-cli -h
```

## Download the model (single instance)

Install Hugging Face Hub in your virtual environment:

```bash
pip3 install huggingface_hub
```

Create a new Python file named `download.py`:

```bash
cd ../..
vi download.py
```

Add the following code:

```python
import os
from huggingface_hub import snapshot_download
model_id = "meta-llama/Llama-3.1-70B"
local_dir = "llama-hf"

# Create the directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)

# Download the model snapshot
snapshot_download( repo_id=model_id, local_dir=local_dir,
    revision="main",
    token="your_hf_token",
    allow_patterns=["*.md", "*.json", "*.safetensors"]
)
```

Run the script:

```bash
python3 download.py
```

## Convert and quantize the model (single instance)

Install the conversion dependencies:

```bash
pip3 install -r llama.cpp/requirements.txt
```

Convert the model:

```bash
python3 llama.cpp/convert_hf_to_gguf.py llama-hf
```

Quantize the model to 4-bit weights:

```bash
cd llama.cpp/build-rpc
bin/llama-quantize ../../llama-hf/Llama-3.1-70B-F16.gguf Q4_0
```

You can rename the output file to `model.gguf` for easier use.

Check available quantization options:

```bash
bin/llama-quantize -h
```

This command lists supported quantization formats and options. For example:

```output
usage: bin/llama-quantize [--help] [--allow-requantize] [--leave-output-tensor] [--pure] [--imatrix] [--include-weights] [--exclude-weights] [--output-tensor-type]
       [--token-embedding-type] [--tensor-type] [--keep-split] [--override-kv] model-f32.gguf [model-quant.gguf] type [nthreads]

  --allow-requantize: Allows requantizing tensors that have already been quantized. Warning: This can severely reduce quality compared to quantizing from 16bit or 32bit
  --leave-output-tensor: Will leave output.weight un(re)quantized. Increases model size but may also increase quality, especially when requantizing
  --pure: Disable k-quant mixtures and quantize all tensors to the same type
  --imatrix file_name: use data in file_name as importance matrix for quant optimizations
  --include-weights tensor_name: use importance matrix for this/these tensor(s)
  --exclude-weights tensor_name: use importance matrix for this/these tensor(s)
  --output-tensor-type ggml_type: use this ggml_type for the output.weight tensor
  --token-embedding-type ggml_type: use this ggml_type for the token embeddings tensor
  --tensor-type TENSOR=TYPE: quantize this tensor to this ggml_type. example: --tensor-type attn_q=q8_0
      Advanced option to selectively quantize tensors. May be specified multiple times.
  --keep-split: will generate quantized model in the same shards as input
  --override-kv KEY=TYPE:VALUE
      Advanced option to override model metadata by key in the quantized model. May be specified multiple times.
Note: --include-weights and --exclude-weights cannot be used together

Allowed quantization types:
   2  or  Q4_0    :  4.34G, +0.4685 ppl @ Llama-3-8B
   3  or  Q4_1    :  4.78G, +0.4511 ppl @ Llama-3-8B
   8  or  Q5_0    :  5.21G, +0.1316 ppl @ Llama-3-8B
   9  or  Q5_1    :  5.65G, +0.1062 ppl @ Llama-3-8B
  19  or  IQ2_XXS :  2.06 bpw quantization
  20  or  IQ2_XS  :  2.31 bpw quantization
  28  or  IQ2_S   :  2.5  bpw quantization
  29  or  IQ2_M   :  2.7  bpw quantization
  24  or  IQ1_S   :  1.56 bpw quantization
  31  or  IQ1_M   :  1.75 bpw quantization
  36  or  TQ1_0   :  1.69 bpw ternarization
  37  or  TQ2_0   :  2.06 bpw ternarization
  10  or  Q2_K    :  2.96G, +3.5199 ppl @ Llama-3-8B
  21  or  Q2_K_S  :  2.96G, +3.1836 ppl @ Llama-3-8B
  23  or  IQ3_XXS :  3.06 bpw quantization
  26  or  IQ3_S   :  3.44 bpw quantization
  27  or  IQ3_M   :  3.66 bpw quantization mix
  12  or  Q3_K    : alias for Q3_K_M
  22  or  IQ3_XS  :  3.3 bpw quantization
  11  or  Q3_K_S  :  3.41G, +1.6321 ppl @ Llama-3-8B
  12  or  Q3_K_M  :  3.74G, +0.6569 ppl @ Llama-3-8B
  13  or  Q3_K_L  :  4.03G, +0.5562 ppl @ Llama-3-8B
  25  or  IQ4_NL  :  4.50 bpw non-linear quantization
  30  or  IQ4_XS  :  4.25 bpw non-linear quantization
  15  or  Q4_K    : alias for Q4_K_M
  14  or  Q4_K_S  :  4.37G, +0.2689 ppl @ Llama-3-8B
  15  or  Q4_K_M  :  4.58G, +0.1754 ppl @ Llama-3-8B
  17  or  Q5_K    : alias for Q5_K_M
  16  or  Q5_K_S  :  5.21G, +0.1049 ppl @ Llama-3-8B
  17  or  Q5_K_M  :  5.33G, +0.0569 ppl @ Llama-3-8B
  18  or  Q6_K    :  6.14G, +0.0217 ppl @ Llama-3-8B
   7  or  Q8_0    :  7.96G, +0.0026 ppl @ Llama-3-8B
   1  or  F16     : 14.00G, +0.0020 ppl @ Mistral-7B
  32  or  BF16    : 14.00G, -0.0050 ppl @ Mistral-7B
   0  or  F32     : 26.00G              @ 7B
          COPY    : only copy tensors, no quantizing
```