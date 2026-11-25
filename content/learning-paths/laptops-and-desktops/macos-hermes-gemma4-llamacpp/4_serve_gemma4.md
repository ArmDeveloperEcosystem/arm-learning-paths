---
title: Serve Gemma 4 E4B with a 64K context window
description: Launch llama-server on macOS with Metal GPU offloading, a 64K context window, Flash Attention, and a quantized KV cache, then validate the OpenAI-compatible API.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure llama-server for Hermes Agent

Hermes Agent communicates with local models over an OpenAI-compatible HTTP API (`/v1/chat/completions`) and needs a minimum 64K context window (`-c 65536`) to hold tool definitions, workspace context, and multi-turn tool-call traces.

Start `llama-server` from `~/hermes-gemma4/llama.cpp` with `gemma-4-E4B-it-Q4_0.gguf`, offloading all layers to the Metal GPU (`-ngl 99`) and setting CPU threads to your performance cores (`hw.perflevel0.physicalcpu`):

```bash
P_CORES=$(sysctl -n hw.perflevel0.physicalcpu)

./build/bin/llama-server \
  -m ./models/gemma-4-E4B-it-Q4_0.gguf \
  --host 127.0.0.1 \
  --port 8080 \
  -ngl 99 \
  -c 65536 \
  -t "$P_CORES" \
  -np 1 \
  --jinja \
  -fa on \
  --cache-type-k q8_0 \
  --cache-type-v q8_0
```

The output is similar to:

```output
0.00.044.506 I srv  llama_server: initializing ...
0.00.044.512 I cmn  common_param: common_params_print_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
0.00.046.485 W srv  server_setup: security: no API key is set and CORS allows all origins (see https://github.com/ggml-org/llama.cpp/pull/25655)
0.00.048.324 I srv    load_model: loading model './models/gemma-4-E4B-it-Q4_0.gguf'
...
0.02.119.154 I cmn          init: llama threadpool init, n_threads = 8
0.03.066.801 I srv    load_model: initializing, n_slots = 1, n_ctx_slot = 65536, kv_unified = 'false'
0.03.072.765 I srv  server_run_i: model loaded
0.03.072.851 I srv  server_on_li: listening on http://127.0.0.1:8080
```

{{% notice Tip %}}
Setting `-t` to `hw.perflevel0.physicalcpu` keeps CPU helper and fallback tasks on your Mac's performance cores and prevents slower efficiency cores from delaying synchronization.
{{% /notice %}}

### Server flag reference

Each flag tunes `llama-server` for single-user autonomous agent reliability on Apple silicon:

| Flag | Purpose |
|---|---|
| `--host 127.0.0.1 --port 8080` | Binds the OpenAI-compatible server locally on port 8080 |
| `-ngl 99` | Offloads all transformer layers to the Metal GPU over unified memory |
| `-c 65536` | Allocates a 64K token context window, meeting Hermes Agent's minimum context requirement |
| `-t "$P_CORES"` | Sets CPU threadpool count to your performance cores rather than including efficiency cores |
| `-np 1` | Reserves the full 64K context for one parallel slot rather than splitting memory across slots |
| `--jinja` | Enables Jinja chat template rendering needed for Gemma 4 E4B structured tool calling |
| `-fa on` | Enables Metal Flash Attention to cut KV memory overhead and boost prefill and decode speed |
| `--cache-type-k q8_0 --cache-type-v q8_0` | Quantizes the 64K K and V caches to 8-bit so weights and context fit in 16 GB or more of unified memory |

## Validate the OpenAI-compatible endpoint

Leave `llama-server` running in its terminal, then open a second terminal to verify the API.

Check the `/v1/models` endpoint:

```bash
curl -s http://127.0.0.1:8080/v1/models | python3 -m json.tool
```

The output is similar to:

```output
{
    "models": [
        {
            "name": "./models/gemma-4-E4B-it-Q4_0.gguf",
            "model": "./models/gemma-4-E4B-it-Q4_0.gguf",
            ...
        }
    ],
    "object": "list",
    "data": [
        {
            "id": "./models/gemma-4-E4B-it-Q4_0.gguf",
            "aliases": [
                "./models/gemma-4-E4B-it-Q4_0.gguf"
            ],
            "tags": [],
            "object": "model",
            ...
            "owned_by": "llamacpp",
            "meta": {
                "vocab_type": 2,
                "n_vocab": 262144,
                "n_ctx": 65536,
                "n_ctx_train": 131072,
                "n_embd": 2560,
                "n_params": 7463013674,
                "size": 4574983336,
                "ftype": "Q4_0"
            }
        }
    ]
}
```

Send a quick `/v1/chat/completions` JavaScript Object Notation (JSON) request to confirm Metal inference works end-to-end:

```bash
curl -s http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "./models/gemma-4-E4B-it-Q4_0.gguf",
    "messages": [
      {"role": "user", "content": "What is 2 + 2? Reply with the number only."}
    ],
    "max_tokens": 256
  }' | python3 -m json.tool
```

The output is similar to:

```output
{
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "4",
                "reasoning_content": "The user wants to know the sum of 2 + 2.\nThe instruction is to reply with the number only.\n2 + 2 = 4."
            }
        }
    ],
    "created": 1795557632,
    "model": "./models/gemma-4-E4B-it-Q4_0.gguf",
    "system_fingerprint": "b1-33aeb17",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 40,
        "prompt_tokens": 30,
        "total_tokens": 70,
        "prompt_tokens_details": {
            "cached_tokens": 0
        }
    },
    "id": "chatcmpl-ZenSfwSXtCjygy6pBBsRBjTfGcC3KrEk",
    "timings": {
        "cache_n": 0,
        "prompt_n": 30,
        "prompt_ms": 177.846,
        "prompt_per_token_ms": 5.9282,
        "prompt_per_second": 168.6852670287777,
        "predicted_n": 40,
        "predicted_ms": 707.27,
        "predicted_per_token_ms": 18.135128205128204,
        "predicted_per_second": 55.14160080308793
    }
}
```

Confirm that the JSON response contains a valid `choices[0].message.content` reply and `usage` token counts. Note the exact `id` reported by `/v1/models` so you can configure Hermes Agent in the next step.

## What you've accomplished and what's next

You've launched `llama-server` with full Metal GPU offloading, a 64K context window, Flash Attention, and an 8-bit KV cache, and verified its local OpenAI-compatible API.

Next, you'll install Nous Research Hermes Agent and configure it to use your local `llama-server` endpoint.
