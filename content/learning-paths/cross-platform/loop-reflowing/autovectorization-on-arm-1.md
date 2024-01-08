---
title: Autovectorization
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Autovectorization on Arm.

Let's look at another example, but this time you will see how you can take advantage of specific Arm instructions.
The following code will calculate the dot product of variable size two integer arrays.

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

int32_t dotprod(int32_t *A, int32_t *B, size_t N) {
    int32_t result = 0;
    for (size_t i=0; i < N; i++) {
        result += A[i]*B[i];
    }
    return result;
}

int main() {
    const int N = 128;
    int32_t A[N], B[N];

    int32_t dot = dotprod(A, B, N);

    printf("dotprod = %d", dot);
}
```

Such code is quite common in audio/video codecs where integer arithmetic is used instead of floating-point.

As it is, if you would compile it with `gcc -O2 -fno-inline` the assembly output for `dotprod` is the following:

```as
dotprod:
        mov     x6, x0
        cbz     x2, .L4
        mov     x3, 0
        mov     w0, 0
.L3:
        ldr     w5, [x6, x3, lsl 2]
        ldr     w4, [x1, x3, lsl 2]
        add     x3, x3, 1
        madd    w0, w5, w4, w0
        cmp     x2, x3
        bne     .L3
        ret
.L4:
        mov     w0, 0
        ret
```

You can see that it's a pretty standard implementation, doing one element at a time. The option `-fno-inline` is necessary to avoid inlining any code from the function `dot-prod()` into `main()` for performance reasons. In general this is a good thing, but in this case we want to demonstrate the autovectorization process and it will be harder if there is no easy way to distinguish the caller from the callee. Now, increase the optimization level to `-O3`, recompile and observe the assembly output again:

```as
dotprod:
        mov     x4, x0
        cbz     x2, .L7
        sub     x0, x2, #1
        cmp     x0, 2
        bls     .L8
        lsr     x0, x2, 2
        mov     x3, 0
        movi    v0.4s, 0
        lsl     x0, x0, 4
.L4:
        ldr     q2, [x4, x3]
        ldr     q1, [x1, x3]
        add     x3, x3, 16
        mla     v0.4s, v2.4s, v1.4s
        cmp     x0, x3
        bne     .L4
        addv    s0, v0.4s
        and     x3, x2, -4
        fmov    w0, s0
        tst     x2, 3
        beq     .L1
.L3:
        ldr     w8, [x4, x3, lsl 2]
        add     x6, x3, 1
        ldr     w7, [x1, x3, lsl 2]
        lsl     x5, x3, 2
        madd    w0, w8, w7, w0
        cmp     x2, x6
        bls     .L1
        add     x6, x5, 4
        add     x3, x3, 2
        ldr     w7, [x4, x6]
        ldr     w6, [x1, x6]
        madd    w0, w7, w6, w0
        cmp     x2, x3
        bls     .L1
        add     x5, x5, 8
        ldr     w2, [x1, x5]
        ldr     w1, [x4, x5]
        madd    w0, w2, w1, w0
.L1:
        ret
.L7:
        mov     w0, 0
        ret
.L8:
        mov     x3, 0
        mov     w0, 0
        b       .L3
```

Quite larger in quantity but the autovectorization is obvious. The label `.L4` includes the main loop and we can see that the instruction `MLA` is used to multiply and accumulate the dot products, 4 elements at a time. At the end of this loop, the instruction `ADDV` does a horizontal addition of the 4 elements in the final vector and includes the final sum. The main loop is executed while the number of the remaining elements is a multiple of 4. The rest of the elements are processed one at a time in the `.L3` part of the code.

This is quite nice and we can expect a performance gain of about 4x faster in general.

You might be wondering if there is a way to hint to the compiler that the sizes are always going to be multiples of 4 and avoid the last part of the code and the answer is yes, but it depends on the compiler. In the case of gcc, it is enough to add an instruction that ensures the size is only multiples of 4:

```C
int32_t dotprod(int32_t *A, int32_t *B, size_t N) {
    int32_t result = 0;
    N -= N % 4;
    for (size_t i=0; i < N; i++) {
        result += A[i]*B[i];
    }
    return result;
}
```

And the assembly output with `-O3` will much more compact, now that it does not have to handle the left over bytes:

```as
dotprod:
        ands    x2, x2, -4
        beq     .L4
        movi    v0.4s, 0
        lsl     x3, x2, 2
        mov     x2, 0
.L3:
        ldr     q2, [x1, x2]
        ldr     q1, [x0, x2]
        add     x2, x2, 16
        mla     v0.4s, v2.4s, v1.4s
        cmp     x3, x2
        bne     .L3
        addv    s0, v0.4s
        fmov    w0, s0
        ret
.L4:
        fmov    s0, wzr
        fmov    w0, s0
        ret
```

But is that all that the compiler can do? Thankfully not, modern compilers are very proficient in generating code that utilizes all available instructions, provided they have the right information.
For example, our `dotprod()` function operates on `int32_t` elements, what if we could limit the range to 8-bit? Something like that is not untypical, and we know there is an Armv8 ISA extension that [provides a pair of new `SDOT`/`UDOT` instructions to perform a dotprot across 8-bit elements of 2 vectors and store the results in the 32-bit elements of the resulting vector](https://developer.arm.com/documentation/102651/a/What-are-dot-product-intructions-). Could the compiler make use of that automatically? Or Should we resort to a hand-written version that uses the respective intrinsics?

It turns out that some compilers can, and will detect that the number or the iterations is a multiple of the number of elements in a SIMD vector. Convert the code to use `int8_t` types for `A` and `B` arrays:

```C
int32_t dotprod(int8_t *A, int8_t *B, size_t N) {
    int32_t result = 0;
    N -= N % 4;
    for (size_t i=0; i < N; i++) {
        result += A[i]*B[i];
    }
    return result;
}

int main() {
    const int N = 128;
    int8_t A[N], B[N];

    int32_t dot = dotprod(A, B, N);

    printf("dotprod = %d", dot);
}
```

You need to recompile the code with `gcc -O3 -Wall -g -fno-inline -march=armv8-a+dotprod` in order to hint to the compiler that it has the new instructions at its disposal.

The assembly output will be quite larger as the use of `SDOT` can only work in the main loop where the size is a multiple of 16. Then the compiler will unroll the loop to use ASIMD instructions if the size is greater than 8, and byte-handling instructions if the size is smaller.
We could eliminate those extra tail instructions by converting `N -= N % 4` to 8 or even 16:

```C
int32_t dotprod(int8_t *A, int8_t *B, size_t N) {
    int32_t result = 0;
    N -= N % 16;
    for (size_t i=0; i < N; i++) {
        result += A[i]*B[i];
    }
    return result;
}
```

The resulting assembly output where we only handle sizes multiple of 16 is the following:

```as
dotprod:
        ands    x2, x2, -16
        beq     .L4
        movi    v0.4s, 0
        mov     x3, 0
.L3:
        ldr     q1, [x1, x3]
        ldr     q2, [x0, x3]
        sdot    v0.4s, v1.16b, v2.16b
        add     x3, x3, 16
        cmp     x2, x3
        bne     .L3
        addv    s0, v0.4s
        fmov    w0, s0
        ret
.L4:
        fmov    s0, wzr
        fmov    w0, s0
        ret
```

Again we see that at the end of the loop `ADDV` is used to perform a horizontal addition of the 32-bit integer elements and produce the final dot product sum.
