---
title: FEXPA
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The FEXPA instruction

Arm introduced in SVE an instruction called FEXPA: the Floating Point Exponential Accelerator. 

Let’s segment the IEEE 754 floating-point representation fraction part into several sub-fields (Index, Exp and Remaining bits) with respective length of _Idxb_, _Expb_ and _Remb_ bits.

| IEEE 754 precision       | Idxb | Expb | Remb |
|-------------------------|------|------|------|
| Half precision (FP16)   | 5    | 5    | 0    |
| Single precision (FP32) | 6    | 8    | 9    |
| Double precision (FP64) | 6    | 11   | 35   |

The FEXPA instruction can be described for any real number x ∈ [2^(Remb + Expb) + 1; 2^(Remb + Expb) + 2^Expb - 1) as: 

$$FEXPA(x)=2^{x-constant}$$

where

$$constant=2^{remBits + expBits} + bias$$

The instruction takes the floating-point value x as an input and, by copying some fraction bits y into the result’s exponent, which is then interpreted as 2^(y-bias), and by getting the correct fraction value from a hardware lookup table using the lower fraction bits, the result becomes 2^(x-constant).

## Usage of lookup tables
Lookup tables can be combined with polynomial approximations. In this approach, the exponential function is reformulated as:

$$e^x = e^{(m \times 2^L + j) \times ln2⁄2^L +r} = 2^m \times (2^{j⁄2^L} + 2^{j⁄2^L} \times p(r)) $$

where

$$r∈[-ln2/2^{L+1}, +ln2/2^{L+1}], j \in [0, 2^L - 1]$$

and p(r) approximates e^r -1.

If the 2^L possible values of 2^(j⁄2^L) are precomputed in table T, the exponential can be approximated as:
$$ e^x = 2^m \times T[j] \times (1 + p(r)) $$

With a table of size 2^L, the evaluation interval for the approximation polynomial is narrowed  by a factor of 2^L. This reduction leads to improved accuracy for a given polynomial degree due to the narrower approximation range. Alternatively, for a given accuracy target, the degree of the polynomial—and hence its computational complexity—can be reduced.

## Exponential implementation with FEXPA

FEXPA can be used to rapidly perform the table lookup. With this instruction a degree-2 polynomial is sufficient to obtain the same accuracy as the degree-4 polynomial implementation from the previous section.

### Add the FEXPA implementation

Open your `exp_sve.c` file and add the following function after the `exp_sve()` function:

```C
// SVE exponential implementation with FEXPA (degree-2 polynomial)
void exp_sve_fexpa(float *x, float *y, size_t n) {
    // FEXPA-specific coeffs
    const float c0_fexpa = 1.000003695487976f;   // 0x1.00003ep0
    const float c1_fexpa = 0.5000003576278687f;  // 0x1.00000cp-1
    const float shift_fexpa = 196735.0f;         // 1.5*2^(23-6) + 127

    size_t i = 0;

    const svfloat32_t ln2lo_vec = svdup_f32(ln2_lo);

    while (i < n) {
        const svbool_t pg = svwhilelt_b32((uint64_t)i, (uint64_t)n);
        svfloat32_t x_vec = svld1(pg, &x[i]);

        /* Compute k as round(x/ln2) using shift = 1.5*2^(23-6) + 127 */
        svfloat32_t z = svmad_x(pg, svdup_f32(inv_ln2), x_vec, svdup_f32(shift_fexpa));
        svfloat32_t k = svsub_x(pg, z, svdup_f32(shift_fexpa));

        /* Compute r as x - k*ln2 with Cody and Waite */
        svfloat32_t r = svmsb_x(pg, svdup_f32(ln2_hi), k, x_vec);
                    r = svmls_lane_f32(r, k, ln2lo_vec, 0);

        /* Compute the scaling factor 2^k using FEXPA */
        svfloat32_t scale = svexpa(svreinterpret_u32_f32(z));

        /* Compute poly(r) = exp(r) - 1 (degree-2 polynomial) */
        svfloat32_t p01  = svmla_x(pg, svdup_f32(c0_fexpa), r, svdup_f32(c1_fexpa)); // c0 + c1 * r
        svfloat32_t poly = svmul_x(pg, r, p01); // r * (c0 + c1 * r)

        /* exp(x) = scale * exp(r) = scale * (1 + poly(r)) */
        svfloat32_t result = svmla_f32_x(pg, scale, poly, scale);

        svst1(pg, &y[i], result);
        i += svcntw();
    }
}
```

{{% notice Arm Optimized Routines %}}
This implementation can be found in [ARM Optimized Routines](https://github.com/ARM-software/optimized-routines/blob/ba35b32/math/aarch64/sve/sv_expf_inline.h).
{{% /notice %}}


Now register this new implementation in the `implementations` array in `main()`. Find this section:

```C
    exp_impl_t implementations[] = {
        {"Baseline (expf)", exp_baseline},
        {"SVE (degree-4 poly)", exp_sve},
        // Add more implementations here as you develop them
    };
```

Add your FEXPA implementation to the array:

```C
    exp_impl_t implementations[] = {
        {"Baseline (expf)", exp_baseline},
        {"SVE (degree-4 poly)", exp_sve},
        {"SVE+FEXPA (degree-2)", exp_sve_fexpa},
    };
```

## Compile and compare

Recompile the program:

```bash
gcc -O3 -march=armv8-a+sve exp_sve.c -o exp_sve -lm
```

Run the benchmark:

```bash
./exp_sve
```

The output shows the final comparison:

```output
Performance Results:
Implementation              Time (sec) Speedup vs Baseline
-------------              ----------- -------------------
Baseline (expf)               0.002462            1.00x
SVE (degree-4 poly)           0.000578            4.26x
SVE+FEXPA (degree-2)          0.000414            5.95x
```

## Results analysis

The benchmark shows the performance progression:

1. **SVE with degree-4 polynomial**: Provides up to 4x speedup through vectorization
2. **SVE with FEXPA and degree-2 polynomial**: Achieves an additional 1-2x improvement

The FEXPA instruction delivers this improvement by:
- Replacing manual bit manipulation with a single hardware instruction (`svexpa()`)
- Enabling a simpler polynomial (degree-2 instead of degree-4) while maintaining accuracy

Both SVE implementations maintain comparable accuracy (errors in the 10^-9 to 10^-10 range), demonstrating that specialized hardware instructions can significantly improve performance without sacrificing precision.
