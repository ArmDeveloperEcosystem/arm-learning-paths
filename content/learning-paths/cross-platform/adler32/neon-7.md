---
title: Create a NEON version of Adler32
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Can I Create a NEON Version of Adler32 To Improve Performance? 

Writing NEON intrinsics is an advanced programming topic which requires time and effort to learn and apply. GitHub Copilot is a good way to get started with NEON, both to write new code and to debug issues during development. 

You can instruct Github Copilot to create a NEON-optimized version of Adler32 using the prompt below: 

```console
Add a second implementation of adler32 that processes data in blocks and uses Arm NEON intrinsics to improve performance.
Create it in the file adler32-neon.c 
For inputs less than 16 bytes use a standard implementation. 
Update the Makefile and other files to add this new version and compare performance. 
Print out the speedup from the original version.
Make sure the checksum values are the same for both versions.
```

The output is:

```output

GitHub Copilot: I'll help you create a NEON-optimized version of adler32 and update the project to compare performance with the original implementation. Let's start by examining the existing code structure to understand the current implementation.Great, I've found the header file for the simple Adler-32 implementation. Now let's look at the implementation file to understand how it works.I've examined the existing code for the Adler32 implementation. Now let's check the test file to understand how to properly integrate our new implementation:I've analyzed your Adler32 implementation and test code. Now I'll create a NEON-optimized version that processes data in blocks, update the Makefile, and compare the performance between both implementations.

Let's first create the NEON implementation file:

/*
 * adler32-neon.h - Header file for NEON-optimized Adler-32 checksum implementation
 */

#ifndef ADLER32_NEON_H
#define ADLER32_NEON_H

#include <stdint.h>
#include <stddef.h>

/**
 * Calculate Adler-32 checksum for a data buffer using NEON optimization
 * 
 * @param data    Pointer to the data buffer
 * @param length  Length of the data in bytes
 * @param initial Initial Adler-32 value (typically 1)
 * 
 * @return The calculated Adler-32 checksum
 */
uint32_t adler32_neon(const unsigned char *data, size_t length, uint32_t initial);

/**
 * Initialize Adler-32 checksum calculation
 * 
 * @return The initial Adler-32 value (1)
 */
uint32_t adler32_neon_init(void);

/**
 * Update Adler-32 checksum with new data using NEON optimization
 * 
 * @param adler  Current Adler-32 value
 * @param data   Pointer to the data buffer
 * @param length Length of the data in bytes
 * 
 * @return The updated Adler-32 value
 */
uint32_t adler32_neon_update(uint32_t adler, const unsigned char *data, size_t length);

/**
 * Finalize Adler-32 calculation
 * 
 * @param adler Current Adler-32 value
 * 
 * @return The final Adler-32 checksum
 */
uint32_t adler32_neon_final(uint32_t adler);

#endif /* ADLER32_NEON_H */


Made changes.

Now I'll create the implementation file for the NEON-optimized Adler32:

/*
 * adler32-neon.c - NEON-optimized implementation of Adler-32 checksum algorithm
 *
 * This implementation uses ARM NEON SIMD instructions to process multiple bytes in parallel
 * for improved performance on Neoverse N1 and other ARM platforms with NEON support.
 */

#include <stdint.h>
#include <stddef.h>
#include <arm_neon.h>
#include "adler32-neon.h"

/* Adler-32 parameters */
#define MOD_ADLER 65521 /* Largest prime number less than 2^16 */
#define BLOCK_SIZE 16   /* Process 16 bytes at once with NEON */

/*
 * Standard implementation of adler32 for small inputs
 * Used for inputs less than BLOCK_SIZE
 */
static uint32_t adler32_standard(const unsigned char *data, size_t length, uint32_t initial)
{
    uint32_t a = initial & 0xffff;
    uint32_t b = (initial >> 16) & 0xffff;
    size_t i;

    /* Process each byte */
    for (i = 0; i < length; i++) {
        a = (a + data[i]) % MOD_ADLER;
        b = (b + a) % MOD_ADLER;
    }

    /* Combine the two 16-bit values */
    return (b << 16) | a;
}

/*
 * adler32_neon - Calculate the Adler-32 checksum of a data buffer using NEON instructions
 * @data: Data buffer
 * @length: Length of data buffer in bytes
 * @initial: Initial Adler-32 value (typically 1)
 * 
 * Returns the calculated Adler-32 checksum
 */
uint32_t adler32_neon(const unsigned char *data, size_t length, uint32_t initial)
{
    uint32_t a = initial & 0xffff;
    uint32_t b = (initial >> 16) & 0xffff;
    
    /* For small inputs, use the standard implementation */
    if (length < BLOCK_SIZE) {
        return adler32_standard(data, length, initial);
    }

    /* Process blocks of BLOCK_SIZE bytes */
    while (length >= BLOCK_SIZE) {
        /* NEON registers to accumulate sums */
        uint16x8_t va = vdupq_n_u16(0);  /* 8 parallel accumulators for a */
        uint16x8_t vb = vdupq_n_u16(0);  /* 8 parallel accumulators for b */
        
        /* 
         * We'll process 16 bytes at a time:
         * - Load 16 bytes into a 16x8 vector
         * - Compute partial sums in vectors
         */
        uint8x16_t vdata = vld1q_u8(data);
        
        /* Convert to 16-bit values for accumulation */
        uint16x8_t vdata_low = vmovl_u8(vget_low_u8(vdata));
        uint16x8_t vdata_high = vmovl_u8(vget_high_u8(vdata));
        
        /* Accumulate a values: a += data[i] */
        va = vaddq_u16(va, vdata_low);
        va = vaddq_u16(va, vdata_high);
        
        /* 
         * Accumulate b values with proper weighting:
         * b += a + data[i] * (BLOCK_SIZE - i)
         * 
         * Since we compute 16 bytes at once, weights are 16,15,...,1
         */
        static const uint16_t weights[16] = {16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
        uint16x8_t vweights_low = vld1q_u16(weights);
        uint16x8_t vweights_high = vld1q_u16(weights + 8);
        
        uint16x8_t weighted_low = vmulq_u16(vdata_low, vweights_low);
        uint16x8_t weighted_high = vmulq_u16(vdata_high, vweights_high);
        
        vb = vaddq_u16(vb, weighted_low);
        vb = vaddq_u16(vb, weighted_high);
        
        /* Accumulate partial sums into scalar a and b values */
        uint16_t partial_a[8];
        uint16_t partial_b[8];
        vst1q_u16(partial_a, va);
        vst1q_u16(partial_b, vb);
        
        for (size_t i = 0; i < 8; i++) {
            a += partial_a[i];
            b += partial_b[i];
        }
        
        /* Apply modulo to avoid overflow */
        a %= MOD_ADLER;
        b = (b + 16 * a) % MOD_ADLER;  /* Add BLOCK_SIZE * a to account for sequential weights */
        
        /* Move to next block */
        data += BLOCK_SIZE;
        length -= BLOCK_SIZE;
    }
    
    /* Process remaining bytes using standard implementation */
    if (length > 0) {
        uint32_t adler = (b << 16) | a;
        adler = adler32_standard(data, length, adler);
        return adler;
    }
    
    /* Combine the two 16-bit values */
    return (b << 16) | a;
}

/* 
 * adler32_neon_init - Initialize an Adler-32 checksum
 * 
 * Returns the initial Adler-32 value
 */
uint32_t adler32_neon_init(void)
{
    return 1;
}

/*
 * adler32_neon_update - Update Adler-32 checksum with new data using NEON optimization
 * @adler: Current Adler-32 value
 * @data: Data buffer
 * @length: Length of data buffer in bytes
 * 
 * Returns the updated Adler-32 value
 */
uint32_t adler32_neon_update(uint32_t adler, const unsigned char *data, size_t length)
{
    return adler32_neon(data, length, adler);
}

/*
 * adler32_neon_final - Finalize Adler-32 calculation
 * @adler: Current Adler-32 value
 * 
 * Returns the final Adler-32 checksum
 */
uint32_t adler32_neon_final(uint32_t adler)
{
    return adler;
}


Made changes.

Now I'll update the test file to add performance comparisons between the original and NEON implementations:

/*
 * adler32-test.c - Test and benchmark for Adler-32 checksum implementation
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdint.h>
#include "adler32-simple.h"
#include "adler32-neon.h"

/* Known test vectors for Adler-32 */
struct test_vector {
    const char *data;
    uint32_t expected;
};

/* Test data sizes in bytes */
#define KB (1024)
#define MB (1024 * 1024)

static const struct test_vector test_vectors[] = {
    { "", 0x00000001 },
    { "a", 0x00620062 },
    { "abc", 0x024d0127 },
    { "message digest", 0x29750586 },
    { "abcdefghijklmnopqrstuvwxyz", 0x90860b20 },
    { "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 0x8adb150c },
};

/* Structure to hold test data */
struct test_data {
    unsigned char *buffer;
    size_t size;
    const char *name;
};

/* Generate random test data of specified size */
static unsigned char* generate_test_data(size_t size) {
    unsigned char *data = malloc(size);
    if (!data) {
        fprintf(stderr, "Failed to allocate memory for test data\n");
        exit(EXIT_FAILURE);
    }
    
    for (size_t i = 0; i < size; i++) {
        data[i] = rand() & 0xFF;
    }
    
    return data;
}

/* Performance test result structure */
struct perf_result {
    double time;
    double throughput;
    uint32_t checksum;
};

/* Run performance test on a data buffer using the specified implementation */
static struct perf_result test_performance_impl(const unsigned char *data, size_t size, 
                                             uint32_t (*adler_func)(const unsigned char *, size_t, uint32_t),
                                             uint32_t (*init_func)(void),
                                             const char *impl_name) {
    clock_t start, end;
    struct perf_result result;
    
    /* Warm-up run */
    adler_func(data, size, init_func());
    
    /* Timed run */
    start = clock();
    result.checksum = adler_func(data, size, init_func());
    end = clock();
    
    result.time = ((double) (end - start)) / CLOCKS_PER_SEC;
    result.throughput = (double)size / (result.time * MB);
    
    printf("  %s:\n", impl_name);
    printf("    Checksum: 0x%08x\n", result.checksum);
    printf("    Time: %.6f seconds\n", result.time);
    printf("    Throughput: %.2f MB/s\n", result.throughput);
    
    return result;
}

/* Run performance test on a data buffer for both implementations */
static void test_performance(const unsigned char *data, size_t size, const char *test_name) {
    printf("Testing %s (%zu bytes):\n", test_name, size);
    
    /* Test the simple implementation */
    struct perf_result simple = test_performance_impl(data, size, adler32, adler32_init, "Simple implementation");
    
    /* Test the NEON implementation */
    struct perf_result neon = test_performance_impl(data, size, adler32_neon, adler32_neon_init, "NEON implementation");
    
    /* Check if checksums match */
    if (simple.checksum != neon.checksum) {
        printf("  CHECKSUM MISMATCH: Simple 0x%08x, NEON 0x%08x\n", 
               simple.checksum, neon.checksum);
    }
    
    /* Calculate speedup */
    double speedup = simple.time / neon.time;
    printf("  Speedup: %.2fx\n\n", speedup);
}

/* Run verification tests with known test vectors */
static void run_verification_tests(void) {
    printf("Running verification tests:\n");
    printf("==========================\n");
    
    int passed_simple = 0;
    int passed_neon = 0;
    int total = sizeof(test_vectors) / sizeof(test_vectors[0]);
    
    for (size_t i = 0; i < total; i++) {
        const struct test_vector *tv = &test_vectors[i];
        uint32_t result_simple = adler32((const unsigned char *)tv->data, strlen(tv->data), adler32_init());
        uint32_t result_neon = adler32_neon((const unsigned char *)tv->data, strlen(tv->data), adler32_neon_init());
        
        printf("Test %zu: \"%s\"\n", i + 1, tv->data);
        printf("  Expected:   0x%08x\n", tv->expected);
        printf("  Simple:     0x%08x (%s)\n", result_simple, 
               (result_simple == tv->expected) ? "PASS" : "FAIL");
        printf("  NEON:       0x%08x (%s)\n", result_neon, 
               (result_neon == tv->expected) ? "PASS" : "FAIL");
        
        if (result_simple == tv->expected) passed_simple++;
        if (result_neon == tv->expected) passed_neon++;
        
        /* Check if both implementations match */
        if (result_simple != result_neon) {
            printf("  WARNING: Simple and NEON implementations produce different results!\n");
        }
        
        printf("\n");
    }
    
    printf("Verification summary:\n");
    printf("  Simple: %d/%d tests passed\n", passed_simple, total);
    printf("  NEON:   %d/%d tests passed\n\n", passed_neon, total);
}

/* Run performance tests with different data sizes */
static void run_performance_tests(void) {
    printf("Running performance tests:\n");
    printf("=========================\n");
    
    /* Define test data sizes */
    struct test_data tests[] = {
        { NULL, 1 * KB, "1 KB" },
        { NULL, 10 * KB, "10 KB" },
        { NULL, 100 * KB, "100 KB" },
        { NULL, 1 * MB, "1 MB" },
        { NULL, 10 * MB, "10 MB" }
    };
    
    /* Generate random test data for each size */
    for (size_t i = 0; i < sizeof(tests) / sizeof(tests[0]); i++) {
        tests[i].buffer = generate_test_data(tests[i].size);
        test_performance(tests[i].buffer, tests[i].size, tests[i].name);
    }
    
    /* Free allocated memory */
    for (size_t i = 0; i < sizeof(tests) / sizeof(tests[0]); i++) {
        free(tests[i].buffer);
    }
}

/* Test the incremental API for both implementations */
static void test_incremental_api(void) {
    printf("Testing incremental API:\n");
    printf("=======================\n");
    
    /* Generate test data */
    size_t size = 1 * MB;
    unsigned char *data = generate_test_data(size);
    
    printf("Simple implementation:\n");
    /* Calculate checksum in one go */
    uint32_t direct = adler32(data, size, adler32_init());
    
    /* Calculate checksum incrementally */
    uint32_t incremental = adler32_init();
    
    /* Process in chunks of 64KB */
    size_t chunk_size = 64 * KB;
    for (size_t offset = 0; offset < size; offset += chunk_size) {
        size_t remaining = size - offset;
        size_t current_chunk = (remaining < chunk_size) ? remaining : chunk_size;
        incremental = adler32_update(incremental, data + offset, current_chunk);
    }
    incremental = adler32_final(incremental);
    
    /* Compare results */
    printf("  Direct calculation:      0x%08x\n", direct);
    printf("  Incremental calculation: 0x%08x\n", incremental);
    printf("  Match: %s\n\n", (direct == incremental) ? "YES" : "NO");
    
    printf("NEON implementation:\n");
    /* Calculate checksum in one go */
    uint32_t direct_neon = adler32_neon(data, size, adler32_neon_init());
    
    /* Calculate checksum incrementally */
    uint32_t incremental_neon = adler32_neon_init();
    
    /* Process in chunks of 64KB */
    for (size_t offset = 0; offset < size; offset += chunk_size) {
        size_t remaining = size - offset;
        size_t current_chunk = (remaining < chunk_size) ? remaining : chunk_size;
        incremental_neon = adler32_neon_update(incremental_neon, data + offset, current_chunk);
    }
    incremental_neon = adler32_neon_final(incremental_neon);
    
    /* Compare results */
    printf("  Direct calculation:      0x%08x\n", direct_neon);
    printf("  Incremental calculation: 0x%08x\n", incremental_neon);
    printf("  Match: %s\n\n", (direct_neon == incremental_neon) ? "YES" : "NO");
    
    /* Compare simple vs NEON */
    printf("Cross implementation comparison:\n");
    printf("  Simple checksum: 0x%08x\n", direct);
    printf("  NEON checksum:   0x%08x\n", direct_neon);
    printf("  Match: %s\n\n", (direct == direct_neon) ? "YES" : "NO");
    
    free(data);
}

int main(void) {
    /* Seed random number generator */
    srand((unsigned int)time(NULL));
    
    printf("Adler-32 Test and Benchmark\n");
    printf("===========================\n\n");
    
    /* Run verification tests with known test vectors */
    run_verification_tests();
    
    /* Test the incremental API */
    test_incremental_api();
    
    /* Run performance tests with different data sizes */
    run_performance_tests();
    
    return 0;
}


Made changes.

Let's update the Makefile to include the NEON implementation in the build:

# Makefile for Adler-32 checksum implementation
# Optimized for Neoverse N1 architecture

# Compiler and flags
CC = gcc
# Neoverse N1 specific optimization flags:
# -march=armv8.2-a+crypto: Target ARMv8.2-A architecture with crypto extensions (Neoverse N1)
# -mcpu=neoverse-n1: Specifically optimize for Neoverse N1
# -O3: Highest standard optimization level
# -flto: Link-time optimization
# -fomit-frame-pointer: Don't keep the frame pointer in a register for functions that don't need one
# -ftree-vectorize: Vectorize loops when possible
# -ffast-math: Enable fast math optimizations
# Additional useful flags:
# -Wall -Wextra: Enable warnings
# -g: Include debugging symbols
CFLAGS = -march=armv8.2-a+crypto -mcpu=neoverse-n1 -O3 -flto -fomit-frame-pointer -ftree-vectorize -ffast-math -Wall -Wextra -g

# Source files
SRCS = adler32-simple.c adler32-neon.c adler32-test.c
OBJS = $(SRCS:.c=.o)
TARGET = adler32-test

# Default target
all: $(TARGET)

# Link the executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

# Compile source files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Run the tests
run: $(TARGET)
	./$(TARGET)

# Clean generated files
clean:
	rm -f $(OBJS) $(TARGET)

# Rebuild the project
rebuild: clean all

.PHONY: all run clean rebuild


Made changes.

Now that I've created the NEON implementation and updated the test code and Makefile, let's compile and run the code to see the performance comparison.

```

GitHub Copilot generated a NEON-optimized implementation of Adler32, along with updates to the test program and Makefile. These changes make it easy to compare the performance of both versions.

Continue to the next section to compile and run the NEON version, and to compare its performance against the original implementation. 
