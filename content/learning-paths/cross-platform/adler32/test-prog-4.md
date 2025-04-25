---
title: Create a test program
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Do I Prompt Copilot to Generate a Test Program?

You can continue your GitHub Copilot Agent session to create a test program using the prompt below. 

Copy and paste the prompt into GitHub Copilot to generate a test program: 

```console
Create a C file named adler32-test.c which includes a main() function and calls the adler32 function in adler32-simple.c 
Add code around the adler32 calls to measure the performance of the adler32 checksum function. 
Generate a simple test to make sure the adler32 generates the expected checksum. 
Add randomly generated test data of various sizes: 1 kb, 10 kb, 100 kb, 1 mb, and 10 mb. 
Add code to run all test data with different sizes and measure performance.
Don't create the Makefile yet.
```

The output is below:

```output

GitHub Copilot: I'll create a test file for the Adler-32 implementation that includes performance testing with different data sizes. I'll first check the current implementation to understand how to use the functions properly.Now I understand how the Adler-32 implementation works. Let me create a test file that measures the performance of the adler32 function with different data sizes and verifies that it produces the expected checksums.

/*
 * adler32-test.c - Test and benchmark for Adler-32 checksum implementation
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdint.h>
#include "adler32-simple.h"

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

/* Run performance test on a data buffer */
static void test_performance(const unsigned char *data, size_t size, const char *test_name) {
    clock_t start, end;
    double cpu_time_used;
    uint32_t checksum;
    
    printf("Testing %s (%zu bytes):\n", test_name, size);
    
    /* Warm-up run */
    adler32(data, size, adler32_init());
    
    /* Timed run */
    start = clock();
    checksum = adler32(data, size, adler32_init());
    end = clock();
    
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    double throughput = (double)size / (cpu_time_used * MB);
    
    printf("  Checksum: 0x%08x\n", checksum);
    printf("  Time: %.6f seconds\n", cpu_time_used);
    printf("  Throughput: %.2f MB/s\n\n", throughput);
}

/* Run verification tests with known test vectors */
static void run_verification_tests(void) {
    printf("Running verification tests:\n");
    printf("==========================\n");
    
    int passed = 0;
    for (size_t i = 0; i < sizeof(test_vectors) / sizeof(test_vectors[0]); i++) {
        const struct test_vector *tv = &test_vectors[i];
        uint32_t result = adler32((const unsigned char *)tv->data, strlen(tv->data), adler32_init());
        
        printf("Test %zu: \"%s\"\n", i + 1, tv->data);
        printf("  Expected: 0x%08x\n", tv->expected);
        printf("  Result:   0x%08x\n", result);
        
        if (result == tv->expected) {
            printf("  Status: PASS\n");
            passed++;
        } else {
            printf("  Status: FAIL\n");
        }
        printf("\n");
    }
    
    printf("Verification summary: %d/%zu tests passed\n\n", 
           passed, sizeof(test_vectors) / sizeof(test_vectors[0]));
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

/* Test the incremental API */
static void test_incremental_api(void) {
    printf("Testing incremental API:\n");
    printf("=======================\n");
    
    /* Generate test data */
    size_t size = 1 * MB;
    unsigned char *data = generate_test_data(size);
    
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

I've created the adler32-test.c file with a comprehensive test suite for the Adler-32 checksum implementation. This test file includes:

1. **Verification tests** with known test vectors to ensure the implementation produces the expected output for standard inputs.

2. **Incremental API test** to verify that performing the checksum calculation incrementally (in chunks) produces the same result as calculating it in one pass.

3. **Performance tests** with randomly generated data of various sizes:
   - 1 KB
   - 10 KB
   - 100 KB
   - 1 MB
   - 10 MB

The test program performs the following operations:
- Generates random test data for each size
- Calculates the checksum for each data buffer
- Measures the execution time
- Calculates and displays the throughput in MB/s

The test output will show:
- Results from verification tests against known checksums
- Comparison between direct and incremental calculation
- Performance metrics for each data size

To compile and run this test, you'll need to use a command like:

gcc -Wall -O2 adler32-simple.c adler32-test.c -o adler32-test
./adler32-test

If you'd like me to create the Makefile for easier compilation, just let me know.

```

You now have a test program which confirms the Adler32 algorithm is working correctly for various input data and can measure the performance of the previously generated C function. 

Continue to the next section to run the test program and see the results.

