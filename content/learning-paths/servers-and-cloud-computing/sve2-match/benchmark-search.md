---
title: Benchmark scalar and SVE2 MATCH search
description: Compile and benchmark scalar and SVE2 MATCH search implementations on an Arm server to compare their performance.
weight: 4
layout: "learningpathall"
---

## Add the benchmark harness

Add a benchmark harness that times the scalar, SVE2 MATCH, and unrolled SVE2 MATCH implementations. Its helper functions prepare test data with controlled hit rates.

Append the following code to `sve2_match_demo.c`, after the search functions that you added earlier:

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
}
```

## Compile and run the benchmark

You can now compile a binary that's portable across Armv9-A systems with SVE2, while tuning it for a specific Neoverse version:

{{%notice Note%}}

If you're building a binary tuned for a Neoverse V3-based systems such as Arm AGI CPU or AWS Graviton 5, you'll need `gcc` version 15 or later to use the `-mtune=neoverse-v3` option.

{{%/notice%}}

{{< tabpane code=true >}}
{{< tab header="Tune for Neoverse V2" >}}
gcc -O3 -march=armv9-a+sve2 -mtune=neoverse-v2 sve2_match_demo.c -o sve2_match_demo
{{< /tab >}}
{{< tab header="Tune for Neoverse V3" >}}
gcc -O3 -march=armv9-a+sve2 -mtune=neoverse-v3 sve2_match_demo.c -o sve2_match_demo
{{< /tab >}}
{{< /tabpane >}}

Run the benchmark on a dataset of 65,536 elements (2^16) with a 0.001% hit rate for 10,000 iterations:

```bash
./sve2_match_demo $((1<<16)) 10000 0.00001
```

The output is similar to:

```output
Haystack length : 65536 elements
Iterations      : 10000
Hit probability : 0.000010 (0.0010 % )

Average latency over 10000 iterations (ns):
  generic_u8       : 104956.90
  sve2_u8          : 1159.93
  sve2_u8_unrolled : 988.12
  speed‑up (orig)  : 90.49x
  speed‑up (unroll): 106.22x

  generic_u16      : 12506.72
  sve2_u16         : 3841.89
  sve2_u16_unrolled: 2997.85
  speed‑up (orig)  : 3.26x
  speed‑up (unroll): 4.17x

Throughput (million items/second):
  generic_u8       : 624.41 Mi/s
  sve2_u8          : 56499.74 Mi/s
  sve2_u8_unrolled : 66323.93 Mi/s
  speed‑up (orig)  : 90.49x
  speed‑up (unroll): 106.22x

  generic_u16      : 5240.06 Mi/s
  sve2_u16         : 17058.25 Mi/s
  sve2_u16_unrolled: 21860.97 Mi/s
  speed‑up (orig)  : 3.26x
  speed‑up (unroll): 4.17x
```

Use the latency and throughput values in the output to compare the implementations with the sample results that follow.

You can experiment with different haystack lengths, iterations and hit probabilities.

```bash
./sve2_match_demo [length] [iterations] [hit_prob]
```

## Compare benchmark results

The following sample results were collected on an instance powered by AWS Graviton4 (Neoverse V2) with GCC 15.2.0, Ubuntu 24.04, and 65,536 elements (2^16). Your results will vary with the system and hit probability.

### Latency (ns per iteration) for different hit rates (8-bit)

| Implementation        | 0% (No Matches) | 0.001% | 0.01% | 0.1% | 1%  |
|-----------------------|-----------------|--------|-------|------|-----|
| Generic Scalar        | 210,818         | 101,721 | 23,131 | 2,103 | 216 |
| SVE2 MATCH            | 2,067           | 1,167  | 374   | 77   | 45  |
| SVE2 MATCH Unrolled   | 1,741           | 989    | 295   | 74   | 48  |

### Latency (ns per iteration) for different hit rates (16-bit)

| Implementation        | 0% (No Matches) | 0.001% | 0.01% | 0.1% | 1% |
|-----------------------|-----------------|--------|-------|------|----|
| Generic Scalar        | 12,047          | 12,485 | 5,879 | 721  | 44 |
| SVE2 MATCH            | 3,852           | 3,161  | 1,331 | 199  | 43 |
| SVE2 MATCH Unrolled   | 2,996           | 2,986  | 1,237 | 178  | 43 |

### Speedup versus generic scalar (8-bit)

| Hit rate | SVE2 MATCH | SVE2 MATCH Unrolled |
|----------|------------|---------------------|
| 0%       | 101.98x    | 121.09x             |
| 0.001%   | 87.19x     | 102.85x             |
| 0.01%    | 61.85x     | 78.47x              |
| 0.1%     | 27.28x     | 28.45x              |
| 1%       | 4.82x      | 4.55x               |

### Speedup versus generic scalar (16-bit)

| Hit rate | SVE2 MATCH | SVE2 MATCH Unrolled |
|----------|------------|---------------------|
| 0%       | 3.13x      | 4.02x               |
| 0.001%   | 3.95x      | 4.18x               |
| 0.01%    | 4.42x      | 4.75x               |
| 0.1%     | 3.63x      | 4.05x               |
| 1%       | 1.02x      | 1.01x               |


### How hit rate affects performance

The sample results show that the SVE2 MATCH speedup changes with the hit rate.

#### Very low hit rates (0%–0.001%)

For 8-bit data, the SVE2 MATCH implementations achieve an 87 to 121 times speedup.  For 16-bit data, the speedup ranges from about 3.1 times to 4.2 times.

At these low hit rates, SVE2 MATCH processes large chunks of data with few or no matches faster than the generic scalar implementation.

#### Low hit rate (0.01%)

The 8-bit implementations are about 62 to 78 times faster than the generic scalar implementation. The 16-bit implementations are about 4.4 to 4.8 times faster.

#### Medium hit rate (0.1%)

The 8-bit implementations retain an approximately 27 to 28 times speedup. The 16-bit implementations remain about 3.6 to 4.1 times faster than the generic scalar implementation.

#### High hit rate (1%)

The 8-bit implementations remain about 4.6 to 4.8 times faster than the generic scalar implementation. The 16-bit implementations perform about the same as the generic scalar implementation.

With frequent matches, early termination reduces the benefit of processing multiple elements at once.

### Interpret the results

The unrolled implementation performs better in most of these measurements, but not at every hit rate:

- When there are very low hit rates, the implementation improves the 0% case from 101.98 times to 121.09 times for 8-bit. It improves the 0% case from 3.13 times to 4.02 times for 16-bit.
- When there are low and medium hit rates, the implementation improves performance for both element sizes. The largest gains can be seen in the 8-bit 0.01% case.
- When there are high hit rates, the implementation performs similarly for 16-bit data. It's slightly slower than the basic SVE2 MATCH implementation for 8-bit data.

These results demonstrate that loop unrolling and prefetching are most useful when the scan processes large portions of the array before finding a match. Such applications include:

- Searching for specific patterns in large datasets
- Filtering operations with high selectivity
- Security applications looking for specific signatures

## What you've accomplished

You've benchmarked scalar, SVE2 MATCH, and unrolled SVE2 MATCH search implementations. The SVE2 MATCH instruction provides a powerful way to accelerate search operations in byte and halfword arrays.

By implementing these optimizations on cloud instances with SVE2, you can achieve significant performance improvements for your applications.
