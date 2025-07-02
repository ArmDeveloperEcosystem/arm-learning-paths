---
title: ULP error and accuracy
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## ULP error and accuracy

In the development of Libamath, a metric called ULP error is used to assess the accuracy of floating-point functions. ULP  (Unit in the Last Place) measures the distance between two numbers, a reference (`want`) and an approximation (`got`), relative to how many floating-point steps (ULPs) separate them.

The formula is:

```
ulp_err = | want - got | / ULP(want)
```

Because ULP error is defined in terms of floating-point spacing, it is inherently scale-aware. In contrast to absolute error, ULP error avoids bias due to the uneven distribution of floating-point numbers across different magnitudes.


## ULP error implementation

In practice, the basic expression is modified to account for additional sources of error introduced during the computation itself.

In the implementation used here, this quantity is held by a term called `tail`:

```
ulp_err = | (got - want) / ULP(want) - tail |
```

This term compensates for the rounding error that occurs when the high-precision reference (`want_l`, a `double`) is cast down to a `float`. This contribution is given in terms of ULP distance:

```
tail = | (want_l - want) / ULP(want) |
```

## A simplified version

 Below is a practical implementation of the ULP error calculation based on the model above. Use the same `ulp.h` header from the previous section.

Use a text editor to copy the code below into a new file called `ulp_error.h`:

```C
// Defines ulpscale(x)
#include "ulp.h"

// Compute ULP error given:
// - got: computed result -> got (float)
// - want_l: high-precision reference -> want (double)
double ulp_error(float got, double want_l) {

    float want = (float) want_l;

    // Early exit for exact match
    if ((want_l == (double) want && got == want)) {
       return 0.0;
    }

    int ulp_exp = ulpscale(want); // Base-2 exponent for scaling ULP(want)

    // Fractional tail from float rounding
    double tail = scalbn(want_l - (double)want, -ulp_exp);

    // Difference between computed and rounded reference
    double diff = (double)got - (double)want;

    // Return total ULP error with bias correction
    return fabs(scalbn(diff, -ulp_exp) - tail);
}
```
{{% notice Note %}}
The final scaling is done with respect to the rounded reference.
{{% /notice %}}

In this implementation, it is possible to get exactly 0.0 ULP error if and only if:

* The high-precision reference (`want_l`, a double) is exactly representable as a float, and
* The computed result (`got`) is bitwise equal to that float representation.

Below is a small example to check this implementation.

Save the code below into a file named `ulp_error.c`.

```C
#include <stdio.h>
#include "ulp_error.h"

int main() {
    float got = 1.0000001f;
    double want_l = 1.0;
    double ulp = ulp_error(got, want_l);
    printf("ULP error: %f\n", ulp);
    return 0;
}
```

Compile the program with GCC.

```bash
gcc -O2 ulp_error.c -o ulp_error
```

Run the program:

```bash
./ulp_error
```

The output should be:

```
ULP error: 1.0
```

If you are interested in diving into the full implementation of the ULP error, you can consult the [tester](https://github.com/ARM-software/optimized-routines/tree/master/math/test) tool in [AOR](https://github.com/ARM-software/optimized-routines/tree/master), with particular focus to the [ulp.h](https://github.com/ARM-software/optimized-routines/blob/master/math/test/ulp.h) file. Note this tool also handles special cases and considers the effect of different rounding modes in the ULP error.