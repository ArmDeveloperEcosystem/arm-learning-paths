---
# User change
title: "Benchmarking bitmap scanning across implementations"

weight: 6

layout: "learningpathall"


---
## Benchmarking code

Now that you've created four different bitmap scanning implementations, let’s build a benchmarking framework to compare their performance.

Copy the code shown below into `bitvector_scan_benchmark.c` :

```c
// Timing function for bit vector scanning
double benchmark_scan(size_t (*scan_func)(bitvector_t*, uint32_t*),
                     bitvector_t* bv, uint32_t* result_positions,
                     int iterations, size_t* found_count) {
    struct timespec start, end;
    *found_count = 0;

    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int iter = 0; iter < iterations; iter++) {
        size_t count = scan_func(bv, result_positions);
        if (iter == 0) {
            *found_count = count;
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &end);

    double elapsed = (end.tv_sec - start.tv_sec) * 1000.0 +
                    (end.tv_nsec - start.tv_nsec) / 1000000.0;
    return elapsed / iterations;
}
```

## Main function
The main function of your program is responsible for setting up the test environment, running the benchmarking code for the four different implementations across various bit densities, and reporting the results. In the context of bitmap scanning, bit density refers to the percentage or proportion of bits that are set (have a value of 1) in the bitmap. 

Copy the main function code below into `bitvector_scan_benchmark.c`:

```C
int main() {
    srand(time(NULL));

    printf("Bit Vector Scanning Performance Benchmark\n");
    printf("========================================\n\n");

    // Parameters
    size_t bitvector_size = 10000000;  // 10 million bits
    int iterations = 10;               // 10 iterations for timing

    // Test different densities
    double densities[] = {0.0, 0.0001, 0.001, 0.01, 0.1};
    int num_densities = sizeof(densities) / sizeof(densities[0]);

    printf("Bit vector size: %zu bits\n", bitvector_size);
    printf("Iterations: %d\n\n", iterations);

    // Allocate result array
    uint32_t* result_positions = (uint32_t*)malloc(bitvector_size * sizeof(uint32_t));

    printf("%-10s %-15s %-15s %-15s %-15s %-15s\n",
           "Density", "Set Bits", "Scalar Gen (ms)", "Scalar Opt (ms)", "NEON (ms)", "SVE (ms)");
    printf("%-10s %-15s %-15s %-15s %-15s %-15s\n",
           "-------", "--------", "--------------", "--------------", "--------", "---------------");

    for (int d = 0; d < num_densities; d++) {
        double density = densities[d];

        // Generate bit vector with specified density
        bitvector_t* bv = generate_bitvector(bitvector_size, density);

	// Count actual set bits
        size_t actual_set_bits = bitvector_count_scalar(bv);

        // Benchmark implementations
        size_t found_scalar_gen, found_scalar, found_neon, found_sve2;

        double scalar_gen_time = benchmark_scan(scan_bitvector_scalar_generic, bv, result_positions,
                                             iterations, &found_scalar_gen);

        double scalar_time = benchmark_scan(scan_bitvector_scalar, bv, result_positions,
                                          iterations, &found_scalar);

        double neon_time = benchmark_scan(scan_bitvector_neon, bv, result_positions,
                                        iterations, &found_neon);

        double sve2_time = benchmark_scan(scan_bitvector_sve2_pnext, bv, result_positions,
                                        iterations, &found_sve2);

        // Print results
        printf("%-10.4f %-15zu %-15.3f %-15.3f %-15.3f %-15.3f\n",
               density, actual_set_bits, scalar_gen_time, scalar_time, neon_time, sve2_time);

	// Print speedups for this density
        printf("Speedups at %.4f density:\n", density);
        printf("  Scalar Opt vs Scalar Gen: %.2fx\n", scalar_gen_time / scalar_time);
        printf("  NEON vs Scalar Gen: %.2fx\n", scalar_gen_time / neon_time);
        printf("  SVE vs Scalar Gen: %.2fx\n", scalar_gen_time / sve2_time);
        printf("  NEON vs Scalar Opt: %.2fx\n", scalar_time / neon_time);
        printf("  SVE vs Scalar Opt: %.2fx\n", scalar_time / sve2_time);
        printf("  SVE vs NEON: %.2fx\n\n", neon_time / sve2_time);

        // Verify results match
        if (found_scalar_gen != found_scalar || found_scalar_gen != found_neon || found_scalar_gen != found_sve2) {
            printf("WARNING: Result mismatch at %.4f density!\n", density);
            printf("  Scalar Gen found %zu bits\n", found_scalar_gen);
            printf("  Scalar Opt found %zu bits\n", found_scalar);
            printf("  NEON found %zu bits\n", found_neon);
            printf("  SVE found %zu bits\n\n", found_sve2);
        }

        // Clean up
        bitvector_free(bv);
    }

    free(result_positions);

    return 0;
}
```

