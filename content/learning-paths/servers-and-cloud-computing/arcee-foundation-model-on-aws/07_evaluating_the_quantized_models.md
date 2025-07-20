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
- **F16 model**: ~15-16 tokens/second, ~15GB memory usage
- **Q8_0 model**: ~25 tokens/second, ~8GB memory usage  
- **Q4_0 model**: ~40 tokens/second, ~4.4GB memory usage

Your actual results might vary depending on your specific instance configuration and system load.

## Run advanced benchmarks

Use this command to benchmark performance across prompt sizes and thread counts:

```bash
bin/llama-bench -m models/afm-4-5b/afm-4-5B-Q4_0.gguf \
  -p 128,256,512 \
  -n 128 \
  -t 8,16,24
```

This command does the following:
- Loads the 4-bit model and runs inference benchmarks
- `-p`: evaluates prompt lengths of 128, 256, and 512 tokens
- `-n`: generates 128 tokens
- `-t`: runs inference using 4, 8, and 24 threads

Here’s an example of how performance scales across threads and prompt sizes:

| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |       4 |           pp128 |         62.90 ± 0.08 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |       4 |           pp512 |         57.63 ± 0.06 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |       4 |           tg128 |         15.18 ± 0.02 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |       8 |           pp128 |        116.23 ± 0.04 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |       8 |           pp512 |        106.39 ± 0.03 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |       8 |           tg128 |         25.29 ± 0.05 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |      16 |           pp128 |        206.67 ± 0.10 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |      16 |           pp512 |        190.18 ± 0.03 |
| llama 8B Q4_0                  |   4.33 GiB |     8.03 B | CPU        |      16 |           tg128 |         40.99 ± 0.36 |

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

Running a full perplexity evaluation on all three models takes about 5 hours. To avoid SSH timeouts and keep the process running after logout, wrap the commands in a shell script and run it in the background.

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

Here are the full results.

| Model | Generation speed (tokens/s, 16 vCPUs) | Memory Usage | Perplexity (Wikitext-2) |
|:-------:|:----------------------:|:------------:|:----------:|
| F16     | ~15–16                 | ~15 GB       | TODO     |
| Q8_0    | ~25                    | ~8 GB        | TODO       |
| Q4_0    | ~40                    | ~4.4 GB      | TODO       |

When you have finished your benchmarking and evaluation, make sure to terminate your AWS EC2 instance in the AWS Management Console to avoid incurring unnecessary charges for unused compute resources.

