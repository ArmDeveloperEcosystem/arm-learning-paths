---
title: Build the example application

description: Build and run a scalar C++ dot-product application on an Arm Linux server for profiling with Arm Performix.

weight: 3

layout: learningpathall
---

## Create the source file

To explore Performix, you can build and profile a small C++ program that computes the dot product of two large floating-point arrays:

```cpp
sum += a[i] * b[i];
```

This performs one multiply and one add per loop iteration. The dot product pattern is common in machine learning inference, signal processing, and linear algebra, making it a good candidate for performance analysis.

SSH into your target:

```bash
ssh username@your-server
```

On the target, create a new directory for your project and navigate to it:

```bash
mkdir performix-analysis
cd performix-analysis
```

Use a text editor to create a C++ source file named `scalar_dot_product.cpp` with the following content:

```cpp
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <random>

#if defined (__GNUC__) || defined (__clang__)
#define NOINLINE __attribute__ ((noinline))
#else
#define NOINLINE
#endif

#if defined (__GNUC__) || defined (__clang__)
#define RESTRICT __restrict__
#else
#define RESTRICT
#endif

static void* aligned_malloc(std::size_t alignment, std::size_t size) {
#if (__cplusplus >= 201703L)
  std::size_t padded = (size + alignment - 1) / alignment * alignment;
  return std::aligned_alloc(alignment, padded);
#else
  void* p = nullptr;
  if (posix_memalign(&p, alignment, size) != 0) return nullptr;
  return p;
#endif
}

NOINLINE float dot_scalar(const float* RESTRICT a, const float* RESTRICT b, std::size_t n) {
 float sum = 0.0f;
 for (std::size_t i = 0; i < n; ++i) {
   sum += a[i] * b[i];
 }
 return sum;
}

static NOINLINE float run_bench(const float* a, const float* b, std::size_t n, int iters) {
 volatile float sink = 0.0f;
 for (int i = 0; i < iters; ++i) {
   sink += dot_scalar(a, b, n);
 }
 return sink;
}

int main(int argc, char** argv) {
 std::size_t n = (argc > 1) ? std::stoull(argv[1]) : (64ull * 1024ull * 1024ull);
 int iters = (argc > 2) ? std::stoi(argv[2]) : 10; 

 float* a = static_cast<float*>(aligned_malloc(64, n * sizeof(float)));
 float* b = static_cast<float*>(aligned_malloc(64, n * sizeof(float)));
 if (!a || !b) {
   std::cerr << "Allocation failed\n";
   return 1;
 }

 std::mt19937 rng(123);
 std::uniform_real_distribution<float> dist(0.0f, 1.0f);
 for (std::size_t i = 0; i < n; ++i) {
   a[i] = dist(rng);
   b[i] = dist(rng);
 }

 (void)run_bench(a, b, std::min<std::size_t>(n, 1ull * 1024ull * 1024ull), 2);
 auto t0 = std::chrono::high_resolution_clock::now();
 float r = run_bench(a, b, n, iters);
 auto t1 = std::chrono::high_resolution_clock::now();
 std::chrono::duration<double> dt = t1 - t0;

 std::cout << "scalar time=" << dt.count() << "s (sink=" << r << ")\n";

 std::free(a);
 std::free(b);
 return 0;
}
```

## Compile the program

Compile the program with the following flags to keep the code purely scalar and enable profiling support:

```bash
g++ -O3 -g -fno-omit-frame-pointer -fno-tree-vectorize -mcpu=native -std=c++17 scalar_dot_product.cpp -o dot_scalar
```

The flags do the following:

- `-O3`: enables high-level optimizations
- `-g`: includes debug symbols for source-level attribution
- `-fno-omit-frame-pointer`: preserves call stacks for profiling
- `-fno-tree-vectorize`: prevents compiler auto-vectorization
- `-mcpu=native`: tunes the code for the target CPU

{{% notice Note %}}
The `-fno-tree-vectorize` flag is used here for learning purposes only. It forces the compiler to produce scalar code, so you can observe the performance difference when you manually optimize with Neon intrinsics later. In most cases, you'd let the compiler auto-vectorize.
{{% /notice %}}

## Verify the program runs

Run the program to confirm it executes correctly:

```bash
./dot_scalar
```

The output is similar to:

```output
scalar time=1.234s (sink=1.67772e+07)
```

The exact values depend on your hardware, but you should see a time and sink value printed without errors.

## What you've accomplished and what's next

You now have a working C++ application on your target.

Next, you'll use the Code Hotspots recipe in Arm Performix to identify which functions consume the most CPU time.
