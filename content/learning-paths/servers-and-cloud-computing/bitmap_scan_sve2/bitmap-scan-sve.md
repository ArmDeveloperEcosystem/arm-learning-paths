---
# User change
title: "Compare performance of different Bitmap Scanning implementations"

weight: 2

layout: "learningpathall"


---

## Introduction

Bitmap scanning is a fundamental operation in database systems, particularly for analytical workloads. It's used in bitmap indexes, bloom filters, and column filtering operations. The performance of bitmap scanning can significantly impact query execution times, especially for large datasets.

In this learning path, you will explore how to use the SVE2 MATCH instruction available on Arm Neoverse V2 based servers like AWS Graviton4 to optimize bitmap scanning operations. You will compare the performance of scalar, NEON, and SVE2 implementations to demonstrate the significant performance benefits of using specialized vector instructions.

## What is Bitmap Scanning?

Bitmap scanning involves searching through a bit vector to find positions where bits are set (1) or unset (0). In database systems, bitmaps are commonly used to represent:

1. **Bitmap Indexes**: Where each bit represents whether a row satisfies a particular condition
2. **Bloom Filters**: Probabilistic data structures used to test set membership
3. **Column Filters**: Bit vectors indicating which rows match certain predicates

The operation of scanning a bitmap to find set bits is often in the critical path of query execution, making it a prime candidate for optimization.

## The Evolution of Vector Processing for Bitmap Scanning

Let's look at how vector processing has evolved for bitmap scanning:

1. **Generic Scalar Processing**: Traditional bit-by-bit processing with conditional branches
2. **Optimized Scalar Processing**: Byte-level skipping to avoid processing empty bytes
3. **NEON**: Fixed-length 128-bit SIMD processing with vector operations
4. **SVE/SVE2**: Scalable vector processing with predication and specialized instructions like MATCH

## Set Up Your Environment

To follow this learning path, you will need:

1. An AWS Graviton4 instance running `Ubuntu 24.04`. 
2. GCC compiler with SVE2 support

Let's start by setting up our environment:

```bash
sudo apt-get update
sudo apt-get install -y build-essential gcc g++
```
An effective way to achieve optimal performance on Arm is not only through optimal flag usage, but also by using the most recent compiler version. This Learning path was tested with GCC 13 which is the default version on `Ubuntu 24.04` but you can run it with newer versions of GCC as well. 

Create a directory for your implementations:
```bash
mkdir -p bitmap_scan
cd bitmap_scan
```

## Bitmap Data Structure

First, let's define a simple bitmap data structure that will serve as the foundation for the different implementations. The bitmap implementation uses a simple structure with three key components:
   - A byte array to store the actual bits
   - Tracking of the physical size(bytes)
   - Tracking of the logical size(bits)

For testing the different implementations in this Learning Path, you will also need functions to generate and analyze the bitmaps.

Use a file editor of your choice and the copy the code below into `bitvector_scan_benchmark.c`:

```c
// Define a simple bit vector structure
typedef struct {
    uint8_t* data;
    size_t size_bytes;
    size_t size_bits;
} bitvector_t;

// Create a new bit vector
bitvector_t* bitvector_create(size_t size_bits) {
    bitvector_t* bv = (bitvector_t*)malloc(sizeof(bitvector_t));
    bv->size_bits = size_bits;
    bv->size_bytes = (size_bits + 7) / 8;
    bv->data = (uint8_t*)calloc(bv->size_bytes, 1);
    return bv;
}

// Free bit vector resources
void bitvector_free(bitvector_t* bv) {
    free(bv->data);
    free(bv);
}

// Set a bit in the bit vector
void bitvector_set_bit(bitvector_t* bv, size_t pos) {
    if (pos < bv->size_bits) {
        bv->data[pos / 8] |= (1 << (pos % 8));
    }
}

// Get a bit from the bit vector
bool bitvector_get_bit(bitvector_t* bv, size_t pos) {
    if (pos < bv->size_bits) {
        return (bv->data[pos / 8] & (1 << (pos % 8))) != 0;
    }
    return false;
}

// Generate a bit vector with specified density
bitvector_t* generate_bitvector(size_t size_bits, double density) {
    bitvector_t* bv = bitvector_create(size_bits);
    
    // Set bits according to density
    size_t num_bits_to_set = (size_t)(size_bits * density);
    
    for (size_t i = 0; i < num_bits_to_set; i++) {
        size_t pos = rand() % size_bits;
        bitvector_set_bit(bv, pos);
    }
    
    return bv;
}

// Count set bits in the bit vector
size_t bitvector_count_scalar(bitvector_t* bv) {
    size_t count = 0;
    for (size_t i = 0; i < bv->size_bits; i++) {
        if (bitvector_get_bit(bv, i)) {
            count++;
        }
    }
    return count;
}
```

