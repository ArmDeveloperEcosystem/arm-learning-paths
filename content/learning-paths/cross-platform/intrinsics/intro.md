---
layout: learningpathall
title: Code Migration to Arm
weight: 2
---

## Migration

Migrating C/C++ applications from x64 to Arm requires recompiling the source code for the Arm architecture. A simple recompile works much of the time, but not always.

SIMD extensions are one of the common barriers encountered when porting C/C++ applications from x64 to Arm. This article is a short background on intrinsics and how to identify them in code. This Learning Path presents options for how to get the code compiled and running on an Arm-based platform.

## Intrinsics

Intrinsics are functions which are built into the compiler and not part of a library. They look like function calls, but don’t require an actual function call. When the compiler encounters intrinsics it directly substitutes a sequence of instructions. Intrinsics are often used to access special instructions that don’t have a direct mapping from C/C++ or when performance optimization is needed.

One use of intrinsics is to access SIMD (single-instruction, multiple-data) instructions directly from C/C++ for improved application performance. Intrinsics are easier to work with compared to assembly language, but they often pose a challenge when porting source code to a new architecture.

Intel Streaming SIMD Extensions (SSE) and [Arm NEON](https://developer.arm.com/documentation/dht0002/a/Introducing-NEON/NEON-architecture-overview/NEON-instructions) SIMD instructions increase processor throughput by performing multiple computations with a single instruction. Over the years, Intel and Arm have introduced a variety of SIMD extensions. NEON is used in many of the Arm Cortex-A, Cortex-R, and Neoverse processors.

There are generally 3 ways to program SIMD hardware:
- The C/C++ compiler recognizes opportunities to use SIMD instructions and inserts them automatically (with or without some guidance)
- Intrinsics to access SIMD instructions directly from C/C++ source code
- Assembly programming

## Source code example

Below is a small example application containing intrinsics.

The source code comes from a [short course titled Efficient Vectorisation with C++](https://chryswoods.com/vector_c++/emmintrin.html) and is copyright (C) Christopher Woods, 2006-2015.\
It is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

This example can be used to show how to port such code to Arm.

Copy the source code into a file named `sse.cpp`.

```cpp { file_name="sse.cpp" }
#include <iostream>

#ifdef __SSE2__
  #include <emmintrin.h>
#else
  #warning SSE2 support is not available. Code will not compile
#endif

int main(int argc, char **argv)
{
    __m128 a = _mm_set_ps(4.0, 3.0, 2.0, 1.0);
    __m128 b = _mm_set_ps(8.0, 7.0, 6.0, 5.0);

    __m128 c = _mm_add_ps(a, b);

    float d[4];
    _mm_storeu_ps(d, c);

    std::cout << "result equals " << d[0] << "," << d[1]
              << "," << d[2] << "," << d[3] << std::endl;

    return 0;
}
```
## Understand the code

There is a reference to the `__SSE2__` preprocessor define and the `emmintrin.h` header file. These are architecture specific extensions.

The function calls starting with `_mm` are [Intel SSE intrinsics](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html).

## Run the example on x86_64

You can build this example on an `x86_64` machine.

If not already installed, install `g++` with the following command (on Ubuntu):

```bash { target="amd64/ubuntu:latest" }
sudo apt install -y g++
```

Build the code with:
```bash { target="amd64/ubuntu:latest" }
g++ -O2 -msse2 --std=c++14 sse.cpp -o sse
```

Run the code:
```bash { target="amd64/ubuntu:latest" }
./sse
```

and observe the output:
```output
result equals 6,8,10,12
```

Unsurprisingly, the code will fail to build as is on an Arm based machine.

The next sections will show how to migrate this application to Arm Neon.
