---
title: Benchmark MoE serving performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## MoE performance benchmarking

Use the `vllm bench serve` CLI to measure online serving performance for the selected MoE models.

The benchmark sends requests to the vLLM OpenAI-compatible API server at:

```text
/v1/chat/completions
```

Start the model server first using the commands from [Run MoE inference with vLLM](../3-run-inference/), and keep it running in one terminal. Then run the benchmark command from another terminal.

Benchmark using ShareGPT prompt subsets. First, download the public ShareGPT dataset from Hugging Face:

```bash
wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
```

The benchmark results in this Learning Path use ShareGPT prompt subsets selected with each model tokenizer. The results shown use prompts with approximately 512 input tokens. You can use your own ShareGPT subset or another dataset by updating the dataset path in the benchmark command.

## Benchmark setup

The benchmark setup used in this Learning Path is:

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

Greedy decoding is configured with `--top-p 1 --temperature 0 --top-k 1`. This selects the next token deterministically instead of sampling from multiple likely tokens.

When prefix caching is enabled, repeating `vllm bench serve` against the same server can reuse prompts from earlier benchmark runs and inflate throughput. To avoid this, start a fresh vLLM server for each concurrency value.

## Run the benchmark

For the ShareGPT ~512 input-token subset, run:

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
  --result-filename gemma4_sharegpt_mc${C}.json \
  --num-warmups 5
```

Repeat the benchmark for:

```text
C=8
C=16
C=32
```

Start a fresh vLLM server before each concurrency value.

For Gemma4, use the Gemma4 ShareGPT subset:

```bash
--dataset-path ./sharegpt_gemma4_512.json
```

For GPT-OSS, use the GPT-OSS ShareGPT subset:

```bash
--dataset-path ./sharegpt_gptoss_512.json
```

For Qwen3 BF16 and Qwen3 W8A8, use the Qwen3 ShareGPT subset:

```bash
--dataset-path ./sharegpt_qwen_512.json
```

To benchmark an alternative dataset or subset, update the dataset path and result filename:

```text
--dataset-path <path_to_dataset>
--result-filename <model>_<dataset>_mc${C}.json
```

## Metrics

The interesting results are:

- Request throughput
- Output token throughput
- Total token throughput
- TTFT, or time to first token
- TPOT, or time per output token

## What you've accomplished and what's next

You've now benchmarked MoE serving performance with `vllm bench serve`.

Next, you'll review the benchmark results and compare the BF16 and INT8/W8A8 MoE runs.