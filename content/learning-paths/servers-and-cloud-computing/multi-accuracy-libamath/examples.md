---
title: Arm Performance Libraries example
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Arm Performance Libraries example

Here is an example invoking all accuracy modes of the Neon single precision exp function. The file `ulp_error.h` is from the previous section. 

Make sure you have [Arm Performance Libraries](/install-guides/armpl/) installed. 

Use a text editor to save the code below in a file named `example.c`.

```C { line_numbers = "true" } 
#include <amath.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "ulp_error.h"

void check_accuracy(float32x4_t (__attribute__((aarch64_vector_pcs)) *vexp_fun)(float32x4_t), float arg, const char *label) {
    float32x4_t varg = vdupq_n_f32(arg);
    float32x4_t vres = vexp_fun(varg);
    double want = exp((double)arg);
    float got = vgetq_lane_f32(vres, 0);

    printf(label, arg);
    printf("\n          got = %a\n", got);
    printf("  (float)want = %a\n", (float)want);
    printf("         want = %.12a\n", want);
    printf("    ULP error = %.4f\n\n", ulp_error(got, want));
}

int main(void) {
    // Inputs that trigger worst-case errors for each accuracy mode
    printf("Libamath example:\n");
    printf("-----------------------------------------------\n");
    printf("  // Display worst-case ULP error in expf for each\n");
    printf("  // accuracy mode, along with approximate (\\\"got\\\") and exact results (\\\"want\\\")\n\n");

    check_accuracy (armpl_vexpq_f32_u10, 0x1.ab312p+4, "armpl_vexpq_f32_u10(%a) delivers error under 1.0 ULP");
    check_accuracy (armpl_vexpq_f32, 0x1.8163ccp+5, "armpl_vexpq_f32(%a) delivers error under 3.5 ULP");
    check_accuracy (armpl_vexpq_f32_umax, -0x1.5b7322p+6, "armpl_vexpq_f32_umax(%a) delivers result with half correct bits");

    return 0;
}
```

Compile the program with:

```bash
gcc -O2 -o example example.c -lamath -lm
```

Run the example:

```bash
./example 
```

The output is:

```output
Libamath example:
-----------------------------------------------
  // Display worst-case ULP error in expf for each
  // accuracy mode, along with approximate (`got`) and exact results (`want`)

armpl_vexpq_f32_u10(0x1.ab312p+4) delivers error under 1.0 ULP
          got = 0x1.6ee554p+38
  (float)want = 0x1.6ee556p+38
         want = 0x1.6ee555bb01d1p+38
    ULP error = 0.8652

armpl_vexpq_f32(0x1.8163ccp+5) delivers error under 3.5 ULP
          got = 0x1.6a09ep+69
  (float)want = 0x1.6a09e4p+69
         want = 0x1.6a09e3e3d585p+69
    ULP error = 1.9450

armpl_vexpq_f32_umax(-0x1.5b7322p+6) delivers result with half correct bits
          got = 0x1.9b56bep-126
  (float)want = 0x1.9b491cp-126
         want = 0x1.9b491b9376d3p-126
    ULP error = 1745.2120
```

The inputs used for each variant correspond to the current worst-case scenario known to date (ULP Error argmax).
This means that the ULP error should not be higher than the one demonstrated here, ensuring the results remain below the defined thresholds for each accuracy.