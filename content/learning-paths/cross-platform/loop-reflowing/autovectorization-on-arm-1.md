---
title: Autovectorization on Arm
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section you will learn how to take advantage of specific Arm instructions.

The following code calculates the dot product of two integer arrays.

Copy the code and save it to a file named `dotprod.c`.

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

Such code is common in audio and video codecs where integer arithmetic is used instead of floating-point.

Compile the code:

```bash
gcc -O2 -fno-inline dotprod.c -o dotprod
```

Look at the assembly code:

```bash
objdump -D dotprod
```

The `objdump` instructions are omitted from the remainder of the examples, but you can use `objdump` every time you recompile to see the assembly output.

The assembly output for the `dotprod()` function is:

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

You can see that it's a pretty standard implementation, doing one element at a time. The option `-fno-inline` is necessary to avoid inlining any code from the function `dot-prod()` into `main()` for performance reasons. In general, this is a good thing, but demonstrating the autovectorization process is more difficult if there is no easy way to distinguish the caller from the callee.

Next, increase the optimization level to `-O3`, recompile, and observe the assembly output again:

```bash
gcc -O3 -fno-inline dotprod.c -o dotprod
```

The assembly for the `dotprod()` function is now:

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

The code is larger, but you can see that some autovectorization has taken place.

The label `.L4` includes the main loop and you can see that the `mla` instruction is used to multiply and accumulate the dot products, 4 elements at a time. 

At the end of this loop, the `addv` instruction does a horizontal addition of the 4 elements in the final vector and returns the final sum. The main loop is executed while the number of the remaining elements is a multiple of 4. The rest of the elements are processed one at a time in the `.L3` section of code.

With the new code, you can expect a performance gain of about 4x.

You might be wondering if there is a way to hint to the compiler that the sizes are always going to be multiples of 4 and avoid the last part of the code. 

The answer is *yes*, but it depends on the compiler. In the case of gcc, it is enough to add an instruction that ensures the sizes are multiples of 4.

Modify the `dotprod()` function to add the multiples of 4 hint as shown below:

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

Compile again ith `-O3`:

```bash
gcc -O3 -fno-inline dotprod.c -o dotprod
```

The assembly output with `-O3` is much more compact because it does not need to handle the left over bytes:

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

Is there anything else the compiler can do? 

Modern compilers are very proficient at generating code that utilizes all available instructions, provided they have the right information.

For example, the `dotprod()` function operates on `int32_t` elements, what if you could limit the range to 8-bit? 

There is an Armv8 ISA extension that [provides signed and unsigned dot product instructions](https://developer.arm.com/documentation/102651/a/What-are-dot-product-intructions-) to perform a dot product across 8-bit elements of 2 vectors and store the results in the 32-bit elements of the resulting vector. 

Could the compiler make use of the instructions automatically or does the code need to be hand-written using intrinsics? 

It turns out that some compilers will detect that the number or the iterations is a multiple of the number of elements in a SIMD vector. 

Modify the `dotprod.c` code to use `int8_t` types for `A` and `B` arrays as shown below:

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

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

Compile the code:

```bash
gcc -O3 -fno-inline -march=armv8-a+dotprod dotprod.c -o dotprod
```

You need to compile with the architecture flag to use the dot product instructions. 

The assembly output will be quite larger as the use of `SDOT` can only work in the main loop where the size is a multiple of 16. The compiler will unroll the loop to use Advanced SIMD instructions if the size is greater than 8, and byte-handling instructions if the size is smaller.

You can eliminate the extra tail instructions by converting `N -= N % 4` to 8 or even 16 as shown below: 

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

The resulting assembly output only handles sizes that are multiple of 16:

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

As before, at the end of the loop `addv` instruction is used to perform a horizontal addition of the 32-bit integer elements and produce the final dot product sum.

This particular implementation will be up to 4x faster than the previous version using `mla`.
