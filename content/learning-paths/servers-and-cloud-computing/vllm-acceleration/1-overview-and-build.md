---
title: Overview and Optimized Build
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is vLLM?

vLLM is an open‑source, high‑throughput inference and serving engine for large language models. It focuses on efficient execution of the LLM inference prefill and decode phases with:

- Continuous batching to keep hardware busy across many requests.
- KV cache management to sustain concurrency during generation.
- Token streaming so results appear as they are produced.

You interact with vLLM in multiple ways:

- OpenAI‑compatible server: expose `/v1/chat/completions` for easy integration.
- Python API: load a model and generate locally when needed.

vLLM works well with Hugging Face models, supports single‑prompt and batch workloads, and scales from quick tests to production serving.

## What you build

You build a CPU‑optimized vLLM for aarch64 with oneDNN and the Arm Compute Library (ACL). You then validate the build with a quick offline chat example.

## Why this is fast on Arm

- Optimized kernels: The aarch64 vLLM build uses direct oneDNN with the Arm Compute Library for key operations.
- 4‑bit weight quantization: INT4 quantization support & acceleration by Arm KleidiAI microkernels.
- Efficient MoE execution: Fused INT4 quantized expert layers reduce memory traffic and improve throughput.
- Optimized Paged attention: Arm SIMD tuned paged attention implementation in vLLM.
- System tuning: Thread affinity and `tcmalloc` help keep latency and allocator overhead low under load.

## Before you begin

- Use Python 3.12 on Ubuntu 22.04+
- Make sure you have at least 32 vCPUs, 64 GB RAM, and 32 GB free disk.

Install the minimum system package used by vLLM on Arm:

```bash
sudo apt-get update -y
sudo apt-get install -y build-essential cmake libnuma-dev
sudo apt install -y python3.12-venv python3.12-dev
```

Optional performance helper you can install now or later:

```bash
sudo apt-get install -y libtcmalloc-minimal4
```

{{% notice Note %}}
On aarch64, vLLM’s CPU backend automatically builds with Arm Compute Library via oneDNN.
{{% /notice %}}

## Build vLLM for aarch64 CPU

Create and activate a virtual environment:

```bash
python3.12 -m venv vllm_env
source vllm_env/bin/activate
python3 -m pip install --upgrade pip
```

Clone vLLM and install build requirements:

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
git checkout 5fb4137
pip install -r requirements/cpu.txt -r requirements/cpu-build.txt
```

Build a wheel targeted at CPU:

```bash
VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel
```

Install the wheel. Use `--no-deps` for incremental installs to avoid clobbering your environment:

```bash
pip install --force-reinstall dist/*.whl              # fresh install
# pip install --no-deps --force-reinstall dist/*.whl  # incremental build
```

{{% notice Tip %}}
Do NOT delete vLLM repo. Local vLLM repository is required for corect inferencing on aarch64 CPU after installing the wheel.
{{% /notice %}}

## Quick validation via offline inferencing

Run the built‑in chat example to confirm the build:

```bash
python examples/offline_inference/basic/chat.py \
  --dtype=bfloat16 \
  --model TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

You should see tokens streaming and a final response. This verifies the optimized vLLM build on your Arm server.

```output
Generated Outputs:
--------------------------------------------------------------------------------
Prompt: None

Generated text: 'The Importance of Higher Education\n\nHigher education is a fundamental right'
--------------------------------------------------------------------------------
Adding requests: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:00<00:00, 9552.05it/s]
Processed prompts: 100%|████████████████████████████████████████████████████████████████████████| 10/10 [00:01<00:00,  6.78it/s, est. speed input: 474.32 toks/s, output: 108.42 toks/s]
...
```

{{% notice Note %}}
As CPU support in vLLM continues to mature, manual builds will be replaced by a simple `pip install` flow for easier setup in near future.
{{% /notice %}}
