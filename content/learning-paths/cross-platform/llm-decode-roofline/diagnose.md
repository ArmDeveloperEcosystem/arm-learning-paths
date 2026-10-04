---
title: Diagnose whether decode is memory-bound
description: Run llama-roofline inspect and diagnose against three GGUF models on an Arm CPU to see how many bytes decode reads per token and how close llama.cpp decode runs to the measured memory bandwidth ceiling.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inspect what each model reads per token

Before you benchmark, check how many bytes decode reads from each file:

```bash
llama-roofline inspect $HOME/models/qwen2.5-0.5b-instruct-q4_0.gguf
```

The output is similar to:

```output
========================================================================
  qwen2.5-0.5b-instruct-q4_0.gguf
========================================================================
  label      : Q4_0   architecture: qwen2
  actually   : 100% Q4_0 in the repeating layers, 4.50 bits per weight
  file       : 429 MB, 291 tensors
  per token  : 346 MB read (82% of the file)
  output head: 145 MB, 42% of what is read per token

  TENSOR TYPES
------------------------------------------------------------------------
    type        tensors        MB   share
    Q4_0            169       278     65%
    Q8_0              1       145     34%
    F32             121         0      0%

  WHAT THE LABEL MEANS HERE
------------------------------------------------------------------------
  This file is what it says: 100% of its repeating-layer bytes are
  Q4_0. The output head is Q8_0. It stores 4.50 bits per weight. A
  GGUF label names a recipe rather than a type. llama-quantize
  substitutes per tensor when a shape does not divide by the block
  size, and it substitutes differently depending on what the file was
  converted from. Neither is visible from the filename, and at small
  model sizes the substitution can take over the file.
```

The `per token` line is smaller than the file size. The token embedding table is part of the file, but decode only looks up one row of it per token instead of streaming all of it. For this 0.5B file, decode reads 346 MB of the 429 MB file, or 82 percent, so using the file size would make the model look slower relative to the ceiling than it is.

## Run the diagnosis

Run the full diagnosis across your three models and the four thread counts of the Raspberry Pi 5:

```bash
cd $HOME
llama-roofline diagnose $HOME/models \
    --llama-bench $HOME/llama.cpp/build/bin/llama-bench \
    --threads 1,2,3,4
```

The command took about 11 minutes on the Raspberry Pi 5 used for this Learning Path. It measures the memory ceiling again, then runs `llama-bench` for each model at each thread count, with a 128-token prompt and 128 generated tokens, and repeats each setting 3 times.

{{% notice Note %}}
Do not run anything else on the board while the diagnosis runs. If you are connected over SSH, run the command under `nohup` and redirect its output to a file so a dropped connection does not stop it.
{{% /notice %}}

The output is similar to:

```output
machine     : Raspberry Pi 5 Model B Rev 1.0 (4 logical cores)
llama-bench : /home/manu/llama.cpp/build/bin/llama-bench
plan        : 3 model(s) x 4 thread setting(s), 3 repetition(s)

[1/2] measuring the memory ceiling ...
      -> 13.8 GB/s (max kernel, 1 threads)

[2/2] benchmarking ...

  qwen2.5-0.5b-instruct-q4_0  (429 MB, Q4_0)
    t=1   decode   32.30 tok/s   prefill    105.9 tok/s
    t=2   decode   34.22 tok/s   prefill    197.0 tok/s
    t=3   decode   30.15 tok/s   prefill    265.3 tok/s
    t=4   decode   28.92 tok/s   prefill    326.5 tok/s

  qwen2.5-0.5b-instruct-q8_0  (676 MB, Q8_0)
    t=1   decode   22.59 tok/s   prefill     76.5 tok/s
    t=2   decode   22.12 tok/s   prefill    101.0 tok/s
    t=3   decode   19.72 tok/s   prefill    197.0 tok/s
    t=4   decode   18.55 tok/s   prefill    250.0 tok/s

  qwen2.5-1.5b-instruct-q4_0  (1066 MB, Q4_0)
    t=1   decode   10.48 tok/s   prefill     29.0 tok/s
    t=2   decode   12.43 tok/s   prefill     51.5 tok/s
    t=3   decode   11.23 tok/s   prefill     72.5 tok/s
    t=4   decode    9.91 tok/s   prefill     82.6 tok/s

========================================================================
  llama-roofline v0.2.0  --  diagnosis
========================================================================
  Machine   : Raspberry Pi 5 Model B Rev 1.0
              4 logical cores, 2.1 GB RAM, Linux aarch64
  Memory    : 13.8 GB/s sustained read (measured: max kernel, 1 threads)
  llama.cpp : build 1 (836d571), backends: CPU

  THE ANSWER
------------------------------------------------------------------------
  Yes. Decode is memory-bandwidth-bound, at 86% of what this machine
  sustains.

  Every token reads the whole model out of RAM, and at this utilisation
  the cores are mostly waiting for it. A faster CPU changes nothing
  here. Fewer bytes does.

  For qwen2.5-0.5b-instruct-q8_0 the ceiling on this machine is about 26
  tok/s. You measured 22.6 at 1 threads.

  WHAT TO CHANGE
------------------------------------------------------------------------
  * Threads: use 1. Running 4 cost 18% of decode throughput, because
    decode is waiting on memory and more waiters do not make memory
    faster.
  * Size is the only dial that moves this. Halving the bytes read per
    token roughly doubles tok/s, which is why a smaller model or a lower
    quantization buys speed almost exactly in proportion to the bytes it
    removes.
  * Not every format of the same size costs the same, though, and which
    one wins depends on your core. Run `llama-roofline advise`.
  * Measured here: qwen2.5-0.5b-instruct-q4_0 is 2.68x smaller than
    qwen2.5-1.5b-instruct-q4_0 and decodes 2.75x faster.
  * Prompt processing is the opposite case: it scaled 3.1x with threads.
    If your workload is long prompts and short answers, you do want the
    cores.
  * This model reads 525 MB per token, not the 670 MB the file weighs:
    the token embedding is a row lookup, so 22% of the file never moves
    during generation. The output head alone is 28% of what does.

  WHAT WAS MEASURED
------------------------------------------------------------------------
  model                     quant         size    decode   prefill  thr    GB/s  %ceil
  ------------------------------------------------------------------------------------
  qwen2.5-0.5b-instruct-q4_ Q4_0        346 MB     34.2t      327t    2    11.8    86%
  qwen2.5-0.5b-instruct-q8_ Q8_0        525 MB     22.6t      250t    1    11.9    86%
  qwen2.5-1.5b-instruct-q4_ Q4_0        929 MB     12.4t       83t    2    11.6    84%

  THE ROOFLINE
------------------------------------------------------------------------
    decode tok/s  =  11.82 GB/s  /  bytes per token
    fitted across 3 models, R^2 = 0.9996,
    taking each model at its own best thread count
    One number predicts your generation speed, so you can size a
    model for a target tok/s instead of guessing.

  CAVEATS
------------------------------------------------------------------------
  * bytes-per-token is the sum of every tensor read on each token: the
    repeating layers and the output head. The token embedding is
    excluded, because decode looks up one row of it rather than
    streaming it, unless the model ties the embedding to the output
    head, in which case it is streamed in full and counted. That is
    exact for a dense transformer at short context and an overestimate
    once the KV cache grows large, or for MoE models.
  * The ceiling is what this machine sustained under a portable
    microbenchmark, not the spec sheet number. It is a floor on the
    truth, so the percentages are conservative.
  * Numbers are throughput only. Nothing here measures output quality.

========================================================================
  wrote:
    llama-roofline-out/diagnosis.json
    llama-roofline-out/diagnosis.md
  diagnosis.md is the shareable one: paste it into an issue or a forum thread as is.
```

## Read the answer

The report starts with a section called `THE ANSWER`. It states whether decode is memory-bound and at what percentage of the measured ceiling.

<!-- MANU WRITES: one or two sentences, in your own words, stating your result from the THE ANSWER section on the Raspberry Pi 5.
Facts from capture 20261003_2358 (see NUMBERS_TRACE.md):
* Verdict: memory-bound (diagnosis.json analysis.verdict).
* Decode runs at 84 to 86 percent of the measured ceiling across the 3 models (diagnose.txt lines 72 to 74).
* Ceiling measured inside diagnose: 13.77 GB/s, printed as 13.8 GB/s (diagnosis.json membw.peak_read_GBs; diagnose.txt line 6).
* Fitted line: decode tokens/s = 11.82 GB/s / bytes per token, R squared 0.9996, 3 models, each at its best thread count (diagnose.txt lines 78 to 80).
* Per model: 0.5B Q4_0 34.2 tokens/s at 2 threads, 86 percent; 0.5B Q8_0 22.6 tokens/s at 1 thread, 86 percent; 1.5B Q4_0 12.4 tokens/s at 2 threads, 84 percent (diagnose.txt lines 72 to 74).
-->

llama-roofline bases its verdict on the median percentage across your models. Use the percentage to decide what to change:

| Decode as a share of the ceiling | What it means | What to change |
|---|---|---|
| 70 percent or more | Decode is memory-bound | Read fewer bytes: use a smaller model or a smaller format |
| 40 to 70 percent | Partly memory-bound | Check thread count and background load first |
| Below 40 percent | Something other than memory is limiting decode | Check throttling, running more threads than cores, and swap |

The `WHAT WAS MEASURED` table lists each model with its size, decode and prefill speed, best thread count, achieved bandwidth and percentage of the ceiling. The `THE ROOFLINE` section prints the fitted line and its R squared value. An R squared close to 1 means the bandwidth equation explains your results. If R squared is below 0.90, llama-roofline adds a warning, because something other than memory bandwidth is affecting decode.

## Save the shareable report

The command writes two files to `llama-roofline-out/`:

```bash
ls llama-roofline-out/
```

```output
diagnosis.json  diagnosis.md
```

`diagnosis.md` is formatted for pasting into an issue or a forum thread. `diagnosis.json` contains every measurement for your own analysis.

## What you've accomplished

You have measured decode and prefill on three models and compared them with your system's bandwidth ceiling. You know whether decode is memory-bound on your Arm CPU and by how much. Next, you use the thread sweep to choose thread counts for decode and for prefill.
