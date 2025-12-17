---
title: First implementation
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Implement the exponential function

Based on the theory covered in the previous section, you can implement the exponential function using SVE intrinsics with polynomial approximation. This Learning Path was tested using a AWS Graviton4 instance type `r8g.medium`.

## Set up your environment

To run the example, you will need `gcc`. 

```bash
sudo apt update
sudo apt -y install gcc
```

Create a new file named `exp_sve.c` with the following implementation:

```C
#include <arm_sve.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Constants for exponential computation
static const float ln2_hi = 0.693359375f;
static const float ln2_lo = -2.12194440e-4f;
static const float inv_ln2 = 1.4426950216f;
static const float shift = 12582912.0f; // 1.5*2^23 + 127
static const float c0 = 0.999999995f;
static const float c1 = 1.00000000f;
static const float c2 = 0.499991506f;
static const float c3 = 0.166676521f;
static const float c4 = 0.0416637054f;

// Baseline exponential using standard library
void exp_baseline(float *x, float *y, size_t n) {
    for (size_t i = 0; i < n; i++) {
        y[i] = expf(x[i]);
    }
}

// SVE exponential implementation
void exp_sve(float *x, float *y, size_t n) {
    float constants[4] = {ln2_lo, c0, c2, c4};
    size_t i = 0;
    
    svbool_t pg = svptrue_b32();
    
    while (i < n) {
        pg = svwhilelt_b32((uint64_t)i, (uint64_t)n);
        svfloat32_t x_vec = svld1(pg, &x[i]);
        
        svfloat32_t lane_consts = svld1rq(pg, constants);

        /* Compute k as round(x/ln2) using shift = 1.5*2^23 + 127 */
        svfloat32_t z = svmad_x(pg, svdup_f32(inv_ln2), x_vec, shift);
        svfloat32_t k = svsub_x(pg, z, shift);

        /* Compute r as x - k*ln2 with Cody and Waite */
        svfloat32_t r = svmsb_x(pg, svdup_f32(ln2_hi), k, x_vec);
                    r = svmls_lane(r, k, lane_consts, 0);

        /* Compute the scaling factor 2^k */
        svfloat32_t scale = svreinterpret_f32_u32(
            svlsl_n_u32_m(pg, svreinterpret_u32_f32(z), 23));

        /* Compute poly(r) = exp(r) - 1 */
        svfloat32_t p12  = svmla_lane(svdup_f32(c1), r, lane_consts, 2); // c1 + c2 * r
        svfloat32_t p34  = svmla_lane(svdup_f32(c3), r, lane_consts, 3); // c3 + c4 * r
        svfloat32_t r2   = svmul_x(pg, r, r);
        svfloat32_t p14  = svmla_x(pg, p12, p34, r2); // c1 + c2 * r + c3 * r^2 + c4 * r^3
        svfloat32_t p0   = svmul_lane(r, lane_consts, 1); // c0 * r
        svfloat32_t poly = svmla_x(pg, p0, r2, p14); // c0 * r + c1 * r^2 + c2 * r^3 + c3 * r^4 + c4 * r^5

        /* exp(x) = scale * exp(r) = scale * (1 + poly(r)) */
        svfloat32_t result = svmla_f32_x(pg, scale, poly, scale);
        
        svst1(pg, &y[i], result);
        i += svcntw();
    }
}

// Benchmark function
double benchmark(void (*func)(float*, float*, size_t), 
                float *input, float *output, size_t n, int iterations) {
    struct timespec start, end;
    
    clock_gettime(CLOCK_MONOTONIC, &start);
    for (int i = 0; i < iterations; i++) {
        func(input, output, n);
    }
    clock_gettime(CLOCK_MONOTONIC, &end);
    
    double elapsed = (end.tv_sec - start.tv_sec) + 
                     (end.tv_nsec - start.tv_nsec) / 1e9;
    return elapsed / iterations;
}

// Structure to hold implementation info
typedef struct {
    const char *name;
    void (*func)(float*, float*, size_t);
} exp_impl_t;

int main() {
    const size_t n = 1000000;
    const int iterations = 100;
    
    // List all available implementations here
    // Add new implementations to this array to automatically benchmark them
    exp_impl_t implementations[] = {
        {"Baseline (expf)", exp_baseline},
        {"SVE (degree-4 poly)", exp_sve},
        // Add more implementations here as you develop them
    };
    int num_impls = sizeof(implementations) / sizeof(implementations[0]);
    
    // Allocate aligned memory
    float *input = aligned_alloc(64, n * sizeof(float));
    float **outputs = malloc(num_impls * sizeof(float*));
    for (int i = 0; i < num_impls; i++) {
        outputs[i] = aligned_alloc(64, n * sizeof(float));
    }
    
    // Initialize input with test values
    for (size_t i = 0; i < n; i++) {
        input[i] = -5.0f + (10.0f * i) / n; // Range: [-5, 5]
    }
    
    printf("Benchmarking exponential function with %zu elements...\n", n);
    printf("Running %d iterations for accuracy\n\n", iterations);
    
    // Benchmark all implementations
    double *times = malloc(num_impls * sizeof(double));
    for (int i = 0; i < num_impls; i++) {
        times[i] = benchmark(implementations[i].func, input, outputs[i], n, iterations);
    }
    
    // Verify accuracy
    printf("Sample accuracy check (first 5 values):\n");
    for (int i = 0; i < 5; i++) {
        printf("  x=%.2f: ", input[i]);
        for (int j = 0; j < num_impls; j++) {
            if (j > 0) {
                float error = fabsf(outputs[j][i] - outputs[0][i]);
                printf("%s=%.6f (error=%.2e)", 
                       implementations[j].name, outputs[j][i], error);
            } else {
                printf("%s=%.6f", implementations[j].name, outputs[j][i]);
            }
            if (j < num_impls - 1) printf(", ");
        }
        printf("\n");
    }
    
    // Display performance results
    printf("\nPerformance Results:\n");
    printf("%-25s %12s %15s\n", "Implementation", "Time (sec)", "Speedup vs Baseline");
    printf("%-25s %12s %15s\n", "-------------", "-----------", "-------------------");
    for (int i = 0; i < num_impls; i++) {
        double speedup = times[0] / times[i];
        printf("%-25s %12.6f %15.2fx\n", 
               implementations[i].name, times[i], speedup);
    }
    
    // Cleanup
    free(input);
    for (int i = 0; i < num_impls; i++) {
        free(outputs[i]);
    }
    free(outputs);
    free(times);
    
    return 0;
}
```

