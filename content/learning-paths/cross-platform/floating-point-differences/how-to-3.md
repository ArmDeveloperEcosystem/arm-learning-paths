---
title: Error Propagation
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## 

Loss in precision can arise from the ordering of operations. Consider the example below. Function 1, `f1` and 2, `f2` are mathematically equivalent. Hence they shuold return the same value given the same input. If we input a very small number, `1e-8`, the error is different due to the loss in precision caused by different operations. Amplifying this result leads to a difference. 


```cpp
#include <stdio.h>
#include <math.h>

// Function 1: Computes sqrt(1 + x) - 1 using the naive approach
float f1(float x) {
    return sqrtf(1 + x) - 1;
}

// Function 2: Computes the same value using an algebraically equivalent transformation
// This version is numerically more stable
float f2(float x) {
    return x / (sqrtf(1 + x) + 1);
}

int main() {
    float x = 1e-8;  // A small value that causes floating-point precision issues
    float result1 = f1(x);
    float result2 = f2(x);

    // Theoretically, result1 and result2 should be the same
    float difference = result1 - result2;
    // Multiply by a large number to amplify the error
    float final_result = 100000000.0f * difference + 0.0001f;

    // Print the results
    printf("f1(%e) = %.10f\n", x, result1);
    printf("f2(%e) = %.10f\n", x, result2);
    printf("Difference (f1 - f2) = %.10e\n", difference);
    printf("Final result after magnification: %.10f\n", final_result);

    return 0;
}
```

x86 and Arm-based machines may perform the computations in different orders so this is another variable. 

Compiling the source code on both x86 and Arm64 with the following command. 
```bash
g++ -g error-propagation.cpp -o error-propagation
```

```output
./err
f1(1.000000e-08) = 0.0000000000
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -4.9999999696e-09
Final result after magnification: -0.4999000132
```

```output
./err
f1(1.000000e-08) = 0.0000000000
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -4.9999999696e-09
Final result after magnification: -0.4998999834
```
