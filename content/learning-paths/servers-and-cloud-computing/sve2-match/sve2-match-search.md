---
# User change
title: "Compare performance of different Search implementations"

weight: 2

layout: "learningpathall"


---
## Introduction

Searching for specific values in large arrays is a fundamental operation in many applications, from databases to text processing. The performance of these search operations can significantly impact overall application performance, especially when dealing with large datasets.

In this learning path, you will learn how to use the SVE2 MATCH instructions available on Arm Neoverse V2 based AWS Graviton4 processors to optimize search operations in byte and half word arrays. You will compare the performance of scalar and SVE2 MATCH implementations to demonstrate the significant performance benefits of using specialized vector instructions.

## What is SVE2 MATCH?

SVE2 (Scalable Vector Extension 2) is an extension to the Arm architecture that provides vector processing capabilities with a length-agnostic programming model. The MATCH instruction is a specialized SVE2 instruction that efficiently searches for elements in a vector that match any element in another vector.

## Set Up Your Environment

To follow this learning path, you will need:

1. An AWS Graviton4 instance running `Ubuntu 24.04`. 
2. GCC compiler with SVE support

Let's start by setting up our environment:

```bash
sudo apt-get update
sudo apt-get install -y build-essential gcc g++
```
An effective way to achieve optimal performance on Arm is not only through optimal flag usage, but also by using the most 
recent compiler version. This Learning path was tested with GCC 13 which is the default version on `Ubuntu 24.04` but you 
can run it with newer versions of GCC as well.

Create a directory for our implementations:
```bash
mkdir -p sve2_match_demo
cd sve2_match_demo
```
## Understanding the Problem

Our goal is to implement a function that searches for any occurrence of a set of keys in an array. The function should return true if any element in the array matches any of the keys, and false otherwise.

This type of search operation is common in many applications:

1. **Database Systems**: Checking if a value exists in a column
2. **Text Processing**: Finding specific characters in a text
3. **Network Packet Inspection**: Looking for specific byte patterns
4. **Image Processing**: Finding specific pixel values

## Implementing Search Algorithms

Let's implement three versions of our search function:

### 1. Generic Scalar Implementation

Create a generic implementation in C, checking each element individually against each key. Open a editor of your choice and copy the code shown into a file named `sve2_match_demo.c`:

```c
#include <arm_sve.h>
#include <inttypes.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int search_generic_u8(const uint8_t *hay, size_t n, const uint8_t *keys,
                      size_t nkeys) {
  for (size_t i = 0; i < n; ++i) {
    uint8_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
return 0;
}

int search_generic_u16(const uint16_t *hay, size_t n, const uint16_t *keys,
                       size_t nkeys) {
  for (size_t i = 0; i < n; ++i) {
    uint16_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}
```
The `search_generic_u8()` and `search_generic_u16()` functions both return 1 immediately when a match is found in the inner loop.

### 2. SVE2 MATCH Implementation

Now create an implementation that uses SVE2 MATCH instructions to process multiple elements in parallel. Copy the code shown into the same file:

```c
int search_sve2_match_u8(const uint8_t *hay, size_t n, const uint8_t *keys,
                         size_t nkeys) {
  if (nkeys == 0) return 0;
  const size_t VL = svcntb();
  svbool_t pg = svptrue_b8();
  uint8_t tmp[256];
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint8_t keyvec = svld1(pg, tmp);
  size_t i = 0;
  for (; i + VL <= n; i += VL) {
    svuint8_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u8(pg, block, keyvec))) return 1;
  }
for (; i < n; ++i) {
    uint8_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}

int search_sve2_match_u16(const uint16_t *hay, size_t n, const uint16_t *keys,
                          size_t nkeys) {
  if (nkeys == 0) return 0;
  const size_t VL = svcnth();
  svbool_t pg = svptrue_b16();
  uint16_t tmp[128];
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint16_t keyvec = svld1(pg, tmp);
  size_t i = 0;
  for (; i + VL <= n; i += VL) {
    svuint16_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u16(pg, block, keyvec))) return 1;
  }
  for (; i < n; ++i) {
    uint16_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}
```
The SVE MATCH implementation with the `search_sve2_match_u8()` and `search_sve2_match_u16()` functions provide an efficient vectorized search approach with these key technical aspects:
   - Uses SVE2's specialized MATCH instruction to compare multiple elements against multiple keys in parallel
   - Leverages hardware-specific vector length through svcntb() for scalability
   - Prepares a vector of search keys that's compared against blocks of data
   - Processes data in vector-sized chunks with early termination when matches are found. Stops immediately when any element in the vector matches.
   - Falls back to scalar code for remainder elements

