---
title: Understand the legacy x86 demo application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clone the demo repository

The demo application is a matrix multiplication benchmark written in C++ with AVX2 intrinsics. Clone it:

```bash
git clone https://github.com/JoeStech/docker-blog-arm-migration
cd docker-blog-arm-migration
```

## Examine the Dockerfile

Open the `Dockerfile`. There are two immediate blockers for Arm migration:

**No Arm64 support in the base image**: The `centos:6` image was built for x86 only. This container will not start on Arm hardware.

**x86-specific compiler flag**: The `-mavx2` flag tells the compiler to use AVX2 vector instructions, which do not exist on Arm processors.

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

Open `matrix_operations.cpp`. The code uses x86 AVX2 intrinsics throughout:

```cpp
#include <immintrin.h>  // x86-only header

// Inside the multiply function:
__m256d sum_vec = _mm256_setzero_pd();
__m256d a_vec = _mm256_loadu_pd(&data[i][k]);
sum_vec = _mm256_add_pd(sum_vec, _mm256_mul_pd(a_vec, b_vec));

// Horizontal reduction
__m128d sum_high = _mm256_extractf128_pd(sum_vec, 1);
__m128d sum_low = _mm256_castpd256_pd128(sum_vec);
```

## Why this code cannot run on Arm

There are several specific blockers:

1. **x86-exclusive header**: `#include <immintrin.h>` only exists on x86 systems. Arm uses `<arm_neon.h>` instead.

2. **AVX2 intrinsics throughout**: Every `_mm256_*` function is Intel-specific:
   - `_mm256_setzero_pd()` creates a 256-bit zero vector (Arm NEON is 128-bit).
   - `_mm256_loadu_pd()` loads 4 doubles at once (NEON loads 2 with `vld1q_f64`).
   - `_mm256_add_pd()` and `_mm256_mul_pd()` are 256-bit operations (NEON uses 128-bit equivalents).
   - `_mm256_extractf128_pd()` extracts the high 128 bits (not needed on NEON).

3. **Vector width mismatch**: AVX2 processes 4 doubles per operation. Arm NEON processes 2 doubles per operation. The entire loop structure needs adjustment.

{{% notice Note %}}
SVE/SVE2 on newer Arm cores (Neoverse V1/V2, Graviton 3/4) provides 256-bit or wider vector-length agnostic (VLA) registers, matching or exceeding AVX2 width. The Arm MCP Server knowledge base can help determine the best approach for your target hardware.
{{% /notice %}}

4. **Horizontal reduction logic**: The pattern using `_mm256_extractf128_pd` and `_mm256_castpd256_pd128` is x86-specific and must be completely rewritten.

Manual conversion requires rewriting 30+ lines of intrinsic code, adjusting loop strides, and testing numerical accuracy. This is exactly where the Docker MCP Toolkit with the Arm MCP Server becomes essential.

In the next section, you will use GitHub Copilot with the Docker MCP Toolkit to automate the entire migration.
