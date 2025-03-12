---
title: Minimising Variability across platforms
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Minimising Variability across platforms

The line `#pragma STDC FENV_ACCESS ON` is a directive that informs the compiler to enable access to the floating-point environment. This is part of the C99 standard and is used to ensure that the program can properly handle floating-point exceptions and rounding modes.

In the context belo, enabling floating-point environment access is crucial because the functions you are working with involve floating-point arithmetic, which can be prone to precision errors and exceptions such as overflow, underflow, division by zero, and invalid operations. By enabling this pragma, you ensure that the program can detect and respond to these exceptions appropriately.

This directive is particularly important when performing operations that require high numerical stability and precision, such as the square root calculations in your functions. It allows the program to manage the floating-point state and handle any anomalies that might occur during these calculations, thereby improving the robustness and reliability of your numerical computations.

Save the C++ file below as `error-propagation-min.cpp`. 

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

Compile with the following command. 

```bash
g++ -o error-propagation-min error-propagation-min.cpp -frounding-math
```

```output
./error-propagation-min 
f1(1.000000e-08) = 0.0000000050
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -1.7887354748e-17
Final result after magnification: 0.0000999982
```