### 3. Optimized SVE2 MATCH Implementation

In this next SVE2 implementation you will add loop unrolling and prefetching to further improve performance. Copy the code shown into the same source file:

```c
int search_sve2_match_u8_unrolled(const uint8_t *hay, size_t n, const uint8_t *keys,
                                 size_t nkeys) {
  if (nkeys == 0) return 0;
  const size_t VL = svcntb();
  svbool_t pg = svptrue_b8();
  
  // Prepare key vector
  uint8_t tmp[256] __attribute__((aligned(64)));
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint8_t keyvec = svld1(pg, tmp);
  
  size_t i = 0;
  // Process 4 vectors per iteration
  for (; i + 4*VL <= n; i += 4*VL) {
    // Prefetch data ahead
    __builtin_prefetch(&hay[i + 16*VL], 0, 0);
    
    svuint8_t block1 = svld1(pg, &hay[i]);
    svuint8_t block2 = svld1(pg, &hay[i + VL]);
    svuint8_t block3 = svld1(pg, &hay[i + 2*VL]);
    svuint8_t block4 = svld1(pg, &hay[i + 3*VL]);
    
    svbool_t match1 = svmatch_u8(pg, block1, keyvec);
    svbool_t match2 = svmatch_u8(pg, block2, keyvec);
    svbool_t match3 = svmatch_u8(pg, block3, keyvec);
    svbool_t match4 = svmatch_u8(pg, block4, keyvec);
    
    if (svptest_any(pg, match1) || svptest_any(pg, match2) || 
        svptest_any(pg, match3) || svptest_any(pg, match4))
      return 1;
}
  
  // Process remaining vectors one at a time
  for (; i + VL <= n; i += VL) {
    svuint8_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u8(pg, block, keyvec))) return 1;
  }
  
  // Handle remainder
  for (; i < n; ++i) {
    uint8_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}

// Optimized 16-bit version with unrolling
int search_sve2_match_u16_unrolled(const uint16_t *hay, size_t n, const uint16_t *keys,
                                  size_t nkeys) {
  if (nkeys == 0) return 0; 
  const size_t VL = svcnth();
  svbool_t pg = svptrue_b16();
    
  // Prepare key vector
  uint16_t tmp[128] __attribute__((aligned(64)));
  for (size_t i = 0; i < VL; ++i) tmp[i] = keys[i % nkeys];
  svuint16_t keyvec = svld1(pg, tmp);
    
  size_t i = 0;
  // Process 4 vectors per iteration
  for (; i + 4*VL <= n; i += 4*VL) {
    // Prefetch data ahead
    __builtin_prefetch(&hay[i + 16*VL], 0, 0);

    svuint16_t block1 = svld1(pg, &hay[i]);
    svuint16_t block2 = svld1(pg, &hay[i + VL]);
    svuint16_t block3 = svld1(pg, &hay[i + 2*VL]);
    svuint16_t block4 = svld1(pg, &hay[i + 3*VL]);

    svbool_t match1 = svmatch_u16(pg, block1, keyvec);
    svbool_t match2 = svmatch_u16(pg, block2, keyvec);
    svbool_t match3 = svmatch_u16(pg, block3, keyvec);
    svbool_t match4 = svmatch_u16(pg, block4, keyvec);

if (svptest_any(pg, match1) || svptest_any(pg, match2) ||
        svptest_any(pg, match3) || svptest_any(pg, match4))
      return 1;
  }

  // Process remaining vectors one at a time
  for (; i + VL <= n; i += VL) {
    svuint16_t block = svld1(pg, &hay[i]);
    if (svptest_any(pg, svmatch_u16(pg, block, keyvec))) return 1;
  }

  // Handle remainder
  for (; i < n; ++i) {
    uint16_t v = hay[i];
    for (size_t k = 0; k < nkeys; ++k)
      if (v == keys[k]) return 1;
  }
  return 0;
}
```
The main highlights of this implementation are:
   - Processes 4 vectors per iteration instead of just one and stops immediately when any match is found in any of the 4 vectors.
   - Uses prefetching (__builtin_prefetch) to reduce memory latency
   - Leverages the svmatch_u8/u16 instruction to efficiently compare each element against multiple keys in a single operation
   - Aligns memory to 64-byte boundaries for better memory access performance

