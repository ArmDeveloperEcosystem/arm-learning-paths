---
title: Run MoE inference with vLLM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate model serving

Start a model server and send a chat request to verify that the selected checkpoint works with your CPU installation.

For each model, start the vLLM server in one terminal, then send a test request from another terminal. Before starting another model, stop the current vLLM server with **Ctrl+C** and wait for it to exit. Only one vLLM server can use the default port `8000` at a time.

## Choose a model

Use the following model IDs in the `vllm serve` and `curl` commands:

| Model | Model ID |
| --- | --- |
| Gemma 4 BF16 | `google/gemma-4-26B-A4B-it` |
| GPT-OSS BF16 | `unsloth/gpt-oss-20b-BF16` |
| Qwen3 BF16 | `Qwen/Qwen3-30B-A3B-Thinking-2507` |
| Qwen3 W8A8 | `RedHatAI/Qwen3-30B-A3B-Thinking-2507-quantized.w8a8` |

## Start a model server

Use the terminal with your virtual environment active and `VLLM_CPU_KVCACHE_SPACE` set. Set the model ID and start the server. For example, to serve Gemma 4 BF16:

```bash
export MODEL=google/gemma-4-26B-A4B-it

vllm serve "$MODEL"
```

On the first run, vLLM downloads the model weights and warms up the model, including CPU code compilation. Wait until you see `Application startup complete` before continuing. The server is now listening on port `8000`.

To test a different model, stop the current server.  Update `MODEL` using one of the model IDs from the table, then run `vllm serve "$MODEL"` again.

## Send a test request

In another terminal on the same server, set the model ID to match the running server and send a test request. 

For example, to send a test request to a Gemma 4 server:

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

`max_tokens` limits generation to 64 tokens, and `temperature: 0` selects greedy decoding. This is a short connectivity and generation check.

The output is similar to the following Gemma 4 response, with some metadata fields omitted for brevity:

```output
{
  "id": "chatcmpl-960932ecaccca7ae",
  "object": "chat.completion",
  "created": 1792608120,
  "model": "google/gemma-4-26B-A4B-it",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Mixture of Experts (MoE) is a neural network architecture that increases model capacity by using a \"router\" to activate only a small, specialized subset of its total parameters for any given input, making it more efficient than dense models."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 21,
    "total_tokens": 70,
    "completion_tokens": 49
  }
}
```

The response text, ID, timestamp, and token counts can vary. The response by the assistant appears in `choices[0].message.content`. In this example, `finish_reason` is `stop`, indicating that generation ended normally rather than reaching the token limit.

A response with generated text confirms that inference is working for the selected model. If `finish_reason` is `length`, generation reached the token limit. Reasoning models can use the short budget before producing a final response. If you need a complete response, inspect any reasoning output and increase `max_tokens`.

## What you've accomplished and what's next

You've validated a chat response from your selected model. Repeat the check for each checkpoint that you plan to benchmark.

Next, you'll benchmark the models with `vllm bench serve`.
