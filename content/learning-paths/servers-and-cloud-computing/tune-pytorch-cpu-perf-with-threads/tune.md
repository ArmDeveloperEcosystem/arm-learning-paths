---
title: Fine-Tune Thread Count
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Tuning thread size

We will run inference on Google's [Gemma-3-1B-it](https://huggingface.co/google/gemma-3-1b-it) and measure how inference performance changes as we vary the thread count for both the 270-million-parameter and 1-billion-parameter models. We will be running the `transformers_llm_text_gen.py` script which by default applies groupwise, layout-aware INT4 quantization of our model. 

Create a file names `comparison-1b.sh` and paste in the following script. 

```bash
#!/usr/bin/env bash
set -euo pipefail

# Loop over OMP_NUM_THREADS: powers of 2 plus 96
for t in 2 4 8 16 32 64 96; do
  echo "==============================="
  echo "Running with OMP_NUM_THREADS=$t"
  echo "==============================="

  TORCHINDUCTOR_CPP_WRAPPER=1 \
  TORCHINDUCTOR_FREEZING=1 \
  OMP_NUM_THREADS="$t" \
  python transformers_llm_text_gen.py --model google/gemma-3-1b-it 2>&1 | \
  grep -E \
    "^(Prefill Tokens|Prefill time|E2E Generation time|Decoded Tokens|Decode time|Prefill Tokens per second|Decode Tokens per second):"
  
  echo    # blank line between runs
done
```

Likewise a separate script for comparing the 270m model 

```bash
#!/usr/bin/env bash
set -euo pipefail

# Loop over OMP_NUM_THREADS: powers of 2 plus 96
for t in 2 4 8 16 32 64 96; do
  echo "==============================="
  echo "Running with OMP_NUM_THREADS=$t"
  echo "==============================="

  TORCHINDUCTOR_CPP_WRAPPER=1 \
  TORCHINDUCTOR_FREEZING=1 \
  OMP_NUM_THREADS="$t" \
  python transformers_llm_text_gen.py --model google/gemma-3-270m-it 2>&1 | \
  grep -E \
    "^(Prefill Tokens|Prefill time|E2E Generation time|Decoded Tokens|Decode time|Prefill Tokens per second|Decode Tokens per second):"
  
  echo    # blank line between runs
done
```

Run both scripts from the directory containing the `transformers_llm_text_gen.py` script with the following commands. For clarity we are only printing the final statistics.

```bash
./comparison-1b.sh
./comparison-270m.sh
```

> Note: In a separate terminal session you can observe the realtime CPU utilization and the spawning on threads by running the following command.

```bash
watch -n 0.1 'pid=$(pgrep -n python); [ -n "$pid" ] && ps -L -p "$pid" -o pid,tid,psr,pcpu,stat,comm'
```

You should see the following output, which shows the CPU utilization of each thread and illustrates how new, inter-op, and intra-op threads are spawned over time.

```output
 PID     TID PSR %CPU STAT COMMAND
  10600   10600  31 85.3 Rl+  python
  10600   10606  32  2.4 Sl+  python
  10600   10607  33  2.4 Sl+  python
  10600   10608  34  2.4 Sl+  python
```

## Results

You should see the following output summarizing the statistics for each run as we sweep through the number of threads.

```out
===============================
Running with OMP_NUM_THREADS=2
===============================
Prefill Tokens: 55
Prefill time: 0.07 seconds
E2E Generation time: 1.50 seconds
Decoded Tokens: 65
Decode time: 1.44 seconds
Prefill Tokens per second: 834.48
Decode Tokens per second: 45.23

...

```

The graph above shows how prefill tokens per second change with the number of OpenMP threads for the 270M and 1B variants of Gemma-3. As expected, the smaller 270M model generally runs faster. Both models reach their optimal token generation rate at around 16–32 threads, though the 270M model exhibits a sharper performance drop-off beyond this range compared with the 1B variant.

![comparison](./Prefill%20Throughput%20vs%20OMP_NUM_THREADS%20(270M%20vs%201B).png)



## Using PyTorch Compilation Mode

So far, we have been running in PyTorch's eager execution mode, we can observe the performance characteristics with PyTorch's compile mode using the following. First install a C++ compiler and various dependencies.

```bash
sudo apt update && sudo apt install g++ python3.10-dev build-essential
```

First, we will run the `gemma-3-270m` model with the `--compile` flag without the default number of OpenMP threads.

```bash
TORCHINDUCTOR_CPP_WRAPPER=1 TORCHINDUCTOR_FREEZING=1 python transformers_llm_text_gen.py --comp
ile --model google/gemma-3-270m-it
```
```output
E2E Generation time: 6.15 seconds
Decoded Tokens: 65
Decode time: 5.74 seconds
Prefill Tokens per second: 133.52
Decode Tokens per second: 11.33
```

Now we can the the following command with `OMP_NUM_THREADS` set to 16.

```bash
TORCHINDUCTOR_CPP_WRAPPER=1 TORCHINDUCTOR_FREEZING=1 OMP_NUM_THREADS=16 python transformers_llm_text_gen.py --compile --model google/gemma-3-270m-it
```

As the output below shows, we see a huge reduction in the end-to-end generation time by reducing the number the thread count from 96 (default) to 16.

```output
E2E Generation time: 0.63 seconds
Decoded Tokens: 65
Decode time: 0.61 seconds
Prefill Tokens per second: 2728.34
Decode Tokens per second: 107.37
```

### Summary

In this learning path, we explored how the number of OpenMP threads is a tunable parameter that can significantly impact the performance of a large language model. This is especially important when running such models on Arm systems with high core counts. You should also take the model’s parameter size into account. In practice, using a heuristic or trial-and-error approach is often the fastest way to determine the optimal thread count for a given system.

