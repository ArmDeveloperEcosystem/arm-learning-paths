---
title: Run MoE inference with vLLM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section validates that the selected MoE models can be served with vLLM on Arm CPUs and queried through the OpenAI-compatible API.

For each model, start the vLLM server in one terminal, then send a test request from another terminal. Before starting another model, stop the current vLLM server. Only one vLLM server can use the default port `8000` at a time.

## Model commands

Use the following model IDs in the `vllm serve` and `curl` commands.

| Model | Model ID |
| --- | --- |
| Gemma4 BF16 | `google/gemma-4-26B-A4B-it` |
| GPT-OSS BF16 | `unsloth/gpt-oss-20b-BF16` |
| Qwen3 BF16 | `Qwen/Qwen3-30B-A3B-Thinking-2507` |
| Qwen3 W8A8 | `RedHatAI/Qwen3-30B-A3B-Thinking-2507-quantized.w8a8` |

## GPT-OSS tiktoken setup

GPT-OSS uses Harmony formatting and requires local tiktoken encoding files in this setup. Download the required encoding files and set the cache environment variables before starting the GPT-OSS vLLM server:

```bash
mkdir -p tiktoken_encodings

wget -O tiktoken_encodings/o200k_base.tiktoken \
  https://openaipublic.blob.core.windows.net/encodings/o200k_base.tiktoken

wget -O tiktoken_encodings/cl100k_base.tiktoken \
  https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken

export TIKTOKEN_ENCODINGS_BASE=$PWD/tiktoken_encodings
export TIKTOKEN_RS_CACHE_DIR=$PWD/tiktoken_encodings
```

## Start a model server

Set the model ID and start the vLLM server. For example, to serve Gemma4 BF16:

```bash
export MODEL=google/gemma-4-26B-A4B-it

vllm serve "$MODEL"
```

Wait until you see `Application startup complete` before continuing. The server is now listening on port `8000`.

To test a different model, stop the current server, update `MODEL` using one of the model IDs from the table, and run `vllm serve "$MODEL"` again.

## Send a test request

In another terminal, set the same model ID and send a test request:

```bash
export MODEL=google/gemma-4-26B-A4B-it

curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$MODEL"'",
    "messages": [
      {"role": "user", "content": "Explain mixture of experts in one sentence."}
    ],
    "max_tokens": 64,
    "temperature": 0
  }'
```

If the server returns a valid chat completion response, inference is working for the selected model.

## What you've accomplished and what's next

You've now served BF16 and INT8/W8A8 MoE models with vLLM on Arm CPUs.

Next, you'll benchmark the models with `vllm bench serve`.