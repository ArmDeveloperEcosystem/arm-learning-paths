---
title: What problem does restrict solve?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The problem: overlapping memory regions as pointer arguments

Before we go into the detail of the `restrict` keyword, let's first demonstrate the problem.

Let's consider this C code:
```C
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void scaleVectors(int64_t *A, int64_t *B, int64_t *C) {
    for (int i = 0; i < 4; i++) {
        A[i] *= *C;
        B[i] *= *C;
    }
}

void printVector(char *t, int64_t *A) {
    printf("%s: ", t);
    for (int i=0;i < 4; i++) {
        printf("%ld ", A[i]);
    }
    printf("\n");
}

int main() {
    int64_t a[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
    int64_t *b = &a[2];
    int64_t c = 2;

    printVector("a(before)", a);
    printVector("b(before)", b);
    scaleVectors(a, b, &c);
    printVector("a(after) ", a);
    printVector("b(after) ", b);
}
```

There are 2 points to make here:
1. `scaleVectors()` is the important function here, it scales two vectors by the same scale factor `*C`
2. vector `a` overlaps with vector `b`. (`b = &a[2]`). 

this rather simple program produces this output:
```
a(before): 1 2 3 4 
b(before): 3 4 5 6 
a(after) : 2 4 12 16 
b(after) : 12 16 10 12
```

Notice that after the scaling, the contents of `a` are also affected by the scaling of `b` as their elements overlap in memory.

We will include the assembly output of `scaleVectors` as produced by `clang-17 -O3`:

```
scaleVectors:                           // @scaleVectors
        ldr     x8, [x2]
        ldr     x9, [x0]
        mul     x8, x9, x8
        str     x8, [x0]
        ldr     x8, [x2]
        ldr     x9, [x1]
        mul     x8, x9, x8
        str     x8, [x1]
        ldr     x8, [x2]
        ldr     x9, [x0, #8]
        mul     x8, x9, x8
        str     x8, [x0, #8]
        ldr     x8, [x2]
        ldr     x9, [x1, #8]
        mul     x8, x9, x8
        str     x8, [x1, #8]
        ldr     x8, [x2]
        ldr     x9, [x0, #16]
        mul     x8, x9, x8
        str     x8, [x0, #16]
        ldr     x8, [x2]
        ldr     x9, [x1, #16]
        mul     x8, x9, x8
        str     x8, [x1, #16]
        ldr     x8, [x2]
        ldr     x9, [x0, #24]
        mul     x8, x9, x8
        str     x8, [x0, #24]
        ldr     x8, [x2]
        ldr     x9, [x1, #24]
        mul     x8, x9, x8
        str     x8, [x1, #24]
        ret
```

This doesn't look optimal. `scaleVectors` seems to be doing each load, multiplication, and store in sequence. Surely it can be better optimized? Because the memory pointers are overlapping, let's try different assignments of `a` and `b` in `main()` to make them explicitly independent. Perhaps the compiler will detect that and generate faster instructions to do the same thing.

```
    int64_t a[] = { 1, 2, 3, 4 };
    int64_t b[] = { 5, 6, 7, 8 };
```

Unsurprisingly, the disassembled output of `scaleVectors` is the same. The reason for this is that the compiler has no hint about the dependency between the two pointers used in the function so it has no choice but to assume that it has to process one element at a time. The function has no way of knowing what arguments need to be called.  We see 8 instances of `mul`, which is correct but the number of loads and stores in between indicates that the CPU spends its time waiting for data to arrive from/to the cache. We need a way to be able to tell the compiler that it can assume the buffers passed are independent.

## The Solution: restrict

This is what the C99 `restrict` keyword resolves. It instructs the compiler that the passed arguments are not dependent on each other and that access to the memory of each happens only through the respective pointer. This way the compiler can schedule the instructions in a much more efficient way. Essentially it can group and schedule the loads and stores. **Note**, `restrict` only works in C, not in C++.

