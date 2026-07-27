---
title: Prepare your environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your environment

On your AArch64 Linux machine, navigate to your home directory or another empty working directory and download the `bsort.cpp` source file:

```bash
wget https://learn.arm.com/learning-paths/servers-and-cloud-computing/bolt-demo/bsort.cpp
```

Create the following directories to organize generated files from this example:

```bash
mkdir -p out prof
```

- **out**: Stores output binaries
- **prof**: Stores profile data

If LLVM is not already installed, follow the [LLVM toolchain for Linux on Arm](/install-guides/llvm/) install guide before continuing.


## Verify tool availability

Check that the LLVM tools are available:

```bash { line_numbers=true }
clang++ --version
ld.lld --version
llvm-profdata --version
llvm-profgen --version
```

For S-PGO, also check that perf is available. The BRBE-based S-PGO workflow in this guide requires a perf binary from Linux kernel 6.17.

```bash
perf --version
```

## What you've learned and what's next

You've created the working directory, verified that the LLVM tools are available, and downloaded the example source.

Next, you'll build the example with Thin-LTO and Full-LTO.
