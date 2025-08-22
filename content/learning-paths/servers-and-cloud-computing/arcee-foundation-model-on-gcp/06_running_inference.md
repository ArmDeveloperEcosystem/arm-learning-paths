---
title: Run inference with AFM-4.5B using Llama.cpp
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you have the [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) models in GGUF format, you can run inference on Google Cloud Axion Arm64 using various Llama.cpp tools. In this step, you’ll generate text, benchmark performance, and interact with the model through both command-line and HTTP APIs.

## Use llama-cli for interactive inference

The `llama-cli` tool provides an interactive command-line interface for text generation. This is useful for quick testing and exploring model behavior.

The `llama-cli` tool provides an interactive command-line interface for text generation. This is ideal for quick testing and hands-on exploration of the model's behavior.

## Basic usage

```bash
bin/llama-cli -m models/afm-4-5b/afm-4-5B-Q8_0.gguf -n 256 --color
```

This starts an interactive session:

- `-m`: specifies the model file to load  
- `-n 256`: sets the maximum tokens per response  
- `--color`: enables colored terminal output  
- You’ll be prompted to enter text, and the model generates a response  

By default, `llama-cli` uses 16 vCPUs. You can change this with `-t <number>`.

### Example interactive session

Once you start the interactive session, you can have conversations like this:

```console
> Give me a brief explanation of the attention mechanism in transformer models.
In transformer models, the attention mechanism allows the model to focus on specific parts of the input sequence when computing the output. Here's a simplified explanation:

1. **Key-Query-Value (K-Q-V) computation**: For each input element, the model computes three vectors:
   - **Key (K)**: This represents the input element in a way that's useful for computing attention weights.
   - **Query (Q)**: This represents the current input element being processed and is used to compute attention weights.
   - **Value (V)**: This represents the input element in its original form, which is used to compute the output based on attention weights.

2. **Attention scores computation**: The attention mechanism computes the similarity between the Query (Q) and each Key (K) element using dot product and softmax normalization. This produces a set of attention scores, which represent how relevant each Key (K) element is to the Query (Q).

3. **Weighted sum**: The attention scores are used to compute a weighted sum of the Value (V) elements. The output is a weighted sum of the Values (V) based on the attention scores.

4. **Output**: The final output is a vector that represents the context of the input sequence, taking into account the attention scores. This output is used in the decoder to generate the next word in the output sequence.

The attention mechanism allows transformer models to selectively focus on specific parts of the input sequence, enabling them to better understand context and relationships between input elements. This is particularly useful for tasks like machine translation, where the model needs to capture long-range dependencies between input words.
```

To exit the session, type `Ctrl+C` or `/bye`.

You'll then see performance metrics like this:

```bash
llama_perf_sampler_print:    sampling time =       9.47 ms /   119 runs   (    0.08 ms per token, 12569.98 tokens per second)
llama_perf_context_print:        load time =     616.69 ms
llama_perf_context_print: prompt eval time =     344.39 ms /    23 tokens (   14.97 ms per token,    66.79 tokens per second)
llama_perf_context_print:        eval time =    9289.81 ms /   352 runs   (   26.39 ms per token,    37.89 tokens per second)
llama_perf_context_print:       total time =   17446.13 ms /   375 tokens
llama_perf_context_print:    graphs reused =          0
```

Here, the 8-bit model on 16 threads produced ~37 tokens per second.

## Run a one-time prompt with llama-cli

You can run `llama-cli` in non-interactive mode:

```bash
bin/llama-cli -m models/afm-4-5b/afm-4-5B-Q4_0.gguf -n 256 --color -no-cnv -p "Give me a brief explanation of the attention mechanism in transformer models."
```

This command:

- Loads the 4-bit model  
- Disables conversation mode with `-no-cnv`  
- Sends a one-time prompt with `-p`  
- Prints the response and exits  

On Axion, the 4-bit model generates ~60 tokens per second, showing the speed benefit of aggressive quantization.

## Use llama-server for API-based inference

The `llama-server` tool runs the model as a web server with an OpenAI-compatible API. This allows integration with applications or batch jobs via HTTP requests.

### Start llama-server

```bash
bin/llama-server -m models/afm-4-5b/afm-4-5B-Q4_0.gguf \
  --host 0.0.0.0 \
  --port 8080 \
  --ctx-size 4096
```

This starts a local server that:
- Loads the specified model
- Listens on all network interfaces (`0.0.0.0`)
- Accepts connections on port 8080
- Supports a 4096-token context window

### Send an API request

Once the server is running, you can make requests using curl, or any HTTP client. 

Open a new terminal on the Google Cloud instance, and run:

```bash
curl -X POST http://localhost:8080/v1/chat/completions   -H "Content-Type: application/json"   -d '{
    "model": "afm-4-5b",
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing in less than 100 words."
      }
    ],
    "max_tokens": 256,
    "temperature": 0.9
  }'
```

The response includes the model’s reply and performance metrics:

```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Quantum computing uses quantum-mechanical phenomena like superposition and entanglement to solve complex problems much faster than classical computers. Instead of binary bits (0 or 1), quantum bits (qubits) can exist in multiple states simultaneously, allowing for parallel processing of vast combinations of possibilities. This enables quantum computers to perform certain calculations exponentially faster, particularly in areas like cryptography, optimization, and drug discovery. However, quantum systems are fragile and prone to errors, requiring advanced error correction techniques. Current quantum computers are still in early stages but show promise for transformative applications."
      }
    }
  ],
  "created": 1753876147,
  "model": "afm-4-5b",
  "system_fingerprint": "b6030-1e15bfd4",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 115,
    "prompt_tokens": 20,
    "total_tokens": 135
  },
  "id": "chatcmpl-0Zwzu03zbu77MFx4ogBsqz8E4IdxHOLU",
  "timings": {
    "prompt_n": 20,
    "prompt_ms": 68.37,
    "prompt_per_token_ms": 3.4185000000000003,
    "prompt_per_second": 292.525961679099,
    "predicted_n": 115,
    "predicted_ms": 1884.943,
    "predicted_per_token_ms": 16.390808695652172,
    "predicted_per_second": 61.00980241842857
  }
}
```

## What's next?

You’ve now successfully:

- Run [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) in interactive and one-shot modes  
- Compared performance with different quantized models on Axion  
- Served the model as an OpenAI-compatible API endpoint  

You can also use the [OpenAI Python client](https://github.com/openai/openai-python) to send requests programmatically, enabling features like streaming responses.
