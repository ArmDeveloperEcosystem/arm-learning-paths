---
title: Export the Vulkan PTE
description: Export a Vulkan-enabled ExecuTorch program for Llama 3.2 1B Instruct with the guide's measured settings.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure export variables

From the ExecuTorch checkout:

```bash
cd $HOME/executorch

export MODEL_DIR="$HOME/Llama-3.2-1B-Instruct/original"
export QUANT="8da4w"
export GROUP_SIZE="64"
export CONTEXT_LENGTH="2048"
```

## Export Llama 3.2 with Vulkan enabled

Run the export command used for the successful device run:

```bash
python -m examples.models.llama.export_llama \
  -c "$MODEL_DIR/consolidated.00.pth" \
  -p "$MODEL_DIR/params.json" \
  -d fp32 \
  --vulkan \
  -qmode "$QUANT" \
  -G "$GROUP_SIZE" \
  --max_seq_length "$CONTEXT_LENGTH" \
  --max_context_length "$CONTEXT_LENGTH" \
  -kv \
  --use_sdpa_with_kv_cache \
  --metadata '{"append_eos_to_prompt": 0, "get_bos_id":128000, "get_eos_ids":[128009, 128001]}' \
  --model "llama3_2" \
  --output_name "$MODEL_DIR/Llama3.2-1B-Instruct_vulkan_8da4w_g64_c2048.pte"
```

The expected output is:

```output
Llama3.2-1B-Instruct_vulkan_8da4w_g64_c2048.pte
```

The exported file was about `1.8 GB`.

## Understand the export choices

These options matter for reproducing the measured run:

- `8da4w` uses dynamic 8-bit activations and 4-bit weights on the relevant quantized paths.
- `-G 64` sets the weight group size to `64`.
- `-kv` and `--use_sdpa_with_kv_cache` enable the KV cache path used during generation.
- `--max_seq_length` and `--max_context_length` were both set to `2048`.
- The metadata sets the BOS and EOS handling expected by the instruct model.

If you change the quantization mode, group size, or context length, expect file size, memory usage, and throughput to change.

## What you've accomplished and what's next

The Vulkan-enabled PTE is exported. Next, build the Android Vulkan runtime.
