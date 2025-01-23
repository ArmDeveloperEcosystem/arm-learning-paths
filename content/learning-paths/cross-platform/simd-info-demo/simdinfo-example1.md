---
title: Example Program
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Have a look at the following C example that uses Intel SSE4.2 intrinsics.

On an x86_64 Linux development machine, create a file named `calculation_sse.c`, populating it with the contents as shown below:

```C
#include <xmmintrin.h>
#include <stdio.h>

int main() {
    __m128 a = _mm_set_ps(16.0f, 9.0f, 4.0f, 1.0f);
    __m128 b = _mm_set_ps(4.0f, 3.0f, 2.0f, 1.0f);

    __m128 cmp_result = _mm_cmpgt_ps(a, b);

    float a_arr[4], b_arr[4], cmp_arr[4];
    _mm_storeu_ps(a_arr, a);
    _mm_storeu_ps(b_arr, b);
    _mm_storeu_ps(cmp_arr, cmp_result);

    for (int i = 0; i < 4; i++) {
        if (cmp_arr[i] != 0.0f) {
            printf("Element %d: %.2f is larger than %.2f\n", i, a_arr[i], b_arr[i]);
        } else {
            printf("Element %d: %.2f is not larger than %.2f\n", i, a_arr[i], b_arr[i]);
        }
    }

    __m128 add_result = _mm_add_ps(a, b);
    __m128 mul_result = _mm_mul_ps(add_result, b);
    __m128 sqrt_result = _mm_sqrt_ps(mul_result);

    float res[4];
    
    _mm_storeu_ps(res, add_result);
    printf("Addition Result: %f %f %f %f\n", res[0], res[1], res[2], res[3]);

    _mm_storeu_ps(res, mul_result);
    printf("Multiplication Result: %f %f %f %f\n", res[0], res[1], res[2], res[3]);

    _mm_storeu_ps(res, sqrt_result);
    printf("Square Root Result: %f %f %f %f\n", res[0], res[1], res[2], res[3]);

    return 0;
}
```

The program does the following:

* Compares whether elements in one vector are greater than those in another vector.
* Prints the result.
* Computes the addition of two vectors.
* Multiplies the result with one of the vectors.
* Takes the square root of the multiplication result.

Compile the code on your Linux x86_64 system that supports SSE4.2:

```bash
gcc -O3 calculation_sse.c -o calculation_sse -msse4.2
```

Now run the program:

```bash
./calculation_sse
```

The output should look like the following:
```output
Element 0: 1.00 is not larger than 1.00
Element 1: 4.00 is larger than 2.00
Element 2: 9.00 is larger than 3.00
Element 3: 16.00 is larger than 4.00

Addition Result: 2.00 6.00 12.00 20.00
Multiplication Result: 2.00 12.00 36.00 80.00
Square Root Result: 1.41 3.46 6.00 8.94
```

It is imperative that you run the code first on an Intel x86_64 reference platform, to make sure that you understand how it works and what kind of results you can expect.
