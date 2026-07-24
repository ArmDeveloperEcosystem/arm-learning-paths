---
title: Run BitNet-2B
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

With Litespark-Inference installed (see the
[install guide](/install-guides/litespark-inference/)), you can generate
text right away.

## The CLI (one line)

```bash
litespark-inference generate "Why is BitNet fast on CPU?" --max-tokens 64
```

What this does:

1. Loads `microsoft/bitnet-b1.58-2B-4T-bf16` from the Hugging Face cache
   (downloaded on first run, around 4.5 GB).
2. Tokenizes the prompt and runs it through the model in one batched
   **prefill** call.
3. Greedy-decodes 64 new tokens, streaming each one to your terminal
   as it is produced.

Other useful CLI commands:

```bash
# Quick health-check - what kernel, what threads, what model
litespark-inference info

# Interactive chat (multi-turn, reuses KV cache across turns)
litespark-inference chat
```

## From Python (a few lines)

If you want to embed Litespark-Inference in an application, the
recommended API is the high-level `BitNet` class - load the model, then
call `generate`:

```python
from litespark_inference.torchless import BitNet

# Auto-downloads from Hugging Face on first use.
bn = BitNet.from_pretrained("bitnet-2b")

# chat=True applies the system + chat template and returns a clean
# instruction-following answer (omit it for a raw continuation).
print(bn.generate("Why is BitNet fast on CPU?", max_new_tokens=64, chat=True))
```

That is the whole surface: `from_pretrained` loads the packed model and
owns the KV cache; `generate` runs the batched prefill plus
autoregressive decoding for you. There is no `torch` import at inference.

## Embed dtype: pick your memory / quality trade-off

The weight matrices are always 2-bit packed (that is what BitNet b1.58
means). The one thing you can vary is the token-embedding table's
dtype - and that controls a big chunk of the model's resident memory:

| Embed dtype | Resident memory | Quality | When to use |
|---|---|---|---|
| `bf16` | around 813 MB | Reference | Default for accuracy-sensitive work |
| `int8` | around 656 MB | Indistinguishable from `bf16` in practice | Good balance |
| **`int4`** | **around 573 MB** | Slight quality cost on rare tokens | **Recommended** - fastest load, smallest footprint |

CLI:

```bash
litespark-inference generate "Why is BitNet fast on CPU?" --embed-dtype int4 --max-tokens 64
```

Python:

```python
from litespark_inference.torchless import BitNet

bn = BitNet.from_pretrained("bitnet-2b", embed_dtype="int4")
print(bn.generate("Why is BitNet fast on CPU?", max_new_tokens=64, chat=True))
```

## What's next

If you just wanted to run BitNet on the CPU, you are done - go build
something with it.

If you want to **know how fast it actually is** versus PyTorch on the
same machine (and how much energy it uses), continue to the next chapter
on benchmarking.
