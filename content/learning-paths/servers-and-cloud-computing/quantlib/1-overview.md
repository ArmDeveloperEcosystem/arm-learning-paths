---
title: Understand the QuantLib benchmark workflow on Azure Cobalt
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is QuantLib?

QuantLib is an open-source C++ library for quantitative finance. It provides tools for pricing, modeling, trading, and risk management, and is widely used as both a development library and a representative financial computing workload.

Because QuantLib is a substantial C++ codebase with realistic compute behavior, it is also useful as a benchmark when evaluating cloud systems and processor architectures. In this Learning Path, you'll build QuantLib from source and run its benchmark executable on an Arm-based Azure Cobalt virtual machine.

## Why use Azure Cobalt?

Azure Cobalt provides Arm64 virtual machines for cloud-native development and performance evaluation. Running QuantLib on Azure Cobalt gives you a practical way to measure how a real C++ finance workload behaves on Arm-based cloud infrastructure.

You'll use:

- Ubuntu Server 22.04 LTS (this Learning Path is also tested on 24.04 LTS)
- an Arm64 Azure Cobalt virtual machine
- a source build of QuantLib
- QuantLib's benchmark executable for repeatable performance testing

## Benchmark workflow

The steps follow a practical benchmark flow:

1. Create and connect to an Arm64 Azure Cobalt virtual machine
2. Install the tools needed to build QuantLib
3. Download and compile QuantLib from source
4. Run benchmark workloads with different problem sizes and thread counts
5. Compare and record results

{{% notice Note %}}
The steps in this Learning Path aren't a general introduction to quantitative finance or QuantLib development.
{{% /notice %}}

## What the benchmark tests

The benchmark executable runs approximately 85 tests drawn directly from QuantLib's own test suite, covering five domains:

- Equity and FX: American and European option pricing, Heston and Bates model calibration, convertible bonds, Andreasen-Huge volatility interpolation
- Interest rates: Short rate models, Bermudan swaptions, Libor market model, piecewise yield curves, overnight indexed swaps, Markov functional models, SABR and ZABR volatility
- Credit derivatives: Nth-to-default pricing and credit default swap calibration
- Energy: Swing options and virtual power plant pricing
- Math: Gaussian quadratures, low-discrepancy sequences, statistics, and special functions

Each test has a fixed iteration count built in. Some run once per task, others run hundreds or thousands of times to produce a measurable signal. The `--size` argument multiplies the entire set: `--size=2` runs each test twice, `--size=5` runs it five times, and so on. Doubling `--size` doubles runtime while leaving throughput unchanged — this is the expected weak scaling behavior of the benchmark.

The `--nProc` argument controls the number of worker processes. Because QuantLib is not thread-safe, the benchmark uses separate processes rather than threads, coordinated through Boost IPC. Before timing begins, the benchmark runs every test once through the Boost unit test framework to verify correctness. The tests produce the `*** No errors detected` line in the output.

System Throughput is calculated as `(size × number_of_tests) / total_runtime`. It is the primary metric for comparing runs across thread counts and system configurations.

## Benchmarking goals

When benchmarking a workload such as QuantLib, the goal is not just to obtain one runtime number. You want a repeatable process that lets you compare runs across system sizes, thread counts, software versions, and compiler settings.

For that reason, this Learning Path emphasizes:

- using a known VM configuration
- keeping the software environment consistent
- changing one benchmark variable at a time
- recording commands and results so runs can be reproduced later

## What you've learned and what's next

You've now learned about QuantLib and why you'll be using Azure Cobalt in this Learning Path. You've also learned how the benchmark works and the intent behind benchmarking a workload such as QuantLib.

Next, you'll set up your Azure Cobalt environment. 