## Benchmarking Framework

To compare the performance of the three implementations, you will use a benchmarking framework that measures the execution time of each implementation. You will also add helper functions for membership testing that are needed to setup the test data with controlled hit rates:

```c
// Timing function
static inline uint64_t nsec_now(void) {
  struct timespec ts;
#if defined(CLOCK_MONOTONIC_RAW)
  clock_gettime(CLOCK_MONOTONIC_RAW, &ts);
#else
  clock_gettime(CLOCK_MONOTONIC, &ts);
#endif
  return (uint64_t)ts.tv_sec * 1000000000ULL + ts.tv_nsec;
}

// ---------------- helper: membership test for RNG fill ----------------------
static int key_in_set_u8(uint8_t v, const uint8_t *keys, size_t nkeys) {
  for (size_t k = 0; k < nkeys; ++k)
    if (v == keys[k]) return 1;
  return 0;
}
static int key_in_set_u16(uint16_t v, const uint16_t *keys, size_t nkeys) {
  for (size_t k = 0; k < nkeys; ++k)
    if (v == keys[k]) return 1;
  return 0;
}

// Fill such that P(match) ~= p.
static void fill_bytes_lowhit(uint8_t *buf, size_t n, const uint8_t *keys,
                              size_t nkeys, double p) {
  for (size_t i = 0; i < n; ++i) {
    if (drand48() < p) {
      buf[i] = keys[rand() % nkeys];
    } else {
      uint8_t v;
      do { v = (uint8_t)rand(); } while (key_in_set_u8(v, keys, nkeys));
      buf[i] = v;
    }
  }
}
static void fill_u16_lowhit(uint16_t *buf, size_t n, const uint16_t *keys,
                            size_t nkeys, double p) {
  for (size_t i = 0; i < n; ++i) {
    if (drand48() < p) {
      buf[i] = keys[rand() % nkeys];
    } else {
      uint16_t v;
      do { v = (uint16_t)rand(); } while (key_in_set_u16(v, keys, nkeys));
      buf[i] = v;
    }
  }
}

// Main benchmarking function
int main(int argc, char **argv) {
  const size_t len        = (argc > 1) ? strtoull(argv[1], NULL, 0) : (1ull << 26);
  const int    iterations = (argc > 2) ? atoi(argv[2])              : 5;
  const double hit_prob   = (argc > 3) ? atof(argv[3])              : 0.001;

  printf("Haystack length : %zu elements\n", len);
  printf("Iterations      : %d\n", iterations);
  printf("Hit probability : %.6f (%.4f %% )\n\n", hit_prob, hit_prob * 100.0);

  // Initialize data and run benchmarks...
  srand48(42);
  srand(42);
    
  // Align memory to 64-byte boundary for better performance
  uint8_t  *hay8  = aligned_alloc(64, len);
  uint16_t *hay16 = aligned_alloc(64, len * sizeof(uint16_t));
  
  const uint8_t keys8[]   = {0x13, 0x7F, 0xA5, 0xEE, 0x4C, 0x42, 0x01, 0x9B};
  const uint16_t keys16[] = {0x1234, 0x7F7F, 0xA5A5, 0xEEEE, 0x4C4C, 0x4242};
  const size_t NKEYS8  = sizeof(keys8)  / sizeof(keys8[0]);
  const size_t NKEYS16 = sizeof(keys16) / sizeof(keys16[0]);

  fill_bytes_lowhit(hay8,  len, keys8,  NKEYS8,  hit_prob); 
  fill_u16_lowhit(hay16, len, keys16, NKEYS16, hit_prob);

  uint64_t t_gen8 = 0, t_sve8 = 0, t_sve8_unrolled = 0;
  uint64_t t_gen16 = 0, t_sve16 = 0, t_sve16_unrolled = 0;
    
  for (int it = 0; it < iterations; ++it) {
    uint64_t t0;
      
    t0 = nsec_now();
    volatile int r = search_generic_u8(hay8, len, keys8, NKEYS8); (void)r;
    t_gen8 += nsec_now() - t0;
  
   #if defined(__ARM_FEATURE_SVE2)
    t0 = nsec_now();
    r = search_sve2_match_u8(hay8, len, keys8, NKEYS8); (void)r;
    t_sve8 += nsec_now() - t0;

    t0 = nsec_now();
    r = search_sve2_match_u8_unrolled(hay8, len, keys8, NKEYS8); (void)r;
    t_sve8_unrolled += nsec_now() - t0;
#endif

t0 = nsec_now();
    r = search_generic_u16(hay16, len, keys16, NKEYS16); (void)r;
    t_gen16 += nsec_now() - t0;

#if defined(__ARM_FEATURE_SVE2)
    t0 = nsec_now();
    r = search_sve2_match_u16(hay16, len, keys16, NKEYS16); (void)r;
    t_sve16 += nsec_now() - t0;

    t0 = nsec_now();
    r = search_sve2_match_u16_unrolled(hay16, len, keys16, NKEYS16); (void)r;
    t_sve16_unrolled += nsec_now() - t0;
#endif
  }
// ---------- latency results ----------
  printf("Average latency over %d iterations (ns):\n", iterations);
  printf("  generic_u8       : %.2f\n", (double)t_gen8 / iterations);
#if defined(__ARM_FEATURE_SVE2)
  printf("  sve2_u8          : %.2f\n", (double)t_sve8 / iterations);
  printf("  sve2_u8_unrolled : %.2f\n", (double)t_sve8_unrolled / iterations);
  printf("  speed‑up (orig)  : %.2fx\n", (double)t_gen8 / t_sve8);
  printf("  speed‑up (unroll): %.2fx\n\n", (double)t_gen8 / t_sve8_unrolled);
#else
  printf("  (SVE2 path not built)\n\n");
#endif
  printf("  generic_u16      : %.2f\n", (double)t_gen16 / iterations);
#if defined(__ARM_FEATURE_SVE2)
  printf("  sve2_u16         : %.2f\n", (double)t_sve16 / iterations);
  printf("  sve2_u16_unrolled: %.2f\n", (double)t_sve16_unrolled / iterations);
  printf("  speed‑up (orig)  : %.2fx\n", (double)t_gen16 / t_sve16);
  printf("  speed‑up (unroll): %.2fx\n", (double)t_gen16 / t_sve16_unrolled);
#else
  printf("  (SVE2 path not built)\n");
#endif
// ---------- throughput results ----------
  const double elems_total = (double)len * iterations;
  printf("\nThroughput (million items/second):\n");
  double tp_gen8  = elems_total / (t_gen8 / 1e9) / 1e6;
  printf("  generic_u8       : %.2f Mi/s\n", tp_gen8);
#if defined(__ARM_FEATURE_SVE2)
  double tp_sve8 = elems_total / (t_sve8 / 1e9) / 1e6;
  double tp_sve8_unrolled = elems_total / (t_sve8_unrolled / 1e9) / 1e6;
  printf("  sve2_u8          : %.2f Mi/s\n", tp_sve8);
  printf("  sve2_u8_unrolled : %.2f Mi/s\n", tp_sve8_unrolled);
  printf("  speed‑up (orig)  : %.2fx\n", tp_sve8 / tp_gen8);
  printf("  speed‑up (unroll): %.2fx\n\n", tp_sve8_unrolled / tp_gen8);
#else
  printf("  (SVE2 path not built)\n\n");
#endif
  double tp_gen16 = elems_total / (t_gen16 / 1e9) / 1e6;
  printf("  generic_u16      : %.2f Mi/s\n", tp_gen16);
#if defined(__ARM_FEATURE_SVE2)
  double tp_sve16 = elems_total / (t_sve16 / 1e9) / 1e6;
  double tp_sve16_unrolled = elems_total / (t_sve16_unrolled / 1e9) / 1e6;
  printf("  sve2_u16         : %.2f Mi/s\n", tp_sve16);
  printf("  sve2_u16_unrolled: %.2f Mi/s\n", tp_sve16_unrolled);
  printf("  speed‑up (orig)  : %.2fx\n", tp_sve16 / tp_gen16);
  printf("  speed‑up (unroll): %.2fx\n", tp_sve16_unrolled / tp_gen16);
#else
  printf("  (SVE2 path not built)\n");
#endif

  free(hay8);
  free(hay16);
  return 0;
```
## Compiling and Running

