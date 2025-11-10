---
title: Serve high throughput inference with vLLM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## About batch sizing in vLLM

vLLM enforces two limits to balance memory use and throughput: a per‑sequence length (`max_model_len`) and a per‑batch token limit (`max_num_batched_tokens`). No single request can exceed the sequence limit, and the sum of tokens in a batch must stay within the batch limit.

## Serve an OpenAI‑compatible API

Start the server with sensible CPU default parameters and a quantized model:

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

## Run multi‑request batch

After confirming a single request works explained in previous example, simulate concurrent load with a small OpenAI API compatible client. Save this as `batch_test.py`:

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

Run 8 concurrent requests against your server:

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
## Optional: Serving BF16 non-quantized model

For a BF16 path on Arm, vLLM is acclerated by direct oneDNN integration in vLLM which allows aarch64 model to be hyperoptimized.

```bash
vllm serve deepseek-ai/DeepSeek-V2-Lite \
  --dtype bfloat16 --max-model-len 4096  \
  --max-num-batched-tokens 4096
```

## Go Beyond: Power Up Your vLLM Workflow
Now that you’ve successfully quantized and served a model using vLLM on Arm, here are some further ways to explore:

* **Try different models:** Apply the same steps to other [Hugging Face models](https://huggingface.co/models) like Llama, Qwen or Gemma.

* **Connect a chat client:**  Link your server with OpenAI-compatible UIs like [Open WebUI](https://github.com/open-webui/open-webui)