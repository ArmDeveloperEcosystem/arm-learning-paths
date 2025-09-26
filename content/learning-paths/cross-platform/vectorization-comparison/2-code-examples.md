---
title: "Vector extension code examples"
weight: 4

# FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## SAXPY example code

This page walks you through a SAXPY (Single-Precision A·X Plus Y) kernel implemented in plain C and with vector extensions on both Arm (NEON, SVE) and x86 (AVX2, AVX-512). You will see how to build and run each version and how the vector width affects throughput.

SAXPY computes `y[i] = a * x[i] + y[i]` across arrays `x` and `y`. It is widely used in numerical computing and is an accessible way to compare SIMD behavior across ISAs.

{{% notice Tip %}}
If a library already provides a tuned SAXPY (for example, BLAS), prefer that over hand-written kernels. These examples are for learning and porting.
{{% /notice %}}


### Reference C version (no SIMD intrinsics)

Below is a plain C implementation of SAXPY without any vector extensions which serves as a reference baseline for the optimized examples provided later:

```c
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

void saxpy(float a, const float *x, float *y, size_t n) {
    for (size_t i = 0; i < n; ++i) {
        y[i] = a * x[i] + y[i];
    }
}

int main() {
    size_t n = 1000;
    float* x = malloc(n * sizeof(float));
    float* y = malloc(n * sizeof(float));
    float a = 2.5f;

    for (size_t i = 0; i < n; ++i) {
        x[i] = (float)i;
        y[i] = (float)(n - i);
    }

    saxpy(a, x, y, n);

    float sum = 0.0f;
    for (size_t i = 0; i < n; ++i) {
        sum += y[i];
    }
    printf("Plain C SAXPY sum: %f\n", sum);

    free(x);
    free(y);
    return 0;
}
```

Use a text editor to copy the code to a file `saxpy_plain.c` and build and run the code using:

```bash
gcc -O3 -o saxpy_plain saxpy_plain.c
./saxpy_plain
```

You can use Clang for any of the examples by replacing `gcc` with `clang` on the command line.

## Arm NEON version (128-bit SIMD, 4 floats per operation)

NEON uses fixed 128-bit registers, processing four `float` values per instruction. It is available on most Armv8-A devices and is excellent for accelerating loops and signal processing tasks in mobile and embedded workloads.

The example below processes 16 floats per iteration using four separate NEON operations to improve instruction-level parallelism and reduce loop overhead:

```c
#include <arm_neon.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

void saxpy_neon(float a, const float *x, float *y, size_t n) {
    size_t i = 0;
    float32x4_t va = vdupq_n_f32(a);
    for (; i + 16 <= n; i += 16) {
        float32x4_t x0 = vld1q_f32(x + i);
        float32x4_t y0 = vld1q_f32(y + i);
        float32x4_t x1 = vld1q_f32(x + i + 4);
        float32x4_t y1 = vld1q_f32(y + i + 4);
        float32x4_t x2 = vld1q_f32(x + i + 8);
        float32x4_t y2 = vld1q_f32(y + i + 8);
        float32x4_t x3 = vld1q_f32(x + i + 12);
        float32x4_t y3 = vld1q_f32(y + i + 12);
        vst1q_f32(y + i,      vfmaq_f32(y0, va, x0));
        vst1q_f32(y + i + 4,  vfmaq_f32(y1, va, x1));
        vst1q_f32(y + i + 8,  vfmaq_f32(y2, va, x2));
        vst1q_f32(y + i + 12, vfmaq_f32(y3, va, x3));
    }
    for (; i < n; ++i) y[i] = a * x[i] + y[i];
}

int main() {
    size_t n = 1000;
    float* x = aligned_alloc(16, n * sizeof(float));
    float* y = aligned_alloc(16, n * sizeof(float));
    float a = 2.5f;

    for (size_t i = 0; i < n; ++i) {
        x[i] = (float)i;
        y[i] = (float)(n - i);
    }

    saxpy_neon(a, x, y, n);

    float sum = 0.0f;
    for (size_t i = 0; i < n; ++i) sum += y[i];
    printf("NEON SAXPY sum: %f\n", sum);

    free(x);
    free(y);
    return 0;
}
```

