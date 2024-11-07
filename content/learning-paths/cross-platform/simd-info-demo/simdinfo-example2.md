---
title: Intrinsics without Equivalents
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Handling intrinsics without direct equivalents

During the porting process, you will observe that certain instructions translate seamlessly. However, there are cases where direct equivalents for some intrinsics may not be readily available across architectures. For example, the [**`_mm_madd_epi16`**](https://simd.info/c_intrinsic/_mm_madd_epi16/) intrinsic from **SSE2**, which performs multiplication of 16-bit signed integer elements in a vector and then does a pairwise addition of adjacent elements increasing the element width, does not have a direct counterpart in **NEON**. However it can be emulated using another intrinsic. Similarly its 256 and 512-bit counterparts, [**`_mm256_madd_epi16`**](https://simd.info/c_intrinsic/_mm256_madd_epi16/) and [**`_mm512_madd_epi16`**](https://simd.info/c_intrinsic/_mm512_madd_epi16/) can be emulated by a sequence of instructions, but here you will see the 128-bit variant.

You may already know the equivalent operations for this particular intrinsic, but let's assume you don't. In this usecase, reading the **`_mm_madd_epi16`** on the **SIMD.info** might indicate that a key characteristic of the instruction involved is the *widening* of the result elements, from 16-bit to 32-bit signed integers. Unfortunately, that is not the case, as this particular instruction does not actually increase the size of the element holding the result values. You will see how that effects the result in the example.

Consider the following code for **SSE2**. Create a new file for the code named `_mm_madd_epi16_test.c` with the contents shown below:

```C
#include <stdint.h>
#include <immintrin.h>
#include <stdio.h>

void print_s16x8(char *label, __m128i v) {
    int16_t out[8];
    _mm_storeu_si128((__m128i*)out, v);
    printf("%-*s: ", 30, label);
    for (size_t i=0; i < 8; i++) printf("%4x ", (uint16_t)out[i]);
    printf("\n");
}

int16_t a_array[8] = {10, 30, 50, 70, 90, 110, 130, 150};
int16_t b_array[8] = {20, 40, 60, 80, 100, 120, 140, 160};

int main() {
    
    __m128i a = _mm_loadu_si128((__m128i*)a_array);
    __m128i b = _mm_loadu_si128((__m128i*)b_array);
    // 130 * 140 = 18200, 150 * 160 = 24000
    // adding them as 32-bit signed integers -> 42000
    // adding them as 16-bit signed integers -> -23336 (overflow!)

    __m128i res = _mm_madd_epi16(a, b);

    print_s16x8("a", a);
    print_s16x8("b", b);
    print_s16x8("_mm_madd_epi16(a, b)", res);

    return 0;
}
```

Compile the code as follows on an x86 system (no extra flags required as **SSE2** is assumed by default on all 64-bit x86 systems):
```bash
gcc -O3 _mm_madd_epi16_test.c -o  _mm_madd_epi16_test
```

Now run the program:
```bash
./_mm_madd_epi16_test
```

The output should look like: 
```output
a                             :    a   1e   32   46   5a   6e   82   96
b                             :   14   28   3c   50   64   78   8c   a0
_mm_madd_epi16(a, b)          :  578    0 2198    0 56b8    0 a4d8    0
```

You will note that the result of the last element is a negative number, even though we added 2 positive results (`130*140` and `150*160`). That is because the result of the addition has to occupy a 16-bit signed integer element and when the first is larger we have the effect of an negative overflow. The result is the same in binary arithmetic, but when interpreted into a signed integer, it turns the number into a negative.

The rest of the values are as expected. Notice how each pair has a zero element next to it. The results are correct, but they are not in the correct order. In this example, we chose to use vmovl to zero-extend values, which achieves the correct order with zero elements in place. While both vmovl and zip could be used for this purpose, we opted for **vmovl** in this implementation. For more details, see the ARM Software Optimization Guides, such as the [Neoverse V2 guide](https://developer.arm.com/documentation/109898/latest/).

```C
#include <arm_neon.h>
#include <stdint.h>
#include <stdio.h>

void print_s16x8(char *label, int16x8_t v) {
    int16_t out[8];
    vst1q_s16(out, v);
    printf("%-*s: ", 30, label);
    for (size_t i = 0; i < 8; i++) printf("%4x ", (uint16_t)out[i]);
    printf("\n");
}

int16_t a_array[8] = {10, 30, 50, 70, 90, 110, 130, 150};
int16_t b_array[8] = {20, 40, 60, 80, 100, 120, 140, 160};

int main() {
    int16x8_t a = vld1q_s16(a_array);
    int16x8_t b = vld1q_s16(b_array);
    int16x8_t zero = vdupq_n_s16(0);
    // 130 * 140 = 18200, 150 * 160 = 24000
    // adding them as 32-bit signed integers -> 42000
    // adding them as 16-bit signed integers -> -23336 (overflow!)

    int16x8_t res = vmulq_s16(a, b);

    print_s16x8("a", a);
    print_s16x8("b", b);
    print_s16x8("vmulq_s16(a, b)", res);
    res = vpaddq_s16(res, zero);
    print_s16x8("vpaddq_s16(a, b)", res);

    // vmovl_s16 would sign-extend; we just want to zero-extend
    // so we need to cast to uint16, vmovl_u16 and then cast back to int16
    uint16x4_t res_u16 = vget_low_u16(vreinterpretq_u16_s16(res));
    res = vreinterpretq_s16_u32(vmovl_u16(res_u16));
    print_s16x8("final", res);

    return 0;
}
```

Write the above program to a file called `_mm_madd_epi16_neon.c` and compile it:

```bash
gcc -O3 _mm_madd_epi16_neon.c -o _mm_madd_epi16_neon
```

Now run the program:
```bash
./_mm_madd_epi16_neon.c
```

The output should look like: 
```output
a                             :    a   1e   32   46   5a   6e   82   96
b                             :   14   28   3c   50   64   78   8c   a0
vmulq_s16(a, b)               :   c8  4b0  bb8 15e0 2328 3390 4718 5dc0
vpaddq_s16(a, b)              :  578 2198 56b8 a4d8    0    0    0    0
final                         :  578    0 2198    0 56b8    0 a4d8    0
```

As you can see the results of both match, **SIMD.info** was especially helpful in this process, providing detailed descriptions and examples that guided the translation of complex intrinsics between different SIMD architectures.

