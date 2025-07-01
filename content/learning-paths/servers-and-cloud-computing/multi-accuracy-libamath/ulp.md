---
title: Units in the Last Place (ULP)
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## ULP

Units in the Last Place (ULP) is the distance between two adjacent floating-point numbers at a given value, representing the smallest possible change in that number's representation.

It is a property of a number and can be calculated with the following expression:

```output
ULP(x) = nextafter(x, +inf) - x
```

Building on the example from the previous section:

Fixed `B = 2, p = 3, e^max = 2, e^min = -1`

| Significand | × 2⁻¹ | × 2⁰ | × 2¹ | × 2² |
|-------------|-------|------|------|------|
| 1.00 (1.0)  | 0.5   | 1.0  | 2.0  | 4.0  |
| 1.01 (1.25) | 0.625 | 1.25 | 2.5  | 5.0  |
| 1.10 (1.5)  | 0.75  | 1.5  | 3.0  | 6.0  |
| 1.11 (1.75) | 0.875 | 1.75 | 3.5  | 7.0  |

Based on the above definition, you can compute the ULP value for the numbers in this set as follows:

```
ULP(0.625) = nextafter(0.625, +inf) - 0.625 = 0.75-0.625 = 0.125
```
```
ULP(4.0) = 1.0
```

As the exponent of `x` increases, `ULP(x)` increases exponentially. That is, the spacing between floating-point values  grows with the magnitude of x.

Numbers with the same exponent have the same ULP.

## ULP in IEEE-754

For normalized IEEE-754 floating-point numbers, a similar behavior is observed: the distance between two adjacent representable values — that is, ULP(x) — is a power of two that depends only on the exponent of x.

A faster, commonly used expression for ULP is:

```
ULP(x) = 2^(e-p+1)
```

Where:
* `e` is the unbiased exponent (in the IEEE-754 definition of single precision this is `E-127`)
* `p` is the precision  (23 for IEEE-754 single-precision)

When computing the ULP of IEEE-754 floats, this expression becomes:
```
ULP(x) = 2^(e-23)
```
This expression is often used in mathematical computations of ULP since it offers performance benefits.


{{% notice ULP of Denormal Numbers %}}
Note that for denormal numbers, the latter expression does not apply.

In single precision as defined in IEEE-754, the smallest positive subnormal is:

```
min_pos_denormal = 2 ^ -23 x 2 ^ -126 = 2^-149
```

The second smallest is:
```
second_min_pos_denormal = 2 ^ -22 x 2 ^ -126 = 2^-148 = 2*2^-149
```
Thus, all denormal numbers are evenly spaced by `2^-149`.

{{% /notice %}}


## ULP implementation in C

Below is an example of an implementation of the ULP function of a number.

Use a text editor to save the code below in a file named `ulp.h`.

```C
#include <stdint.h>
#include <string.h>
#include <math.h>

// Bit cast float to uint32_t
static inline uint32_t asuint(float x) {
    uint32_t u;
    memcpy(&u, &x, sizeof(u));
    return u;
}

// Compute exponent of ULP spacing at x
static inline int ulpscale(float x) {
    //recover the biased exponent E
    int e = asuint(x) >> 23 & 0xff;
    if (e == 0)
        e++;  // handle subnormals

    // get exponent of the ULP
    // e-p = E - 127 -23
    return e - 127 - 23;
}

// Compute ULP spacing at x using ulpscale and scalbnf
static float ulp(float x) {
    return scalbnf(1.0f, ulpscale(x));
}
```

There are three key functions in this implementation:
* the `asuint(x)` function reinterprets the bit pattern of a float as a 32-bit unsigned integer, allowing the extraction of specific bit fields such as the exponent.
* the `ulpscale(x)` function returns the base-2 exponent of the ULP spacing at a given float value x, which is the result of `log2(ULP(x))`. The `e` variable in this function corresponds to the quantity E previously mentioned (the bitwise value of the exponent).
* the `scalbnf(m, n)` function (a standard function declared in math.h) efficiently evaluates `m x 2^n`.


Below is an example which uses the `ulp()` function.

Use a text editor to save the code below in a file named `ulp.c`.

```C
#include <stdio.h>
#include "ulp.h"

int main() {
    float x = 1.00000001f;
    float spacing = ulp(x);

    printf("ULP of %.8f is %.a\n", x, spacing);
    return 0;
}
```

Compile the program with GCC.

```bash
gcc -O2 ulp.c -o ulp
```

Run the program:

```bash
./ulp
```

On most systems, the output will print:

```output
ULP of 1.00000000 is 0x1p-23
```

This is the correct ULP spacing for values near 1.0f in IEEE-754 single-precision format.