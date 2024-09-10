---
title: Verification & Conclusion
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verifying the Ported Code
After successfully porting the code from SSE4.2 to NEON, it's time to verify that the functionality remains intact and performs as expected. Porting SIMD code involves translating low-level operations, and it's critical to ensure that the behavior is consistent in both performance and results. To do this, you will write a simple program that mimics the original SSE operations but now uses NEON intrinsics. Create a new file for the ported NEON code named calculation_sse.c with the contents shown below:
```C
#include <arm_neon.h>
#include <stdio.h>

int main() {
    float32x4_t a = {16.0f, 9.0f, 4.0f, 1.0f};
    float32x4_t b = {4.0f, 3.0f, 2.0f, 1.0f};

    uint32x4_t cmp_result = vcgtq_f32(a, b);

    float a_arr[4], b_arr[4];
    uint32_t cmp_res[4];
    
    vst1q_f32(a_arr, a);
    vst1q_f32(b_arr, b);
    vst1q_u32(cmp_res, cmp_result);

    for (int i = 0; i < 4; i++) {
        if (cmp_res[i] != 0) {
            printf("Element %d: %.2f is larger than %.2f\n", i, a_arr[i], b_arr[i]);
        } else {
            printf("Element %d: %.2f is not larger than %.2f\n", i, a_arr[i], b_arr[i]);
        }
    }

    float32x4_t add_result = vaddq_f32(a, b);
    float32x4_t mul_result = vmulq_f32(add_result, b);
    float32x4_t sqrt_result = vsqrtq_f32(mul_result);

    float res[4];
    
    vst1q_f32(res, add_result);
    printf("Addition Result: %.2f %.2f %.2f %.2f\n", res[0], res[1], res[2], res[3]);
    
    vst1q_f32(res, mul_result);
    printf("Multiplication Result: %.2f %.2f %.2f %.2f\n", res[0], res[1], res[2], res[3]);

    vst1q_f32(res, sqrt_result);
    printf("Square Root Result: %.2f %.2f %.2f %.2f\n", res[0], res[1], res[2], res[3]);

    return 0;
}
```

Compile the code as follows using a machine that supports NEON-Vector-Extension:
```bash
gcc -O3 calculation_neon.c -o calculation_neon -march=native
```

Now run the program:
```bash
./calculation_neon
```

The output should look like: 
```output
Element 0: 16.00 is larger than 4.00
Element 1: 9.00 is larger than 3.00
Element 2: 4.00 is larger than 2.00
Element 3: 1.00 is not larger than 1.00
Addition Result: 20.00 12.00 6.00 2.00
Multiplication Result: 80.00 36.00 12.00 2.00
Square Root Result: 8.94 6.00 3.46 1.41
```

As you can see, the results are exactly the same as in the SSE4.2 example, though they appear in reverse order. This reversal is due to how different SIMD engines handle data. Additionally, the size of the code remains identical, demonstrating that the NEON code is a direct and efficient translation of the SSE4.2 code.

## Conclusion and Additional Resources
In conclusion, successfully porting SIMD code from SSE4.2 to NEON illustrates how well the two architectures can be aligned to perform equivalent operations. SIMD.info was instrumental in this process, providing a centralized and user-friendly resource for finding NEON equivalents to SSE4.2 intrinsics. It saved considerable time and effort by offering detailed descriptions, prototypes, and comparisons directly, eliminating the need for extensive web searches and manual lookups.

For those interested in further exploration, consider diving into additional resources such as SIMD documentation, architecture manuals, and online forums. These can provide deeper insights into SIMD optimizations and new techniques. Leveraging these resources will enhance your understanding and ability to work with various SIMD architectures efficiently.