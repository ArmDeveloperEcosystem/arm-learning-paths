---
title: Verify reproducible results across scalar, NEON, and SVE
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example: Reproducible expf

This example demonstrates reproducibility in Libamath using the single-precision exponential function, `expf()`.

### Setting up your environment

This example uses GCC-14 on a Neoverse V1 machine with the [ArmPL 26.01 module](/install-guides/armpl/) installed.

If you need to install GCC run:

```bash
sudo apt install gcc -y
```

You can set up some environment variables to make compilation commands simpler:

```bash { command_line="ubuntu@localhost" }
export CC=gcc
export LD_LIBRARY_PATH=$ARMPL_DIR/lib:$LD_LIBRARY_PATH
export C_INCLUDE_PATH=$ARMPL_DIR/include
export LIBRARY_PATH=$ARMPL_DIR/lib
```

The commands below show the general compilation pattern used throughout the examples. 

Don't run them yet because `app.c` is introduced in the sections that follow.

To compile with the reproducible Libamath library:

```bash
$CC app.c -DAMATH_REPRO=1 -lamath_repro -o app
```

To compile with the non-reproducible Libamath library instead:

```bash
$CC app.c -lamath -o app
```

This only works if `app.c` only contains functions that are present in both versions of the library (`libamath_repro.a` contains a subset of functions in `libamath.a`).

To run a compiled example:

```bash
./app
```

For SVE applications, add `-march=armv8-a+sve` to the compilation command:

```bash
$CC app.c -DAMATH_REPRO=1 -lamath_repro -march=armv8-a+sve -o app
```

### Scalar usage

The starting point is a small application that uses the scalar implementation of the single-precision exponential function `armpl_exp_f32()`.

Save the following C code in a file called `app.c` using your preferred text editor. Then compile and run it using the compilation patterns from the previous section, once with reproducibility enabled (`-DAMATH_REPRO=1 -lamath_repro`) and once with reproducibility disabled (`-lamath`), to compare the output for each case.

{{< tabpane code=true >}}

  {{< tab header="C code" language="C" output_lines="10">}}
#include <amath.h>
#include <stdio.h>

int main(void)
{
    float y = armpl_exp_f32(0x1.ebe93cp-1f); // 0.960763812065125
    printf("y = %.15f [%a]\n", y, y);
    return 0;
}
  {{< /tab >}}

  {{< tab header="Output (repro enabled)" language="bash">}}
y = 2.613692283630371 [0x1.4e8d78p+1]
  {{< /tab >}}

  {{< tab header="Output (repro disabled)" language="bash">}}
y = 2.613692045211792 [0x1.4e8d76p+1]
  {{< /tab >}}

{{< /tabpane >}}


### NEON usage

Next, replace the contents of `app.c` with the following NEON application that invokes the reproducible NEON implementation of the single-precision exponential function `armpl_vexpq_f32()`. Compile and run it again with reproducibility enabled and disabled to compare the results.

{{< tabpane code=true >}}
  {{< tab header="C code" language="C" output_lines="15">}}
#include <amath.h>
#include <arm_neon.h>
#include <stdio.h>

int main(void)
{
    float32x4_t x = vdupq_n_f32(0x1.ebe93cp-1f); // 0.960763812065125
    float32x4_t y = armpl_vexpq_f32(x);

    printf("y (lane 0) = %.15f [%a]\n", vgetq_lane_f32(y, 0), vgetq_lane_f32(y, 0));
    printf("y (lane 1) = %.15f [%a]\n", vgetq_lane_f32(y, 1), vgetq_lane_f32(y, 1));
    printf("y (lane 2) = %.15f [%a]\n", vgetq_lane_f32(y, 2), vgetq_lane_f32(y, 2));
    printf("y (lane 3) = %.15f [%a]\n", vgetq_lane_f32(y, 3), vgetq_lane_f32(y, 3));
    return 0;
}


  {{< /tab >}}

  {{< tab header="Output (repro enabled)" language="bash">}}
y (lane 0) = 2.613692283630371 [0x1.4e8d78p+1]
y (lane 1) = 2.613692283630371 [0x1.4e8d78p+1]
y (lane 2) = 2.613692283630371 [0x1.4e8d78p+1]
y (lane 3) = 2.613692283630371 [0x1.4e8d78p+1]
  {{< /tab >}}


  {{< tab header="Output (repro disabled)" language="bash">}}
