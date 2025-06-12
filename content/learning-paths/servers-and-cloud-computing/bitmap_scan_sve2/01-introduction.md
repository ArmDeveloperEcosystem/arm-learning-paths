---
# User change
title: "Optimizing Bitmap Scanning with SVE and NEON on Arm Servers"

weight: 2

layout: "learningpathall"
---
## Introduction

Bitmap scanning is a fundamental operation in database systems, particularly for analytical workloads. It's used in bitmap indexes, bloom filters, and column filtering operations. The performance of bitmap scanning can significantly affect query execution times, especially for large datasets.

In this Learning Path, you will:

* Explore how to use SVE instructions on Arm Neoverse V2–based servers like AWS Graviton4 to optimize bitmap scanning
* Compare scalar, NEON, and SVE implementations to demonstrate the performance benefits of specialized vector instructions

## What is bitmap scanning?

Bitmap scanning involves searching through a bit vector to find positions where bits are set (1) or unset (0). In database systems, bitmaps are commonly used to represent:

* **Bitmap Indexes**: each bit represents whether a row satisfies a particular condition
* **Bloom Filters**: probabilistic data structures used to test set membership
* **Column Filters**: bit vectors indicating which rows match certain predicates

The operation of scanning a bitmap to find set bits is often in the critical path of query execution, making it a prime candidate for optimization.

## The evolution of vector processing for bitmap scanning

Here's how vector processing has evolved to improve bitmap scanning performance:

* **Generic Scalar Processing**: traditional bit-by-bit processing with conditional branches
* **Optimized Scalar Processing**: byte-level skipping to avoid processing empty bytes
* **NEON**: fixed-length 128-bit SIMD processing with vector operations
* **SVE**: scalable vector processing with predication and specialized instructions like MATCH 

## Set up your environment

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
## Next Steps
In the next section, you’ll define the core bitmap data structure and utility functions for setting, clearing, and inspecting bits.