## Bitmap Scanning Implementations

Now, let's implement four versions of a bitmap scanning operation that finds all positions where a bit is set:

### 1. Generic Scalar Implementation

This is the most straightforward implementation, checking each bit individually. It serves as our baseline for comparison against the other implementations to follow. Copy the code below into the same file:

```c
// Generic scalar implementation of bit vector scanning (bit-by-bit)
size_t scan_bitvector_scalar_generic(bitvector_t* bv, uint32_t* result_positions) {
    size_t result_count = 0;

    for (size_t i = 0; i < bv->size_bits; i++) {
        if (bitvector_get_bit(bv, i)) {
            result_positions[result_count++] = i;
        }
    }

    return result_count;
}
```

You will notice this generic C implementation processes every bit, even when most bits are not set. It has high function call overhead and does not advantage of vector instructions.

In the following implementations, you will address these inefficiencies with more optimized techniques.

### 2. Optimized Scalar Implementation

This implementation adds byte-level skipping to avoid processing empty bytes. Copy this optimized C scalar implementation code into the same file:

```c
// Optimized scalar implementation of bit vector scanning (byte-level)
size_t scan_bitvector_scalar(bitvector_t* bv, uint32_t* result_positions) {
size_t result_count = 0;

    for (size_t byte_idx = 0; byte_idx < bv->size_bytes; byte_idx++) {
        uint8_t byte = bv->data[byte_idx];

        // Skip empty bytes
        if (byte == 0) {
            continue;
        }

        // Process each bit in the byte
        for (int bit_pos = 0; bit_pos < 8; bit_pos++) {
            if (byte & (1 << bit_pos)) {
                size_t global_pos = byte_idx * 8 + bit_pos;
                if (global_pos < bv->size_bits) {
                    result_positions[result_count++] = global_pos;
                }
            }
        }
    }

    return result_count;
}
```
Instead of iterating through each bit, this implementation processes one byte(8 bits) at a time. The main optimization over the previous scalar implementation is checking if an entire byte is zero and skipping it entirely, For sparse bitmaps, this can dramatically reduce the number of bit checks.

### 3. NEON Implementation

This implementation uses NEON SIMD (Single Instruction, Multiple Data) instructions to process 16 bytes (128 bits) at a time, significantly accelerating the scanning process. Copy the NEON implementation shown below into the same file:
```c
// NEON implementation of bit vector scanning
size_t scan_bitvector_neon(bitvector_t* bv, uint32_t* result_positions) {
    size_t result_count = 0;

    // Process 16 bytes at a time using NEON
    size_t i = 0;
    for (; i + 16 <= bv->size_bytes; i += 16) {
        uint8x16_t data = vld1q_u8(&bv->data[i]);

        // Quick check if all bytes are zero
        uint8x16_t zero = vdupq_n_u8(0);
        uint8x16_t cmp = vceqq_u8(data, zero);
        uint64x2_t cmp64 = vreinterpretq_u64_u8(cmp);

        // If all bytes are zero (all comparisons are true/0xFF), skip this chunk
        if (vgetq_lane_u64(cmp64, 0) == UINT64_MAX &&
            vgetq_lane_u64(cmp64, 1) == UINT64_MAX) {
            continue;
        }

        // Process each byte
        uint8_t bytes[16];
        vst1q_u8(bytes, data);

        for (int j = 0; j < 16; j++) {
	    uint8_t byte = bytes[j];

            // Skip empty bytes
            if (byte == 0) {
                continue;
            }

            // Process each bit in the byte
            for (int bit_pos = 0; bit_pos < 8; bit_pos++) {
                if (byte & (1 << bit_pos)) {
                    size_t global_pos = (i + j) * 8 + bit_pos;
                    if (global_pos < bv->size_bits) {
                        result_positions[result_count++] = global_pos;
                    }
                }
            }
        }
    }

    // Handle remaining bytes with scalar code
    for (; i < bv->size_bytes; i++) {
        uint8_t byte = bv->data[i];

        // Skip empty bytes
        if (byte == 0) {
            continue;
        }

        // Process each bit in the byte
    for (int bit_pos = 0; bit_pos < 8; bit_pos++) {
            if (byte & (1 << bit_pos)) {
                size_t global_pos = i * 8 + bit_pos;
                if (global_pos < bv->size_bits) {
                    result_positions[result_count++] = global_pos;
                }
            }
        }
    }

    return result_count;
}
```
This NEON implementation processes 16 bytes at a time with vector instructions. For sparse bitmaps, entire 16-byte chunks can be skipped at once, providing a significant speedup over byte-level skipping. After vector processing, it falls back to scalar code for any remaining bytes that don't fill a complete 16-byte chunk.

