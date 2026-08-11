---
title: Optimize with NEON intrinsics

weight: 7

layout: learningpathall
---
Let's optimize the scalar dot-product loop using Arm NEON intrinsics to improve instruction efficiency. By introducing data-level parallelism, you can reduce the number of instructions required per element and relieve frontend pressure.

The key changes are:

- **Data-Level Parallelism**: The NEON implementation processes 4 elements per instruction using Advanced SIMD instructions.
- **Fused Multiply-Add**: Increases efficiency by combining multiplication and addition into a single instruction.
- **SIMD Pipelines**: Actively used to improve instruction efficiency.

There are no changes to memory access pattern, branch structure or working set size.

## Implementing NEON Optimization

1. Create a new C++ source file named `dot_neon_optimized.cpp` and copy the following code into it:

  ```cpp
  #include <arm_neon.h>
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

  NOINLINE float dot_neon(const float* RESTRICT a, const float* RESTRICT b, std::size_t n) {
   float32x4_t acc = vdupq_n_f32(0.0f);

    std::size_t i = 0;
    for (; i + 4 <= n; i += 4) {
     float32x4_t va = vld1q_f32(a + i);
     float32x4_t vb = vld1q_f32(b + i);
  #if defined (__aarch64__)
      acc = vfmaq_f32(acc, va, vb);
  #else
     acc = vmlaq_f32(acc, va, vb);
  #endif
   }

  #if defined (__aarch64__)
   float sum = vaddvq_f32(acc);
  #else
    float32x2_t tmp = vadd_f32(vget_low_f32(acc), vget_high_f32(acc));
    tmp = vpadd_f32(tmp, tmp);
    float sum = vget_lane_f32(tmp, 0);
  #endif

    for (; i < n; ++i) sum += a[i] * b[i];
    return sum;
  }

  static NOINLINE float run_bench(const float* a, const float* b, std::size_t n, int iters) {
    volatile float sink = 0.0f;
    for (int i = 0; i < iters; ++i) {
     sink += dot_neon(a, b, n);
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

   std::cout << "neon time=" << dt.count() << "s (sink=" << r << ")\n";

    std::free(a);
    std::free(b);
    return 0;
  }
  ```

2. Compile the optimized C++ workload with the following command:

  ```bash
  g++ -O3 -g -fno-omit-frame-pointer -mcpu=native -std=c++17 dot_neon_optimized.cpp -o dot_neon
  ```
  
With the NEON optimization implemented, you're ready to compare the performance of the scalar and optimized versions using Arm Performix.
