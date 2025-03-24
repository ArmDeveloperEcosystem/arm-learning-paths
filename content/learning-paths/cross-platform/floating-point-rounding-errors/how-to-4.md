---
title: Minimizing variability across platforms
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How can I minimize variability across x86 and Arm?

The line `#pragma STDC FENV_ACCESS ON` is a directive that informs the compiler to enable access to the floating-point environment. 

This is part of the C++11 standard and is used to ensure that the program can properly handle floating-point exceptions and rounding modes enabling your program to continue running if an exception is thrown. 

In the context below, enabling floating-point environment access is crucial because the functions you are working with involve floating-point arithmetic, which can be prone to precision errors and exceptions such as overflow, underflow, division by zero, and invalid operations. This is not necessary for this example, but is included because it may be relevant for your own application. 

This directive is particularly important when performing operations that require high numerical stability and precision, such as the square root calculations in functions below. It allows the program to manage the floating-point state and handle any anomalies that might occur during these calculations, thereby improving the robustness and reliability of your numerical computations.

Use an editor to copy and paste the C++ file below into a file named `error-propagation-min.cpp`. 

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

You should use this flat when your program dynamically changes the floating-point rounding mode or needs to run correctly under different rounding modes. In this example, it results in a predictable rounding mode on function `f1` across x86 and Arm. 

```bash
g++ -o error-propagation-min error-propagation-min.cpp -frounding-math
```

Running the new binary on both systems leads to function, `f1` having a similar value to `f2`. Further the difference is now identical across both Arm64 and x86. 

Here is the output on both systems:

```output
./error-propagation-min 
f1(1.000000e-08) = 0.0000000050
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -1.7887354748e-17
Final result after magnification: 0.0000999982
```

G++ provides several compiler flags to help balance accuracy and performance such as`-ffp-contract` which is useful when lossy, fused operations are used, such as fused-multiple. 

Another example is `-ffloat-store` which prevents floating point variables from being stored in registers which can have different levels of precision and rounding. 

You can refer to compiler documentation for more information about the available flags.