### 4. SVE2 MATCH Implementation

This implementation uses SVE2 instructions which are available in the Arm Neoverse V2 based AWS Graviton 4 processor. It uses the SVE2 MATCH instruction in particular, which is specifically designed for pattern matching operations to efficiently find set bits:

```c
// Optimized SVE2 MATCH implementation for bit vector scanning
size_t scan_bitvector_sve2_match(bitvector_t* bv, uint32_t* result_positions) {
    size_t result_count = 0;
    size_t sve_len = svcntb();

    // Create pattern vectors for each bit position
    svuint8_t bit0 = svdup_n_u8(1);   // 00000001
    svuint8_t bit1 = svdup_n_u8(2);   // 00000010
    svuint8_t bit2 = svdup_n_u8(4);   // 00000100
    svuint8_t bit3 = svdup_n_u8(8);   // 00001000
    svuint8_t bit4 = svdup_n_u8(16);  // 00010000
    svuint8_t bit5 = svdup_n_u8(32);  // 00100000
    svuint8_t bit6 = svdup_n_u8(64);  // 01000000
    svuint8_t bit7 = svdup_n_u8(128); // 10000000

    // Fast path for checking if there are any matches at all
    bool any_matches = false;
    for (size_t offset = 0; offset < bv->size_bytes; offset += sve_len) {
        svbool_t pg = svwhilelt_b8((uint64_t)offset, (uint64_t)bv->size_bytes);
        svuint8_t data = svld1_u8(pg, bv->data + offset);

        // Prefetch next chunk
        if (offset + sve_len < bv->size_bytes) {
            __builtin_prefetch(bv->data + offset + sve_len, 0, 0);
        }
     // Check if any non-zero bytes in this chunk
        svuint8_t zero = svdup_n_u8(0);
        svbool_t is_zero = svcmpeq_u8(pg, data, zero);
        svbool_t non_zero = svnot_b_z(pg, is_zero);

        if (svptest_any(pg, non_zero)) {
            any_matches = true;
            break;
        }
    }

    // If no matches found in the entire bitvector, return early
    if (!any_matches) {
        return 0;  // No matches found
    }

    // Process the bitvector to find all set bits
    for (size_t offset = 0; offset < bv->size_bytes; offset += sve_len) {
        svbool_t pg = svwhilelt_b8((uint64_t)offset, (uint64_t)bv->size_bytes);
        svuint8_t data = svld1_u8(pg, bv->data + offset);

// Check for each bit position using MATCH
        // Bit 0
        svbool_t matches = svmatch_u8(pg, svand_u8_z(pg, data, bit0), bit0);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 0;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }

        // Repeat for bits 1-7...
        // Bit 1
        matches = svmatch_u8(pg, svand_u8_z(pg, data, bit1), bit1);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 1;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }

        // Bit 2
        matches = svmatch_u8(pg, svand_u8_z(pg, data, bit2), bit2);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 2;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }

	// Bit 3
        matches = svmatch_u8(pg, svand_u8_z(pg, data, bit3), bit3);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 3;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }

        // Bit 4
        matches = svmatch_u8(pg, svand_u8_z(pg, data, bit4), bit4);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 4;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }
	
	// Bit 5
        matches = svmatch_u8(pg, svand_u8_z(pg, data, bit5), bit5);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 5;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }

        // Bit 6
        matches = svmatch_u8(pg, svand_u8_z(pg, data, bit6), bit6);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 6;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }
	
	// Bit 7
        matches = svmatch_u8(pg, svand_u8_z(pg, data, bit7), bit7);
        while (svptest_any(pg, matches)) {
            uint64_t match_idx = svlasta_u64(matches, svindex_u64(0, 1));
            size_t global_pos = (offset + match_idx) * 8 + 7;
            if (global_pos < bv->size_bits) {
                result_positions[result_count++] = global_pos;
            }
            matches = svbic_b_z(pg, matches, svbrka_b_z(pg, matches));
        }
    }

    return result_count;
}
```
The SVE2 implementation processes all occurences of a specific bit position in parallel across the entire vector. On Graviton4, SVE vectors are 128 bits (16 bytes), allowing processing of 16 bytes at once. It uses the MATCH instruction (`svmatch_u8`) to compare each element in a vector against a specific pattern and sets corresponding bits in a predicate register if they match. 

