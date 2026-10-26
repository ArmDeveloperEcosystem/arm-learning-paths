---
title: Benchmark MoE serving performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## MoE performance benchmarking

Use `vllm bench serve` to measure throughput and latency while a model serves concurrent requests.

The benchmark sends requests to the vLLM OpenAI-compatible API server at:

```text
/v1/chat/completions
```

Start the model server first using the commands from [Run mixture of experts (MoE) inference with vLLM](/learning-paths/servers-and-cloud-computing/vllm-moe/3-run-inference/), and keep it running in one terminal. Then, run the benchmark command from another terminal.

In the benchmark terminal, change to the directory where you created `vllm_env_new`. Activate that environment and set `MODEL` to match the running server:

```bash
source vllm_env_new/bin/activate
export MODEL=google/gemma-4-26B-A4B-it
```

Download the full ShareGPT dataset into this directory:

```bash
wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
```

The reported results use subsets selected with each model tokenizer for approximately 512 input tokens. Downloading the full dataset doesn't create those subsets. Create the model-specific subsets before running the benchmark commands.

## Create ShareGPT prompt subsets

Create a file named `create_sharegpt_512_subsets.py` with the following code:

```python
import json
from pathlib import Path
from transformers import AutoTokenizer

INPUT = Path("ShareGPT_V3_unfiltered_cleaned_split.json")

MODELS = {
    "gemma4": "google/gemma-4-26B-A4B-it",
    "gptoss": "unsloth/gpt-oss-20b-BF16",
    "qwen": "Qwen/Qwen3-30B-A3B-Thinking-2507",
}

TOKEN_RANGE = (460, 580)
MAX_SAMPLES = 256

data = json.loads(INPUT.read_text())

for model_name, model_id in MODELS.items():
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    rows = []

    for item in data:
        conversations = item.get("conversations") or item.get("conversation")
        if not conversations:
            continue

        first = conversations[0]
        prompt = first.get("value") or first.get("content")
        if not prompt:
            continue

        n_tokens = len(tokenizer.encode(prompt))

        if TOKEN_RANGE[0] <= n_tokens <= TOKEN_RANGE[1] and len(rows) < MAX_SAMPLES:
            rows.append(item)

    out = Path(f"sharegpt_{model_name}_512.json")
    out.write_text(json.dumps(rows, indent=2))
    print(f"{model_name}: {len(rows)} samples -> {out}")
```
Run the script:

```bash
python create_sharegpt_512_subsets.py
```

This creates the subset files that are used by the benchmark commands:

```text
sharegpt_gemma4_512.json
sharegpt_gptoss_512.json
sharegpt_qwen_512.json
```

## Review benchmark setup

The benchmark setup that you'll use includes the following configuration:

```text
Dataset: ShareGPT prompt subsets
Prompt subset: ~512 input tokens
Number of prompts: 128
Requested output length: 512 output tokens
Prefix caching: enabled
Warmup requests: 5
Decoding: greedy decoding with temperature=0, top-p=1, top-k=1
Concurrency values: 4, 8, 16, 32
Benchmark tool: vllm bench serve
```

Greedy decoding is configured with `--top-p 1 --temperature 0 --top-k 1`. This selects the highest-probability next token instead of sampling. It doesn't guarantee identical responses across different builds or precision settings.

When prefix caching is enabled, repeating `vllm bench serve` against the same server can reuse prompts from earlier benchmark runs and inflate throughput. To avoid cache reuse across runs, start a fresh vLLM server for each concurrency value. Warmup requests can still populate the cache within a run. Keep the warmup and cache settings consistent across comparisons.

## Run the benchmark

After the Gemma 4 subset is available in your current directory, run the benchmark:

```bash
export C=4

vllm bench serve \
  --model "$MODEL" \
  --backend openai-chat \
  --dataset-name sharegpt \
  --dataset-path ./sharegpt_gemma4_512.json \
  --num-prompts 128 \
  --max-concurrency "$C" \
  --sharegpt-output-len 512 \
  --top-p 1 \
  --temperature 0 \
  --top-k 1 \
  --percentile-metrics ttft,tpot \
  --metric-percentiles 50,95,99 \
  --endpoint /v1/chat/completions \
  --save-result \
  --result-dir bench_out \
  --result-filename gemma4_bf16_sharegpt_mc${C}.json \
  --num-warmups 5
```

`--max-concurrency` limits simultaneous requests. `--num-prompts` sets the total number of requests, and `--num-warmups` sends warmup requests before measurement. The benchmark prints a summary and saves JSON to `bench_out/gemma4_sharegpt_mc4.json` for this run.

`--sharegpt-output-len 512` requests up to 512 generated tokens. Responses can stop earlier, so inspect actual output token counts when comparing throughput.

Repeat the command with `C=8`, then `C=16`, then `C=32`. Restart the server and wait for it to become ready before each run. Keep the model, dataset, and server settings unchanged while varying concurrency.

For each additional model, update `MODEL` in both terminals. Then, restart the server and replace the dataset and result filename arguments. Use distinct result filenames for each model and precision to avoid overwriting earlier runs:

| Model | Required subset file | Example result filename |
| --- | --- | --- |
| Gemma 4 BF16 | `sharegpt_gemma4_512.json` | `gemma4_bf16_sharegpt_mc${C}.json` |
| GPT-OSS BF16 | `sharegpt_gptoss_512.json` | `gptoss_bf16_sharegpt_mc${C}.json` |
| Qwen3 BF16 | `sharegpt_qwen_512.json` | `qwen3_bf16_sharegpt_mc${C}.json` |
| Qwen3 W8A8 | `sharegpt_qwen_512.json` | `qwen3_w8a8_sharegpt_mc${C}.json` |

Use the same Qwen3 subset for both precisions. Record the following values alongside your results:

- CPU thread binding
- Server arguments
- Package versions
- Any changes to the key-value (KV) cache budget 

## Review metrics

Check that all 128 measured requests completed successfully before interpreting performance. Investigate failed requests in the server logs.

Use the summary and saved JSON to compare the following metrics at the same concurrency:

| Metric | Meaning | Preferred direction |
| --- | --- | --- |
| Request throughput | Completed requests per second | Higher |
| Output token throughput | Generated tokens per second | Higher |
| Total token throughput | Input and output tokens per second | Higher |
| TTFT | Time to first token, reported in milliseconds | Lower |
| TPOT | Time per output token after the first, reported in milliseconds | Lower |

The command reports the 50th, 95th, and 99th percentiles for TTFT and TPOT. Higher percentiles help you assess latency for slower requests.  

Different response lengths change the amount of work performed. You should therefore compare actual input and output token counts as well as throughput.

## What you've accomplished and what's next

After completing a run, you have a serving-performance summary and a saved JSON result for your selected model and workload.

Next, you'll review the benchmark results and compare the BF16 and INT8/W8A8 MoE runs.
