---
title: FEXPA
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The FEXPA instruction

Arm introduced in SVE an instruction called FEXPA: the Floating Point Exponential Accelerator. 

Let’s segment the IEEE754 floating-point representation fraction part into several sub-fields (Index, Exp and Remaining bits) with respective length of Idxb, Expb and Remb bits.

| IEEE754 precision       | Idxb | Expb | Remb |
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

## Exponential implementation wth FEXPA
FEXPA can be used to rapidly perform the table lookup. With this instruction a degree-2 polynomial is sufficient to obtain the same accuracy of the implementation we have seen before:

```C
svfloat32_t lane_consts = svld1rq(pg, ln2_lo); // Load only ln2_lo

/* Compute k as round(x/ln2) using shift = 1.5*2^(23-6) + 127 */
svfloat32_t z = svmad_x(pg, svdup_f32(inv_ln2), x, shift);
svfloat32_t k = svsub_x(pg, z, shift);

/* Compute r as x - k*ln2 with Cody and Waite */
svfloat32_t r = svmsb_x(pg, svdup_f32(ln2_hi), k, x);
            r = svmls_lane(r, k, lane_consts, 0);

/* Compute the scaling factor 2^k */
svfloat32_t scale = svexpa(svreinterpret_u32(z));

/* Compute poly(r) = exp(r) - 1 (2nd degree polynomial) */
svfloat32_t p01 = svmla_x (pg, svdup_f32(c0), r, svdup_f32(c1)); // c0 + c1 * r
svfloat32_t poly = svmul_x (pg, r, p01); // r c0 + c1 * r^2

/* exp(x) = scale * exp(r) = scale * (1 + poly(r)) */
svfloat32_t result = svmla_f32_x(pg, scale, poly, scale);
```
