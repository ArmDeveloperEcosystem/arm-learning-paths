---
title: Evaluate Llama3.1-8B throughput and accuracy
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Llama performance benchmarking

We will use the vLLM bench cli to measure the throughput of our models. First, start the server and keep it running:
```bash
vllm serve \
  --model meta-llama/Llama-3.1-8B-Instruct \
  --max-num-batched-tokens 16000 \
  --max-num-seqs 4 \
  --data-parallel-size 1 \
  --max-model-len 2048 &
  ```

vLLM uses dynamic continuous batching to maximise hardware utilisation. Three key parameters govern this process:

  * max-model-len, which is the maximum sequence length (number of tokens per request). No single prompt or generated sequence can exceed this limit.
  * max-num-batched-tokens, which is the total number of tokens processed in one batch across all requests. The sum of input and output tokens from all concurrent requests must stay within this limit.
  * max-num-seqs, which is the maximum number of requests the scheduler can place in one iteration.

Now the server is running, we can benchmark using the public ShareGPT dataset.
```bash
wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
 
vllm bench serve \
  --model meta-llama/Llama-3.1-8B-Instruct \
  --dataset-name sharegpt \
  --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
  --num-prompts 128 \
  --request-rate 8 \
  --max-concurrency 8 \
  --percentile-metrics ttft,tpot \
  --metric-percentiles 50,95,99 \
  --save-result --result-dir bench_out --result-filename serve.json

```
The interesting results are Request throughput, Output token throughput, Total token throughput, TTFT (time to first token) and TPOT (time per output token). 

Repeat with the quantised model. You should see a significant improvement in the throughput results (increased tokens/s).
```bash
vllm serve \
  --model RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 \
  --max-num-batched-tokens 16000 \
  --max-num-seqs 4 \
  --data-parallel-size 1 \
  --max-model-len 2048 &
 
vllm bench serve \
  --model RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 \
  --dataset-name sharegpt \
  --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
  --num-prompts 128 \
  --request-rate 8 \
  --max-concurrency 8 \
  --percentile-metrics ttft,tpot \
  --metric-percentiles 50,95,99 \
  --save-result --result-dir bench_out --result-filename serve.json
```

## Llama accuracy benchmarking

The lm-evaluation-harness is the standard way to measure model accuracy across common academic benchmarks (for example MMLU, HellaSwag, GSM8K) and runtimes (such as Hugging Face, vLLM, and llama.cpp). In this section, you’ll run accuracy tests for both BF16 and INT8 deployments of your Llama models served by vLLM on Arm-based servers.

You will:
- Install the lm-eval harness with vLLM support
- Run benchmarks on a BF16 model and an INT8 (weight-quantized) model
- Interpret key metrics and compare quality across precisions

First install the required libraries for benchmarking with lm_eval.
```bash
pip install ray lm_eval[vllm] 
```

Then use a limited number of prompts to validate your environment. This will be slower the first time through as you will download the test data associated with your selected task:
```bash
lm_eval --model vllm --model_args pretrained=meta-llama/Llama-3.1-8B,dtype=bfloat16,max_model_len=4096 --tasks mmlu --batch_size auto --limit 10
 
lm_eval --model vllm --model_args pretrained=meta-llama/Llama-3.1-8B,dtype=bfloat16,max_model_len=4096 --tasks gsm8k --batch_size 4 --limit 10
```

The [MMLU task](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmlu) is a set of multiple choice questions split into the subgroups listed above. It allows you to measure the ability of an LLM to understand questions and select the right answers.

The [GSM8k task](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gsm8k) is a set of math problems that test an LLM's mathematical reasoning ability.

Repeat with the quantised model.
```bash
lm_eval --model vllm --model_args pretrained=RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8,dtype=bfloat16,max_model_len=4096 --tasks mmlu,gsm8k --batch_size auto --limit 10
 
lm_eval --model vllm --model_args pretrained=RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8,dtype=bfloat16,max_model_len=4096 --tasks gsm8k --batch_size 4 --limit 10
```

We would expect to see the precision is slightly lower with INT8.

## Summary of results

The benchmarking results you generate will depend on the hardware you are using. The values below were measured on an AWS Graviton4 c8g.12xlarge instance and provided as an example only. We've applied limits to the number of samples used to make them easily reproducible. A proper accuracy benchmark should be run over the whole dataset, though this can be time consuming. Using the INT8 quantised Llama3.1-8B model we observe throughput improvements of up to ~3x at a cost of up to ~7% in accuracy.

Llama benchmark config:
  * Throughput: --num-prompts 128
  * Accuracy: --limit mmlu=10,gsm8k=500

### Throughput ratios: INT8/BF16
| Requests/s | Total Tokens/s | Output Tokens/s |
| --------   | --------       | -------- |
| 3.17x      | 2.30x          | 1.44x    |

### Accuracy delta: (BF16-INT8)/BF16
|  MMLU    | GSM8k    | 
| -------- | -------- |
| 3%       | 6-7%     |
