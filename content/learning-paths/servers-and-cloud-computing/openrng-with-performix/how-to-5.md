---
title: Measure performance improvements with a microbenchmark
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the microbenchmark sweep

The microbenchmark in `tests/sweep-microbenchmark.cpp` isolates the `generateDistribution` function and times it across eight input sizes, from 2^8 to 2^15 elements (256 to 32,768 points). Each run generates the sum of two distributions and records the elapsed time in microseconds using a scoped timer. Running both the baseline build, using the `std::mt19937` class from the standard library, and the accelerated build using OpenRNG across this range lets you see how the speedup from OpenRNG scales with data size.

Run the microbenchmark sweep to compare baseline versus accelerated generation across input sizes:

```bash
make clean
cmake -S . -B build-baseline -DBUILD_TESTS=ON
cmake -S . -B build-apl -DBUILD_TESTS=ON -DUSE_APL=ON

cmake --build build-baseline --target sweep_microbench_baseline
cmake --build build-apl --target sweep_microbench_with_apl
```

Run the baseline benchmark first:

```bash
./build-baseline/tests/sweep_microbench_baseline
```

The output shows elapsed time in microseconds for each input size:

```output
Generating Distribution of size 256 = 174 us
Generating Distribution of size 512 = 280 us
Generating Distribution of size 1024 = 554 us
Generating Distribution of size 2048 = 1117 us
Generating Distribution of size 4096 = 2231 us
Generating Distribution of size 8192 = 4429 us
Generating Distribution of size 16384 = 8908 us
Generating Distribution of size 32768 = 17818 us
```

Then run the accelerated benchmark:

```bash
./build-apl/tests/sweep_microbench_with_apl
```

The output shows the accelerated times across the same input sizes:

```output
Generating Distribution of size 256 = 58 us
Generating Distribution of size 512 = 59 us
Generating Distribution of size 1024 = 102 us
Generating Distribution of size 2048 = 186 us
Generating Distribution of size 4096 = 370 us
Generating Distribution of size 8192 = 709 us
Generating Distribution of size 16384 = 1431 us
Generating Distribution of size 32768 = 2785 us
```

The observed speedup of the `generateDistribution` function varies with distribution size, showing smaller gains at lower data sizes and larger gains as size grows, which indicates when Arm Performance Libraries are likely to provide meaningful performance improvements for a given application.

## What you've accomplished

You completed a full profile-first optimization workflow on Arm. Starting from a baseline C++ workload, you used Arm Performix Code Hotspots to find the highest-cost function, then replaced it with OpenRNG and Arm Performance Libraries. The microbenchmark confirmed that the speedup scales with data size, giving you a repeatable method for identifying and targeting bottlenecks in your Arm workloads.
