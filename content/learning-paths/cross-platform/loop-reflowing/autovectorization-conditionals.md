---
title: Autovectorization and conditionals
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Autovectorization and conditionals 

In the previous section we mentioned that compilers cannot autovectorize loops with branches. In this section, you will see that in more detail, when is it possible to enable the vectorizer in the compiler by adapting the loop and when it is required to modify the algorithm or write manually optimized code.

### If/else/switch in loops

Consider the following function, a modified form of the previous function that uses weighted coefficients for `A[i]`.

```C
void addmatweight(float *restrict C, float *A, float *B,
                    size_t N, float weight) {
    for (size_t i=0; i < N; i++) {
        if (weight < 0.5f)
            C[i] = A[i] + B[i];
        else
            C[i] = 1.5f*A[i] + 0.5f * B[i];
    }
}
```

You would tempted to think that this loop cannot be vectorized. Such loops are not that uncommon and compilers have a difficult time understanding the pattern and transforming them to vectorizeable forms, when it is possible. However, this is actually a vectorizable loop, as the conditional can actually be moved out of the loop, as this is a loop-invariant conditional. Essentially the compiler would transform -internally- the loop in something like the following:

```C
void addmatweight(float *restrict C, float *A, float *B, size_t N) {
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

which is in essence, two different loops and we know that the compiler can vectorize them. Both gcc and llvm can actually autovectorize this loop, but the output is slightly different, performance may actually vary depending on the flags used and the exact nature of the loop.

However, something like the following is not yet autovectorized by all compilers (llvm/clang autovectorizes this loop, but not gcc):

```C
void addmatweight2(float *restrict C, float *A, float *B,
                    size_t N, float weight) {
    for (size_t i=0; i < N; i++) {
        if (A[i] < 0.5f)
            C[i] = A[i] + B[i];
        else
            C[i] = 1.5f*A[i] + 0.5f * B[i];
    }
}
```

Similarly with `switch` statements, if the condition expression in loop-invariant, that is if it does not depend on the loop variable or the elements involved in each iteration.
For this reason we know that this loop is actually autovectorized:

```C
void addmatweight(float *restrict C, float *A, float *B,
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

But this one is not:

```C
#define sign(x) (x > 0) ? 1 : ((x < 0) ? -1 : 0)

void addmatweight(float *restrict C, float *A, float *B,
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

The cases you have seen so far are generic, they will work in other architectures besides Arm. In the next section, you will see Arm-specific usecases for autovectorization.