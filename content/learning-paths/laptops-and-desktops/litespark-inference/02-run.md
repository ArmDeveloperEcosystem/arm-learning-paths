---
title: Run BitNet-2B with Litespark-Inference
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

With Litespark-Inference installed, you can start generating text.

## Run inference from the command line

You can generate text directly from your terminal using the `litespark-inference generate` command. Use BF16 embeddings as the reference case and limit the response to 64 new tokens:

```bash
litespark-inference generate "Why is BitNet fast on CPU?" --embed-dtype bf16 --max-tokens 64
```

The output is similar to:

```output
[litespark-inference] torchless runtime (model=bitnet-2b).
Loading tokenizer...
  17.03s
Prompt (40 tokens): 'System: You are Litespark, a helpful AI assistant running locally. Provide accurate, concise, and practical answers.<|eot_id|>User: Why is BitNet fast on CPU?<|eot_id|>Assistant: '
Prefill...
  40 tokens in 0.50s (79.53 tok/s)
Generate:
BitNet is fast on CPU because it uses a unique architecture that allows for efficient
data processing and communication...

Generated 64 tokens in 3.46s (18.51 tok/s)
```

The exact answer and timing vary by system. The key indicators are that prefill and generation both complete successfully with reported throughput.

When executed, Litespark-Inference:

1. Downloads and loads the `microsoft/bitnet-b1.58-2B-4T-bf16` model from Hugging Face on first run (around 4.5 GB).
2. Tokenizes the input prompt and processes it in a single batched prefill call.
3. Decodes up to 64 new tokens sequentially, streaming each token directly to your terminal.

You can also inspect system hardware detection or launch an interactive session using additional CLI commands:

```bash
# List available models and architecture
litespark-inference info

# Start an interactive multi-turn chat session with KV cache reuse
litespark-inference chat
```

The `litespark-inference info` output is similar to:

```output
Litespark-Inference v1.0.3
==================================================

Architecture: aarch64
Platform: Unknown

Available Models:
  bitnet-2b: BitNet b1.58 2B parameters, 4T tokens trained (~556 MB)
  falcon-edge-1b: Falcon Edge 1B base model
  falcon-edge-1b-instruct: Falcon Edge 1B instruct model
  falcon-edge-3b: Falcon Edge 3B base model
  falcon-edge-3b-instruct: Falcon Edge 3B instruct model
```

For lower-level details about the compiled kernel, OpenMP threading, and CPU feature detection, use the module-level info command:

```bash
python -m litespark_inference.torchless info
```

The output is similar to:

```output
litespark_inference.torchless
  platform : Linux aarch64
  python   : 3.12.3
  kernel   : /home/ubuntu/.venv/lib/python3.12/site-packages/litespark_inference/torchless/_matmul_lut_neon.cpython-312-aarch64-linux-gnu.so
  OpenMP   : True  (max_threads=64)
  Accelerate: False
```

Confirm that the kernel name contains `neon` on Arm and that `OpenMP` is `True`.

## Run inference from Python

The [Litespark-Inference install guide](/install-guides/litespark-inference/) creates a Python virtual environment named `.venv` and installs Litespark-Inference in it. If you opened a new terminal after completing the install guide, return to the directory that contains `.venv` and activate the virtual environment again:

```bash
source .venv/bin/activate
```

To integrate Litespark-Inference into a Python application, use the high-level `BitNet` API to load the model and generate responses. Copy the following code into a text file named `run_bitnet.py`:

```python
from litespark_inference.torchless import BitNet

# Auto-downloads from Hugging Face on first use.
# Use BF16 embeddings as the reference case for the later comparison.
bn = BitNet.from_pretrained("bitnet-2b", embed_dtype="bf16")

memory = bn.memory_bytes()
mb = 1024 * 1024
print(f"Embedding tensor storage: {memory['embedding'] / mb:.1f} MB")
print(f"Total model tensor storage: {memory['total_incl_embedding'] / mb:.1f} MB")

# chat=True applies the system + chat template and returns a clean
# instruction-following answer (omit it for a raw continuation).
print(bn.generate("Why is BitNet fast on CPU?", max_new_tokens=64, chat=True))
```

Run the Python file from the activated virtual environment:

```bash
python run_bitnet.py
```

The output is similar to:

```output
Embedding tensor storage: 626.2 MB
Total model tensor storage: 1126.6 MB
BitNet is fast on CPU because it uses a unique architecture that allows for efficient
data processing and communication...
```

The `BitNet` class handles model loading, KV cache management, and autoregressive token generation without needing PyTorch at inference. The program first prints the memory used to store the embedding and all model tensors, followed by the generated answer. With BF16 embeddings, the embedding tensor storage is approximately 626 MB.

The values returned by `memory_bytes()` account for model tensor storage. They do not include Python, native-library, or KV-cache overhead, so they differ from the resident-memory values in the following table.

## Configure token embedding dtypes

BitNet b1.58 model weights are stored in 2-bit packed format. You can configure the token-embedding table's data type to optimize memory usage versus output quality.

The following resident-memory values are illustrative. Actual usage varies with the operating system, package version, runtime configuration, and workload. The optional benchmarking section shows you how to measure resident memory on your system.

| Embed Dtype | Illustrative Resident Memory | Quality | Recommendation |
|---|---|---|---|
| BF16 | ~813 MB | Reference | Use for high-accuracy workloads |
| INT8 | ~656 MB | Reduced embedding precision | Balance memory use and output quality; validate your workload |
| INT4 | ~573 MB | Lowest embedding precision | Default; smallest memory footprint; validate your workload |

Set the embedding dtype from the CLI:

```bash
litespark-inference generate "Why is BitNet fast on CPU?" --embed-dtype int4 --max-tokens 64
```

To set the embedding dtype in Python, replace the contents of `run_bitnet.py` with the following code:

```python
from litespark_inference.torchless import BitNet

bn = BitNet.from_pretrained("bitnet-2b", embed_dtype="int4")

memory = bn.memory_bytes()
mb = 1024 * 1024
print(f"Embedding tensor storage: {memory['embedding'] / mb:.1f} MB")
print(f"Total model tensor storage: {memory['total_incl_embedding'] / mb:.1f} MB")

print(bn.generate("Why is BitNet fast on CPU?", max_new_tokens=64, chat=True))
```

Compared with the earlier Python example, the `embed_dtype="int4"` argument is the only configuration change. It stores the token-embedding table as INT4 instead of the explicitly selected BF16 format. The main BitNet model weights remain in their 2-bit packed format.

Run the updated Python file from the activated virtual environment:

```bash
python run_bitnet.py
```

The output is similar to:

```output
Embedding tensor storage: 157.1 MB
Total model tensor storage: 657.4 MB
BitNet is fast on CPU because it uses a combination of hardware and software
optimizations...
```

The program prints approximately 157 MB of embedding tensor storage for INT4, compared with approximately 626 MB for BF16. It then answers the same prompt as before, although the exact answer can vary. The illustrative resident-memory figures are around 573 MB for INT4 and 813 MB for BF16. Measure resident memory on your system and validate the generated output for your workload.

## What you've accomplished

In this section, you:

- Generated text using BitNet-2B from the command line.
- Integrated `litespark-inference` into Python using the `BitNet` API.
- Configured BF16 and INT4 embeddings and compared their memory and quality trade-offs with INT8.

Next, continue to the benchmarking section to compare performance against a PyTorch baseline.
