---
title: ULP Error and Accuracy
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# ULP Error and Accuracy

In the development of Libamath, we use a metric called ULP error to assess the accuracy of our functions.
This metric measures the distance between two numbers, a reference (`want`) and an approximation (`got`), relative to how many floating-point “steps” (ULPs) these two numbers are apart.

It can be calculated by:

```
ulp_err = | want - got | / ULP(want)
```

Because this is a relative measure in terms of floating-point spacing (ULPs) - i.e. this metric is scale-aware - it is ideal for comparing accuracy across magnitudes. Otherwise, error measure would be very biased by the uneven distribution of the floats.


# ULP Error Implementation

In practice, however, the above expression may take different forms, to account for sources of error that may happen during the computation of the error itself.

In our implementation, this quantity is held by a term called `tail`:

```
ulp_err = | (got - want) / ULP(want) - tail |
```

This term takes into account the error introduced by casting `want` from a higher precision to working precision. This contribution is given in terms of ULP distance:

```
tail = | (want_l - want) / ULP(want) |
```

Here is a simplified version of our ULP Error (where `ulp.h` is the implementation of ULP in the [previous section](/learning-paths/servers-and-cloud-computing/multi-accuracy-libamath/ulp/)):


```C
// Defines ulpscale(x)
#include "ulp.h"

// Compute ULP error given:
// - got: computed result -> got (float)
// - want_l: high-precision reference -> want (double)
double ulp_error(float got, double want_l) {

    float want = (float) want_l;

    // Early exit for exact match
    if (want_l == (double)want && got == want) {
       return 0.0;
    }

    int ulp_exp = ulpscale(want);

    // Fractional tail from float rounding
    double tail = scalbn(want_l - (double)want, -ulp_exp);

    // Difference between computed and rounded reference
    double diff = (double)got - (double)want;

    // Return total ULP error with bias correction
    return fabs(scalbn(diff, -ulp_exp) - tail);
}
```
Note that the final scaling is done with respect to the rounded reference.

In this implementation, it is possible to get exactly 0.0 ULP error in this implementation if and only if:

* The high-precision reference (`want_l`, a double) is exactly representable as a float, and
* The computed result (`got`) is bitwise equal to that float representation.

Here is a small snippet to check out this implementation in action.


```C
#include "ulp_error.h"

int main() {
    float got = 1.0000001f;
    double want_l = 1.0;
    double ulp = ulp_error(got, want_l);
    printf("ULP error: %f\n", ulp);
    return 0;
}
```
The output should be:
```
ULP error: 1.0
```
Note that 
If you are interested in diving into the full implementation of the ulp error we use internally, you can consult the [tester](https://github.com/ARM-software/optimized-routines/tree/master/math/test) tool in [AOR](https://github.com/ARM-software/optimized-routines/tree/master), with particular focus to the [ulp.h](https://github.com/ARM-software/optimized-routines/blob/master/math/test/ulp.h) file. Note this tool also handles special cases and considers the effect of different rounding modes in the ULP error.