---
title: Understand the legacy x86 demo application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clone the demo repository

The demo application is a matrix multiplication benchmark written in C++ using AVX2 intrinsics for vectorized performance on x86 processors. 
Clone the repository:
```bash
git clone https://github.com/JoeStech/docker-blog-arm-migration
cd docker-blog-arm-migration
```
This example is intentionally optimized for x86 so that you can see how architecture-specific code appears in practice and how it can be adapted for Arm.

## Examine the Dockerfile

Open the `Dockerfile`. There are two areas that require updates for Arm compatibility.

**Add Arm64 support in the base image**: The centos:6 image was published for x86 architecture and does not provide a `linux/arm64` variant. To run on Arm hardware, the base image must support Arm64.

Modern multi-architecture base images typically publish both `linux/amd64` and `linux/arm64` manifests. Updating the base image is the first step toward portability.

**Update compiler flags**: The `-mavx2` flag enables AVX2 vector instructions on x86. Arm processors use different SIMD instruction sets (NEON or SVE), so this flag must be removed or replaced when compiling for Arm.

Here is the full Dockerfile for reference:
```dockerfile
FROM centos:6

RUN yum install -y \
    devtoolset-2-gcc \
    devtoolset-2-gcc-c++ \
    devtoolset-2-binutils \
    make \
    && yum clean all

WORKDIR /app
COPY *.h *.cpp ./

RUN scl enable devtoolset-2 "g++ -O2 -mavx2 -o benchmark \
    main.cpp \
    matrix_operations.cpp \
    -std=c++11"

CMD ["./benchmark"]
```

## Examine the source code
Open `matrix_operations.cpp`. At the top of the file:

```cpp
#include <immintrin.h>  // x86-only header
```
The <immintrin.h> header provides Intel SIMD intrinsics, including AVX and AVX2. On Arm systems, SIMD intrinsics are provided through <arm_neon.h> instead.

Inside the matrix multiplication routine, you will see AVX2 intrinsics such as:
```cpp
// Inside the multiply function:
__m256d sum_vec = _mm256_setzero_pd();
__m256d a_vec = _mm256_loadu_pd(&data[i][k]);
sum_vec = _mm256_add_pd(sum_vec, _mm256_mul_pd(a_vec, b_vec));

// Horizontal reduction
__m128d sum_high = _mm256_extractf128_pd(sum_vec, 1);
__m128d sum_low = _mm256_castpd256_pd128(sum_vec);
```
These _mm256_* functions map directly to 256-bit AVX2 instructions.

## Architecture considerations for Arm

To run this code on Arm, several adjustments are required:

1. **SIMD header replacement**: x86 uses `#include <immintrin.h>`. Arm uses `<arm_neon.h>` instead.

2. **Intrinsic mapping**: Each AVX2 intrinsic must be mapped to an Arm equivalent.
   For example:
   - `_mm256_setzero_pd()` creates a 256-bit zero vector of four doubles. Arm NEON uses 128-bit registers.
   - `_mm256_loadu_pd()` loads 4 doubles at once (NEON loads 2 with `vld1q_f64`).
   - `_mm256_add_pd()` and `_mm256_mul_pd()` are 256-bit operations (NEON uses 128-bit equivalents).
   - `_mm256_extractf128_pd()` extracts the high 128 bits (not needed on NEON).

3. **Vector width differences**: AVX2 operates on 256-bit registers (four double-precision values). NEON operates on 128-bit registers (two double-precision values). This affects:
   - Loop stride
   - Accumulation logic
   - Horizontal reduction patterns

4. **Horizontal reduction logic**: The AVX2 pattern:

```cpp
   _mm256_extractf128_pd(...)
  _mm256_castpd256_pd128(...)
```
is specific to x86 register structure. On Arm, reduction is implemented using NEON reduction or pairwise-add instructions instead.

{{% notice Note %}}
On newer Arm platforms supporting SVE or SVE2 (for example Neoverse V1/V2 based platforms), wider vector lengths may be available. SVE uses a vector-length-agnostic (VLA) model, which differs from fixed-width AVX2 and NEON programming. The Arm MCP Server knowledge base can help determine the appropriate approach for your target platform.
{{% /notice %}}

## What you've accomplished and what's next

You have:
- Examined a legacy x86 application with AVX2 intrinsics
- Identified the architecture-specific elements: base image, compiler flags, SIMD headers, and intrinsic functions
- Understood how vector width differences between AVX2 (256-bit) and NEON (128-bit) affect the migration approach

Next, you'll use GitHub Copilot with the Docker MCP Toolkit to automate the migration process.
