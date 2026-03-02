---
title: Understand numerical reproducibility in floating-point math
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is reproducibility?

In numerical software, reproducibility (also referred to as determinism) means you get the exact same floating-point bits for the same inputs, even if you run a different implementation (scalar vs NEON vs SVE).

In pure mathematics, two functions `𝑓(𝑥)` and `𝑔(𝑥)` are equivalent if, for all `𝑥` in their domain `𝑓(𝑥) = 𝑔(𝑥)`.

In practice, numerical software replaces continuous mathematical functions over real numbers with discrete approximations using floating-point numbers. Instead of comparing two abstract functions, you compare two implementations. For example, a scalar version and a vectorized version of the same routine.

Two programs are reproducible if, for the same input values, they produce exactly the same floating-point results, down to the last bit.

{{% notice Accuracy vs Reproducibility %}}

This requirement is **independent** of the accuracy requirement: two results can both be within an acceptable error bound and still differ in their bit patterns.

However correctly rounded routines (maximum error under 0.5ULP) are reproducible by essence, since for a given input, rounding mode and precision, the output is the floating-point number closest to the exact mathematical result.

{{% /notice %}}

## Levels of Reproducibility

Reproducibility can be defined at different levels, depending on how similar or different the execution environments are:

* **Cross-architecture reproducibility**

  Reproducibility across different processor architectures, such as x86 and AArch64.
* **Cross-vector-extension reproducibility**

  Reproducibility across different vector execution paths on the same architecture, such as scalar, NEON, and SVE on AArch64.

This Learning Path focuses on cross-vector-extension reproducibility (scalar, NEON, SVE on AArch64).

Now that you understand what numerical reproducibility means and the different levels it can operate at, the next section covers real-world applications where this property is critical.