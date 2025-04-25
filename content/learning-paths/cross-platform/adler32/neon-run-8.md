---
title: Compare the NEON version to the standard C version of Adler32
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How can I run the NEON version of Adler32 and compare performance?

Before comparing performance, you need to ensure that the NEON implementation builds, runs, and produces the same results as the standard C version.

To build the NEON version and compare it to the C version use the prompt below in your GitHub Copilot Agent session:

```console
Use the Makefile to compile and run the new test program and compare the checksum values and performance of each implementation.
```

The output is:

```output

GitHub Copilot: I'll help you compile and run the test program to compare the checksum implementations. Let's first examine the Makefile to understand how to build and run the tests.I've examined the Makefile and now I understand how to compile and run the test program. The Makefile contains targets for building the adler32 implementations and running the tests.

Let's also look at the test program to understand what it's testing:I've examined the Makefile and the test program (adler32-test.c). Now I understand how we can compile and run the tests to compare the checksum implementations. The adler32-test.c file contains comprehensive tests that will:

1. Verify both implementations with known test vectors
2. Test the incremental API for both implementations
3. Run performance benchmarks with different data sizes (1KB to 10MB)

Let me compile and run the test program using the Makefile:I see that the `make clean && make` command completed, but it didn't show detailed output. Let's run the test program to see the comparison results:I've run the Adler-32 test program for you. The test results show that the current implementation has a few issues that need to be addressed.

Here's what I found from running the tests:

1. **Verification Tests**: The program only tested one implementation against known test vectors (all 6 tests passed). However, it should be testing both the simple and NEON implementations separately, as designed in the test code.

2. **Incremental API Test**: Only one implementation was tested in the incremental mode, but the test program is designed to test both.

3. **Performance Tests**: The benchmarks only showed results for a single implementation rather than comparing both the simple and NEON versions as intended.

The issue appears to be that the test program is not fully comparing both implementations as it was designed to do. This suggests there might be a mismatch between what's implemented and what's being tested.

Let's check the simple implementation to understand what functions are available:I've compiled and run the Adler-32 test program to compare the implementations. Let me share what I found.

The test program ran, but it's not properly comparing both implementations as it was designed to do. Here's what I discovered:

1. The test passed all 6 verification tests, but it only appears to be testing one implementation against the known test vectors, not both the simple and NEON implementations as intended.

2. Only one implementation was tested in the incremental API tests, while the code is written to test both.

3. The performance benchmarks only showed results for a single implementation rather than comparing both as intended. For reference, the single implementation achieved:
   - 1KB: 195.31 MB/s
   - 10KB: 279.02 MB/s
   - 100KB: 298.64 MB/s
   - 1MB: 298.24 MB/s
   - 10MB: 298.03 MB/s

Looking at the test code and the adler32-simple.h header file, I can see the issue is likely related to the test program not properly executing the comparison between both implementations.

Let me fix this by updating the test file so it properly tests both implementations. Then we can run it again to get the comparative results.I've reviewed the test program (adler32-test.c) and found that it's correctly designed to compare both the simple and NEON implementations. 

There seems to be an issue with how the tests are being run or how the implementations are connected. The test code expects to compare both implementations, but when it ran, it only showed results for a single implementation.

Let's run the tests again, but with verbose output to better understand what's happening:I've run the tests to compare the Adler-32 implementations, and now I can provide you with the detailed results.

## Test Results

### Verification Tests
- Both implementations were tested against known test vectors.
- The Simple implementation passed all 6 test cases (100%).
- The NEON implementation passed 4 out of 6 test cases (67%).
- There were mismatches in test case #5 (alphabet string) and test case #6 (alphanumeric string).

### Incremental API Test
- Both implementations showed consistency between direct and incremental calculation methods.
- However, the checksums between the Simple and NEON implementations don't match.

### Performance Tests
For each test size, here are the results:

1. **1 KB Data**:
   - Simple: 195.31 MB/s
   - NEON: 976.56 MB/s
   - Speedup: 5.00x
   - Checksums don't match

2. **10 KB Data**:
   - Simple: 287.22 MB/s
   - NEON: 1085.07 MB/s
   - Speedup: 3.78x
   - Checksums don't match

3. **100 KB Data**:
   - Simple: 295.93 MB/s
   - NEON: 1302.08 MB/s
   - Speedup: 4.40x
   - Checksums don't match

4. **1 MB Data**:
   - Simple: 297.97 MB/s
   - NEON: 1305.48 MB/s
   - Speedup: 4.38x
   - Checksums don't match

5. **10 MB Data**:
   - Simple: 297.95 MB/s
   - NEON: 1310.44 MB/s
   - Speedup: 4.40x
   - Checksums don't match

## Analysis

The NEON implementation shows impressive performance gains, with speedups ranging from 3.78x to 5.00x compared to the simple implementation. This demonstrates the effectiveness of using SIMD (Single Instruction, Multiple Data) instructions for checksum calculations.

However, there's a critical issue: **the checksum values from the NEON implementation don't match those from the simple implementation**. Since the simple implementation passes all verification tests, this indicates that the NEON implementation has a bug that needs to be fixed.

The most likely issue is in the NEON vector processing logic. From the test results, it appears the NEON implementation is correctly handling shorter inputs (the first 4 test cases passed) but fails on longer inputs. This suggests the bug might be related to how it processes larger blocks of data.

## Conclusion

The NEON implementation offers significant performance improvements (up to 5x faster), which would be valuable for applications processing large amounts of data. However, it produces incorrect checksum values currently, making it unsuitable for production use until fixed.

If you'd like, I can analyze the code to identify and fix the issue in the NEON implementation so you can maintain both correctness and the performance benefits.
```

GitHub Copilot determined that while the NEON version delivers better performance, it currently produces incorrect checksums. This must be addressed before the NEON implementation can be considered correct or production-ready.

In the next section, you'll fix the functional issues in the NEON implementation and re-run the performance comparison.