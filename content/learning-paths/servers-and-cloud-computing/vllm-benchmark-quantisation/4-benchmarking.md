---
title: Evaluate Llama3.1-8B throughput and accuracy
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark Llama performance

Use the vLLM bench CLI to measure the throughput of your models. First, install the required library then start the server in the background:
```bash
pip install vllm[bench]

vllm serve \
  --model meta-llama/Llama-3.1-8B \
  --max-num-batched-tokens 8192 \
  --max-model-len 4096 &
```

Wait for `Application startup complete` in the server output before continuing. The following `wget` command will take a few seconds, which usually gives the server enough time to start.

vLLM uses dynamic continuous batching to maximise hardware utilisation. Two key parameters govern this process:
- `max-model-len`: the maximum sequence length (number of tokens per request). No single prompt or generated sequence can exceed this limit. The value chosen here is large enough for the selected model and dataset.
- `max-num-batched-tokens`: the total number of tokens processed in one batch across all requests. The sum of input and output tokens from all concurrent requests must stay within this limit. The value chosen here, combined with the concurrency limit shown as follows, gives optimal throughput and latency.

Now the server is running, you can benchmark using the public ShareGPT dataset:
```bash
wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
 
vllm bench serve \
  --model meta-llama/Llama-3.1-8B \
  --dataset-name sharegpt \
  --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
  --num-prompts 256 \
  --request-rate 8 \
  --max-concurrency 10 \
  --top-p 1 --temperature 0 \
  --percentile-metrics ttft,tpot \
  --metric-percentiles 50,95,99 \
  --save-result --result-dir bench_out --result-filename serve.json
```

The output is similar to:

```output
Failed requests:                         0         
Maximum request concurrency:             10        
Request rate configured (RPS):           8.00      
Benchmark duration (s):                  551.96    
Total input tokens:                      54084     
Total generated tokens:                  35468     
Request throughput (req/s):              0.46      
Output token throughput (tok/s):         64.26     
Peak output token throughput (tok/s):    120.00    
Peak concurrent requests:                13.00     
Total token throughput (tok/s):          162.24    
---------------Time to First Token----------------
Mean TTFT (ms):                          1077.07   
Median TTFT (ms):                        610.55    
P50 TTFT (ms):                           610.55    
P95 TTFT (ms):                           2657.55   
P99 TTFT (ms):                           4134.92   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          168.44    
Median TPOT (ms):                        140.70    
P50 TPOT (ms):                           140.70    
P95 TPOT (ms):                           224.80    
P99 TPOT (ms):                           966.98    
==================================================
```

Here greedy decoding (`--top-p 1 --temperature 0`) selects the highest-probability token at each step rather than sampling, giving deterministic and reproducible results. The key metrics to focus on are output token throughput, total token throughput, mean TTFT, and mean TPOT. As shown in the output, the mean TPOT exceeds the 100ms target at `max-concurrency 10` for the BF16 model. The quantized model that you'll run next uses higher concurrency to demonstrate the throughput improvement.

Repeat with the quantized model. With the reduced model size, you can increase concurrency, which results in a significant throughput improvement. Stop the running BF16 server first with Ctrl+C, then start the quantized model server:
```bash
vllm serve \
  --model RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 \
  --max-num-batched-tokens 8192 \
  --max-model-len 4096 &
```

Wait for `Application startup complete`, then run the benchmark:
```bash
vllm bench serve \
  --model RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 \
  --dataset-name sharegpt \
  --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
  --num-prompts 256 \
  --request-rate 8 \
  --max-concurrency 24 \
  --top-p 1 --temperature 0 \
  --percentile-metrics ttft,tpot \
  --metric-percentiles 50,95,99 \
  --save-result --result-dir bench_out --result-filename serve.json
```

The output is similar to:

```output
Failed requests:                         0         
Maximum request concurrency:             24        
Request rate configured (RPS):           8.00      
Benchmark duration (s):                  210.01    
Total input tokens:                      54084     
Total generated tokens:                  29058     
Request throughput (req/s):              1.22      
Output token throughput (tok/s):         138.36    
Peak output token throughput (tok/s):    336.00    
Peak concurrent requests:                31.00     
Total token throughput (tok/s):          395.89    
---------------Time to First Token----------------
Mean TTFT (ms):                          1227.51   
Median TTFT (ms):                        702.22    
P50 TTFT (ms):                           702.22    
P95 TTFT (ms):                           4682.75   
P99 TTFT (ms):                           7564.33   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          189.36    
Median TPOT (ms):                        152.23    
P50 TPOT (ms):                           152.23    
P95 TPOT (ms):                           304.81    
P99 TPOT (ms):                           1221.36   
==================================================
```

The quantized model completes the same benchmark in roughly 2.6x less time than the BF16 model. Output token throughput and total token throughput both increase by over 2x, confirming significant throughput gains from INT8 quantization at higher concurrency.