You can now compile the different search implementations:

```bash
gcc -O3 -march=armv9-a+sve2 -mcpu=neoverse-v2 sve2_match_demo.c -o sve2_match_demo
```

Now run the benchmark on a dataset of 65,536 elements (2^16) with a 0.001% hit rate:

```bash
./sve2_match_demo $((1<<16)) 3 0.00001
```
The output will look like:

```output
Haystack length : 65536 elements
Iterations      : 3
Hit probability : 0.000010 (0.0010 % )

Average latency over 3 iterations (ns):
  generic_u8       : 79149.33
  sve2_u8          : 1051.00
  sve2_u8_unrolled : 871.67
  speed‑up (orig)  : 75.31x
  speed‑up (unroll): 90.80x

  generic_u16      : 85405.33
  sve2_u16         : 4118.67
  sve2_u16_unrolled: 3137.00
  speed‑up (orig)  : 20.74x
  speed‑up (unroll): 27.23x
```
You can experiment with different haystack lengths, iterations and hit probabilities.

```bash
./sve2_match_demo [length] [iterations] [hit_prob]
```
## Performance Results

When running on a Graviton4 instance with Ubuntu 24.04 and a dataset of 65,536 elements (2^16), you will observe the following results for different hit probabilities:

### Latency (ns per iteration) for Different Hit Rates (8-bit)

