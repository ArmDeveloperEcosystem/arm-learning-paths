---
title: Run QuantLib benchmark workloads
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Run a baseline benchmark

After building QuantLib, move to the test suite directory:

```bash
cd ~/QuantLib-$QL_VER/test-suite
```

From the test suite directory, run a baseline benchmark:

```bash
./quantlib-benchmark
```

This confirms that the benchmark is working correctly on your system.

## Vary thread count

To understand how performance scales, run benchmarks with different numbers of threads:

```bash
./quantlib-benchmark --size=80 --nProc=1
./quantlib-benchmark --size=80 --nProc=2
./quantlib-benchmark --size=80 --nProc=4
```

These runs keep the workload size constant while changing the number of threads.

## Vary workload size

Next, vary the problem size while keeping the thread count fixed:

```bash
./quantlib-benchmark --size=1 --nProc=1
./quantlib-benchmark --size=5 --nProc=1
./quantlib-benchmark --size=8 --nProc=1
```

This shows how runtime changes as the workload increases.

## Choose appropriate thread counts

The Standard_D4ps_v5 virtual machine has a limited number of cores.

Start with:

* 1 thread
* 2 threads
* 4 threads

Using larger values can oversubscribe the system and lead to inconsistent results.

Your notes include larger values such as 12, 24, and 48 threads, but these are better suited for larger machines.

## Keep benchmark runs controlled

For meaningful comparisons:

* change one parameter at a time
* keep the environment consistent
* repeat runs if results vary

This helps ensure that differences in runtime reflect real performance changes.

## What you’ve accomplished and what’s next

You have successfully run QuantLib benchmarks and explored how performance changes with workload size and thread count.

In the next section, you will record and analyze the results.