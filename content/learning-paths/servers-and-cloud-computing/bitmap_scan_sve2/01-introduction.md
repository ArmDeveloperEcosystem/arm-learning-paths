---
# User change
title: "Bitmap Scanning and Vectorization on Arm"

weight: 2

layout: "learningpathall"
---
## Introduction

Bitmap scanning is a fundamental operation in database systems, particularly for analytical workloads. It's used in bitmap indexes, bloom filters, and column filtering operations. The performance of bitmap scanning can significantly affect query execution times, especially for large datasets.

In this Learning Path, you will explore how to use SVE instructions available on Arm Neoverse V2 based servers like AWS Graviton4 to optimize bitmap scanning operations. You will compare the performance of scalar, NEON, and SVE implementations to demonstrate the significant performance benefits of using specialized vector instructions.

## What is Bitmap Scanning?

Bitmap scanning involves searching through a bit vector to find positions where bits are set (1) or unset (0). In database systems, bitmaps are commonly used to represent:

1. **Bitmap Indexes**: Each bit represents whether a row satisfies a particular condition
2. **Bloom Filters**: Probabilistic data structures used to test set membership
3. **Column Filters**: Bit vectors indicating which rows match certain predicates

The operation of scanning a bitmap to find set bits is often in the critical path of query execution, making it a prime candidate for optimization.

## The Evolution of Vector Processing for Bitmap Scanning

Let's look at how vector processing has evolved for bitmap scanning:

1. **Generic Scalar Processing**: Traditional bit-by-bit processing with conditional branches
2. **Optimized Scalar Processing**: Byte-level skipping to avoid processing empty bytes
3. **NEON**: Fixed-length 128-bit SIMD processing with vector operations
4. **SVE**: Scalable vector processing with predication and specialized instructions

## Set up your environment

To follow this learning path, you will need:

1. An AWS Graviton4 instance running `Ubuntu 24.04`. 
2. GCC compiler with SVE support

Let's start by setting up our environment:

```bash
sudo apt-get update
sudo apt-get install -y build-essential gcc g++
```
An effective way to achieve optimal performance on Arm is not only through optimal flag usage, but also by using the most recent compiler version. This Learning path was tested with GCC 13 which is the default version on `Ubuntu 24.04` but you can run it with newer versions of GCC as well. 

Create a directory for your implementations:
```bash
mkdir -p bitmap_scan
cd bitmap_scan
```
## Next Steps
In the next section, you’ll define the core bitmap data structure and utility functions for setting, clearing, and inspecting bits.