| Implementation        | 0% (No Matches) | 0.001%      | 0.01%      | 0.1%      | 1%       |
|-----------------------|-----------------|-------------|------------|-----------|----------|
| Generic Scalar        | 145,042.80      | 79,414.40   | 22,351.20  | 2,244.60  | 332.60   |
| SVE2 MATCH            | 2,180.60        | 1,092.00    | 425.80     | 109.40    | 67.40    |
| SVE2 MATCH Unrolled   | 1,520.20        | 861.60      | 320.20     | 89.60     | 55.60    |

### Latency (ns per iteration) for Different Hit Rates (16-bit)

| Implementation        | 0% (No Matches) | 0.001%     | 0.01%     | 0.1%     | 1%      |
|-----------------------|-----------------|------------|-----------|----------|---------|
| Generic Scalar        | 86,936.80       | 86,882.40  | 33,973.40 | 4,054.80 | 117.60  |
| SVE2 MATCH            | 3,941.40        | 4,012.20   | 1,618.00  | 235.00   | 59.60   |
| SVE2 MATCH Unrolled   | 3,102.00        | 3,192.40   | 1,254.60  | 193.40   | 59.40   |

### Speedup vs Generic Scalar (8-bit)

| Hit Rate | SVE2 MATCH | SVE2 MATCH Unrolled |
|----------|------------|---------------------|
| 0%       | 66.52x     | 95.41x              |
| 0.001%   | 72.72x     | 92.17x              |
| 0.01%    | 52.49x     | 69.80x              |
| 0.1%     | 20.52x     | 25.05x              |
| 1%       | 4.93x      | 5.98x               |

