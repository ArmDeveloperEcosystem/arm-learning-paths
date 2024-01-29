---
title: More autovectorization on Arm
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The previous example using the `SDOT`/`UDOT` instructions is only one of the Arm-specific optimizations possible.

While it is not possible to demonstrate all of the specialized instructions offered by the Arm architecture, it's worth looking at another example.

Below is a very simple loop, calculating what is known as a Sum of Absolute Differences (SAD). Such code is very common in video codecs and used in calculating differences between video frames.

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

uint32_t sad8(int8_t *A, int8_t *B, size_t N) {
    uint32_t result = 0;
    N -= N % 16;
    for (size_t i=0; i < N; i++) {
        result += abs(A[i] - B[i]);
    }
    return result;
}

int main() {
    const int N = 128;
    int8_t A[N], B[N];

    uint32_t sad = sad8(A, B, N);

    printf("sad = %d\n", sad);
}
```

A hint to the compiler was added that the size is a multiple of 16 to avoid generating cases for smaller lengths. *This is for demonstration purposes only*.

Save the above code to a file named `sadtest.c` and compile it:

```bash
gcc -O3 -fno-inline sadtest.c -o sadtest
```

The assembly output for `sad8()` is the following:

```as
sad8:
        ands    x2, x2, -16
        beq     .L4
        movi    v3.4s, 0
        mov     x3, 0
.L3:
        ldr     q1, [x0, x3]
        ldr     q2, [x1, x3]
        add     x3, x3, 16
        sabdl2  v0.8h, v1.16b, v2.16b
        sabal   v0.8h, v1.8b, v2.8b
        sadalp  v3.4s, v0.8h
        cmp     x2, x3
        bne     .L3
        addv    s3, v3.4s
        fmov    w0, s3
        ret
.L4:
        fmov    s3, wzr
        fmov    w0, s3
        ret
```

You can see that the compiler generates code that uses 3 specialized instructions that exist only on Arm: [`SABDL2`](https://developer.arm.com/documentation/ddi0596/2021-03/SIMD-FP-Instructions/SABDL--SABDL2--Signed-Absolute-Difference-Long-?lang=en), [`SABAL`](https://developer.arm.com/documentation/ddi0596/2021-03/SIMD-FP-Instructions/SABAL--SABAL2--Signed-Absolute-difference-and-Accumulate-Long-?lang=en) and [`SADALP`](https://developer.arm.com/documentation/ddi0596/2021-03/SIMD-FP-Instructions/SADALP--Signed-Add-and-Accumulate-Long-Pairwise-?lang=en).

The accumulator variable is not 8-bit but 32-bit, so the typical SIMD implementation that would involve 16 x 8-bit subtractions, then 16 x absolute values and 16 x additions would not do, and a widening conversion to 32-bit would have to take place before the accumulation.

This would mean that 4x items at a time would be accumulated but, with the use of these instructions, the performance gain can be up to 16x faster than the original scalar code, or about 4x faster than the typical SIMD implementation.

For completeness the SVE2 version will be provided, which does not depend on size being a multiple of 16.

This version is without the `N -= N % 16` before the loop.

You can compile it on any Arm system (even one without support for SVE2) just by adding the appropriate `-march` flag:

```bash
gcc -O3 -fno-inline -march=armv9-a sadtest.c -o sadtest
```

Depending on your compiler version `-march=armv9-a` might not be available. If this is the case, you can use `-march=march8-a+sve2` instead.

The SVE2 assembly output for `sad8()` is:

```as
sad8:
        ands    x2, x2, -16
        beq     .L4
        mov     x3, 0
        mov     x4, x2
        whilelo p0.b, xzr, x2
        uqdecb  x4
        mov     z2.b, #0
        mov     z3.b, #1
        ptrue   p1.b, all
.L3:
        ld1b    z0.b, p0/z, [x0, x3]
        ld1b    z1.b, p0/z, [x1, x3]
        sel     z1.b, p0, z1.b, z0.b
        whilelo p0.b, x3, x4
        sabd    z0.b, p1/m, z0.b, z1.b
        incb    x3
        udot    z2.s, z0.b, z3.b
        b.any   .L3
        uaddv   d2, p1, z2.s
        fmov    w0, s2
        ret
.L4:
        fmov    s2, wzr
        fmov    w0, s2
        ret
```

## Conclusion

You might ask why you should learn about autovectorization if you need to have specialized knowledge of instructions like `SDOT`/`SADAL` in order to benefit.

Autovectorization is a tool. The goal is to minimize the effort required by developers and maximize the performance, while at the same time requiring low maintenance in terms of code size. 

It is far easier to maintain hundreds or thousands of functions that are known to generate the fastest code using autovectorization for all platforms, than it is to maintain the same number of functions in multiple versions for each supported architecture and SIMD engine. 

As with most tools, the better you know how to use it, the better the results will be.

