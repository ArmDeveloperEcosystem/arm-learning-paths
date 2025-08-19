---
title: Benchmark and evaluate the quantized models
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark performance using llama-bench

Use the [`llama-bench`](https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench) tool to measure model performance, including inference speed and memory usage.

## Run basic benchmarks

Benchmark multiple model versions to compare performance:

```bash
# Benchmark the full-precision model
bin/llama-bench -m models/afm-4-5b/afm-4-5B-F16.gguf

# Benchmark the 8-bit quantized model
bin/llama-bench -m models/afm-4-5b/afm-4-5B-Q8_0.gguf

# Benchmark the 4-bit quantized model
bin/llama-bench -m models/afm-4-5b/afm-4-5B-Q4_0.gguf
```

Typical results on a 16 vCPU instance:
- **F16 model**: ~25 tokens/second, ~9GB memory usage
- **Q8_0 model**: ~40 tokens/second, ~5GB memory usage
- **Q4_0 model**: ~60 tokens/second, ~3GB memory usage

Your actual results might vary depending on your specific instance configuration and system load.

## Run advanced benchmarks

Use this command to benchmark performance across prompt sizes and thread counts:

```bash
bin/llama-bench -m models/afm-4-5b/afm-4-5B-Q4_0.gguf \
  -p 128,256,512 \
  -n 128 \
  -t 4,8,16
```

This command does the following:
- Loads the 4-bit model and runs inference benchmarks
- `-p`: evaluates prompt lengths of 128, 256, and 512 tokens
- `-n`: generates 128 tokens
- `-t`: runs inference using 4, 8, and 16 threads

Here’s an example of how performance scales across threads and prompt sizes (pp = prompt processing, tg = text generation):

| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       4 |           pp128 |        106.03 ± 0.21 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       4 |           pp256 |        102.82 ± 0.05 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       4 |           pp512 |         95.41 ± 0.18 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       4 |           tg128 |         24.15 ± 0.02 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       8 |           pp128 |        196.02 ± 0.42 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       8 |           pp256 |        190.23 ± 0.34 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       8 |           pp512 |        177.14 ± 0.31 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |       8 |           tg128 |         40.86 ± 0.11 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |      16 |           pp128 |        346.08 ± 0.62 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |      16 |           pp256 |        336.72 ± 1.43 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |      16 |           pp512 |        315.83 ± 0.22 |
| arcee 4B Q4_0                  |   2.50 GiB |     4.62 B | CPU        |      16 |           tg128 |         62.39 ± 0.20 |

Even with just four threads, the Q4_0 model achieves comfortable generation speeds. On larger instances, you can run multiple concurrent model processes to support parallel workloads.

To benchmark batch inference, use [`llama-batched-bench`](https://github.com/ggml-org/llama.cpp/tree/master/tools/batched-bench).


## Evaluate model quality using llama-perplexity

Use the llama-perplexity tool to measure how well each model predicts the next token in a sequence. Perplexity is a measure of how well a language model predicts text. It gives you insight into the model’s confidence and predictive ability, representing the average number of possible next tokens the model considers when predicting each word: 

- A lower perplexity score indicates the model is more confident in its predictions and generally performs better on the given text. 
- For example, a perplexity of 2.0 means the model typically considers ~2 tokens per step when making each prediction, while a perplexity of 10.0 means it considers 10 possible tokens on average, indicating more uncertainty.

The `llama-perplexity` tool evaluates the model's quality on text datasets by calculating perplexity scores. Lower perplexity indicates better quality.

## Download a test dataset

Use the following script to download and extract the Wikitext-2 dataset:

```bash
sh scripts/get-wikitext-2.sh
```
This script downloads and extracts the dataset to a local folder named `wikitext-2-raw`.

## Run a perplexity evaluation

Run the llama-perplexity tool to evaluate how well each model predicts the Wikitext-2 test set:

```bash
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-F16.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-Q8_0.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-Q4_0.gguf -f wikitext-2-raw/wiki.test.raw
```

{{< notice Tip >}}
To reduce runtime, add the `--chunks` flag to evaluate a subset of the data. For example: `--chunks 50` runs the evaluation on the first 50 text blocks.
{{< /notice >}}

## Run the evaluation as a background script

Running a full perplexity evaluation on all three models takes about 3 hours. To avoid SSH timeouts and keep the process running after logout, wrap the commands in a shell script and run it in the background.

Create a script named ppl.sh:

For example:
```bash
#!/bin/bash
# ppl.sh
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-F16.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-Q8_0.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-Q4_0.gguf -f wikitext-2-raw/wiki.test.raw
```
```bash
 nohup sh ppl.sh >& ppl.sh.log &
 tail -f ppl.sh.log
 ```

| Model | Generation speed (batch size 1, 16 vCPUs) | Memory Usage | Perplexity (Wikitext-2) | Perplexity Increase |
|:-------:|:----------------------:|:------------:|:----------:|:----------------------:|
| F16     | ~25 tokens per second  | ~9 GB        | 8.4612 +/- 0.06112 | 0 (baseline)           |
| Q8_0    | ~40 tokens per second  | ~5 GB        | 8.4776 +/- 0.06128 | +0.19%                |
| Q4_0    | ~60 tokens per second  | ~3 GB        | 9.1897 +/- 0.06604 | +8.6%                   |

We can see that 8-bit quantization introduces negligible degradation. The 4-bit model does suffer more, but may still serve its purpose for simpler use cases. As always, you should run your own tests and make up your own mind.

When you have finished your benchmarking and evaluation, make sure to terminate your Google instance in the console to avoid incurring unnecessary charges for unused compute resources.

