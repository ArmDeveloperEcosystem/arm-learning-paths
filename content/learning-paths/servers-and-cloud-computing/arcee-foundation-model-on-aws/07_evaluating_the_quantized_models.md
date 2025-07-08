---
title: Evaluating the quantized models
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Using llama-bench for Performance Benchmarking

The [`llama-bench`](https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench) tool allows you to measure the performance characteristics of your model, including inference speed and memory usage.

### Basic Benchmarking

You can benchmark multiple model versions to compare their performance:

```bash
# Benchmark the full precision model
bin/llama-bench -m models/afm-4-5b/afm-4-5B-F16.gguf

# Benchmark the 8-bit quantized model
bin/llama-bench -m models/afm-4-5b/afm-4-5B-Q8_0.gguf

# Benchmark the 4-bit quantized model
bin/llama-bench -m models/afm-4-5b/afm-4-5B-Q4_0.gguf
```

Running each model on 16 vCPUs, you should see results like:
- **F16 model**: ~15-16 tokens/second, ~15GB memory usage
- **Q8_0 model**: ~25 tokens/second, ~8GB memory usage  
- **Q4_0 model**: ~40 tokens/second, ~4.4GB memory usage

The exact performance will depend on your specific instance configuration and load.

### Advanced Benchmarking

```bash
bin/llama-bench -m models/afm-4-5b/afm-4-5B-Q4_0.gguf \
  -p 128,256,512 \
  -n 128 \
  -t 8,16,24
```

This command:
- Loads the model and runs inference benchmarks
- `-p`: Evaluates a random prompt of 128, and 512 tokens
- `-n`: Generates 128 tokens
- `-t`: Run the model on 4, 8, and 16 threads

The results should look like this:

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

It's pretty amazing to see that with only 4 threads, the 4-bit model can still generate at the very comfortable speed of 15 tokens per second. We could definitely run several copies of the model on the same instance to serve concurrent users or applications.

You can also try [`llama-batched-bench`](https://github.com/ggml-org/llama.cpp/tree/master/tools/batched-bench) to benchmark performance on batch sizes larger than 1.


## Using llama-perplexity for Model Evaluation

Perplexity is a measure of how well a language model predicts text. It represents the average number of possible next tokens the model considers when predicting each word. A lower perplexity score indicates the model is more confident in its predictions and generally performs better on the given text. For example, a perplexity of 2.0 means the model typically considers 2 possible tokens when making each prediction, while a perplexity of 10.0 means it considers 10 possible tokens on average.

The `llama-perplexity` tool evaluates the model's quality on text datasets by calculating perplexity scores. Lower perplexity indicates better quality.

### Downloading a Test Dataset

First, download the Wikitest-2 test dataset.

```bash
sh scripts/get-wikitext-2.sh
```

### Running Perplexity Evaluation

Next, measure perplexity on the test dataset.

```bash
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-F16.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-Q8_0.gguf -f wikitext-2-raw/wiki.test.raw
bin/llama-perplexity -m models/afm-4-5b/afm-4-5B-Q4_0.gguf -f wikitext-2-raw/wiki.test.raw
```

If you want to speed things up, you can add the `--chunks` option to use a fraction of 564 chunks contained in the test dataset.

On the full dataset, these three commands will take about 5 hours. You should run them in a shell script to avoid SSH timeouts.

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

| Model | Generation Speed (tokens/s, 16 vCPUs) | Memory Usage | Perplexity (Wikitext-2) |
|:-------:|:----------------------:|:------------:|:----------:|
| F16     | ~15–16                 | ~15 GB       | TODO     |
| Q8_0    | ~25                    | ~8 GB        | TODO       |
| Q4_0    | ~40                    | ~4.4 GB      | TODO       |

When you have finished your benchmarking and evaluation, make sure to terminate your AWS EC2 instance in the AWS Management Console to avoid incurring unnecessary charges for unused compute resources.

