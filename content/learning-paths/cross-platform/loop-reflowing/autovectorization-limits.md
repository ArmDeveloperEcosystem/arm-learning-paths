---
title: Autovectorization limits
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Autovectorization limits

Autovectorization is not as easy as adding a flag like `restrict` in the arguments list. There are some requirements for autovectorization to be enabled, namely:

* The loops have to be countable

This means that the following can be vectorized:

```C
    for (size_t i=0; i < N; i++) {
        C[i] = A[i] + B[i];
    }
```

but this one cannot be vectorized:

```C
    i = 0;
    while(true) {
        C[i] = A[i] + B[i];
        i++;
        if (condition) break;
    }
```

Having said that, if condition is such that the `while` loop is actually a countable loop in disguise, then the loop might be vectorizable. For example, this loop will *actually be vectorized*:

```C
    i = 0;
    while(1) {
        C[i] = A[i] + B[i];
        i++;
        if (i >= N) break;
    }
```
but this one will not be vectorizable:

```C
    i = 0;
    while(1) {
        C[i] = A[i] + B[i];
        i++;
        if (C[i] > 0) break;
    }
```

* No function calls inside the loop

For example if, `f()`, `g()` are functions that take `float` arguments, this loop cannot be autovectorized:

```C
    for (size_t i=0; i < N; i++) {
        C[i] = f(A[i]) + g(B[i]);
    }
```

There is a special case of the math library trigonometry and transcendental functions (like `sin`, `cos`, `exp`, etc). There is progress underway to enable these functions to be autovectorized, as the compiler will be able to use their vectorized counterparts in `mathvec` library (`libmvec`).

So for example, something like the following is actually *already autovectorized* in current gcc trunk for Arm (note you have to add `-Ofast` to compilation flags to enable such autovectorization):

```C
void addfunc(float *restrict C, float *A, float *B, size_t N) {
    for (size_t i=0; i < N; i++) {
        C[i] = cosf(A[i]) + sinf(B[i]);
    }
}
```

This will be in gcc 14 and require a new glibc as well (2.39). Until these are released, if you are using a released compiler as part of a distribution (gcc 13.2 at the time of writing), you will have to manually vectorize such code for performance.

We will expand on autovectorization of conditionals in the next section.

* In general, no branches in the loop, no if/else/switch

This is not universally true, there are cases where branches can actually be vectorized, we will expand this in the next section.
And in the case of SVE/SVE2 on Arm, predicates will actually make this easier and remove or minimize these limitations at least in some cases. There is currently work in progress on the compiler front to enable the use of predicates in such loops. We will probably return with a new LP to explain SVE/SVE2 autovectorization and predicates in more depth.

* Only inner-most loops will be vectorized.

To clarify, consider the following nested loop:

```C
    for (size_t i=0; i < N; i++) {
        for (size_t j=0; j < M; j++) {
           C[i][j] = A[i][j] + B[i][j];
        }
    }
```

In such a case, only the inner loop will be vectorized, again provided all the other conditions also apply (no branches and the inner loop is countable). 
In fact, there are some cases where outer loop types are also autovectorized, but these are outside the scope of this LP.

* No data inter-dependency between iterations

This means that each iteration depends on the result of the previous iteration. Such a problem is difficult -but not impossible- to autovectorize. Consider the following example:

```C
    for (size_t i=1; i < N; i++) {
        C[i] = A[i] + B[i] + C[i-1];
    }
```

This example cannot be autovectorized as it is. 