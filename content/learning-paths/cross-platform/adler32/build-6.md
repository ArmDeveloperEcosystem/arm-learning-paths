---
title: Build and run the test program
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How can I build and run the test program? 

You now have all the required files to test the Adler32 algorithm:
- A C implementation of the Adler32 function.
- A test program to verify correctness and measure performance.
- A Makefile to build and run the project.

Paste the following prompt into your GitHub Copilot Agent session:

```console
Use the Makefile to build the project and run to make sure the checksum results are correct for all data sizes.
```

The output is:

```output

GitHub Copilot: I'll help you build and run the Adler-32 checksum project to verify the results. Let me do this step-by-step.

First, let's build the project using the provided Makefile:Great! The build completed successfully without any errors or warnings. The Makefile compiled both source files (`adler32-simple.c` and adler32-test.c) and linked them into the executable adler32-test.

Now let's run the tests to verify that the Adler-32 checksum implementation works correctly for all data sizes:I ran the Adler-32 checksum project, and here are the results:

The build completed successfully without any errors or warnings. The Makefile correctly compiled both source files (`adler32-simple.c` and adler32-test.c) and linked them into the executable adler32-test.

When running the tests, I got the following results:

### Verification Tests
All 6 verification tests passed successfully:
1. Empty string: PASS
2. "a": PASS
3. "abc": PASS
4. "message digest": PASS
5. "abcdefghijklmnopqrstuvwxyz": PASS
6. "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789": PASS

### Incremental API Test
The incremental API test also passed, showing that both direct and incremental calculation methods produce the same checksum (0x3d094d1a).

### Performance Tests
The implementation was benchmarked with different data sizes:
- 1 KB: 195.31 MB/s
- 10 KB: 128.50 MB/s
- 100 KB: 261.11 MB/s
- 1 MB: 297.80 MB/s
- 10 MB: 298.17 MB/s

The results confirm that your Adler-32 checksum implementation is correct for all data sizes and performs efficiently. The optimizations for the Neoverse N1 architecture specified in the Makefile appear to be working properly, with throughput reaching nearly 300 MB/s for larger data sizes.

```

The results from GitHub Copilot confirm that the Adler32 checksum calculations are correct and provide initial performance benchmarks. These results offer a solid baseline, but a meaningful comparison requires an optimized implementation.

In the next section, you’ll implement Adler32 using NEON intrinsics and compare its performance against this baseline.