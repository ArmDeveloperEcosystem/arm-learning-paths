---
title: Summarize the project with a README.md file
weight: 10 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Can I Summarize the Project Results?

You can use GitHub Copilot to generate a project summary in a README file. 

Use the prompt below to collaborate with GitHub Copilot Agent to generate your README. 

Review and refine the results to align them with your project's goals.

```console
Review the files in my project.
Create a README.md file that describes the background and overview of the project. 
Explain the two implementations of the adler32 checksum. 
Add a note that the performance results recorded on the Neoverse N1 processor. 
Use a table to compare the original version and the NEON version and show the performance improvement factor.
```

Below is the created README.md file. The formatting doesn't match the Learning Path template exactly, but you can copy the README file to a new repository in GitHub for improved results. 

## Adler-32 Checksum Implementation Comparison

### Background

The Adler-32 checksum is an algorithm invented by Mark Adler, used in the zlib compression library and specified in RFC 1950. It provides a fast way to calculate a checksum for data integrity verification, balancing speed and reliability. It generates a 32-bit integer value based on the input data.

### Overview

This project provides and compares two implementations of the Adler-32 checksum algorithm:

1.  A simple, standard C implementation.
2.  An optimized implementation using ARM NEON SIMD instructions.

The goal is to demonstrate the performance benefits of using NEON intrinsics for this type of computation on compatible ARM architectures, such as the Neoverse N1.

The project includes:
*   Source code for both implementations (`adler32-simple.c`, `adler32-neon.c`).
*   Header files (`adler32-simple.h`, `adler32-neon.h`).
*   A test and benchmark program (`adler32-test.c`) to verify correctness and measure performance.
*   A `Makefile` for easy compilation and testing.

### Implementations

#### 1. Simple Implementation

The code in `adler32-simple.c` is a straightforward C implementation following the standard Adler-32 algorithm definition. It processes the input data byte by byte, updating two 16-bit accumulators (`a` and `b`) modulo 65521 (the largest prime smaller than 2^16).

#### 2. NEON-Optimized Implementation

The code in `adler32-neon.c` leverages ARM NEON SIMD (Single Instruction, Multiple Data) instructions to accelerate the checksum calculation. Key aspects include:
*   Processing data in blocks (16 bytes at a time).
*   Using NEON intrinsics (`vld1q_u8`, `vmovl_u8`, `vaddq_u16`, `vpaddlq_u16`, `vmulq_u16`, etc.) to perform parallel operations on data vectors.
*   Calculating the sums `S1` (sum of bytes) and `S2` (weighted sum) for each block using vector operations.
*   Updating the scalar `a` and `b` accumulators based on the block results.
*   Falling back to the standard implementation for data lengths smaller than the block size or for the remaining bytes after processing full blocks.

### Performance

The performance of both implementations was measured on an **AWS Graviton2 processor (based on Arm Neoverse N1 cores)**. The benchmark program (`adler32-test`) calculates the checksum for various data sizes and measures the time taken and throughput (in MB/s).

The following table summarizes the throughput results and the performance improvement factor of the NEON version compared to the simple version:

| Data Size | Simple Throughput (MB/s) | NEON Throughput (MB/s) | Speedup Factor |
| :-------- | :----------------------- | :--------------------- | :------------- |
| 1 KB      | 244.14                   | 976.56                 | 4.00x          |
| 10 KB     | 295.93                   | 3255.21                | 11.00x         |
| 100 KB    | 298.64                   | 3150.20                | 10.55x         |
| 1 MB      | 298.33                   | 3215.43                | 10.78x         |
| 10 MB     | 298.37                   | 3194.89                | 10.71x         |

**Note:** Performance results can vary based on the specific hardware, compiler, and system load. The results above demonstrate a significant performance improvement (around **10-11x** for larger data sizes) when using NEON optimization on the Neoverse N1 architecture.

### Building and Running

Use the provided `Makefile`:

```bash
# Compile the code
make

# Run verification and performance tests
make run

# Clean up generated files
make clean
```

The table summarizes the speedup obtained by the NEON version. 

Using Agent mode in GitHub Copilot is a significant benefit when you are actively building and running software. Agent mode can create files and modify them to make needed improvements. 

### Tips for Using GitHub Copilot Effectively

This project was completed using GitHub Copilot Agent without modifying the generated files. While that might not be practical in every case, the demonstration shows how NEON intrinsics can significantly boost performance. 

GitHub Copilot is especially useful for:
* Generating vectorized versions of scalar code.
* Writing and adapting NEON intrinsics.
* Identifying and fixing bugs in complex low-level code, even for developers who aren’t SIMD experts.

Make sure to try different LLMs with Copilot as the results will vary greatly depending on the model.


