---
title: Example workload

weight: 4

layout: learningpathall
---
To demonstrate how Performix helps uncover real performance issues, we’ll use a deliberately simple workload: a vector dot product. The benchmark computes the dot product of two large floating-point arrays:

```
sum += a[i] * b[i];
```

It performs one multiply and one add per loop iteration, simple, predictable, and seemingly efficient. This pattern appears in real-world applications everywhere:

* Machine learning inference
* Signal processing
* Linear algebra
* Analytics pipelines

## Prepare the workload

1. Create a new directory for your project and navigate to it:

  ```bash
  mkdir performix-analysis
  cd performix-analysis
  ```

2. Create a C++ source file named `dot_scalar_problem.cpp` and copy the following code into it:

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

3. Compile the C++ workload with the following command to ensure it remains purely scalar:

  ```bash
  g++ -O3 -g -fno-omit-frame-pointer -fno-tree-vectorize -mcpu=native -std=c++17 dot_scalar_problem.cpp -o dot_scalar
  ```

  Key Compiler Flags

  - `-O3`: Enables high-level optimizations.
  - `-g`: Includes debug symbols for source-level attribution.
  - `-fno-omit-frame-pointer`: Preserves call stacks for profiling.
  - `-fno-tree-vectorize`: Prevents compiler auto-vectorization.
  - `-mcpu=native`: Tunes the code for the target CPU.

4. Copy the compiled file to the target machine.

  ```bash
  scp dot_scalar <target_machine_location>
  ```

Now you're ready to start analyzing the workload using Arm Performix.
