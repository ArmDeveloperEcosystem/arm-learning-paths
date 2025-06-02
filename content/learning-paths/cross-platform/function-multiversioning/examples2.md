---
title: Example 2 - runtime using ACLE intrinsics
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This example computes the dot product of two vectors using Arm C Language Extensions (ACLE) intrinsics. 

The intention is to enable the compiler to use SVE instructions in the specialized case, while restricting it to use only Armv8 instructions in the default case.

Use a text editor to create a file named `dotprod.c` with the code below:

```c
#include <stdio.h>
#include <stdlib.h>
#include <arm_neon.h>
#include <arm_sve.h>

__attribute__((target_version("sve")))
int dotProduct(short *vec1, short* vec2, short len) {
  printf("Running the sve version of dotProduct\n");

  int i = 0;
  svbool_t pg = svwhilelt_b32(i, len);
  svbool_t pt = svptrue_b32();
  svint32_t res = svdup_s32(0);
  while (svptest_any(pt, pg)) {
    svint32_t sv1 = svld1sh_s32(pg, vec1 + i);
    svint32_t sv2 = svld1sh_s32(pg, vec2 + i);
    res = svmla_m(pg, res, sv1, sv2);
    i += svcntw();
    pg = svwhilelt_b32(i, len);
  }
  return (int) svaddv(pt, res);
}

__attribute__((target_version("default")))
int dotProduct(short* vec1, short* vec2, short len) {
  printf("Running the default version of dotProduct\n");

  const short transferSize = 4;
  short segments = len / transferSize;

  // 4-element vector of zeros
  int32x4_t partialSumsNeon = vdupq_n_s32(0);
  int32x4_t sum1 = vdupq_n_s32(0);
  int32x4_t sum2 = vdupq_n_s32(0);
  int32x4_t sum3 = vdupq_n_s32(0);
  int32x4_t sum4 = vdupq_n_s32(0);

  // Main loop (note that loop index goes through segments). Unroll with 4
  int i = 0;
  for(; i+3 < segments; i+=4) {
    // Load vector elements to registers
    int16x8_t v11 = vld1q_s16(vec1);
    int16x4_t v11_low = vget_low_s16(v11);
    int16x4_t v11_high = vget_high_s16(v11);

    int16x8_t v12 = vld1q_s16(vec2);
    int16x4_t v12_low = vget_low_s16(v12);
    int16x4_t v12_high = vget_high_s16(v12);

    int16x8_t v21 = vld1q_s16(vec1+8);
    int16x4_t v21_low = vget_low_s16(v21);
    int16x4_t v21_high = vget_high_s16(v21);

    int16x8_t v22 = vld1q_s16(vec2+8);
    int16x4_t v22_low = vget_low_s16(v22);
    int16x4_t v22_high = vget_high_s16(v22);

    // Multiply and accumulate: partialSumsNeon += vec1Neon * vec2Neon
    sum1 = vmlal_s16(sum1, v11_low, v12_low);
    sum2 = vmlal_s16(sum2, v11_high, v12_high);
    sum3 = vmlal_s16(sum3, v21_low, v22_low);
    sum4 = vmlal_s16(sum4, v21_high, v22_high);

    vec1 += 16;
    vec2 += 16;
  }
  partialSumsNeon = sum1 + sum2 + sum3 + sum4;

  // Sum up remain parts
  int remain = len % transferSize;
  for(i = 0; i < remain; i++) {
    int16x4_t vec1Neon = vld1_s16(vec1);
    int16x4_t vec2Neon = vld1_s16(vec2);
    partialSumsNeon = vmlal_s16(partialSumsNeon, vec1Neon, vec2Neon);
    vec1 += 4;
    vec2 += 4;
  }

  // Store partial sums
  int partialSums[transferSize];
  vst1q_s32(partialSums, partialSumsNeon);

  // Sum up partial sums
  int result = 0;
  for(i = 0; i < transferSize; i++)
    result += partialSums[i];

  return result;
}

int scanVector(short *vec, short len) {
  short *p = vec;
  for (int i = 0; i < len; i++, p++)
    if (scanf("%hd", p) != 1)
      return 0;
  return 1;
}

int main(int argc, char **argv) {
  if (argc == 2) {
    int n = atoi(argv[1]);
    if (n < 16 || n > 1024)
      return -1;
    short v1[1024];
    short v2[1024];
    if (!scanVector(v1, n) || !scanVector(v2, n))
      return -1;
    int result = dotProduct(v1, v2, n);
    printf("dotProduct = %d\n", result);
  }
  return 0;
}
```

You can compile and run the above example on hardware that has both SVE and Armv8 instructions (no SVE):

To compile with Clang, run:

```console
clang --target=aarch64-linux-gnu -march=armv8-a -O3 dotprod.c --rtlib=compiler-rt
```

To compile with GCC, use:

```console
g++ -march=armv8-a -O3 dotprod.c
```

{{% notice Note %}}
Note that `gcc-14` does not yet support `target_version` when using the c-frontend. You can use `g++-14` instead.
{{% /notice %}}

To run the application:

```console
echo 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 | ./a.out 16
```

The expected output is:

```output
Running the sve version of dotProduct
dotProduct = 32
```

The SVE version is being selected because it has higher priority than the default, as indicated by the [mapping table](https://arm-software.github.io/acle/main/acle.html#mapping).