Let's add `restrict` to `A` in the parameter list:
```C
void scaleVectors(int64_t *restrict A, int64_t *B, int64_t *C) {
    for (int i = 0; i < 4; i++) {
        A[i] *= *C;
        B[i] *= *C;
    }
}
```

This is the assembly output with `clang-17 -O3` (gcc has a similar output):

```assembly
scaleVectors:                           // @scaleVectors
        ldp     x9, x10, [x1]
        ldr     x8, [x2]
        ldp     x11, x12, [x1, #16]
        mul     x9, x9, x8
        ldp     x13, x14, [x0]
        str     x9, [x1]
        ldr     x9, [x2]
        mul     x8, x13, x8
        mul     x10, x10, x9
        mul     x9, x14, x9
        str     x10, [x1, #8]
        ldr     x10, [x2]
        stp     x8, x9, [x0]
        mul     x11, x11, x10
        str     x11, [x1, #16]
        ldp     x15, x11, [x0, #16]
        ldr     x13, [x2]
        mul     x10, x15, x10
        mul     x11, x11, x13
        mul     x12, x12, x13
        stp     x10, x11, [x0, #16]
        str     x12, [x1, #24]
        ret
```

We see an obvious reduction in the number of instructions, from 32 instructions down to 22! That's 68% of the original count, which is impressive. One can easily see that the loads are grouped, as well as the multiplications. Of course, there are still 8 multiplications as that cannot change, but there are far fewer loads and stores as the compiler found the opportunity to use `LDP`/`STP` which load/store in pairs for the pointer `A`.

Let's try adding `restrict` to `B` as well:
```C
void scaleVectors(int64_t *restrict A, int64_t *restrict B, int64_t *C) {
    for (int i = 0; i < 4; i++) {
        A[i] *= *C;
        B[i] *= *C;
    }
}
```

And the assembly output with `clang-17 -O3`:

```
scaleVectors:                           // @scaleVectors
        ldp     x9, x10, [x0]
        ldr     x8, [x2]
        ldp     x11, x12, [x0, #16]
        ldp     x13, x14, [x1]
        mul     x9, x9, x8
        ldp     x15, x16, [x1, #16]
        mul     x10, x10, x8
        mul     x11, x11, x8
        mul     x12, x12, x8
        mul     x13, x13, x8
        stp     x9, x10, [x0]
        mul     x9, x14, x8
        mul     x10, x15, x8
        mul     x8, x16, x8
        stp     x11, x12, [x0, #16]
        stp     x13, x9, [x1]
        stp     x10, x8, [x1, #16]
        ret
```

There is another reduction in the number of instructions, this time down to 17 from the original 32. There are only 5 loads and 4 stores and, as before, all the loads/stores are paired (because the `LDP`/`STP` instructions are used).

It is interesting to see that in such an example adding the `restrict` keyword reduced our code size to almost half. This will have an obvious impact in both performance and efficiency.

## What about SVE2?

We have shown the obvious benefit of `restrict` in this function, on an armv8-a CPU, but we have new armv9-a CPUs out there with SVE2 as well as Neon/ASIMD. 
Could the compiler generate better code in that case using `restrict`? The output without `restrict` is almost the same, but with `restrict` used, this is the result (we used `clang-17 -O3 -march=armv9-a`):

```
scaleVectors:                           // @scaleVectors
        ldp     q1, q2, [x0]
        ldp     q3, q4, [x1]
        ld1r    { v0.2d }, [x2]
        mul     z1.d, z1.d, z0.d
        mul     z2.d, z2.d, z0.d
        stp     q1, q2, [x0]
        mul     z1.d, z3.d, z0.d
        mul     z0.d, z4.d, z0.d
        stp     q1, q0, [x1]
        ret
```

There are just 10 instructions, 31% of the original code size! The compiler has made great use of the SVE2 features, combining the multiplications and reducing them to 4 and, at the same time, grouping loads and stores down to 2 each. We have optimized our code by more than 3x just by adding a C99 keyword.

We are now going to look at another example.