Use a text editor to copy the code to a file `saxpy_neon.c`. 

First, verify your system supports NEON:

```bash
grep -m1 -ow asimd /proc/cpuinfo
```

If NEON is supported, you should see `asimd` in the output. If no output appears, NEON is not available.

Then build and run the code using:

```bash
gcc -O3 -march=armv8-a+simd -o saxpy_neon saxpy_neon.c
./saxpy_neon
```

{{% notice optional_title %}}
On AArch64, NEON is mandatory; the flag is shown for clarity.
{{% /notice %}}



## x86 AVX2 version (256-bit SIMD, 8 floats per operation)

AVX2 doubles the SIMD width compared to NEON, processing 8 single-precision floats at a time in 256-bit registers. 

This wider SIMD capability enables higher data throughput for numerical and HPC workloads on Intel and AMD CPUs.

```c
#include <immintrin.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

void saxpy_avx2(float a, const float *x, float *y, size_t n) {
    const __m256 va = _mm256_set1_ps(a);
    size_t i = 0;
    for (; i + 8 <= n; i += 8) {
        __m256 vx = _mm256_loadu_ps(x + i);
        __m256 vy = _mm256_loadu_ps(y + i);
        __m256 vout = _mm256_fmadd_ps(va, vx, vy);
        _mm256_storeu_ps(y + i, vout);
    }
    for (; i < n; ++i) y[i] = a * x[i] + y[i];
}

int main() {
    size_t n = 1000;
    float* x = aligned_alloc(32, n * sizeof(float));
    float* y = aligned_alloc(32, n * sizeof(float));
    float a = 2.5f;

    for (size_t i = 0; i < n; ++i) {
        x[i] = (float)i;
        y[i] = (float)(n - i);
    }

    saxpy_avx2(a, x, y, n);

    float sum = 0.0f;
    for (size_t i = 0; i < n; ++i) sum += y[i];
    printf("AVX2 SAXPY sum: %f\n", sum);

    free(x);
    free(y);
    return 0;
}
```

Use a text editor to copy the code to a file `saxpy_avx2.c`. 

First, verify your system supports AVX2:

```bash
grep -m1 -ow avx2 /proc/cpuinfo
```

If AVX2 is supported, you should see `avx2` in the output. If no output appears, AVX2 is not available.

Then build and run the code using:

```bash
gcc -O3 -mavx2 -mfma -o saxpy_avx2 saxpy_avx2.c
./saxpy_avx2
```

### Arm SVE (hardware dependent: 4 to 16+ floats per operation)

Arm SVE lets the hardware determine the register width, which can range from 128 up to 2048 bits. This means each operation can process from 4 to 64 single-precision floats at a time, depending on the implementation. 

Cloud instances using AWS Graviton, Google Axion, and Microsoft Azure Cobalt processors implement 128-bit SVE. The Fujitsu A64FX processor implements a vector length of 512 bits.

SVE encourages writing vector-length agnostic code: the compiler automatically handles tail cases, and your code runs efficiently on any Arm SVE hardware.

```c
#include <arm_sve.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void saxpy_sve(float a, const float *x, float *y, size_t n) {
    size_t i = 0;
    svfloat32_t va = svdup_f32(a);
    while (i < n) {
        svbool_t pg = svwhilelt_b32((uint32_t)i, (uint32_t)n);
        svfloat32_t vx = svld1(pg, x + i);
        svfloat32_t vy = svld1(pg, y + i);
        svfloat32_t vout = svmla_m(pg, vy, va, vx);
        svst1(pg, y + i, vout);
        i += svcntw();
    }
}

int main() {
    size_t n = 1000;
    float* x = aligned_alloc(64, n * sizeof(float));
    float* y = aligned_alloc(64, n * sizeof(float));
    float a = 2.5f;

    for (size_t i = 0; i < n; ++i) {
        x[i] = (float)i;
        y[i] = (float)(n - i);
    }

    saxpy_sve(a, x, y, n);

    float sum = 0.0f;
    for (size_t i = 0; i < n; ++i) sum += y[i];
    printf("SVE SAXPY sum: %f\n", sum);

    free(x);
    free(y);
    return 0;
}
```