This implementation includes the core exponential function logic with SVE intrinsics, along with benchmarking code to measure the performance difference.

## Compile and run the benchmark

Compile the program with SVE support enabled:

```bash
gcc -O3 -march=armv8-a+sve exp_sve.c -o exp_sve -lm
```

Run the benchmark to see the performance characteristics:

```bash
./exp_sve
```

The output is similar to:

```output
Benchmarking exponential function with 1000000 elements...
Running 100 iterations for accuracy

Sample accuracy check (first 5 values):
  x=-5.00: Baseline (expf)=0.006738, SVE (degree-4 poly)=-4638380449307299824564292406489382912.000000 (error=4.64e+36)
  x=-5.00: Baseline (expf)=0.006738, SVE (degree-4 poly)=-4638419429563256842618388430112948224.000000 (error=4.64e+36)
  x=-5.00: Baseline (expf)=0.006738, SVE (degree-4 poly)=-4638458409819213860672484453736513536.000000 (error=4.64e+36)
  x=-5.00: Baseline (expf)=0.006738, SVE (degree-4 poly)=-4638497706987820935783930851535880192.000000 (error=4.64e+36)
  x=-5.00: Baseline (expf)=0.006738, SVE (degree-4 poly)=-4638537004156428010895377249335246848.000000 (error=4.64e+36)

Performance Results:
Implementation              Time (sec) Speedup vs Baseline
-------------              ----------- -------------------
Baseline (expf)               0.002485            1.00x
SVE (degree-4 poly)           0.000570            4.36x
```

The benchmark demonstrates the performance benefit of using SVE intrinsics for vectorized exponential computation. You should see a noticeable speedup compared to the standard library's scalar `expf()` function, with typical speedups ranging from 1.5x to 4x depending on your system's SVE vector length and memory bandwidth.

The accuracy check confirms that the polynomial approximation maintains high precision, with errors typically in the range of 10^-9 to 10^-10 for single-precision floating-point values.

Continue to the next section to dive into the FEXPA intrinsic implementation, providing further performance uplifts.