### Speedup vs Generic Scalar (16-bit)

| Hit Rate | SVE2 MATCH | SVE2 MATCH Unrolled |
|----------|------------|---------------------|
| 0%       | 22.06x     | 28.03x              |
| 0.001%   | 21.65x     | 27.22x              |
| 0.01%    | 21.00x     | 27.08x              |
| 0.1%     | 17.25x     | 20.97x              |


### Impact of Hit Rate on Performance
The benchmark results reveal several important insights about the performance characteristics of SVE2 MATCH instructions. The most striking observation is how the performance advantage of SVE2 MATCH varies with the hit rate:

1. **Very Low Hit Rates (0% - 0.001%)**: 
   - For 8-bit data, SVE2 MATCH Unrolled achieves an impressive 90-95x speedup
   - For 16-bit data, the speedup is around 27-28x
   - This is where SVE2 MATCH truly shines, as it can quickly process large chunks of data with few or no matches

2. **Low Hit Rates (0.01%)**: 
   - Still excellent performance with 70x speedup for 8-bit and 27x for 16-bit
   - The vectorized approach continues to be highly effective

3. **Medium Hit Rates (0.1%)**: 
   - Good performance with 25x speedup for 8-bit and 21x for 16-bit
   - Early termination starts to reduce the advantage somewhat

4. **High Hit Rates (1%)**: 
   - Moderate speedup of 6x for 8-bit and 2x for 16-bit
   - With frequent matches, early termination limits the benefits of vectorization

This pattern makes SVE2 MATCH particularly well-suited for applications where matches are rare but important to find, such as:
- Searching for specific patterns in large datasets
- Filtering operations with high selectivity
- Security applications looking for specific signatures

### Benefits of Loop Unrolling

The unrolled implementation consistently outperforms the basic SVE2 MATCH implementation:

1. **Low Hit Rates**: Up to 30% additional speedup
2. **Higher Hit Rates**: 5-20% additional speedup

This demonstrates the value of combining algorithmic optimizations (loop unrolling, prefetching) with hardware-specific instructions for maximum performance.

### Applications of SVE2 MATCH

The SVE2 MATCH instruction can be applied to various real-world scenarios such as:

**Database Systems**

In database systems, MATCH can accelerate:
- String pattern matching in text columns
- Value existence checks in arrays
- Filtering operations in columnar databases

**Text Processing**

For text processing applications, MATCH can speed up:
- Character set membership tests
- Word boundary detection
- Special character identification

**Network Packet Inspection**

In network applications, MATCH can improve:
- Protocol header inspection
- Pattern matching in packet payloads
- Signature-based intrusion detection

**Image Processing**

For image processing, MATCH can accelerate:
- Color palette lookups
- Pixel value classification
- Image mask operations

## Conclusion

The SVE2 MATCH instruction provides a powerful way to accelerate search operations in byte and half word arrays. By implementing these optimizations on Graviton4 instances, you can achieve significant performance improvements for your applications.


