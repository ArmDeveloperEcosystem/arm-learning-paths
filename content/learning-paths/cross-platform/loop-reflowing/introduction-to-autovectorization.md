---
title: An introduction to autovectorization
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

You should have an Arm system with either the gcc or Clang compiler installed. The examples use gcc as the compiler but you can also use Clang. Refer to the [GNU compiler](/install-guides/gcc/native/) install guide for instructions.

## Introduction to autovectorization

CPU time is often spent executing code inside loops. Software that performs time-consuming calculations in image/video processing, games, scientific software, and AI, often revolves around a few loops doing most of the calculations.

With the advent of single instruction, multiple data (SIMD) processing and vector engines in modern CPUs (like Neon and SVE), specialized instructions are available to improve the performance and efficiency of loops. However, the loops themselves need to be adapted to use SIMD instructions. The adaptation process is called *__vectorization__* and is synonymous with SIMD optimization.

Depending on the actual loop and the operations involved, vectorization is either possible or not and the loop is labeled as vectorizable or non-vectorizable.

Consider the following simple loop which adds 2 vectors:

```C
#include <stdint.h>
#include <stdlib.h>

#define N 100

void addvec(float *C, float *A, float *B) {
    for (size_t i=0; i < N; i++) {
    	C[i] = A[i] + B[i];
    }
}

int main() {
    float A[N], B[N], C[N];

    addvec(C, A, B);
}
```

Use a text editor to copy the code above and save it as `addvec.c`.

This is the most referred-to example with regards to vectorization because it is easy to explain. 

For Advanced SIMD/Neon, the vectorized form is the following:

```C
#include <stdint.h>
#include <stdlib.h>
#include <arm_neon.h>

#define N 100

void addvec(float *C, float *A, float *B) {
    for (size_t i=0; i < N; i+= 4) {
    	float32x4_t va = vld1q_f32(&A[i]);
		float32x4_t vb = vld1q_f32(&B[i]);
		float32x4_t vc = vaddq_f32(va, vb);
		vst1q_f32(&C[i], vc);
    }
}

int main() {
    float A[N], B[N], C[N];

    addvec(C, A, B);
}
``` 

Save the second example as `addvec_neon.c`.

As you can see, vectorizing a loop can be a difficult task that takes time and very specialized knowledge. The knowledge is specific to the architecture, the SIMD engine, and sometimes the revision of the SIMD engine. 

For many developers, vectorizing is a daunting task. Automating the process is one of the biggest milestones in compiler advancement in many years. Enabling the compiler to perform automatic adaptation of the loop in order to be vectorizable and use SIMD instructions is called *__autovectorization__*. 

Autovectorization in compilers has been in development for the past 20 years. However, recent advances in both major compilers (Clang and GCC) have started to render autovectorization a viable alternative to hand-written SIMD code for more than just the basic loops. Some loop types are still not detected as autovectorizable, and it is not directly obvious which kinds of loops are autovectorizable and which are not.

As a constantly advancing field, it is not easy to keep track of compiler support for autovectorization. It is an advanced Computer Science topic that involves the subjects of graph theory, compilers, and a deep understanding of each architecture and the respective SIMD engines. The number of experts in the field is extremely small.

In this Learning Path, you will learn about autovectorization through examples and identify how to adapt some loops to enable autovectorization.



