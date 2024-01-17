---
title: Autovectorization limits
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Autovectorization is not as easy as adding a flag like `restrict` in the arguments list. 

There are some requirements for autovectorization to be enabled. Some of the requirements with examples are shown below.

#### Countable loops

A countable loop is a loop where the number of iterations is known before the loop begins executing.

Countable loops means the following can be vectorized:

```C
for (size_t i=0; i < N; i++) {
    C[i] = A[i] + B[i];
}
```

This loop is not countable and cannot be vectorized:

```C
i = 0;
while(1) {
    C[i] = A[i] + B[i];
    i++;
    if (condition) break;
}
```

If the `while` loop is actually a countable loop in disguise, then the loop might be vectorizable. 

For example, this loop is vectorizable:

```C
i = 0;
while(1) {
    C[i] = A[i] + B[i];
    i++;
    if (i >= N) break;
}
```

This loop is not vectorizable:

```C
i = 0;
while(1) {
    C[i] = A[i] + B[i];
    i++;
    if (C[i] > 0) break;
}
```

#### No function calls inside the loop

If `f()` and `g()` are functions that take `float` arguments this loop cannot be autovectorized:

```C
for (size_t i=0; i < N; i++) {
    C[i] = f(A[i]) + g(B[i]);
}
```

There is a special case of the math library trigonometry and transcendental functions (like `sin`, `cos`, `exp`, etc). There is work underway to enable these functions to be autovectorized, as the compiler will use their vectorized counterparts in the `mathvec` library (`libmvec`).

The loop below is *already autovectorized* in current gcc trunk for Arm (note you have to add `-Ofast` to the compilation flags to enable autovectorization):

```C
void addfunc(float *restrict C, float *A, float *B, size_t N) {
    for (size_t i=0; i < N; i++) {
        C[i] = cosf(A[i]) + sinf(B[i]);
    }
}
```

This feature will be in gcc 14 and require a new glibc version 2.39 as well. Until then, if you are using a released compiler as part of a Linux distribution (such as gcc 13.2), you will need to manually vectorize such code for performance.

There is more about autovectorization of conditionals in the next section.

#### No branches in the loop and no if/else/switch statements

This is not universally true, there are cases where branches can actually be vectorized. 

In the case of SVE/SVE2 on Arm, predicates will actually make this easier and remove or minimize these limitations at least in some cases. There is currently work in progress to enable the use of predicates in such loops. SVE/SVE2 autovectorization and predicates is a good topic for a future Learning Path. 

There is more information on this in the next section.

#### Only inner-most loops will be vectorized.

Consider the following nested loop:

```C
for (size_t i=0; i < N; i++) {
    for (size_t j=0; j < M; j++) {
       C[i][j] = A[i][j] + B[i][j];
    }
}
```

In this case, only the inner loop will be vectorized, again provided all the other conditions also apply (no branches and the inner loop is countable).

There are some cases where outer loop types are autovectorized, but these are not covered in this Learning Path.

#### No data inter-dependency between iterations

This means that each iteration depends on the result of the previous iteration. This example is difficult, but not impossible to autovectorize. 

The loop below cannot be autovectorized as it is. 

```C
for (size_t i=1; i < N; i++) {
    C[i] = A[i] + B[i] + C[i-1];
}
```
