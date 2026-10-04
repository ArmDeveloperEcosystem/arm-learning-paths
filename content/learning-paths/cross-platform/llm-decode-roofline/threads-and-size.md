---
title: Choose thread count and model size from the measurements
description: Run a llama-bench thread sweep on an Arm CPU to find the decode thread knee, see how prefill scales with cores, and use the fitted bandwidth to predict decode speed for other model sizes.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Measure the thread sweep directly

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
- `t/s` is tokens per second, with the standard deviation over 5 repetitions.

This table was measured on a Raspberry Pi 5 with 2 GB of RAM, llama.cpp commit `836d571` built with GCC 12.2.0 and the default Release flags, the `ondemand` governor, and `get_throttled` reporting `throttled=0x0` before and after the sweep. Threads were not pinned to cores.

## Find the decode knee

Look at the `tg128` rows as threads increase. On a memory-bound system, decode stops improving after a small number of threads, because the extra threads wait on the same memory, and it can fall as you add more.

<!-- MANU WRITES: one sentence, in your own words, stating the decode knee on the Raspberry Pi 5 and how much decode is lost at 4 threads.
Facts from capture 20261003_2358, llama-bench sweep above (see NUMBERS_TRACE.md):
* tg128: 1 thread 32.42, 2 threads 33.84, 3 threads 29.37, 4 threads 27.28 tokens/s (llamabench_qwen05_q4_0.md lines 4, 6, 8, 10).
* Knee: 2 threads, the best decode at 33.84 tokens/s (outputs/LP_FACTS_FOR_MANU.md line 25; diagnosis.json analysis.decode_thread_knee = 2).
* 4 threads decode 19.4 percent less than 2 threads: (33.84 minus 27.28) / 33.84 (outputs/LP_FACTS_FOR_MANU.md line 26).
-->

Now look at the `pp512` rows. Prefill keeps rising up to 4 threads, because it is compute-bound.

<!-- MANU WRITES: one sentence, in your own words, stating how much prefill scales from 1 to 4 threads on the Raspberry Pi 5.
Facts from capture 20261003_2358, llama-bench sweep above (see NUMBERS_TRACE.md):
* pp512: 1 thread 93.49, 2 threads 173.68, 3 threads 233.22, 4 threads 289.92 tokens/s (llamabench_qwen05_q4_0.md lines 3, 5, 7, 9).
* Scaling 1 to 4 threads: 289.92 / 93.49 = 3.10 times (outputs/LP_FACTS_FOR_MANU.md line 28).
* The diagnose run (pp128, 3 repetitions) reports 3.1 times (diagnose.txt line 61; diagnosis.json analysis.prefill_scaling 3.08). Quote the sweep figure here, because this sentence sits under the sweep table.
-->

This means:

- For chat and other workloads with short prompts and long answers, set `-t` to the decode knee.
- For summarization and other workloads with long prompts and short answers, use all cores.
- Always set `-t` explicitly. The default is not chosen for your workload.

## Predict the effect of a smaller model

Because decode is memory-bound, the ratio of model sizes predicts the ratio of decode speeds. The `WHAT TO CHANGE` section of the diagnosis compares two of your models:

```output
Measured here: qwen2.5-0.5b-instruct-q4_0 is 2.68x smaller than qwen2.5-1.5b-instruct-q4_0 and decodes 2.75x faster.
```

If the size ratio and the speed ratio are close, the bandwidth equation holds on your system, and you can estimate the decode speed of any dense model before you download it:

```output
expected tokens/s  =  fitted bandwidth  /  bytes per token
```

For example, with the fitted bandwidth of 11.82 GB/s measured on the Raspberry Pi 5, a model that reads 2 GB per token decodes at about 6 tokens/s.

{{% notice Note %}}
This estimate is a short-context result. As the KV cache grows during a long conversation, decode reads more than the weights and slows down beyond what the equation predicts. Use the `--depth` option of `llama-roofline run` to measure decode with tokens already in the context.
{{% /notice %}}

## What you've accomplished

In this Learning Path, you have:

- Measured the sustained memory-read bandwidth of an Arm system.
- Determined how close llama.cpp decode runs to that ceiling on your Arm CPU.
- Chosen thread counts for decode and prefill from measurements.
- Learned to predict decode speed from model size and fitted bandwidth.

You can now explain why a given Arm system generates tokens at the rate it does, and which change will make it faster. Run the same commands on any other Arm Linux system to compare its ceiling, fitted bandwidth and decode knee with the Raspberry Pi 5 results.
