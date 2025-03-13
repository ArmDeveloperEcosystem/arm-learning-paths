---
title: Floating Point Representations
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Recap on Floating Point Numbers

If you are unfamiliar with floating point representations, we recommend looking at this [introductory learning path](https://learn.arm.com/learning-paths/cross-platform/integer-vs-floats/introduction-integer-float-types/). 

Floating-point numbers are a fundamental representation of real numbers in computer systems, enabling efficient storage and computation of decimal values with varying degrees of precision. The IEEE 754 standard, established in 1985, is the most widely used format for floating-point arithmetic, ensuring consistency across different hardware and software implementations.

IEEE 754 defines two primary formats: single-precision (32-bit) and double-precision (64-bit). Each floating-point number consists of three components: the sign bit (determining positive or negative value), the exponent (defining the scale or magnitude), and the significand (also called the mantissa, representing the significant digits of the number). The standard uses a biased exponent to handle both large and small numbers efficiently, and it incorporates special values such as NaN (Not a Number), infinity, and subnormal numbers for robust numerical computation. 

A key feature of IEEE 754 is its support for rounding modes and exception handling, ensuring predictable behavior in mathematical operations. However, floating-point arithmetic is inherently imprecise due to limited precision, leading to small rounding errors.

![floating-point](./floating-point-numbers.png)

## Rounding Errors 

The unit in last place (ULP) is the smallest difference between two consecutive floating-point numbers. It measures floating-point rounding error, which arises because not all real numbers can be exactly represented. When an operation is performed, the result is rounded to the nearest representable value, introducing a small error. This error, often measured in ULPs, indicates how close the computed value is to the exact result. For a simple example, if we construct a floating-point schema with 3 bits for the mantissa (precision) and an exponent in the range of -1 to 2. The possible values will look like the graph below. 

![ulp](./ulp.png)

Key takeaways:

- ULP size varies with the number’s magnitude.
- Larger numbers have bigger ULPs due to wider spacing between values.
- Smaller numbers have smaller ULPs, reducing quantization error.
- ULP behavior impacts numerical stability and precision in computations.


## Implementation defined behaviour


