---
title: Examples
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example: Reproducible expf

In this example, you will take a look into reproducibility Libamath usage, considering the case of a simple computation using the exponential function in single precision (`expf`).


#### Setting up your environment
In this example we use **`GCC-14`** compiler on a **`Neoverse V1`** machine. We use [ArmPL 26.01 module](/install-guides/armpl/).
You can setup some environment variables to make compilation commands simpler:

```bash { command_line="root@localhost" }
export LD_LIBRARY_PATH=<armpl-install-path>/lib:$LD_LIBRARY_PATH
export C_INCLUDE_PATH=<armpl-install-path>/include
export LIBRARY_PATH=<armpl-install-path>/lib
```

With this setup, you can compile the examples to use the reproducible Libamath library via:
```bash { command_line="root@localhost" }
$CC app.c -DAMATH_REPRO=1 -lamath_repro -o app
```

If in turn you are interested in using the non-reproducible Libamath library, you should compile with:
```bash { command_line="root@localhost" }
$CC app.c -lamath -o app
```

Note that that this only works if `app.c` only contains functions that are present in both versions of the library (`libamath_repro.a` contains a subset of functions in `libamath.a`).

You can run examples via:

```bash { command_line="root@localhost" }
./app
```

For `SVE` applications, add `-march=armv8-a+sve` to the compilation command. For example:

```bash { command_line="root@localhost" }
$CC app.c -DAMATH_REPRO=1 -lamath_repro -march=armv8-a+sve -o app
```


#### Scalar usage

Our starting point is a small application that uses the scalar implementation of the single precision exponential function `armpl_exp_f32`.
Below you can find the example-code, the output when reproducibility is enabled versus when reproducibility is disabled.

{{< tabpane code=true >}}

  {{< tab header="C Application" language="C" output_lines="10">}}
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


#### Neon usage

Now we build a simple Neon application that invokes the reproducible Neon implementation of the single precision exponential function `armpl_vexpq_f32`.

{{< tabpane code=true >}}
  {{< tab header="C" language="C" output_lines="15">}}
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


Once we run this example, each lane of `y` will contain the same bit pattern as the scalar result of `armpl_exp_f32(1.0f)` (as you can see in the *Output* tab).

#### SVE usage
Finally we build a simple SVE application that invokes the reproducible SVE implementation of the single precision exponential function `armpl_svexp_f32_x`.

{{< tabpane code=true >}}
  {{< tab header="C" language="C" output_lines="15">}}
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

All active lanes of `y` are guaranteed to match the scalar and Neon results exactly.

#### Scope and Limitations

In this section we observed that, when reproducibility is enabled (`AMATH_REPRO` enabled), `expf` produces bitwise-identical results whether it is executed as a scalar, Neon or SVE function.

This behaviour extends to other reproducible math routines in reproducible Libamath:

* Scalar, Neon, and SVE implementations are numerically aligned
* Only functions listed in `amath_repro.h` are reproducible
* Reproducible symbols are always prefixed by `armpl_`. They are not provided with `ZGV` mangling.
* Reproducibility is provided on Linux platforms
* Results are independent of vector width or instruction selection
* Reproducible routines prioritize determinism over peak performance