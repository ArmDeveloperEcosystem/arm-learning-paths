---
title: Choose thread count and model size from the measurements
description: Use llama-bench measurements on Arm CPUs to choose decode and prefill thread counts and predict throughput for different model sizes.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Measure the thread sweep directly

You're now ready to make decisions based on the decode and prefill diagnosis that you performed. 

The diagnosis picks the best thread count for each model. To see the whole sweep, run `llama-bench` directly on one model:

```bash
cd $HOME/llama.cpp
./build/bin/llama-bench -m $HOME/models/qwen2.5-0.5b-instruct-q4_0.gguf \
    -t 1,2,3,4 -p 512 -n 128 -r 5 -o md
```

The output is similar to:

```output
| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       1 |           pp512 |         93.49 ± 0.20 |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       1 |           tg128 |         32.42 ± 0.14 |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       2 |           pp512 |        173.68 ± 0.08 |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       2 |           tg128 |         33.84 ± 0.05 |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       3 |           pp512 |        233.22 ± 0.94 |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       3 |           tg128 |         29.37 ± 0.05 |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       4 |           pp512 |        289.92 ± 0.11 |
| qwen2 1B Q4_0                  | 403.20 MiB |   630.17 M | CPU        |       4 |           tg128 |         27.28 ± 0.02 |

build: 836d571 (1)
```

Each row of the table is one test at one thread count:

- `pp512` is prompt processing of a 512-token prompt.
- `tg128` is token generation of 128 tokens.
- `t/s` is tokens per second, with the standard deviation over five repetitions.

The example measurements were made on a Raspberry Pi 5 with 2 GB of RAM. The build used llama.cpp commit `836d571`, GCC 12.2.0, and the default Release flags. The board used the `ondemand` governor. The `get_throttled` command reported `throttled=0x0` before and after the sweep. Threads weren't pinned to cores.

## Find the decode knee

Look at the `tg128` rows as threads increase. On a memory-bound system, decode stops improving after a small number of threads. Extra threads wait on the same memory, and decode performance can fall as you add more.

The decode knee is at two threads. Using four threads reduces decode performance by 19.4%.

Now look at the `pp512` rows. Prefill keeps rising up to four threads, because it's compute-bound.

Prefill scales well with more threads, reaching 3.10x the one-thread result when using four threads.

You can draw the following conclusions from this:

- For workloads with short prompts and long answers, such as a chat, set `-t` to the decode knee.
- For workloads with long prompts and short answers, such as summarization, use all cores.
- Always set `-t` explicitly. The default isn't chosen for your workload.

## Predict the effect of a smaller model

Because decode is memory-bound, the ratio of model sizes predicts the ratio of decode speeds. 

The `WHAT TO CHANGE` section of the diagnosis compares two of your models:

```output
Measured here: qwen2.5-0.5b-instruct-q4_0 is 2.68x smaller than qwen2.5-1.5b-instruct-q4_0 and decodes 2.75x faster.
```

If the size ratio and the speed ratio are close, the bandwidth equation holds on your system. 

You can then estimate the decode speed of any dense model before you download it:

```text
expected tokens/s  =  fitted bandwidth  /  bytes per token
```

For example, consider the fitted bandwidth of 11.82 GB/s measured on the Raspberry Pi 5. On a Pi with that bandwidth, a model that reads 2 GB per token decodes at about 6 tokens/s.

{{% notice Note %}}
This estimate is a short-context result. As the key-value (KV) cache grows during a long conversation, decode reads more than the weights. It slows down beyond what the equation predicts. Use the `--depth` option of `llama-roofline run` to measure decode with tokens already in the context.
{{% /notice %}}

## What you've accomplished

You've now chosen thread counts for decode and prefill from measurements. You've learned to predict decode speed from model size and fitted bandwidth. You know why an Arm system generates tokens at a given rate, and what change will make it faster. 

Run the same commands on other Arm Linux systems to evaluate their ceiling, fitted bandwidth, and decode knee.
