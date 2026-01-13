---
title: Serve high throughput inference with vLLM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Batch Sizing in vLLM

vLLM uses dynamic continuous batching to maximize hardware utilization. Two key parameters govern this process:
  * `max_model_len`, which is the maximum sequence length (number of tokens per request).
No single prompt or generated sequence can exceed this limit.
  * `max_num_batched_tokens`, which is the total number of tokens processed in one batch across all requests.
The sum of input and output tokens from all concurrent requests must stay within this limit.

Together, these parameters determine how much memory the model can use and how effectively CPU threads are saturated.
On Arm-based servers, tuning them helps achieve stable throughput while avoiding excessive paging or cache thrashing.

## Serve an OpenAI‑compatible API

Start vLLM's OpenAI-compatible API server using the quantized INT4 model and environment variables optimized for performance:

```bash
export VLLM_TARGET_DEVICE=cpu
export VLLM_CPU_KVCACHE_SPACE=32
export VLLM_CPU_OMP_THREADS_BIND="0-$(($(nproc)-1))"
export VLLM_MLA_DISABLE=1 
export ONEDNN_DEFAULT_FPMATH_MODE=BF16
export OMP_NUM_THREADS="$(nproc)"
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4

vllm serve DeepSeek-V2-Lite-w4a8dyn-mse-channelwise \
  --dtype float32 --max-model-len 4096 --max-num-batched-tokens 4096
```

The server now exposes the standard OpenAI-compatible /v1/chat/completions endpoint.

You can test it using any OpenAI-style client library to measure tokens-per-second throughput and response latency on your Arm-based server.

## Run multi‑request batch
After verifying a single request in the previous section, simulate concurrent load against the OpenAI-compatible server to exercise vLLM's continuous batching scheduler.

About the client:
Uses AsyncOpenAI with base_url="http://localhost:8000/v1" to target the vLLM server.
A semaphore caps concurrency to 8 simultaneous requests (adjust CONCURRENCY to scale load).
max_tokens limits generated tokens per request—this directly affects batch size and KV cache use.

Save the code below in a file named `batch_test.py`:

```python
import asyncio
import time
from openai import AsyncOpenAI

# vLLM's OpenAI-compatible server
client = AsyncOpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

model = "DeepSeek-V2-Lite-w4a8dyn-mse-channelwise"   # vllm server model

# Batch of 8 prompts
messages_list = [
    [{"role": "user", "content": "Explain Big O notation with two examples."}],
    [{"role": "user", "content": "Show a simple recursive function and explain how it works."}],
    [{"role": "user", "content": "Draft a polite email requesting a project deadline extension."}],
    [{"role": "user", "content": "Explain what a hash function is and common uses."}],
    [{"role": "user", "content": "Explain binary search and its time complexity."}],
    [{"role": "user", "content": "Write a Python function that checks if a string is a palindrome."}],
    [{"role": "user", "content": "Explain how caching improves performance with a simple analogy."}],
    [{"role": "user", "content": "Explain the difference between supervised and unsupervised learning."}],
]

CONCURRENCY = 8

async def run_one(i: int, messages):
    resp = await client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=128,  # Change as per comfiguration
    )
    return i, resp.choices[0].message.content

async def main():
    t0 = time.time()
    sem = asyncio.Semaphore(CONCURRENCY)

    async def guarded_run(i, msgs):
        async with sem:
            try:
                return await run_one(i, msgs)
            except Exception as e:
                return i, f"[ERROR] {type(e).__name__}: {e}"

    tasks = [asyncio.create_task(guarded_run(i, msgs)) for i, msgs in enumerate(messages_list, start=1)]
    results = await asyncio.gather(*tasks)  # order corresponds to tasks list

    # Print outputs in input order
    results.sort(key=lambda x: x[0])
    for idx, out in results:
        print(f"\n=== Output {idx} ===\n{out}\n")

    print(f"Batch completed in : {time.time() - t0:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())
```

Run 8 concurrent requests:

```bash
python3 batch_test.py
```

This validates multi‑request behavior and shows aggregate throughput in the server logs.

```output
(APIServer pid=4474) INFO 11-10 01:00:56 [loggers.py:221] Engine 000: Avg prompt throughput: 19.7 tokens/s, Avg generation throughput: 187.2 tokens/s, Running: 8 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.6%, Prefix cache hit rate: 0.0%
(APIServer pid=4474) INFO:     127.0.0.1:44060 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO:     127.0.0.1:44134 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO:     127.0.0.1:44076 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO:     127.0.0.1:44068 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO:     127.0.0.1:44100 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO:     127.0.0.1:44112 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO:     127.0.0.1:44090 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO:     127.0.0.1:44120 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=4474) INFO 11-10 01:01:06 [loggers.py:221] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 57.5 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
```
## Serve a BF16 (non-quantized) model (optional)

For a non-quantized path, vLLM on Arm can run BF16 end-to-end using its oneDNN integration (which routes to Arm-optimized kernels using ACL under aarch64).

```bash
vllm serve deepseek-ai/DeepSeek-V2-Lite \
  --dtype bfloat16 --max-model-len 4096  \
  --max-num-batched-tokens 4096
```
Use this BF16 setup to establish a quality reference baseline, then compare throughput and latency against your INT4 deployment to quantify the performance/accuracy trade-offs on your Arm system.

## Try different models
Explore other Hugging Face models that work well with vLLM:

- Meta Llama 2 and Llama 3: these versatile models work well for general tasks, and you can try them to compare BF16 and INT4 performance
- Qwen and Qwen-Chat: these models support multiple languages and are tuned for instructions, giving you high-quality results
- Gemma (Google): this compact and efficient model is a good choice for edge devices or deployments where cost matters

You can quantize and serve any of these models using the same `quantize_vllm_models.py` script. Just update the model name in the script.

You can also try connecting a chat client by linking your server with OpenAI-compatible user interfaces such as [Open WebUI](https://github.com/open-webui/open-webui).
