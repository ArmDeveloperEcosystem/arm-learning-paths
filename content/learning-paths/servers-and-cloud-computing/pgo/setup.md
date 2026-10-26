---
title: Prepare your AArch64 environment and verify LLVM tool availability
description: Prepare an AArch64 Linux environment, download the example C++ source, and verify the LLVM tools required for LTO and PGO workflows.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your environment

On your AArch64 Linux machine, create a working directory and enter it:

```bash
mkdir pgo-example
cd pgo-example
```

Download the `bsort.cpp` source file from the Arm Learning Paths repository:

```bash
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/bolt/bsort.cpp
```

Create directories for the generated files:

```bash
mkdir -p out prof
```

The `out` directory stores object files and binaries. The `prof` directory stores raw and converted profile data.

If LLVM isn't already installed, follow the [LLVM toolchain for Linux on Arm](/install-guides/llvm/) install guide before continuing.


## Verify LLVM tool availability

Confirm that the machine uses the AArch64 architecture:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

Check that the required LLVM tools are available:

```bash { line_numbers=true }
clang++ --version
ld.lld --version
llvm-bcanalyzer --version
llvm-profdata --version
llvm-profgen --version
llvm-readelf --version
```

For sample-based profile-guided optimization (S-PGO), also check that `perf` is available:

```bash
perf --version
uname -r
```
The S-PGO workflow uses the Arm Branch Record Buffer Extension (BRBE) and needs Linux kernel 6.17 or later.

The version commands confirm that the programs are in your `PATH`. They don't confirm that the processor implements BRBE or that you have permission to access performance events. The profile collection step checks those requirements when it runs `perf record`.

## What you've accomplished and what's next

You've created the working directory, downloaded the example source, and verified that the required tools are available.

Next, you'll build the example with Thin-LTO and Full-LTO.
