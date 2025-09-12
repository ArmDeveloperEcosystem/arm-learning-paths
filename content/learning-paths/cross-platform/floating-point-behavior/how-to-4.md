---
title: Minimize floating-point variability across platforms
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How can I ensure consistent floating-point results across x86 and Arm?

The most effective way to ensure consistent floating-point results across platforms is to use double precision arithmetic. Both Arm and x86 produce identical results when using double precision for the same operations.

### Double precision floating-point eliminates differences

The example below demonstrates how using double precision eliminates the small differences observed in the previous single-precision example. Switching from `float` to `double` ensures identical results on both architectures.

Use an editor to copy and paste the C++ file below into a file named `double-precision.cpp` 

```cpp
#include <stdio.h>
#include <math.h>

// Function 1: Computes sqrt(1 + x) - 1 using the naive approach
double f1(double x) {
    return sqrtf(1 + x) - 1;
}

// Function 2: Computes the same value using an algebraically equivalent transformation
// This version is numerically more stable
double f2(double x) {
    return x / (sqrtf(1 + x) + 1);
}

int main() {
    double x = 1e-8;  
    double result1 = f1(x);
    double result2 = f2(x);

    // Theoretically, result1 and result2 should be the same
    double difference = result1 - result2;
    // Multiply by a large number to amplify the error
    double final_result = 100000000.0f * difference + 0.0001f;

    // Print the results
    printf("f1(%e) = %.10f\n", x, result1);
    printf("f2(%e) = %.10f\n", x, result2);
    printf("Difference (f1 - f2) = %.10e\n", difference);
    printf("Final result after magnification: %.10f\n", final_result);

    return 0;
}
```

Compile on both computers:

```bash
g++ -o double-precision double-precision.cpp 
./double-precision 
```

Running the new binary on both systems shows that both functions produce identical results.

Here is the output on both systems:

```output
f1(1.000000e-08) = 0.0000000050
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -1.7887354748e-17
Final result after magnification: 0.0000999982
```

By choosing appropriate precision levels, you can write code that remains consistent and reliable across architectures. Precision, however, involves a trade-off: single precision reduces memory use and often improves performance, while double precision is essential for applications demanding higher accuracy and greater numerical stability, particularly to control rounding errors.

For the vast majority of floating-point application code, you will not notice any differences between x86 and Arm architectures. However, in rare cases where differences do occur, they are usually due to undefined behaviors or non-portable code. These differences should not be a cause for concern, but rather an opportunity to improve the code for better portability and consistency across platforms. By addressing these issues, you can ensure that your floating-point code runs reliably and produces identical results on both x86 and Arm systems.