## Benchmark Llama accuracy 

The lm-evaluation-harness is the standard way to measure model accuracy across common academic benchmarks (for example [MMLU](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmlu), [HellaSwag](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/hellaswag), [GSM8K](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gsm8k)) and runtimes (such as [Hugging Face](https://github.com/huggingface/transformers), [vLLM](https://github.com/vllm-project/vllm), and [llama.cpp](https://github.com/ggml-org/llama.cpp)). In this step, you'll install the `lm_eval` harness with vLLM support, run benchmarks on both the BF16 and INT8 deployments, and interpret the accuracy difference between precisions.

First, install the required libraries for benchmarking with `lm_eval`:
```bash
pip install ray lm_eval[vllm] 
```

You can use a limited number of prompts to validate your environment by appending ```--limit 10``` to the following command:
```bash
lm_eval --model vllm --model_args pretrained=meta-llama/Llama-3.1-8B,dtype=bfloat16,max_model_len=4096 --tasks mmlu,gsm8k --batch_size auto
```
A proper accuracy benchmark should be run over the whole dataset, though this can be time consuming and is considered optional for this Learning Path. This accuracy benchmark will be slower the first time through as you will download the test data associated with your selected task

The output is similar to:

```output
|      Groups      |Version|Filter|n-shot|Metric|   |Value |   |Stderr|
|------------------|------:|------|-----:|------|---|-----:|---|-----:|
|mmlu              |      2|none  |      |acc   |   |0.6895|±  |0.0183|
| - humanities     |      2|none  |     0|acc   |↑  |0.7462|±  |0.0378|
| - other          |      2|none  |     0|acc   |↑  |0.6538|±  |0.0395|
| - social sciences|      2|none  |     0|acc   |↑  |0.7917|±  |0.0363|
```

{{% notice Note %}}
This output was generated with `--limit 10`, which runs only 10 prompts per task. Results will vary between runs at this sample size. Remove `--limit 10` for a full benchmark over the complete dataset.
{{% /notice %}}

The [MMLU task](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmlu) is a set of multiple choice questions split into the subgroups listed in the output. The task allows you to measure the ability of an LLM to understand questions and select the right answers.

The [GSM8k task](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gsm8k) is a set of math problems that test an LLM's mathematical reasoning ability.

Repeat with the quantized model:
```bash
lm_eval --model vllm --model_args pretrained=RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8,dtype=bfloat16,max_model_len=4096 --tasks mmlu,gsm8k --batch_size auto
```

The output is similar to:

```output
|      Groups      |Version|Filter|n-shot|Metric|   |Value |   |Stderr|
|------------------|------:|------|-----:|------|---|-----:|---|-----:|
|mmlu              |      2|none  |      |acc   |   |0.6614|±  |0.0189|
| - humanities     |      2|none  |     0|acc   |↑  |0.7231|±  |0.0359|
| - other          |      2|none  |     0|acc   |↑  |0.6077|±  |0.0416|
| - social sciences|      2|none  |     0|acc   |↑  |0.7417|±  |0.0390|
| - stem           |      2|none  |     0|acc   |↑  |0.6053|±  |0.0345|
```

The INT8 model scores approximately 3% lower on MMLU than the BF16 model, which is consistent with the expected accuracy cost of INT8 weight quantization. For full reference results, see the [Red Hat model card](https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8#accuracy).

## Summary of benchmarking results

The benchmarking results you generate will depend on the hardware you are using. The following values are illustrative examples measured on a 96-core machine with 128-bit SVE and 192 GB of RAM. Treat them as a guide to the relative improvements rather than absolute targets.

Using the INT8 quantized Llama3.1-8B model resulted in throughput improvements of over 2x. The following accuracy results used `--limit 10`. A full dataset run might show up to an 8% accuracy drop.

### Throughput: BF16 vs INT8 (max-concurrency 10 vs 24)
| Metric | BF16 | INT8 | Ratio |
|---|---|---|---|
| Request throughput (req/s) | 0.46 | 1.22 | 2.7x |
| Output token throughput (tok/s) | 64.26 | 138.36 | 2.2x |
| Total token throughput (tok/s) | 162.24 | 395.89 | 2.4x |

### Accuracy recovery: INT8/BF16 (--limit 10)
| MMLU | GSM8k |
|---|---|
| 97% | 92% |

Run without `--limit` for a statistically representative accuracy comparison.

## What you've accomplished

You've now succesfully benchmarked quantized and non-quantized LLama3.1-8B models for throughput and accuracy. The results suggest that quantization improves a model's throughput but can reduce its accuracy.

Now that your environment is set up for running inference, benchmarking, and quantizing different models, you can experiment further. Try benchmarking accuracy with different tasks, different quantization techniques, or different models. Your results will allow you to balance accuracy and performance when making decisions about model deployment.
