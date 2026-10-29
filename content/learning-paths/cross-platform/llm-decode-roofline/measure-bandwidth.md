---
title: Measure the memory bandwidth ceiling
description: Prepare an idle Arm Linux system and use llama-roofline membw to measure its sustained memory-read bandwidth, the ceiling that llama.cpp decode runs into.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the system for measurement

After setting up llama-roofline and downloading three models, you're ready to measure memory bandwidth.

Background load lowers measured bandwidth and makes every result that depends on it wrong. 

Before you measure bandwidth, complete the following steps:

1. Close other applications and stop any running benchmarks.
2. Check that the board is idle and has free memory:

    ```bash
    uptime
    free -m
    ```

    The load average should be close to zero. Ensure that the `available` column is larger than the largest model file that you'll run. The largest file is 1,066 MB.

3. On a Raspberry Pi 5, check that the board isn't throttling:

    ```bash
    vcgencmd measure_temp
    vcgencmd get_throttled
    ```

    Ensure that the output of `get_throttled` is `throttled=0x0`. If it isn't, fit the active cooler and wait for the board to cool down.

4. Check the CPU frequency governor:

    ```bash
    cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
    ```

    The outputs were measured with the `ondemand` governor, the Raspberry Pi OS default. Record the governor with your results, because changing it changes the results.

## Measure the sustained read bandwidth

Run the bandwidth measurement on its own:

```bash
llama-roofline membw
```

The tool runs read-only kernels (`sum`, `max` and `dot`) at several thread counts over a working set much larger than the caches. It repeats each one and reports the best sustained read rate as the ceiling. 

The tool also prints a `copy` kernel for reference. However, it doesn't use the kernel for the ceiling because a copy writes as well as reads.

The output is similar to:

```output
machine: Raspberry Pi 5 Model B Rev 1.0 (4 logical cores, 2.1 GB RAM)
    1 threads   sum   13.7   max   13.8   dot   12.2   copy   10.3  GB/s
    2 threads   sum   12.7   max   12.6   dot   11.4   copy    8.7  GB/s
    4 threads   sum   10.5   max   10.7   dot    8.8   copy    6.5  GB/s

sustained read ceiling: 13.78 GB/s (max kernel @ 1 threads, 263 MB working set)
this is a measured lower bound on true peak; pass it to `run` with --peak-bw 13.78
wrote /home/manu/lp_capture/20261003_2358/membw_1.json
```

One thread already reaches the highest read rate. Adding threads lowers it. This is the first sign that decode, which streams the weights from memory, doesn't need all four cores.

{{% notice Note %}}
The ceiling is a measured lower bound on the true peak. llama.cpp hand-written kernels can stream faster than the Python kernels that the tool uses. If decode exceeds the measured ceiling, llama-roofline warns you and treats the percentages as lower bounds.

If you already have a trusted STREAM result for your system, pass it with `--peak-bw` to skip this step.
{{% /notice %}}

## Check that the measurement is repeatable

Run `llama-roofline membw` two more times and compare the `sustained read ceiling` lines. On an idle board, the values agree closely. On the Raspberry Pi 5, the three runs reported 13.78, 13.78 and 13.77 GB/s.

If your runs differ by more than 5 percent, something else is using memory bandwidth. Find and stop it before you continue, because you'll compare every later result with this ceiling.

## What you've accomplished and what's next

You've measured how many bytes per second your Arm system can read from DRAM. This is the roof that decode runs into. 

Next, you'll measure decode and prefill, and compare them with this ceiling.
