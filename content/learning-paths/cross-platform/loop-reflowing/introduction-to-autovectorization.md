---
title: An introduction to autovectorization
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Vectorization and autovectorization

CPU time is mostly spent executing code inside loops. Almost all software, especially software that performs time-consuming calculations, be it image/video processing, games, scientific software or even AI, revolves around a few loops that do most of the calculations and the majority of the code is executed only from within those loops.

With the advent of SIMD and Vector engines in modern CPUs (like Neon and SVE), specialized instructions became available to developers to improve performance and efficiency of those loops. However the loops themselves had to be adapted to allow the use of those instructions. The process of this adaptation is called *Vectorization* and most SIMD developers are familiar with it and it is a synonym with SIMD optimization.

Depending on the actual loop and the operations involved, vectorization can be possible -even with adaptations- or impossible and respectively the loop can be identified as vectorizable or non-vectorizable.

Consider the following simple loop:

```C
#include <stdint.h>
#include <stdlib.h>

#define N 100

void addmat(float *C, float *A, float *B) {
    for (size_t i=0; i < N; i++) {
    	C[i] = A[i] + B[i];
    }
}

int main() {
    float A[N], B[N], C[N];

    addmat(C, A, B);
}
```

Save this file as `addmat.c`.

This is practically the most referred-to example with regards to vectorization, because it is easy to explain. For Advanced SIMD/Neon the vectorized form is the following:

```C
#include <stdint.h>
#include <stdlib.h>
#include <arm_neon.h>

#define N 100

void addmat(float *C, float *A, float *B) {
    for (size_t i=0; i < N; i+= 4) {
    	float32x4_t va = vld1q_f32(&A[i]);
		float32x4_t vb = vld1q_f32(&B[i]);
		float32x4_t vc = vaddq_f32(va, vb);
		vst1q_f32(&C[i], vc);
    }
}

int main() {
    float A[N], B[N], C[N];

    addmat(C, A, B);
}
``` 

Save this file as `addmat_neon.c`.

As you understand, vectorizing a loop can be quite a difficult task that takes time and very specialized knowledge, not only particular to a specific architecture but to the specific SIMD engine and revision. For many developers it is such a daunting task that automating this process became the holy grail for many developers. Enabling the compiler to perform automatic adaptation of the loop in order to be vectorizable and use SIMD instructions is called *Autovectorization*. 

Autovectorization in compilers is being developed for the past 20 years, however recent advances in both major compilers (LLVM and gcc) have started to render autovectorization a viable alternative to hand-written SIMD code for more than just the basic loops. Some loop types are still not detected as autovectorizable and it is not directly obvious which kinds of loops are autovectorizable and which are not.

As it is a constantly advancing field, it is not easy to keep track of what the current compiler supports with regards to autovectorization. It is a very highly advanced Computer Science topic that involves subjects such as Graph Theories, Compilers and deep understanding of each architecture and the respective SIMD engines and the number of people that are experts is extremely small.

In this Learning Path, we will help with demonstrating autovectorization through examples and identifying how to adapt some loops to enable autovectorization in the compiler, on both Advanced SIMD and SVE/SVE2 systems.



