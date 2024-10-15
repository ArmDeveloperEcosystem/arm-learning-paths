---
title: Complex Example
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Handling Intrinsics Without Direct Equivalents
As we successfully port the code from SSE4.2 to NEON, we observe that certain instructions translate seamlessly. However, there are cases where direct equivalents for some intrinsics may not be readily available across architectures. For example, the [**_mm_hadd_ps**](https://simd.info/c_intrinsic/_mm_hadd_ps/) intrinsic from SSE4.2, which performs horizontal addition of packed single-precision floating-point elements, does not have a direct counterpart in NEON. 

In this situation, SIMD.info’s purpose description becomes essential for understanding the operation at a high level. By analyzing the core functionality of **_mm_hadd_ps**, we can implement an alternative solution using available NEON intrinsics. For **_mm_hadd_ps**, which combines the elements of two vectors in a way that sums adjacent elements both horizontally and vertically, we break down the operation into a series of steps. For instance, to achieve the same result, we extract the [lower](https://simd.info/c_intrinsic/vget_low_f32/) and [upper](https://simd.info/c_intrinsic/vget_high_f32/) halves of the vectors, perform horizontal additions on each half separately using [vpadd_f32](https://simd.info/c_intrinsic/vpadd_f32/), and then [combine](https://simd.info/c_intrinsic/vcombine_f32/) the results into a single vector. This approach ensures that the intended horizontal addition operation is preserved, even though there is no direct one-to-one match between SSE4.2 and NEON for this specific instruction.

Consider the following code for SSE4.2. Create a new file for the code named complex_sse.c with the contents shown below: 
```C
#include <pmmintrin.h>
#include <stdio.h>

int main() {
    __m128 a = _mm_set_ps(1.0f, 2.0f, 3.0f, 4.0f);
    __m128 b = _mm_set_ps(5.0f, 6.0f, 7.0f, 8.0f);

    __m128 res = _mm_hadd_ps(a, b);

    float out[4];
    _mm_storeu_ps(out, res);

    printf("SSE4.2 Result: %.2f %.2f %.2f %.2f\n", out[0], out[1], out[2], out[3]);
    return 0;
}
```

Compile the code as follows using a machine that supports SSE-Vector-Extension:
```bash
gcc -O3 -msse4.2 complex_sse.c -o complex_sse -march=native
```

Now run the program:
```bash
./complex_sse
```

The output should look like: 
```output
SSE4.2 Result: 7.00 3.00 15.00 11.00
```

To achieve the same result with NEON, follow these steps using the equivalents we discussed. Implement the corresponding NEON code that extracts the lower and upper halves of the vectors, performs horizontal additions, and combines the results. Create a new file for the NEON code named complex_neon.c with the contents shown below: 
```C
#include <arm_neon.h>
#include <stdio.h>

int main() {
    float32x4_t a = {1.0f, 2.0f, 3.0f, 4.0f};
    float32x4_t b = {5.0f, 6.0f, 7.0f, 8.0f};

    float32x2_t a_low = vget_low_f32(a);
    float32x2_t a_high = vget_high_f32(a);
    float32x2_t b_low = vget_low_f32(b);
    float32x2_t b_high = vget_high_f32(b);

    float32x2_t a_sum_low = vpadd_f32(a_low, a_high);
    float32x2_t b_sum_low = vpadd_f32(b_low, b_high);

    float32x4_t result = vcombine_f32(a_sum_low, b_sum_low);

    float res[4];
    vst1q_f32(res, result);

    printf("NEON Result: %.2f %.2f %.2f %.2f\n", res[0], res[1], res[2], res[3]);
    return 0;
}
```

Compile the code as follows using a machine that supports NEON-Vector-Extension:
```bash
gcc -O3 complex_neon.c -o complex_neon -march=native
```

Now run the program:
```bash
./complex_neon
```

The output should look like: 
```output
NEON Result: 3.00 7.00 11.00 15.00
```

The results match, although the order differs due to how the data is handled in each architecture. SIMD.info was especially helpful in this process, providing detailed descriptions and examples that guided the translation of complex intrinsics between different SIMD architectures.

### Conclusion and Additional Resources
In conclusion, porting SIMD code from SSE4.2 to NEON demonstrates how well the two architectures can be aligned to perform equivalent operations. SIMD.info was instrumental in this process, providing a centralized and user-friendly resource for finding NEON equivalents to SSE4.2 intrinsics. It saved considerable time and effort by offering detailed descriptions, prototypes, and comparisons directly, eliminating the need for extensive web searches and manual lookups. While porting between vectors of different sizes is more complex, work is already underway to match instructions like SVE/SVE2 with AVX512.

For those interested in further exploration, consider diving into additional resources such as SIMD documentation, architecture manuals, and online forums. These can provide deeper insights into SIMD optimizations and new techniques. Leveraging these resources will enhance your understanding and ability to work with various SIMD architectures efficiently.