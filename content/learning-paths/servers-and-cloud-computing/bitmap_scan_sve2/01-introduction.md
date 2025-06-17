---
# User change
title: "Optimize bitmap scanning in databases with SVE and NEON on Arm servers"

weight: 2

layout: "learningpathall"
---
## Overview

Bitmap scanning is a core operation in many database systems. It's essential for powering fast filtering in bitmap indexes, Bloom filters, and column filters. However, these scans can become performance bottlenecks in complex analytical queries.

In this Learning Path, you’ll learn how to accelerate bitmap scanning using Arm’s vector processing technologies - NEON and SVE - on Neoverse V2–based servers like AWS Graviton4. 

Specifically, you will:

* Explore how to use SVE instructions on Arm Neoverse V2–based servers like AWS Graviton4 to optimize bitmap scanning
* Compare scalar, NEON, and SVE implementations to demonstrate the performance benefits of specialized vector instructions

## What is bitmap scanning in databases?

Bitmap scanning involves searching through a bit vector to find positions where bits are set (`1`) or unset (`0`). 

In database systems, bitmaps are commonly used to represent:

* **Bitmap indexes**: each bit represents whether a row satisfies a particular condition
* **Bloom filters**: probabilistic data structures used to test set membership
* **Column filters**: bit vectors indicating which rows match certain predicates

The operation of scanning a bitmap to find set bits is often in the critical path of query execution, making it a prime candidate for optimization.

## The evolution of vector processing for bitmap scanning

Here's how vector processing has evolved to improve bitmap scanning performance:

* **Generic scalar processing**: traditional bit-by-bit processing with conditional branches
* **Optimized scalar processing**: byte-level skipping to avoid processing empty bytes
* **NEON**: fixed-width 128-bit SIMD processing with vector operations
* **SVE**: scalable vector processing with predication and specialized instructions like MATCH 

## Set up your Arm development environment

To follow this Learning Path, you will need:

* An AWS Graviton4 instance running `Ubuntu 24.04`. 
* A GCC compiler with SVE support

First, install the required development tools:

```bash
sudo apt-get update
sudo apt-get install -y build-essential gcc g++
```
{{% notice Tip %}}
An effective way to achieve optimal performance on Arm is not only through optimal flag usage, but also by using the most recent compiler version. For best performance, use the latest available GCC version with SVE support. This Learning Path was tested with GCC 13, the default on Ubuntu 24.04. Newer versions should also work.
{{% /notice %}}


Create a directory for your implementations:
```bash
mkdir -p bitmap_scan
cd bitmap_scan
```

## Next up: build the bitmap scanning foundation
With your development environment set up, you're ready to dive into the core of bitmap scanning. In the next section, you’ll define a minimal bitmap data structure and implement utility functions to set, clear, and inspect individual bits.