y (lane 0) = 2.613692283630371 [0x1.4e8d78p+1]
y (lane 1) = 2.613692283630371 [0x1.4e8d78p+1]
y (lane 2) = 2.613692283630371 [0x1.4e8d78p+1]
y (lane 3) = 2.613692283630371 [0x1.4e8d78p+1]
  {{< /tab >}}
{{< /tabpane >}}


Once you run this example, each lane of `y` contains the same bit pattern as the scalar result of `armpl_exp_f32(0x1.ebe93cp-1f)` (as you can see in the *Output* tab).

### SVE usage

Finally, replace the contents of `app.c` with the following SVE application that invokes the reproducible SVE implementation of the single-precision exponential function `armpl_svexp_f32_x()`. Compile and run using the SVE compilation command (with `-march=armv8-a+sve`), once with reproducibility enabled and once disabled.

{{< tabpane code=true >}}
  {{< tab header="C code" language="C" output_lines="15">}}
#include <amath.h>
#include <arm_sve.h>
#include <stdio.h>

int main(void)
{
    svbool_t pg = svptrue_b32();
    svfloat32_t x = svdup_f32(0x1.ebe93cp-1f); // 0.960763812065125
    svfloat32_t y = armpl_svexp_f32_x(x, pg);
    float result[svcntw()];
    svst1(pg, result, y);
    for (int i = 0; i < svcntw(); i++) {
        printf("y (lane %d): %.15f [%a]\n", i, result[i], result[i]);
    }
    return 0;
}
  {{< /tab >}}

  {{< tab header="Output (repro enabled)" language="bash">}}
y (lane 0): 2.613692283630371 [0x1.4e8d78p+1]
y (lane 1): 2.613692283630371 [0x1.4e8d78p+1]
y (lane 2): 2.613692283630371 [0x1.4e8d78p+1]
y (lane 3): 2.613692283630371 [0x1.4e8d78p+1]
y (lane 4): 2.613692283630371 [0x1.4e8d78p+1]
y (lane 5): 2.613692283630371 [0x1.4e8d78p+1]
y (lane 6): 2.613692283630371 [0x1.4e8d78p+1]
y (lane 7): 2.613692283630371 [0x1.4e8d78p+1]
  {{< /tab >}}

  {{< tab header="Output (repro disabled)" language="bash">}}
y (lane 0): 2.613692045211792 [0x1.4e8d76p+1]
y (lane 1): 2.613692045211792 [0x1.4e8d76p+1]
y (lane 2): 2.613692045211792 [0x1.4e8d76p+1]
y (lane 3): 2.613692045211792 [0x1.4e8d76p+1]
y (lane 4): 2.613692045211792 [0x1.4e8d76p+1]
y (lane 5): 2.613692045211792 [0x1.4e8d76p+1]
y (lane 6): 2.613692045211792 [0x1.4e8d76p+1]
y (lane 7): 2.613692045211792 [0x1.4e8d76p+1]
  {{< /tab >}}
{{< /tabpane >}}

All active lanes of `y` are guaranteed to match the scalar and NEON results exactly.

### Scope and limitations

In this section you observed that, when reproducibility is enabled (`AMATH_REPRO` enabled), `expf()` produces bitwise-identical results whether it is executed as a scalar, NEON or SVE function.

This behavior extends to other reproducible math routines in Libamath. Scalar, NEON, and SVE implementations are numerically aligned for all functions listed in `amath_repro.h`. Reproducible symbols are always prefixed by `armpl_` and are not provided with `ZGV` mangling. Reproducibility is available on Linux platforms, and results are independent of vector width or instruction selection. Reproducible routines prioritize determinism over peak performance.

## What you've learned and what's next

In this Learning Path, you learned what numerical reproducibility means in floating-point software and explored real-world applications where it is critical. You then enabled cross-vector-extension reproducibility in Libamath and verified that scalar, NEON, and SVE code paths produce bitwise-identical results for the `expf()` function. You can now apply these techniques to your own applications using Arm Performance Libraries.