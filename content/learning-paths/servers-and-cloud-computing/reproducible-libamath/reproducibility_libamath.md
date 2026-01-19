---
title: Reproducibility in Libamath
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-vector-extension reproducibility

On Linux platforms, Libamath supports bitwise-reproducible results across scalar, Neon (AdvSIMD), and SVE implementations for a subset of math functions.

When reproducibility is enabled, the same input values produce identical floating-point results, regardless of whether a supported function is executed using the scalar, Neon, or SVE code path. This keeps your results deterministic even if your app takes different vector paths.

Reproducible Libamath routines operate in the default accuracy mode, guaranteeing results within 3.5 ULP of the correctly rounded value.

Note that reproducible routines prioritize determinism over peak performance.

## Reproducible symbols

When reproducibility is enabled:

* Reproducible functions use the same public function names as their non-reproducible counterparts

* The linker resolves calls to the reproducible implementations when you build with `-DAMATH_REPRO=1` and link `-lamath_repro`

* Scalar, Neon, and SVE variants of a function all produce bitwise-identical results

* Unlike the symbols you find in `amath.h` (which don't guarantee reproducibility), reproducible symbols in `amath_repro` are not provided in `ZGV` mangling (only the `armpl_` notation is used).

The full list of functions that support reproducible behavior is provided in the header file `amath_repro.h`

## How to use reproducible Libamath

To enable reproducibility in a C or C++ application:

1. Include the Libamath header

```C
#include <amath.h>
```

2. Compile with reproducibility enabled

```bash
-DAMATH_REPRO=1
```

3. Link against the reproducible Libamath library
```bash
-lamath_repro
```

When you follow these steps, calls to supported functions resolve to the reproducible scalar, Neon, or SVE implementations.