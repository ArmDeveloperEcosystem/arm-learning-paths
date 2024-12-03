---
title: Code Verification
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Step-by-Step Porting

Follow this step-by-step process to porting:

1. Change the loading process to follow NEON's method for initializing vectors. The SSE4.2 intrinsic **`_mm_set_ps`** is in reality a macro, in NEON you can do the same thing with curly braces **`{}`** initialization.
2. Next, replace the SSE4.2 intrinsics with the NEON equivalents that you identified earlier. The key is to ensure that the operations perform the same tasks, such as comparison, addition, multiplication, and square root calculations.
3. Finally, modify the storing process to match NEON’s way of moving data from vectors to memory. In NEON, you use functions like [**`vst1q_f32`**](https://simd.info/c_intrinsic/vst1q_f32/) for storing 128-bit floating-point vectors and [**`vst1q_u32`**](https://simd.info/c_intrinsic/vst1q_u32/) for storing 128-bit integer vectors.

After identifying the NEON intrinsics that you require in the ported program, it's now time to write the code.

This time on your Arm Linux machine, create a new file for the ported NEON code named `calculation_neon.c`, populating with the contents as shown below:

```C
#include <arm_neon.h>
#include <stdio.h>

float32_t a_array[4] = {1.0f, 4.0f, 9.0f, 16.0f};
float32_t b_array[4] = {1.0f, 2.0f, 3.0f, 4.0f};

int main() {
    float32x4_t a = vld1q_f32(a_array);
    float32x4_t b = vld1q_f32(b_array);

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

### Verifying the Ported Code

It's time to verify that the functionality remains the same, which means that you achieve the same results and similar performance.

Compile the above code as follows on your Arm Linux machine:

```bash
gcc -O3 calculation_neon.c -o calculation_neon
```

Now run the program:
```bash
./calculation_neon
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

You can see that the results are the same as in the SSE4.2 example.

{{% notice Note %}} 
You initialized the vectors in reverse order compared to the SSE4.2 version because the array initialization and vld1q_f32 function load vectors from LSB to MSB, whereas **`_mm_set_ps`** loads elements MSB to LSB.
{{% /notice %}}