Use a text editor to copy the code to a file `saxpy_sve.c`. 

First, verify your system supports SVE:

```bash
grep -m1 -ow sve /proc/cpuinfo
```

If SVE is supported, you should see `sve` in the output. If no output appears, SVE is not available.

Then build and run the code using:

```bash
gcc -O3 -march=armv8-a+sve -o saxpy_sve saxpy_sve.c
./saxpy_sve
```

## x86 AVX-512 version (512-bit SIMD, 16 floats per operation)

AVX-512 provides the widest SIMD registers of mainstream x86 architectures, processing 16 single-precision floats per 512-bit operation. 

AVX-512 availability varies across x86 processors. It's found on Intel Xeon server processors and some high-end desktop processors, as well as select AMD EPYC models.

For large arrays and high-performance workloads, AVX-512 delivers extremely high throughput, with additional masking features for efficient tail processing.

```c
#include <immintrin.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

void saxpy_avx512(float a, const float* x, float* y, size_t n) {
    const __m512 va = _mm512_set1_ps(a);
    size_t i = 0;
    for (; i + 16 <= n; i += 16) {
        __m512 vx = _mm512_loadu_ps(x + i);
        __m512 vy = _mm512_loadu_ps(y + i);
        __m512 vout = _mm512_fmadd_ps(va, vx, vy);
        _mm512_storeu_ps(y + i, vout);
    }
    const size_t r = n - i;
    if (r) {
        __mmask16 m = (1u << r) - 1u;
        __m512 vx = _mm512_maskz_loadu_ps(m, x + i);
        __m512 vy = _mm512_maskz_loadu_ps(m, y + i);
        __m512 vout = _mm512_fmadd_ps(va, vx, vy);
        _mm512_mask_storeu_ps(y + i, m, vout);
    }
}

int main() {
    size_t n = 1000;
    float *x = aligned_alloc(64, n * sizeof(float));
    float *y = aligned_alloc(64, n * sizeof(float));
    float a = 2.5f;

    for (size_t i = 0; i < n; ++i) {
        x[i] = (float)i;
        y[i] = (float)(n - i);
    }

    saxpy_avx512(a, x, y, n);

    float sum = 0.0f;
    for (size_t i = 0; i < n; ++i) sum += y[i];
    printf("AVX-512 SAXPY sum: %f\n", sum);

    free(x);
    free(y);
    return 0;
}
```

First, verify your system supports AVX-512:

```bash
grep -m1 -ow avx512f /proc/cpuinfo
```

If AVX-512 is supported, you should see `avx512f` in the output. If no output appears, AVX-512 is not available.

Then build and run the code using:

```bash
gcc -O3 -mavx512f -o saxpy_avx512 saxpy_avx512.c
./saxpy_avx512
```

## Summary

Wider data lanes mean each operation processes more elements, offering higher throughput on supported hardware. However, actual performance depends on factors like memory bandwidth, the number of execution units, and workload characteristics. 

Processors also improve performance by implementing multiple SIMD execution units rather than just making vectors wider. For example, Arm Neoverse V2 has 4 SIMD units while Neoverse N2 has 2 SIMD units. Modern CPUs often combine both approaches (wider vectors and multiple execution units) to maximize parallel processing capability.

Each vector extension requires different intrinsics, compilation flags, and programming approaches. While x86 and Arm vector extensions serve similar purposes and achieve comparable performance gains, you will need to understand the options and details to create portable code. 

You can also look for existing libraries that already work across vector extensions before you get too deep into code porting. This is often a good way to leverage the available SIMD capabilities on your target hardware.