## Benchmarking Code

Now, that you have created four different implementations of a bitmap scanning algorithm, let's create a benchmarking framework to compare the performance of our implementations. Copy the code shown below into `bitvector_scan_benchmark.c` :

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

## Main Function
The main function of your program is reposible for setting up the test environment, running the benchmarking code for the four different implementations across various bit densities, and reporting the results. In the context of bitmap scanning, bit density refers to the percentage or proportion of bits that are set (have a value of 1) in the bitmap. Copy the main function code below into `bitvector_scan_benchmark.c`:

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
           "Density", "Set Bits", "Scalar Gen (ms)", "Scalar Opt (ms)", "NEON (ms)", "SVE2 MATCH (ms)");
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

        double sve2_time = benchmark_scan(scan_bitvector_sve2_match, bv, result_positions,
                                        iterations, &found_sve2);

        // Print results
        printf("%-10.4f %-15zu %-15.3f %-15.3f %-15.3f %-15.3f\n",
               density, actual_set_bits, scalar_gen_time, scalar_time, neon_time, sve2_time);

	// Print speedups for this density
        printf("Speedups at %.4f density:\n", density);
        printf("  Scalar Opt vs Scalar Gen: %.2fx\n", scalar_gen_time / scalar_time);
        printf("  NEON vs Scalar Gen: %.2fx\n", scalar_gen_time / neon_time);
        printf("  SVE2 MATCH vs Scalar Gen: %.2fx\n", scalar_gen_time / sve2_time);
        printf("  NEON vs Scalar Opt: %.2fx\n", scalar_time / neon_time);
        printf("  SVE2 MATCH vs Scalar Opt: %.2fx\n", scalar_time / sve2_time);
        printf("  SVE2 MATCH vs NEON: %.2fx\n\n", neon_time / sve2_time);

        // Verify results match
        if (found_scalar_gen != found_scalar || found_scalar_gen != found_neon || found_scalar_gen != found_sve2) {
            printf("WARNING: Result mismatch at %.4f density!\n", density);
            printf("  Scalar Gen found %zu bits\n", found_scalar_gen);
            printf("  Scalar Opt found %zu bits\n", found_scalar);
            printf("  NEON found %zu bits\n", found_neon);
            printf("  SVE2 MATCH found %zu bits\n\n", found_sve2);
        }

        // Clean up
        bitvector_free(bv);
    }

    free(result_positions);

    return 0;
}
```

## Compiling and Running

You are now ready to compile and run your bitmap scanning implementations.

To compile our bitmap scanning implementations with the appropriate flags, run:

```bash
gcc -O3 -march=armv9-a+sve2 -o bitvector_scan_benchmark bitvector_scan_benchmark.c -lm
```

## Performance Results

When running on a Graviton4 c8g.4xlarge instance with Ubuntu 24.04, the results should look similar to:

### Execution Time (ms)

| Density | Set Bits | Scalar Generic | Scalar Optimized | NEON  | SVE2 MATCH |
|---------|----------|----------------|------------------|-------|------------|
| 0.0000  | 0        | 7.169          | 0.456            | 0.056 | 0.087      |
| 0.0001  | 1,000    | 7.176          | 0.477            | 0.090 | 0.263      |
| 0.0010  | 9,996    | 7.236          | 0.591            | 0.377 | 0.351      |
| 0.0100  | 99,511   | 7.821          | 1.570            | 2.252 | 0.924      |
| 0.1000  | 951,491  | 12.817         | 8.336            | 9.106 | 4.846      |

### Speedup vs Generic Scalar

| Density | Scalar Optimized | NEON    | SVE2 MATCH |
|---------|------------------|---------|------------|
| 0.0000  | 15.71x           | 127.75x | 82.68x     |
| 0.0001  | 15.04x           | 80.09x  | 27.26x     |
| 0.0010  | 12.24x           | 19.21x  | 20.59x     |
| 0.0100  | 4.98x            | 3.47x   | 8.46x      |
| 0.1000  | 1.54x            | 1.41x   | 2.64x      |

## Understanding the Performance Results

### Generic Scalar vs Optimized Scalar

The optimized scalar implementation shows significant improvements over the generic scalar implementation due to:

1. **Byte-level Skipping**: Avoiding processing empty bytes
2. **Reduced Function Calls**: Accessing bits directly rather than through function calls
3. **Better Cache Utilization**: More sequential memory access patterns

### Optimized Scalar vs NEON

The NEON implementation shows further improvements over the optimized scalar implementation for sparse bit vectors due to:

1. **Chunk-level Skipping**: Quickly skipping 16 empty bytes at once
2. **Vectorized Comparison**: Checking multiple bytes in parallel
3. **Early Termination**: Quickly determining if a chunk contains any set bits

### NEON vs SVE2 MATCH

The performance comparison between NEON and SVE2 MATCH depends on the bit density:

1. **Very Sparse Bit Vectors (0% - 0.01% density)**:
   - NEON performs better due to lower overhead
   - NEON achieves up to 127.75x speedup over generic scalar

2. **Higher Density Bit Vectors (0.1% - 10% density)**:
   - SVE2 MATCH performs better due to more efficient bit pattern matching
   - SVE2 MATCH achieves up to 2.44x speedup over NEON at 1% density

# Key Optimizations in SVE2 MATCH Implementation

The SVE2 MATCH implementation includes several key optimizations:

1. **Early Termination**: A fast path that quickly checks if there are any non-zero bytes in the bit vector, allowing early termination for the no-hits case.

2. **Prefetching**: Using `__builtin_prefetch` to reduce memory latency by prefetching the next chunk of data.

3. **Bit-Position-Specific Processing**: Using separate MATCH operations for each bit position (0-7) to efficiently find all set bits.

4. **Efficient Match Extraction**: Using SVE instructions like `svlasta_u64` and `svbrka_b_z` to efficiently extract match positions.

## Application to Database Systems

These bitmap scanning optimizations can be applied to various database operations:

### 1. Bitmap Index Scans

Bitmap indexes are commonly used in analytical databases to accelerate queries with multiple filter conditions. The SVE2 MATCH implementation can significantly speed up the scanning of these bitmap indexes, especially for queries with low selectivity.

### 2. Bloom Filter Checks

Bloom filters are probabilistic data structures used to test set membership. They are often used in database systems to quickly filter out rows that don't match certain conditions. The SVE2 MATCH implementation can accelerate these bloom filter checks.

### 3. Column Filtering

In column-oriented databases, bitmap filters are often used to represent which rows match certain predicates. The SVE2 MATCH implementation can speed up the scanning of these bitmap filters, improving query performance.

## Best Practices

Based on our benchmark results, here are some best practices for optimizing bitmap scanning operations:

1. **Choose the Right Implementation**: Select the appropriate implementation based on the expected bit density:
   - For very sparse bit vectors (< 0.1% density): NEON is optimal
   - For higher densities (≥ 0.1% density): SVE2 MATCH is optimal

2. **Implement Early Termination**: Always include a fast path for the no-hits case, as this can provide dramatic performance improvements.

3. **Use Byte-level Skipping**: Even in scalar implementations, skipping empty bytes can provide significant performance improvements.

4. **Consider Memory Access Patterns**: Optimize memory access patterns to improve cache utilization.

5. **Leverage Vector Instructions**: Use NEON or SVE2 instructions to process multiple bytes in parallel.

## Conclusion

The SVE2 MATCH instruction provides a powerful way to accelerate bitmap scanning operations in database systems. By implementing these optimizations on Graviton4 instances, you can achieve significant performance improvements for your database workloads.

The most dramatic speedups are observed for the no-hits case, where early termination optimizations allow the vector implementations to quickly determine that no bits are set without processing the entire bit vector. For higher bit densities, the SVE2 MATCH implementation continues to show significant performance advantages over both scalar and NEON implementations.

These performance improvements can translate directly to faster query execution times, especially for analytical workloads that involve multiple bitmap operations.
