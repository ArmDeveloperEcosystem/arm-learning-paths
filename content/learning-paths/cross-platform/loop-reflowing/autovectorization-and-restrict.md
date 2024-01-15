---
title: Autovectorization and restrict
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Autovectorization and restrict keyword

You have already experienced some form of autovectorization by learning about the [`restrict` keyword in a previous Learning Path](https://learn.arm.com/learning-paths/cross-platform/restrict-keyword-c99/).
Our example is a classic textbook example that the compiler will autovectorize simply by using `restrict`:

Try the previously saved files, compile them both and compare the assembly output:

```bash
gcc -O2 addvec.c -o addvec
gcc -O2 addvec_neon.c -o addvec_neon
```

Let's look at the assembly output of `addvec`:

```as
addvec:
        mov     x3, 0
.L2:
        ldr     s0, [x1, x3, lsl 2]
        ldr     s1, [x2, x3, lsl 2]
        fadd    s0, s0, s1
        str     s0, [x0, x3, lsl 2]
        add     x3, x3, 1
        cmp     x3, 100
        bne     .L2
        ret
```

Similarly, for the `addvec_neon` executable:

```as
addvec:
        mov     x3, 0
.L6:
        ldr     q0, [x1, x3]
        ldr     q1, [x2, x3]
        fadd    v0.4s, v0.4s, v1.4s
        str     q0, [x0, x3]
        add     x3, x3, 16
        cmp     x3, 400
        bne     .L6
        ret
 ```

The latter uses Advanced SIMD/Neon instructions `fadd` with operands `v0.4s`, `v1.4s` to perform calculations in 4 x 32-bit floating-point elements.

Let's try to add `restrict` to the output argument `C` in the first `addvec` function:

```C
void addvec(float *restrict C, float *A, float *B) {
    for (size_t i=0; i < N; i++) {
    	C[i] = A[i] + B[i];
    }
}
```

Recompile and check the assembly output again:

```as
addvec:
        mov     x3, 0
.L2:
        ldr     q0, [x1, x3]
        ldr     q1, [x2, x3]
        fadd    v0.4s, v0.4s, v1.4s
        str     q0, [x0, x3]
        add     x3, x3, 16
        cmp     x3, 400
        bne     .L2
        ret
 ```

As you can see, the compiler has enabled autovectorization for this algorithm and the output is identical to the hand-written function! Strictly speaking, you don't even need `restrict` in such a trivial loop as it will be autovectorized anyway when certain optimization levels are added to the compilation flags (`-O2` for clang, `-O3` for gcc). However, the use of restrict simplifies the code and generates SIMD code similar to the hand written version in `addvec_neon.c`.

The reason for this is because of the way each compiler decides whether to use autovectorization or not. For each candidate loop the compiler will estimate the possible performance gains against a cost model, which is affected by many parameters and of course the optimization level in the compilation flags. This cost model will estimate whether the autovectorized code grows in size and if the performance gains are enough to outweigh this increase in code size. Based on this estimation, the compiler will decide to use this vectorized code or fall back to a more 'safe' scalar implementation. This decision however is something that is not set in stone and is constantly reevaluated during compiler development.

This analysis goes beyond the scope of this LP, this was just one trivial example to demonstrate how the autovectorization can be triggered by a flag.

You will see some more advanced examples in the next sections.