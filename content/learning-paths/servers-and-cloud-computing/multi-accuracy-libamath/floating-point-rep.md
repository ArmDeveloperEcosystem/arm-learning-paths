---
title: Floating Point Representation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Floating-Point Representation Basics

Floating Point numbers are a finite and discrete approximation of the real numbers, allowing us to implement and compute functions in the continuous domain with an adequate (but limited) resolution.

A Floating Point number is typically expressed as:

```output
+/-d.dddd...d x B^e
```

where:
* B is the base;
* e is the exponent;
* d.dddd...d is the mantissa (or significand). It is p-bit word, where p represents the precision;
* +/- sign which is usually stored separately.

If the leading digit is non-zero then it is a normalized representation/normal number.

{{% notice Example 1 %}}
Fixing `B=2, p=24`

`0.1 = 1.10011001100110011001101 ×  2^4` is a normalized representation of 0.1

`0.1 = 0.000110011001100110011001 × 2^0` is a non normalized representation of 0.1

{{% /notice %}}

Usually a Floating Point number has multiple non-normalized representations, but only 1 normalized representation (assuming leading digit is strictly smaller than base), when fixing a base and a precision.

### Building a Floating-Point Ruler

Given a base `B`, a precision `p`, a maximum exponent `emax` and a minimum exponent `emin`, we can create the set of all the normalized values in this system.

{{% notice Example 2 %}}
`B=2, p=3, emax=2, emin=-1`

| Significand | × 2⁻¹ | × 2⁰ | × 2¹ | × 2² |
|-------------|-------|------|------|------|
| 1.00 (1.0)  | 0.5   | 1.0  | 2.0  | 4.0  |
| 1.01 (1.25) | 0.625 | 1.25 | 2.5  | 5.0  |
| 1.10 (1.5)  | 0.75  | 1.5  | 3.0  | 6.0  |
| 1.11 (1.75) | 0.875 | 1.75 | 3.5  | 7.0  |


{{% /notice %}}

Note that, for any given integer n, numbers are evenly spaced between 2ⁿ and 2ⁿ⁺¹. But the gap between them (also called [ULP](/learning-paths/servers-and-cloud-computing/multi-accuracy-libamath/ulp/), which is explained in the more detail in the next section) grows as the exponent increases. So the spacing between floating point numbers gets larger as numbers get bigger.

### The Floating-Point bitwise representation

Since there are `B^p` possible mantissas, and `emax-emin+1` possible exponents, then `log2(B^p) + log2(emax-emin+1) + 1` (sign) bits are needed to represent a given Floating Point number in a system.

In Example 2, 3+2+1=6 bits are needed.

Based on this, the floating point's bitwise representation is defined to be: 

```
b0 b1 b2 b3 b4 b5
```

where

```output
b0 -> sign (S)
b1, b2 -> exponent (E)
b3, b4, b5 -> mantissa (M)
```

However, this is not enough. In this bitwise definition, the possible values of E are 0, 1, 2, 3.
But in the system being defined, only the integer values in the range [-1, 2] are of interest.

For this reason, E is called the biased exponent, and in order to retrieve the value it is trying to represent (i.e. the unbiased exponent) an offset must be added or subtracted (in this case, subtract 1):

```output
x = (-1)^S x M x 2^(E-1)
```

## IEEE-754 Single Precision

Single precision (also called float) is a 32-bit format defined by the [IEEE-754 Floating Point Standard](https://ieeexplore.ieee.org/document/8766229)

In this standard the sign is represented using 1 bit, the exponent uses 8 bits and the mantissa uses 23 bits. 

The value of a (normalized) Floating Point in IEEE-754 can be represented as:

```output
x=(−1)^S x 1.M x 2^E−127
```

The exponent bias of 127 allows storage of exponents from -126 to +127. The leading digit is implicit - that is we have 24 bits of precision. In normalized numbers the leading digit is implicitly 1.

{{% notice Special Cases in IEEE-754 Single Precision %}}
Since we have 8 bits of storage, meaning E ranges between 0 and 2^8-1=255. However not all these 256 values are going to be used for normal numbers.

If the exponent E is:
* 0, then we are either in the presence of a denormalized number or a 0 (if M is 0 as well);
* 1 to 254 then we are in the normalized range;
* 255 then we are in the presence of Inf (if M==0), or Nan (if M!=0).

Subnormal numbers (also called denormal numbers) are special floating-point values defined by the IEEE-754 standard.

They allow the representation of numbers very close to zero, smaller than what is normally possible with the standard exponent range.

Subnormal numbers do not have the a leading 1 in their representation. They also assume exponent is 0.

The interpretation of denormal Floating Point in IEEE-754 can be represented as:

```
x=(−1)^S x 0.M x 2^−126
```

<!-- ### Subnormal numbers

Subnormal numbers (also called denormal numbers) are special floating-point values defined by the IEEE-754 standard.
They allow the representation of numbers very close to zero, smaller than what is normally possible with the standard exponent range.
Subnormal numbers do not have the a leading 1 in their representation. They also assume exponent is 0.

x=(−1)^s x 0.M x 2^−126

-->

<!-- | Significand | 0.? × 2⁻¹ | 1.? × 2⁻¹ | 1.? × 2⁰ | 1.? × 2¹ | 1.? × 2² |
|-------------|-----------|-----------|----------|----------|----------|
| 00 (1.0)    | 0         | 0.5       | 1.0      | 2.0      | 4.0      |
| 01 (1.25)   | 0.125     | 0.625     | 1.25     | 2.5      | 5.0      |
| 10 (1.5)    | 0.25      | 0.75      | 1.5      | 3.0      | 6.0      |
| 11 (1.75)   | 0.375     | 0.875     | 1.75     | 3.5      | 7.0      |  -->
{{% /notice %}}

If you're interested in diving deeper in this subject, [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) by David Goldberg is a good place to start.

