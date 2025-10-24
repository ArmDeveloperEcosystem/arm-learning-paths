---
title: SME2 assembly matrix multiplication
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Overview

In this section, you'll learn how to run an SME2-optimized matrix multiplication implemented directly in assembly.

This implementation is based on the algorithm described in [Arm's SME Programmer's
Guide](https://developer.arm.com/documentation/109246/0100/matmul-fp32--Single-precision-matrix-by-matrix-multiplication) and has been adapted to integrate with the existing C and intrinsics-based code in this Learning Path. It demonstrates how to apply low-level optimizations for matrix multiplication using the SME2 instruction set, with a focus on preprocessing and outer-product accumulation.

You'll explore how the assembly implementation works in practice, how it interfaces with C wrappers, and how to verify or benchmark its performance. Whether you're validating correctness or measuring execution speed, this example provides a clear, modular foundation for working with SME2 features in your own codebase.

By mastering this assembly implementation, you'll gain deeper insight into SME2 execution patterns and how to integrate low-level optimizations in high-performance workloads.

## About the SME2 assembly implementation

This Learning Path reuses the assembly version described in [The SME Programmer's
Guide](https://developer.arm.com/documentation/109246/0100/matmul-fp32--Single-precision-matrix-by-matrix-multiplication)
where you will find both high-level concepts and in-depth descriptions of the two key steps:
preprocessing and matrix multiplication.

The assembly code has been modified to work seamlessly alongside the intrinsic version.

The key changes include:
* Delegating streaming mode control to the compiler
* Avoiding register `x18`, which is reserved as a platform register

Here:
- The `preprocess` function is named `preprocess_l_asm` and is defined in `preprocess_l_asm.S`
- The outer product-based matrix multiplication is named `matmul_asm_impl` and is defined in `matmul_asm_impl.S`

Both functions are declared in `matmul.h`:

```C
// Matrix preprocessing, in assembly.
void preprocess_l_asm(uint64_t M, uint64_t K, const float *restrict a,
                      float *restrict a_mod) __arm_streaming __arm_inout("za");

// Matrix multiplication (with the *transposed* RHS), in assembly.
void matmul_asm_impl(
    uint64_t M, uint64_t K, uint64_t N, const float *restrict matLeft_mod,
    const float *restrict matRight,
    float *restrict matResult) __arm_streaming __arm_inout("za");
```

Both functions are annotated with the `__arm_streaming` and `__arm_inout("za")` attributes. These indicate that the function expects streaming mode to be active and does not need to save or restore the ZA storage.

These two functions are stitched together in `matmul_asm.c` with the same prototype as the reference implementation of matrix multiplication, so that a top-level `matmul_asm` can be called from the `main` function:

```C
__arm_new("za") __arm_locally_streaming void matmul_asm(
    uint64_t M, uint64_t K, uint64_t N, const float *restrict matLeft,
    const float *restrict matRight, float *restrict matLeft_mod,
    float *restrict matResult) {

    preprocess_l_asm(M, K, matLeft, matLeft_mod);
    matmul_asm_impl(M, K, N, matLeft_mod, matRight, matResult);
}
```

You can see that `matmul_asm` is annotated with two attributes: `__arm_new("za")` and `__arm_locally_streaming`. These attributes instruct the compiler to enable streaming mode and manage ZA state on entry and return.

## How it integrates with the main function

The same `main.c` file supports both the intrinsic and assembly implementations. The implementation to use is selected at compile time via the `IMPL` macro. This design reduces duplication and simplifies maintenance.

## Execution modes

- On a baremetal platform, the program runs in *verification mode*, where it compares the results of the assembly-based matrix multiplication with the vanilla reference implementation. When targeting a non-baremetal platform, a *benchmarking mode* is also available.

```C { line_numbers="true" }
#ifndef __ARM_FEATURE_SME2
#error __ARM_FEATURE_SME2 is not defined
#endif

#ifndef IMPL
#error matmul implementation selection macro IMPL is not defined
#endif

#include "matmul.h"
#include "misc.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define STRINGIFY_(I) #I
#define STRINGIFY(I) STRINGIFY_(I)
#define FN(M, I) M##I
#define MATMUL(I, M, K, N, mL, mR, mM, m) FN(matmul_, I)(M, K, N, mL, mR, mM, m)

void usage(const char *prog_name) {
#if BAREMETAL == 1
    printf("Usage: %s <M> <K> <N>\n", prog_name);
    printf("  M: number of rows in matLeft (default: 125)\n");
    printf("  K: number of columns in matLeft and matRight (default: 35)\n");
    printf("  N: number of columns in matRight (default: 70)\n");
    printf("Example: matmul 125 35 70\n");
#else
    printf("Depending on the number of arguments, the program can be invoked "
           "in two modes:\n");
    printf(" - verification mode. The program will run the assembly or "
           "intrinsics implementatation of the matrix multiplication and "
           "compare the results with a reference implementation.\n");
    printf(" - benchmarking mode. The program will run the assembly or "
           "intrinsics implementation of the matrix multiplication a number of "
           "times and print the time taken to perform the operation.\n");

    printf("\n");
    printf("Verification mode:\n");
    printf(" %s\n", prog_name);
    printf(" %s <M> <K> <N>\n", prog_name);
    printf("with:\n");
    printf("  - M: number of rows in matLeft (default: 125)\n");
    printf("  - K: number of columns in matLeft and number of rows in matRight "
           "(default: 35). Must be > 2 for assembly version of matmul.\n");
    printf("  - N: number of columns in matRight (default: 70)\n");
    printf("Example: %s 67 18 23\n", prog_name);

    printf("\n");
    printf("Benchmarking mode:\n");
    printf(" %s <I>\n", prog_name);
    printf(" %s <I> <M> <K> <N>\n", prog_name);
    printf("with:\n");
    printf("  - I: number of iterations to perform. Must be > 0.\n");
    printf("  - M: number of rows in matLeft (default: 125)\n");
    printf("  - K: number of columns in matLeft and number of rows in matRight "
           "(default: 35). Must be > 2 for assembly version of matmul.\n");
    printf("  - N: number of columns in matRight (default: 70)\n");
    printf("Example: %s 1000 67 18 23\n", prog_name);
#endif
}

int main(int argc, char **argv) {

    /* Matrices size parameters, defaults to 125x35x70.
       Assumptions (for assembly handwritten matmul) are:
         - number of rows in matLeft (M): any
         - number of columns in matLeft and number of rows in matRight (K): any K > 2
         - number of columns in matRight (N): any
    */
    uint64_t I = 0; // Number of iterations to perform for benchmarking.
    uint64_t M = 125; // Number of rows in matLeft.
    uint64_t N = 35;  // Number of columns in matRight.
    uint64_t K = 70;  // Number of columns (resp. rows) in matLeft (resp. matRight).

    switch (argc) {
    case 1:
        // Verification mode, with default matrix sizes.
        break;
#if BAREMETAL == 0
    case 2:
        // Benchmarking mode, with default matrix sizes.
        I = strtoull(argv[1], NULL, 0);
        if (I == 0) {
            printf("Error, in benchmarking mode, I must be > 0.\n");
            return EXIT_FAILURE;
        }
        break;
#endif
    case 4:
        // Verification mode, with user-defined matrix sizes.
        M = strtoul(argv[1], NULL, 0);
        K = strtoul(argv[2], NULL, 0);
        N = strtoul(argv[3], NULL, 0);
        break;
#if BAREMETAL == 0
    case 5:
        // Benchmarking mode, with user-defined matrix sizes.
        I = strtoull(argv[1], NULL, 0);
        if (I == 0) {
            printf("Error, in benchmarking mode, I must be > 0.\n");
            return EXIT_FAILURE;
        }
        M = strtoul(argv[2], NULL, 0);
        K = strtoul(argv[3], NULL, 0);
        N = strtoul(argv[4], NULL, 0);
        break;
#endif
    default:
        usage(argv[0]);
        return EXIT_FAILURE;
    }

    // Check assumptions hold.
    if (strcmp(STRINGIFY(IMPL), "asm")==0 && K <= 2) {
        printf("Error, for assembly implementation of matmul, K must be > 2.\n");
        return EXIT_FAILURE;
    }

    // Describe the operation that will be performed.
    printf("SME2 Matrix Multiply fp32 *%s* ", STRINGIFY(IMPL));
    if (I != 0)
        printf("[benchmarking mode, %" PRIu64 " iterations] ", I);
    else
        printf("[verification mode] ");
    printf("with M=%" PRIu64 ", K=%" PRIu64 ", N=%" PRIu64 "\n", M, K, N);

#if BAREMETAL == 1
    setup_sme_baremetal();
#endif

    const uint64_t SVL = svcntsw();

    // Calculate M of transformed matLeft.
    const uint64_t M_mod = SVL * (M / SVL + (M % SVL != 0 ? 1 : 0));

    // Allocate memory for all matrices.
    float *matRight = (float *)malloc(K * N * sizeof(float));

    float *matLeft = (float *)malloc(M * K * sizeof(float));
    float *matLeft_mod = (float *)malloc(M_mod * K * sizeof(float));
    float *matLeft_mod_ref = (float *)malloc(M_mod * K * sizeof(float));

    float *matResult = (float *)malloc(M * N * sizeof(float));
    float *matResult_ref = (float *)malloc(M * N * sizeof(float));

    // Initialize matrices. Input matrices are initialized with random values in
    // non-debug mode. In debug mode, all matrices are initialized with linear
    // or known values for easier debugging.
#ifdef DEBUG
    initialize_matrix(matLeft, M * K, LINEAR_INIT);
    initialize_matrix(matRight, K * N, LINEAR_INIT);
    initialize_matrix(matLeft_mod, M_mod * K, DEAD_INIT);
    initialize_matrix(matResult, M * N, DEAD_INIT);

    print_matrix(M, K, matLeft, "matLeft");
    print_matrix(K, N, matRight, "matRight");
#else
    initialize_matrix(matLeft, M * K, RANDOM_INIT);
    initialize_matrix(matRight, K * N, RANDOM_INIT);
#endif

    unsigned error = 0;
    if (I == 0) {
        // Verification mode.
        MATMUL(IMPL, M, K, N, matLeft, matRight, matLeft_mod, matResult);

        // Compute the reference values with the vanilla implementations.
        preprocess_l(M, K, SVL, matLeft, matLeft_mod_ref);
        matmul(M, K, N, matLeft, matRight, matResult_ref);

        error = compare_matrices(K, M_mod, matLeft_mod_ref, matLeft_mod,
                                 "Matrix preprocessing");
        if (!error)
            error = compare_matrices(M, N, matResult_ref, matResult,
                                     "Matrix multiplication");
    } else {
#if BAREMETAL == 0
        // Benchmarking mode.
        uint64_t min_time = UINT64_MAX;
        uint64_t max_time = 0;
        double sum = 0.0;

        // Warm-up runs to ensure the CPU is ready for benchmarking.
        for (uint64_t i = 0; i < 10; i++)
            matmul(M, K, N, matLeft, matRight, matResult_ref);

        // Measure the time taken by the matrix multiplication.
        for (uint64_t i = 0; i < I; i++) {
            const uint64_t start_time = get_time_microseconds();
            matmul(M, K, N, matLeft, matRight, matResult_ref);
            const uint64_t elapsed_time = get_time_microseconds() - start_time;

            if (elapsed_time < min_time)
                min_time = elapsed_time;
            if (elapsed_time > max_time)
                max_time = elapsed_time;
            sum += elapsed_time;
        }
        printf("Reference implementation: min time = %" PRIu64 " us, "
               "max time = %" PRIu64 " us, avg time = %.2f us\n",
               min_time, max_time, sum / I);

        // Benchmarking mode (SME2 implementation).
        min_time = UINT64_MAX;
        max_time = 0;
        sum = 0.0;

        // Warm-up runs to ensure the CPU is ready for benchmarking.
        for (uint64_t i = 0; i < 10; i++)
            MATMUL(IMPL, M, K, N, matLeft, matRight, matLeft_mod, matResult);

        // Measure the time taken by the SME2 matrix multiplication.
        for (uint64_t i = 0; i < I; i++) {
            const uint64_t start_time = get_time_microseconds();
            MATMUL(IMPL, M, K, N, matLeft, matRight, matLeft_mod, matResult);
            const uint64_t elapsed_time = get_time_microseconds() - start_time;

            if (elapsed_time < min_time)
                min_time = elapsed_time;
            if (elapsed_time > max_time)
                max_time = elapsed_time;
            sum += elapsed_time;
        }
        printf("SME2 implementation *%s*: min time = %" PRIu64 " us, "
               "max time = %" PRIu64 " us, avg time = %.2f us\n",
               STRINGIFY(IMPL), min_time, max_time, sum / I);
#else
        printf("Error, can not run in benchmarking mode in baremetal.\n");
        return EXIT_FAILURE;
#endif
    }

    // Free allocated memory.
    free(matRight);

    free(matLeft);
    free(matLeft_mod);
    free(matLeft_mod_ref);

    free(matResult);
    free(matResult_ref);

    return error ? EXIT_FAILURE : EXIT_SUCCESS;
}
```

The same `main.c` file is used for the assembly and intrinsic-based versions of the matrix multiplication. It first sets the `M`, `K` and `N` parameters, to either the arguments supplied on the command line (lines 93-95) or uses the default value (lines 73-75). In non-baremetal mode, it also accepts (lines 82-89 and lines 98-108), as first parameter, an iteration count `I`
used for benchmarking.

Depending on the `M`, `K`, `N` dimension parameters, `main` allocates memory for all the matrices and initializes `matLeft` and `matRight` with random data. The actual matrix multiplication implementation is provided through the `IMPL` macro.

In *verification mode*, it then runs the matrix multiplication from `IMPL` (line 167) and computes the reference values for the preprocessed matrix as well as the result matrix (lines 170 and 171). It then compares the actual values to the reference values and reports errors, if there are any (lines 173-177). Finally, all the memory is deallocated (lines 236-243) before exiting the
program with a success or failure return code at line 245.

In *benchmarking mode*, it will first run the vanilla reference matrix multiplication (resp. assembly- or intrinsic-based matrix multiplication) 10 times without measuring elapsed time to warm-up the CPU. It will then measure the elapsed execution time of the vanilla reference matrix multiplication (resp.assembly- or intrinsic-based matrix multiplication) `I` times and then compute
and report the minimum, maximum and average execution times.

{{% notice Note %}}
Benchmarking and profiling are not simple tasks. The purpose of this Learning Path is to provide some basic guidelines on the performance improvement that can be obtained with SME2.
{{% /notice %}}

### Compile and run it

First, make sure that the `sme2_matmul_asm` executable is up-to-date:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-3">}}
ninja -C build-native/ sme2_matmul_asm
ninja: Entering directory `build-native/'
ninja: no work to do.
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2-3">}}
ninja -C build-android/ sme2_matmul_asm
ninja: Entering directory `build-android/'
ninja: no work to do.
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-3">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ninja -C build-baremetal/ sme2_matmul_asm
ninja: Entering directory `build-baremetal/'
ninja: no work to do.
{{< /tab >}}

{{< /tabpane >}}

Then execute `sme2_matmul_asm` either natively, or on the FVP, or on the Android phone:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-4">}}
./build-native/sme2_matmul_asm
SME2 Matrix Multiply fp32 *asm* [verification mode] with M=125, K=70, N=35
Matrix preprocessing: PASS !
Matrix multiplication: PASS !
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2,5-7">}}
adb push build-android/sme2_matmul_asm /data/local/tmp
build-android/sme2_matmul_asm: 1 file pushed, 0 skipped. 29.7 MB/s (19456 bytes in 0.001s)
adb shell chmod 755 /data/local/tmp/sme2_matmul_asm
adb shell /data/local/tmp/sme2_matmul_asm
SME2 Matrix Multiply fp32 *asm* [verification mode] with M=125, K=70, N=35
Matrix preprocessing: PASS !
Matrix multiplication: PASS !
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-6">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ./run-fvp.sh build-baremetal/sme2_matmul_asm
SME2 Matrix Multiply fp32 *asm* [verification mode] with M=125, K=70, N=35
Matrix preprocessing: PASS !
Matrix multiplication: PASS !

Info: /OSCI/SystemC: Simulation stopped by user.
{{< /tab >}}

{{< /tabpane >}}

`sme2_matmul_asm` prints the version of the matrix multiplication performed
(`asm` or `intr`) as well as the `M`, `K` and `N` parameters. It also prints
whether the preprocessing and matrix multiplication passed (`PASS`) or failed
(`FAILED`) the comparison the vanilla reference implementation.

{{% notice Tip %}}
The example above uses the default values for the `M` (125), `K`(70) and `N`(70)
parameters. You can override this and provide your own values on the command line
when executing `sme2_matmul_asm`:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash">}}
./build-native/sme2_matmul_asm 7 8 9
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash">}}
adb shell /data/local/tmp/sme2_matmul_asm 7 8 9
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ./run-fvp.sh build-baremetal/sme2_matmul_asm 7 8 9
{{< /tab >}}

{{< /tabpane >}}

In this example, `M=7`, `K=8`, and `N=9` are used.
{{% /notice %}}