## Compiling and running

You are now ready to compile and run your bitmap scanning implementations.

To compile our bitmap scanning implementations with the appropriate flags, run:

```bash
gcc -O3 -march=armv9-a+sve2 -o bitvector_scan_benchmark bitvector_scan_benchmark.c -lm
```

## Performance results

When running on a Graviton4 c8g.large instance with Ubuntu 24.04, the results should look similar to:

### Execution time (ms)

| Density | Set Bits | Scalar Generic | Scalar Optimized | NEON  | SVE	      |
|---------|----------|----------------|------------------|-------|------------|
| 0.0000  | 0        | 7.169          | 0.456            | 0.056 | 0.093      |
| 0.0001  | 1,000    | 7.176          | 0.477            | 0.090 | 0.109      |
| 0.0010  | 9,996    | 7.236          | 0.591            | 0.377 | 0.249      |
| 0.0100  | 99,511   | 7.821          | 1.570            | 2.252 | 1.353      |
| 0.1000  | 951,491  | 12.817         | 8.336            | 9.106 | 6.770      |

### Speed-up vs generic scalar

| Density | Scalar Optimized | NEON    | SVE        |
|---------|------------------|---------|------------|
| 0.0000  | 15.72x           | 127.41x | 77.70x     |
| 0.0001  | 15.05x           | 80.12x  | 65.86x     |
| 0.0010  | 12.26x           | 19.35x  | 29.07x     |
| 0.0100  | 5.02x            | 3.49x   | 5.78x      |
| 0.1000  | 1.54x            | 1.40x   | 1.90x      |

## Understanding the results

The benchmarking results reveal how different bitmap scanning implementations perform across a range of bit densities—from completely empty vectors to those with millions of set bits. Understanding these trends is key to selecting the most effective approach for your specific use case.

### Generic scalar vs optimized scalar

The optimized scalar implementation shows significant improvements over the generic scalar implementation due to:

* **Byte-level Skipping**: avoiding processing empty bytes
* **Reduced Function Calls**: accessing bits directly rather than through function calls
* **Better Cache Utilization**: more sequential memory access patterns

### Optimized scalar vs NEON

The NEON implementation shows further improvements over the optimized scalar implementation for sparse bit vectors due to:

* **Chunk-level Skipping**: quickly skipping 16 empty bytes at once
* **Vectorized Comparison**: checking multiple bytes in parallel
* **Early Termination**: quickly determining if a chunk contains any set bits

### NEON vs SVE

The performance comparison between NEON and SVE depends on the bit density:

*  **Very Sparse Bit Vectors (0% - 0.01% density)**:
   - NEON performs better for empty bitvectors due to lower overhead
   - NEON achieves up to 127.41x speedup over generic scalar
   - SVE performs better for very sparse bitvectors (0.001% density)
   - SVE achieves up to 29.07x speedup over generic scalar at 0.001% density

* **Higher Density Bit Vectors (0.1% - 10% density)**:
   - SVE consistently outperforms NEON
   - SVE achieves up to 1.66x speedup over NEON at 0.01% density

### Key optimizations in SVE implementation

The SVE implementation includes several key optimizations:

* **Efficient Non-Zero Byte Detection**: using `svcmpne_u8` to quickly identify non-zero bytes in the bitvector.

* **Byte-Level Processing**: using `svpnext_b8` to efficiently find the next non-zero byte without processing zero bytes.

* **Value Extraction**: using `svlastb_u8` to extract both the index and value of non-zero bytes.

* **Hybrid Vector-Scalar Approach**: combining vector operations for finding non-zero bytes with scalar operations for processing individual bits.

* **Prefetching**: Using `__builtin_prefetch` to reduce memory latency by prefetching the next chunk of data.

## Next up: apply what you’ve learned to real-world workloads

Now that you’ve benchmarked all four bitmap scanning implementations—scalar (generic and optimized), NEON, and SVE—you have a data-driven understanding of how vectorization impacts performance across different bitmap densities.

In the next section, you’ll explore how to apply these techniques in real-world database workloads, including:

* Bitmap index scans

* Bloom filter checks

* Column-level filtering in analytical queries

You’ll also learn practical guidelines for choosing the right implementation based on bit density, and discover optimization tips that go beyond the code to help you get the most out of Arm-based systems like Graviton4.


