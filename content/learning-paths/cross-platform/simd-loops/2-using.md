---
title: Using SIMD Loops
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To get started, clone the SIMD Loops project and change current directory:

```bash
git clone https://gitlab.arm.com/architecture/simd-loops simd-loops.git
cd simd-loops.git
```

## SIMD Loops structure

In the SIMD Loops project, the
source code for the loops is organized under the loops directory. The complete
list of loops is documented in the loops.inc file, which includes a brief
description and the purpose of each loop. Every loop is associated with a
uniquely named source file following the naming pattern `loop_<NNN>.c`, where
`<NNN>`  represents the loop number.

A loop is structured as follows:

```C
// Includes and loop_<NNN>_data structure definition

#if defined(HAVE_NATIVE) || defined(HAVE_AUTOVEC)

// C code
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#if defined(HAVE_xxx_INTRINSICS)

// Intrinsics versions: xxx = SME, SVE, or SIMD (NEON) versions
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#elif defined(<ASM_COND>)

 // Hand-written inline assembly :
// <ASM_COND> = __ARM_FEATURE_SME2p1, __ARM_FEATURE_SME2, __ARM_FEATURE_SVE2p1,
//              __ARM_FEATURE_SVE2, __ARM_FEATURE_SVE, or __ARM_NEON
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#else

#error "No implementations available for this target."

#endif

// Main of loop: Buffers allocations, loop function call, result functional checking
```

Each loop is implemented in several SIMD extension variants, and conditional
compilation is used to select one of the optimizations for the
`inner_loop_<NNN>` function. The native C implementation is written first, and
it can be generated either when building natively (HAVE_NATIVE) or through
compiler auto-vectorization (HAVE_AUTOVEC). When SIMD ACLE is supported (e.g.,
SME, SVE, or NEON), the code is compiled using high-level intrinsics. If ACLE
support is not available, the build process falls back to handwritten inline
assembly targeting one of the available SIMD extensions, such as SME2.1, SME2,
SVE2.1, SVE2, and others. The overall code structure also includes setup and
cleanup code in the main function, where memory buffers are allocated, the
selected loop kernel is executed, and results are verified for correctness.

At compile time, you can select which loop optimization to compile, whether it
is based on SME or SVE intrinsics, or one of the available inline assembly
variants (`make scalar neon sve2 sme2 sve2p1 sme2p1 sve_intrinsics
sme_intrinsics` ...).

As the result of the build, two types of binaries are generated. The first is a
single executable named `simd_loops`, which includes all the loop
implementations. A specific loop can be selected by passing parameters to the
program (e.g., `simd_loops -k <NNN> -n <iterations>`). The second type consists
of individual standalone binaries, each corresponding to a specific loop.
