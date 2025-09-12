---
title: Single and double precision considerations
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding numerical precision differences in single vs double precision

This section explores how different levels of floating-point precision can affect numerical results. The differences shown here are not architecture-specific issues, but demonstrate the importance of choosing appropriate precision levels for numerical computations. 

### Single precision limitations

Consider two mathematically equivalent functions, `f1()` and `f2()`. While they should theoretically produce the same result, small differences can arise due to the limited precision of floating-point arithmetic. 

The differences shown in this example are due to using single precision (float) arithmetic, not due to architectural differences between Arm and x86. Both architectures handle single precision arithmetic according to IEEE 754.

Functions `f1()` and `f2()` are mathematically equivalent. You would expect them to return the same value given the same input. 
 
Use an editor to copy and paste the C++ code below into a file named `single-precision.cpp` 

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

Compile and run the code on both x86 and Arm with the following command:

```bash
g++ -g single-precision.cpp -o single-precision
./single-precision
```

Output running on x86:

```output
f1(1.000000e-08) = 0.0000000000
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -4.9999999696e-09
Final result after magnification: -0.4999000132
```

Output running on Arm:

```output
f1(1.000000e-08) = 0.0000000000
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -4.9999999696e-09
Final result after magnification: -0.4998999834
```

Depending on your compiler and library versions, you may get the same output on both systems. You can also use the `clang` compiler and see if the output matches. 

```bash
clang -g single-precision.cpp -o single-precision -lm
./single-precision
```

In some cases the GNU compiler output differs from the Clang output. 

Here's what's happening:

1. Different square root algorithms: x86 and Arm use different hardware and library implementations for `sqrtf(1 + 1e-8)`

2. Tiny implementation differences get amplified. The difference between the two `sqrtf()` results is only about 3e-10, but this gets multiplied by 100,000,000, making it visible in the final result.

3. Both `f1()` and `f2()` use `sqrtf()`. Even though `f2()` is more numerically stable, both functions call `sqrtf()` with the same input, so they both inherit the same architecture-specific square root result.

4. Compiler and library versions may produce different output due to different implementations of library functions such as `sqrtf()`.

The final result is that x86 and Arm libraries compute `sqrtf(1.00000001)` with tiny differences in the least significant bits. This is normal and expected behavior and IEEE 754 allows for implementation variations in transcendental functions like square root, as long as they stay within specified error bounds.

The very small difference you see is within acceptable floating-point precision limits.

### Key takeaways

- The small differences shown are due to library implementations in single-precision mode, not fundamental architectural differences.
- Single-precision arithmetic has inherent limitations that can cause small numerical differences.
- Using numerically stable algorithms, like `f2()`, can minimize error propagation.
- Understanding [numerical stability](https://en.wikipedia.org/wiki/Numerical_stability) is important for writing portable code.

By adopting best practices and appropriate precision levels, developers can ensure consistent results across platforms. 

Continue to the next section to see how precision impacts the results.
