---
title: Run inference with AFM-4.5B
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you have the AFM-4.5B models in GGUF format, you can run inference using various Llama.cpp tools. In this step, you'll explore how to generate text, benchmark performance, and interact with the model through both command-line and HTTP APIs.


## Use llama-cli for interactive text generation

The `llama-cli` tool provides an interactive command-line interface for text generation. This is ideal for quick testing and hands-on exploration of the model's behavior.

## Basic usage

```bash
bin/llama-cli -m models/afm-4-5b/afm-4-5B-Q8_0.gguf -n 256 --color
```

This command starts an interactive session:

- `-m` (model file path) specifies the model file to load
- `-n 256` sets the maximum number of tokens to generate per response
- `--color` enables colored terminal output
- The tool will prompt you to enter text, and the model will generate a response

In this example, `llama-cli` uses 16 vCPUs. You can try different values with `-t <number>`.

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
llama_perf_sampler_print:    sampling time =      26.66 ms /   356 runs   (    0.07 ms per token, 13352.84 tokens per second)
llama_perf_context_print:        load time =     782.72 ms
llama_perf_context_print: prompt eval time =     392.40 ms /    24 tokens (   16.35 ms per token,    61.16 tokens per second)
llama_perf_context_print:        eval time =   13173.66 ms /   331 runs   (   39.80 ms per token,    25.13 tokens per second)
llama_perf_context_print:       total time =  129945.08 ms /   355 tokens
```

In this example, the 8-bit model running on 16 threads generated 355 tokens, at ~25 tokens per second (`eval time`).

## Run a non-interactive prompt

You can also use `llama-cli` in one-shot mode with a prompt:

```bash
bin/llama-cli -m models/afm-4-5b/afm-4-5B-Q4_0.gguf -n 256 --color -no-cnv -p "Give me a brief explanation of the attention mechanism in transformer models."
```
This command:
- Loads the 4-bit model
- Disables conversation mode using  `-no-cnv`
- Sends a one-time prompt using `-p`
- Prints the generated response and exits

The 4-bit model delivers faster generation—expect around 40 tokens per second on Graviton4. This shows how a more aggressive quantization recipe helps deliver faster performance.

## Use llama-server for API access

The `llama-server` tool runs the model as a web server compatible with the OpenAI API format, allowing you to make HTTP requests for text generation. This is useful for integrating the model into applications or for batch processing.

## Start the server

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

### Make an API request

Once the server is running, you can make requests using curl, or any HTTP client. 

Open a new terminal on the AWS instance, and run:

```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
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
        "content": "Quantum computing uses quantum-mechanical phenomena, such as superposition and entanglement, to perform calculations. It allows for multiple possibilities to exist simultaneously, which can speed up certain processes. Unlike classical computers, quantum computers can solve complex problems and simulate systems more efficiently. Quantum bits (qubits) store information, and quantum gates perform operations. Quantum computing has potential applications in fields like cryptography, optimization, and materials science. Its development is an active area of research, with companies like IBM, Google, and Microsoft investing in quantum computing technology."
      }
    }
  ],
  "created": 1750929895,
  "model": "afm-4-5b",
  "system_fingerprint": "b5757-716301d1",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 111,
    "prompt_tokens": 20,
    "total_tokens": 131
  },
  "id": "chatcmpl-tb93ww9iYCErwLJmsV0YLrIadVvpBk4m",
  "timings": {
    "prompt_n": 11,
    "prompt_ms": 105.651,
    "prompt_per_token_ms": 9.604636363636363,
    "prompt_per_second": 104.11638318615064,
    "predicted_n": 111,
    "predicted_ms": 2725.982,
    "predicted_per_token_ms": 24.558396396396397,
    "predicted_per_second": 40.719271073690145
  }
}
```

## What's next?

You’ve now successfully:

- Run AFM-4.5B in interactive and non-interactive modes
- Tested performance with different quantized models
- Served the model as an OpenAI-compatible API endpoint

You can also interact with the server using Python with the [OpenAI client library](https://github.com/openai/openai-python), enabling streaming responses, and other features.
