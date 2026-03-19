---
title: Enable reproducibility in Libamath
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-vector-extension reproducibility

On Linux platforms, Libamath supports bitwise-reproducible results across scalar, Neon (AdvSIMD), and SVE implementations for a subset of math functions.

When reproducibility is enabled, the same input values produce identical floating-point results, regardless of whether a supported function is executed using the scalar, Neon, or SVE code path. This keeps your results deterministic even if your app takes different vector paths.

Reproducible Libamath routines operate in the default accuracy mode, guaranteeing results within 3.5 ULP of the correctly rounded value.

Reproducible routines prioritize determinism over peak performance.

## Reproducible symbols

When reproducibility is enabled, reproducible functions use the same public function names as their non-reproducible counterparts. The linker resolves calls to the reproducible implementations when you build with `-DAMATH_REPRO=1` and link `-lamath_repro`, and the scalar, Neon, and SVE variants of a function all produce bitwise-identical results.

Unlike the symbols in `amath.h` (which don't guarantee reproducibility), reproducible symbols in `amath_repro` are not provided in `ZGV` mangling. Only the `armpl_` notation is used.

The full list of functions that support reproducible behavior is provided in the header file `amath_repro.h`.

## How to use reproducible Libamath

To enable reproducibility in a C or C++ application, include the Libamath header in your source file:

```C
#include <amath.h>
```

Then compile and link with reproducibility enabled:

```bash
gcc app.c -DAMATH_REPRO=1 -lamath_repro -o app
```

The `-DAMATH_REPRO=1` flag enables reproducibility at compile time, and `-lamath_repro` links against the reproducible Libamath library. When you follow these steps, calls to supported functions resolve to the reproducible scalar, Neon, or SVE implementations.

With reproducibility configured, the next section walks through hands-on examples using `expf` across scalar, Neon, and SVE code paths.

## What you've learned and what's next

You've learned how to enable reproducible math routines in Libamath through compile-time configuration and library linking. You can now compile code with the reproducible library variant and understand the trade-offs between reproducibility and peak performance.

Next, you'll verify reproducible behavior through hands-on examples that compare scalar, Neon, and SVE implementations of the exponential function.