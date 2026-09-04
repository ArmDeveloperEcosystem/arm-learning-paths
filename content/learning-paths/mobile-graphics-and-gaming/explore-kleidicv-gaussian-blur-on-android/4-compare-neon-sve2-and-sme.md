---
title: Compare NEON, SVE2, and SME performance
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a comparison matrix

The following commands run 3000 measurements for 5x5, 7x7, 9x9, and 15x15
Gaussian blur on CPUs 0, 4, and 7. The masks `1`, `10`, and `80` select those
individual CPUs on the test device; replace them with masks appropriate for
your device.

```bash
for cpu_mask in 1 10 80; do
  for kernel in 5 7 9 15; do
    adb shell "taskset $cpu_mask /data/local/tmp/gaussian_blur_benchmark \
      --kernel $kernel --iterations 3000"
  done
done
```

Use p50 as the primary comparison metric. It is the median of all measured
calls, so it better represents typical per-call time than the mean when
interrupts or frequency changes create occasional long calls.

## Results from an SME-capable device

The table shows NEON p50 divided by SME p50. A value above 1.00x means SME is
faster. Each result is from one process with a fixed CPU affinity and 3000
measured calls.

| Kernel | CPU | 640x640 | 1920x1080 | 3840x2160 |
|---|---:|---:|---:|---:|
| 5x5 | 0 | 0.65x | 1.55x | 1.27x |
| 5x5 | 4 | 0.49x | 0.88x | 1.12x |
| 5x5 | 7 | 0.66x | 1.66x | 1.76x |
| 7x7 | 0 | 1.78x | 1.67x | 2.44x |
| 7x7 | 4 | 1.28x | 2.05x | 1.52x |
| 7x7 | 7 | 1.15x | 2.03x | 2.09x |
| 9x9 | 0 | 2.52x | 2.87x | 2.64x |
| 9x9 | 4 | 1.76x | 1.83x | 1.85x |
| 9x9 | 7 | 1.31x | 1.97x | 2.05x |
| 15x15 | 0 | 1.21x | 1.91x | 1.68x |
| 15x15 | 4 | 1.29x | 1.14x | 1.13x |
| 15x15 | 7 | 1.45x | 1.74x | 2.01x |

## Explain the performance behavior

The 5x5 blur has inconsistent SME benefit. At 640x640, SME is slower on all
three tested CPUs. The smaller workload does not sufficiently amortize
streaming-mode setup, loop overhead, border processing, and intermediate
buffer management.

The 7x7, 9x9, and 15x15 kernels perform more work per pixel. This increases
arithmetic intensity and lets the wider streaming-SVE vectors contribute more
of the total execution time. The highest measured speedup is 2.87x for the
9x9 kernel at 1920x1080 on CPU 0.

The 15x15 results show an SME speedup for every tested CPU and resolution,
ranging from 1.13x to 2.01x. Unlike the 3x3 through 9x9 fixed kernels, the
15x15 implementation does not use a binomial variant. Its largest measured
benefit is at 3840x2160 on CPU 7, where SME is 2.01x faster than NEON.

This does not imply a fixed speedup for every device or image. The separable
filter writes and reads an intermediate `uint16_t` buffer, so cache capacity,
memory bandwidth, streaming vector length, frequency scaling, and thermal
state all affect the result. Do not compare absolute times across CPU clusters.
Compare NEON and SME within the same process, CPU affinity, kernel, and device
state. For more confidence, run several independent processes and take the
median of their p50 values.

## What you have learned

You built a standalone KleidiCV Gaussian blur example, measured explicit NEON,
SVE2, and SME implementations, and used CPU affinity to make comparisons more
repeatable. You also saw that a larger kernel can expose more of the benefit
of SME on an Arm-based Android device.
