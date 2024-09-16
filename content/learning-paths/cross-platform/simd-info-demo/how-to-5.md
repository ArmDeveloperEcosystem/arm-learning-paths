---
title: Code Verification
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Verifying the Ported Code
After successfully porting the code from SSE4.2 to NEON, it's time to verify that the functionality remains intact and performs as expected. Porting SIMD code involves translating low-level operations, and it's critical to ensure that the behavior is consistent in both performance and results. To do this, you will write a simple program that mimics the original SSE operations but now uses NEON intrinsics. Create a new file for the ported NEON code named calculation_sse.c with the contents shown below:
```C
#include <arm_neon.h>
#include <stdio.h>

int main() {
    float32x4_t a = {1.0f, 4.0f, 9.0f, 16.0f};
    float32x4_t b = {1.0f, 2.0f, 3.0f, 4.0f};

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
    printf("\n");

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
Element 0: 1.00 is not larger than 1.00
Element 1: 4.00 is larger than 2.00
Element 2: 9.00 is larger than 3.00
Element 3: 16.00 is larger than 4.00

Addition Result: 2.00 6.00 12.00 20.00
Multiplication Result: 2.00 12.00 36.00 80.00
Square Root Result: 1.41 3.46 6.00 8.94
```
As you can clearly see, the results are exactly the same as in the SSE4.2 example. However, we initialized the vectors in reverse order compared to the SSE4.2 version because NEON loads vectors from LSB to MSB, ensuring consistent output across both architectures. Additionally, the size of the code remains identical, demonstrating that the NEON code is a direct and efficient translation of the SSE4.2 code.

