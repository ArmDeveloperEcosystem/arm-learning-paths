---
title: Autovectorization using the restrict keyword
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You may have already experienced some form of autovectorization by reading [Understand the restrict keyword in C99](/learning-paths/cross-platform/restrict-keyword-c99/).

The example in the previous section is a classic textbook example that the compiler will autovectorize by using `restrict`.

Compile the previously saved files:

```bash
gcc -O2 addvec.c -o addvec
gcc -O2 addvec_neon.c -o addvec_neon
```

Generate the assembly output using:

```bash
objdump -D addvec 
```

The assembly output of the `addvec()` function is shown below:

```output
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

Generate the assembly output for `addvec_neon` using:

```bash
objdump -D addvec_neon
```

The assembly output for the `addvec()` function from the `addvec_neon` executable is shown below:

```output
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

The second example uses the Advanced SIMD/Neon instruction `fadd` with operands `v0.4s`, `v1.4s` to perform calculations in 4 x 32-bit floating-point elements.

Add the `restrict` keyword to the output argument `C` in the `addvec()` function in `addvec.c`:

```C
void addvec(float *restrict C, float *A, float *B) {
    for (size_t i=0; i < N; i++) {
    	C[i] = A[i] + B[i];
    }
}
```

Recompile and check the assembly output again:
```bash
gcc -O2 addvec.c -o addvec
objdump -D addvec
```

The assembly output for the `addvec` function is now: 

```output
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

As you can see, the compiler has enabled autovectorization for this algorithm and the output is identical to the hand-written function.

Strictly speaking, you don't even need `restrict` in such a trivial loop as it will be autovectorized anyway when certain optimization levels are added to the compilation flags (`-O2` for clang, `-O3` for gcc). However, the use of restrict simplifies the code and generates SIMD code similar to the hand written version in `addvec_neon.c`.

The reason for this is related to how each compiler decides whether to use autovectorization or not. 

For each candidate loop the compiler will estimate the possible performance gains against a cost model, which is affected by many parameters and of course the optimization level in the compilation flags. 

The cost model estimates whether the autovectorized code grows in size and if the performance gains are enough to outweigh the increase in code size. Based on this estimation, the compiler will decide to use vectorized code or fall back to a more 'safe' scalar implementation. This decision, however, is fluid and is constantly reevaluated during compiler development.

Compiler cost model analysis is beyond the scope of this Learning Path but the above example demonstrates how autovectorization can be triggered by a flag.

You will see some more advanced examples in the next sections.
