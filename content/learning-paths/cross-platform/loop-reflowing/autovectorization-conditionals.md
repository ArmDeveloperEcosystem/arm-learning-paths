---
title: Autovectorization and conditionals
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, you learned that compilers cannot autovectorize loops with branches. 

In this section, you will see more examples of loops with branches.

You will learn when it is possible to enable the vectorizer in the compiler by adapting the loop, and when you are required to modify the algorithm or write manually optimized code.

### Loops with if/else/switch statements

Consider the following function, a modified form of the previous function that uses weighted coefficients for `A[i]`.

```C
void addvecweight(float *restrict C, float *A, float *B,
                    size_t N, float weight) {
    for (size_t i=0; i < N; i++) {
        if (weight < 0.5f)
            C[i] = A[i] + B[i];
        else
            C[i] = 1.5f*A[i] + 0.5f * B[i];
    }
}
```

You might think that this loop cannot be vectorized. Such loops are not uncommon and compilers have a difficult time understanding the pattern and transforming them to vectorizable forms. However, this is actually a vectorizable loop, as the conditional can be moved out of the loop, as this is a loop-invariant conditional. 

The compiler will internally transform the loop into something similar to the code below: 

```C
void addvecweight(float *restrict C, float *A, float *B, size_t N) {
    if (weight < 0.5f) {
        for (size_t i=0; i < N; i++) {
            C[i] = A[i] + B[i];
        }
    } else {
        for (size_t i=0; i < N; i++) {
            C[i] = 1.5f*A[i] + 0.5f * B[i];
        }
    }
}
```

These are two different loops that the compiler can vectorize. 

Both GCC and Clang can autovectorize this loop, but the output is slightly different, performance may vary depending on the flags used and the exact nature of the loop.

However, the loop below is autovectorized by Clang but it is not autovectorized by GCC. 

```C
void addvecweight2(float *restrict C, float *A, float *B,
                    size_t N, float weight) {
    for (size_t i=0; i < N; i++) {
        if (A[i] < 0.5f)
            C[i] = A[i] + B[i];
        else
            C[i] = 1.5f*A[i] + 0.5f * B[i];
    }
}
```

The situation is similar with `switch` statements. If the condition expression is loop-invariant, that is if it does not depend on the loop variable or the elements involved in each iteration, it can be autovectorized.

This example is autovectorized:

```C
void addvecweight(float *restrict C, float *A, float *B,
                    size_t N, int w) {
    for (size_t i=0; i < N; i++) {
        switch (w) {
        case 1:
            C[i] = A[i] + B[i];
            break;
        case :
            C[i] = 1.5f*A[i] + 0.5f * B[i];
            break;
        default:
            break;
        }
    }
}
```

This example is not autovectorized: 

```C
#define sign(x) (x > 0) ? 1 : ((x < 0) ? -1 : 0)

void addvecweight(float *restrict C, float *A, float *B,
                    size_t N, int w) {
    for (size_t i=0; i < N; i++) {
        switch (sign(A[i])) {
        case 1:
            C[i] = 0.5f * A[i] + 1.5f * B[i];
            break;
        case -1:
            C[i] = 1.5f * A[i] + 0.5f * B[i];
            break;
        default:
            C[i] = A[i] + B[i];
            break;
        }
    }
}
```

The cases you have seen so far are generic, they work the same for any architecture. 

In the next section, you will see Arm-specific cases for autovectorization.