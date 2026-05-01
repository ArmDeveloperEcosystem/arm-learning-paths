---
title: Evaluate Llama3.1-8B throughput and accuracy
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Llama performance benchmarking

We will use the vLLM bench CLI to measure the throughput of our models. First, install the required library then start the server and keep it running:
```bash
pip install vllm[bench]

vllm serve \
  --model meta-llama/Llama-3.1-8B \
  --max-num-batched-tokens 8192 \
  --max-model-len 4096 &
```

vLLM uses dynamic continuous batching to maximise hardware utilisation. Two key parameters govern this process:
  * max-model-len, which is the maximum sequence length (number of tokens per request). No single prompt or generated sequence can exceed this limit.
  * max-num-batched-tokens, which is the total number of tokens processed in one batch across all requests. The sum of input and output tokens from all concurrent requests must stay within this limit.

Now the server is running, we can benchmark using the public ShareGPT dataset.
```bash
wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
 
vllm bench serve \
  --model meta-llama/Llama-3.1-8B \
  --dataset-name sharegpt \
  --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
  --num-prompts 256 \
  --request-rate 8 \
  --max-concurrency 10 \
  --percentile-metrics ttft,tpot \
  --metric-percentiles 50,95,99 \
  --save-result --result-dir bench_out --result-filename serve.json
```
The interesting results are request throughput, output token throughput, total token throughput, TTFT (time to first token) and TPOT (time per output token). We're aiming for a mean TPOT < 100ms, so the maximum concurrency selected should be as high as possible while meeting that TPOT requirement.

Repeat with the quantised model. The smaller model allows us to increase the concurrency. You should see a significant improvement in the throughput results (increased tokens/s).
```bash
vllm serve \
  --model RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 \
  --max-num-batched-tokens 8192 \
  --max-model-len 4096 &
 
vllm bench serve \
  --model RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 \
  --dataset-name sharegpt \
  --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
  --num-prompts 256 \
  --request-rate 8 \
  --max-concurrency 24 \
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

You can use a limited number of prompts to validate your environment by appending ```--limit 10``` to the command below. A proper accuracy benchmark should be run over the whole dataset, though this can be time consuming and is considered optional for this Learning Path. This accuracy benchmark will be slower the first time through as you will download the test data associated with your selected task:
```bash
lm_eval --model vllm --model_args pretrained=meta-llama/Llama-3.1-8B,dtype=bfloat16,max_model_len=4096 --tasks mmlu,gsm8k --batch_size auto
```

The [MMLU task](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmlu) is a set of multiple choice questions split into the subgroups listed above. It allows you to measure the ability of an LLM to understand questions and select the right answers.

The [GSM8k task](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gsm8k) is a set of math problems that test an LLM's mathematical reasoning ability.

Repeat with the quantised model.
```bash
lm_eval --model vllm --model_args pretrained=RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8,dtype=bfloat16,max_model_len=4096 --tasks mmlu,gsm8k --batch_size auto
```

We would expect to see the precision is slightly lower with INT8.

## Summary of results

The benchmarking results you generate will depend on the hardware you are using. The values below, provided as an example only, were measured on a 96 core machine with 128-bit SVE and 192 GB of RAM. Using the INT8 quantised Llama3.1-8B model we observe throughput improvements of over 2x at a cost of up to ~8% in accuracy.

### Throughput ratios: INT8/BF16
| Requests/s | Output Tokens/s | Total Tokens/s |
| --------   | --------        | --------       |
| 2.7x       | 2.2x            | 2.5x           |

### Accuracy recovery: INT8/BF16
|  MMLU    | GSM8k    |
| -------- | -------- |
| 97%       | 92%     |

## Next steps

Now that you have your environment set up for running inference, benchmarking and quantising different models, you can experiment with:
- Benchmarking accuracy with different tasks
- Different quantisation techniques
- Different models

Your results will allow you to balance accuracy and performance when making decisions about model deployment.
