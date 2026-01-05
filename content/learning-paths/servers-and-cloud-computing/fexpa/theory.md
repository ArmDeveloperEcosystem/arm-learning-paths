---
title: Theory
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The exponential function
The exponential function is a fundamental mathematical function used across a wide range of algorithms for signal processing, High-Performance Computing and Machine Learning. Optimizing its computation has been the subject of extensive research for decades. The precision of the computation depends both on the selected approximation method and on the inherent rounding errors associated with finite-precision arithmetic, and it is directly traded off against performance when implementing the exponential function. 

## Range reduction
Polynomial approximations are among the most widely used methods for software implementations of the exponential function. The accuracy of a Taylor series approximation for exponential function can be improved with the polynomial’s degree but will always deteriorate as the evaluation point moves further from the expansion point. By applying range reduction techniques, the approximation of the exponential function can however be restricted to a very narrow interval where the function is well-conditioned. This approach consists in reformulating the exponential function in the following way:

$$e^x=e^{k×ln2+r}=2^k \times e^r$$

where

$$x=k×ln2+r, k \in Z, r \in [-ln2/2, +ln2/2]$$

Since k is an integer, the evaluation of 2^k can be efficiently performed using bit manipulation techniques, while e^r can be approximated with a polynomial p(r). Hence:

$$e^x \approx 2^k \times p(r)$$

It is important to note that the polynomial p(r) is evaluated exclusively over the interval [-ln2/2, +ln2/2]. So, the computational complexity can be optimized by selecting the polynomial degree based on the required precision of p(r) within this narrow range. Rather than relying on a Taylor polynomial, a minimax polynomial approximation can be used to minimize the maximum approximation error over the considered interval.

## Decomposition of the input
The decomposition of an input value as x = k × ln2 + r can be done in 2 steps:
- Compute k as: k = round(x⁄ln2), where round(.) is the round-to-nearest function
- Compute r as: r = x - k × ln2

Rounding of k is performed by adding an adequately chosen large number to a floating-point value and subtracting it just afterward (the original value is rounded due to the finite precision of floating-point representation). Although explicit rounding instructions are available in both SVE and SME, this method remains advantageous as the addition of the constant can be fused with the multiplication by the reciprocal of ln2. This approach assumes however that the floating-point rounding mode is set to round-to-nearest, which is the default mode in Armv9-A. By integrating the bias into the constant, 2^k can also be directly computed by shifting the intermediate value.

Rounding error during the second step will introduce a global error as we will have:

$$ x \approx k \times ln2 + r $$

To reduce the rounding errors during the computation of the reduced argument r, the Cody and Waite argument reduction technique is used. 

## Computation of the scaling factor
By leveraging the structure of floating-point number formats, it becomes relatively straightforward to compute 2^k for k∈Z. In the IEEE-754 standard, normalized floating-point numbers in binary interchange format are represented as:

$$ (-1)^s \times 2^{(exponent - bias)} \times (1.fraction)_2 $$

where s is the sign bit and 1.fraction represents the significand.

The value 2^k can be encoded by setting both the sign and fraction bits to zero and assigning the exponent field the value k + bias. If k is an 8-bits integer, 2^k can be efficiently computed by adding the bias value and positioning the result into the exponent bits of a 32-bit floating-point number using a logical shift.

Taking this approach a step further, a fast approximation of exponential function can be achieved using bits manipulation techniques alone. Specifically, adding a bias to an integer k and shifting the result into the exponent field can be accomplished by computing an integer i as follows:  

$$i=2^{23} \times (k+bias) = 2^{23} \times k+2^{23} \times bias$$

This formulation assumes a 23-bit significand, but the method can be generalized to other floating-point precisions.

Now, consider the case where k is a real number. The fractional part of k will propagate into the significand bits of the resulting 2^k approximation. However, this side effect is not detrimental, it effectively acts as a form of linear interpolation, thereby improving the overall accuracy of the approximation. To approximate the exponential function, the following identity can be used:

$$e^x = 2^{x⁄ln2}$$

As previously discussed, this value can be approximated by computing a 32-bit integer:

$$i = 2^{23} \times x⁄ln2 + 2^{23} \times bias = a \times x + b $$

Continue to the next section to make a C-based implementation of the exponential function.