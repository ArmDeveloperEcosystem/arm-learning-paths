---
title: Minimizing floating-point variability across platforms
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How can I minimize floating-point variability across x86 and Arm?

The line `#pragma STDC FENV_ACCESS ON` is a directive that informs the compiler to enable access to the floating-point environment. This is part of the C++11 standard and ensures that the program can properly handle floating-point exceptions and rounding modes, enabling your program to continue running if an exception is thrown. 

In the context below, enabling floating-point environment access is crucial because the functions in this example involve floating-point arithmetic, which can be prone to precision errors and exceptions such as overflow, underflow, division by zero, and invalid operations. Although not strictly necessary for this example, the directive is included because it may be relevant for your own applications. 

This directive is particularly important when performing operations that require high numerical stability and precision, such as the square root calculations in functions below. It allows the program to manage the floating-point state and handle any anomalies that might occur during these calculations, thereby improving the robustness and reliability of your numerical computations.

Use an editor to copy and paste the C++ file below into a file named `error-propagation-min.cpp`: 

```cpp
#include <cstdio>
#include <cmath>
#include <cfenv>

// Enable floating-point exceptions
#pragma STDC FENV_ACCESS ON

// Function 1: Computes sqrt(1 + x) - 1 using the naive approach
double f1(double x) {
    return sqrt(1 + x) - 1;
}

// Function 2: Computes the same value using an algebraically equivalent transformation
// This version is numerically more stable
double f2(double x) {
    return x / (sqrt(1 + x) + 1);
}

int main() {
    // Enable all floating-point exceptions
    std::feclearexcept(FE_ALL_EXCEPT);
    std::feraiseexcept(FE_DIVBYZERO | FE_INVALID | FE_OVERFLOW);

    double x = 1e-8;  // A small value that causes floating-point precision issues
    double result1 = f1(x);
    double result2 = f2(x);

    // Theoretically, result1 and result2 should be the same
    double difference = result1 - result2;
    // Multiply by a large number to amplify the error
    double final_result = 100000000.0 * difference + 0.0001;

    // Print the results
    printf("f1(%e) = %.10f\n", x, result1);
    printf("f2(%e) = %.10f\n", x, result2);
    printf("Difference (f1 - f2) = %.10e\n", difference);
    printf("Final result after magnification: %.10f\n", final_result);

    return 0;
}
```

Compile on both computers, using the C++ flag, `-frounding-math`. 

You should use this flag when your program dynamically changes the floating-point rounding mode or needs to run correctly under different rounding modes. In this example, it ensures that `f1` uses a predictable rounding mode across both x86 and Arm. 

```bash
g++ -o error-propagation-min error-propagation-min.cpp -frounding-math
```

Running the new binary on both systems shows that function `f1` produces a value nearly identical to `f2`, and the difference between them is now identical across both Arm64 and x86. 

```bash
./error-propagation-min 
```

Here is the output on both systems:

```output
f1(1.000000e-08) = 0.0000000050
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -1.7887354748e-17
Final result after magnification: 0.0000999982
```

G++ provides several compiler flags to help balance accuracy and performance. For example, `-ffp-contract` is useful when lossy, fused operations are used, such as fused-multiple. 

Another example is `-ffloat-store` which prevents floating-point variables from being stored in registers which can have different levels of precision and rounding. 

You can refer to compiler documentation for more information on the flags available.

