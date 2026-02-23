---
title: Test your fine-tuned model with vLLM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you've fine-tuned your model on Raspberry Pi datasheet content, it's time to compare its behavior against the original. You'll serve both versions using vLLM, a high-performance inference server optimized for large language models, and observe how fine-tuning on domain-specific data changes the model's factual accuracy.

## Download vLLM container

NVIDIA provides a pre-built vLLM container that includes all the necessary components for efficient model serving. This container is optimized for NVIDIA GPUs and includes support for various quantization methods and multi-GPU inference.

Pull the vLLM container from NVIDIA's registry:

```bash
docker pull nvcr.io/nvidia/vllm:26.01-py3
```

The January 2026 release includes the latest optimizations for model serving and inference acceleration.

## Launch container instance

Launch a vLLM container instance that allows you to serve models through an OpenAI-compatible API. This setup makes it easy to test your models using standard HTTP requests.

Start the container with port forwarding enabled:

```bash
docker run --gpus all -it --rm --ipc=host \
-v $HOME/.cache/huggingface:/root/.cache/huggingface \
-v ${PWD}:/workspace -w /workspace \
-p 8000:8000 nvcr.io/nvidia/vllm:26.01-py3
```

The flags are similar to the PyTorch container launch, with one addition:

- `-p 8000:8000` maps port 8000 from the container to your host system, so you can send HTTP requests to the model server from outside the container

## Test the original model

Before testing your fine-tuned model, first observe how the original, unmodified Llama model responds to a Raspberry Pi hardware question. This establishes a baseline that reveals where the base model's knowledge falls short.

### Launch vLLM

Start the vLLM server with the original Llama 3.1 8B model:

```bash
python3 -m vllm.entrypoints.openai.api_server \
--model "meta-llama/Llama-3.1-8B" --trust-remote-code \
--tensor-parallel-size 1 --quantization fp8 \
--gpu-memory-utilization 0.80
```

The server exposes an OpenAI-compatible API with the following configuration:

- `--model` specifies the Hugging Face model to load, which will be pulled from the Hugging Face cache we made available to this container
- `--trust-remote-code` allows loading models with custom code (required for some architectures)
- `--tensor-parallel-size 1` runs inference on a single GPU (like on a DGX Spark)
- `--quantization fp8` uses 8-bit floating point quantization to reduce memory usage and improve throughput
- `--gpu-memory-utilization 0.80` limits memory usage to 80%, leaving room for the rest of the OS because the DGX Spark implements unified memory between CPU and GPU.

Wait for the server to fully load the model and display the message indicating it's ready to accept requests (this typically takes 30-60 seconds).

### Test prompt


From a new terminal window (outside the container), send a Raspberry Pi hardware question to the model using the Alpaca instruction format. For this example, use a question about the memory size:

```bash
curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
  "prompt": "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nHow much memory does the RP2350 have?\n\n### Response:",
  "max_tokens": 200
}'
```

The `max_tokens` parameter limits the response length to prevent runaway generation.

### Output

The original model hallucinates an incorrect specification. The output is similar to:

```json
{
  "id": "cmpl-91e070e2a34aaf01",
  "object": "text_completion",
  "created": 1770998840,
  "model": "meta-llama/Llama-3.1-8B",
  "choices": [
    {
      "index": 0,
      "text": " \nThe RP2350 has 256MB of memory.",
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 35,
    "total_tokens": 48,
    "completion_tokens": 13
  }
}
```

The base model confidently reports the RP2350 has "256MB of memory," which is off by three orders of magnitude. The actual specification from the datasheet is 520 KB of SRAM. The model doesn't have Raspberry Pi datasheet content in its training data, so it fabricates a plausible-sounding but completely incorrect answer.

## Test the fine-tuned model

Now test your fine-tuned model to see how training on Raspberry Pi datasheet content improved its factual accuracy. Stop the current vLLM server (press Ctrl+C in the container terminal) before launching the fine-tuned model.

{{% notice Dependency Conflict %}}
As of this writing, vLLM does not support version 5 of the `transformers` library that was used when fine-tuning the model, so you need to patch its `tokenizer_config.json`. Run the following command to update the `tokenizer_class` to `PreTrainedTokenizerFast`, which is compatible with the older `transformers` version bundled in the vLLM container:

```bash
sed -i 's/"tokenizer_class": "TokenizersBackend"/"tokenizer_class": "PreTrainedTokenizerFast"/' /workspace/models/Llama-3.1-8B-FineTuned/tokenizer_config.json
```
{{% /notice %}}

### Launch vLLM

Start the vLLM server with your fine-tuned model:

```bash
python3 -m vllm.entrypoints.openai.api_server \
--model "/workspace/models/Llama-3.1-8B-FineTuned" --trust-remote-code \
--tensor-parallel-size 1 --quantization fp8 \
--gpu-memory-utilization 0.80
```

The only change from the previous command is the `--model` parameter, which now points to your fine-tuned model directory instead of the Hugging Face model ID.

### Test prompt

Send the same Raspberry Pi question to your fine-tuned model:

```bash
curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
  "prompt": "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nHow much memory does the RP2350 have?\n\n### Response:",
  "max_tokens": 200
}'
```

### Output

The fine-tuned model produces a correct, datasheet-accurate response. The output is similar to:

```json
{
  "id": "cmpl-bad36ff5edddfb74",
  "object": "text_completion",
  "created": 1770999123,
  "model": "/workspace/models/Llama-3.1-8B-FineTuned",
  "choices": [
    {
      "index": 0,
      "text": " The RP2350 has 520 KB of on-chip SRAM.",
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 35,
    "total_tokens": 51,
    "completion_tokens": 16
  }
}
```

The improvement is clear. Where the base model hallucinated "256MB," your fine-tuned model correctly answers "520 KB of on-chip SRAM," matching the official RP2350 datasheet specification. The model:

- Provides a direct, concise answer without generating extra questions
- Stops naturally (`finish_reason: "stop"`) when the answer is complete
- Uses only a handful of tokens instead of rambling

```bash
curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
    "prompt": "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nWhat memory options are available for the Raspberry Pi Compute Module 4?\n\n### Response:",
    "max_tokens": 200
}'
```

The fine-tuned model responds with accurate specifications from the CM4 datasheet, while the base model would likely guess or hallucinate memory options.

Fine-tuning on the Raspberry Pi datasheet dataset transformed the base model from one that confidently fabricates hardware specifications into one that provides accurate, verified answers sourced from real datasheets.

## What you've accomplished and what's next

You've successfully fine-tuned a large language model on domain-specific data using PyTorch and Hugging Face libraries on an NVIDIA DGX Spark system. Throughout this Learning Path, you:

- Set up a containerized environment with all necessary dependencies
- Learned how supervised fine-tuning teaches domain knowledge to a base model
- Patched a fine-tuning script to load a custom Raspberry Pi datasheet dataset
- Ran full fine-tuning to train the model on hardware specifications
- Compared base and fine-tuned model responses to verify factual accuracy improvements

The approach you used can be applied to any domain where you need accurate, grounded responses. Consider experimenting with different datasets from your own technical documentation, product specifications, or internal knowledge bases.