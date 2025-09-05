---
title: Using SIMD Loops
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

First, clone [SIMD Loops](https://gitlab.arm.com/architecture/simd-loops) and
change current directory to it with:

```BASH
git clone https://gitlab.arm.com/architecture/simd-loops simd-loops.git
cd simd-loops.git
```

## SIMD Loops structure

In the [SIMD Loops](https://gitlab.arm.com/architecture/simd-loops) project, the
source code for the loops is organized under the loops directory. The complete
list of loops is documented in the loops.inc file, which includes a brief
description and the purpose of each loop. Every loop is associated with a
uniquely named source file following the naming pattern `loop_<NNN>.c`, where
`<NNN>`  represents the loop number.

A loop is structured as follows:

```C
// Includes and loop_<NNN>_data structure definition

#if defined(HAVE_xxx_INTRINSICS)

// Intrinsics versions: xxx = SME, SVE, or SIMD (Neon) versions
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#elif defined(HAVE_xxx)

// Hand-written inline assembly : xxx = SME2P1, SME2, SVE2P1, SVE2, SVE, or SIMD
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#else

// Equivalent C code
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#endif

// Main of loop: Buffers allocations, loop function call, result functional checking
```

Each loop is implemented in several SIMD extension variants, and conditional
compilation is used to select one of the optimisations for the
`inner_loop_<NNN>` function. When ACLE is supported (e.g. SME, SVE, or
SIMD/Neon), a high-level intrinsic implementation is compiled. If ACLE is not
available, the tool falls back to handwritten inline assembly targeting one of
the various SIMD extensions, including SME2.1, SME2, SVE2.1, SVE2, and others.
If no handwritten inline assembly is detected, a fallback implementation in
native C is used. The overall code structure also includes setup and cleanup
code in the main function, where memory buffers are allocated, the selected loop
kernel is executed, and results are verified for correctness.

At compile time, you can select which loop optimisation to compile, whether it
is based on SME or SVE intrinsics, or one of the available inline assembly
variants (`make scalar neon sve2 sme2 sve2p1 sme2p1 sve_intrinsics
sme_intrinsics` ...).

As the result of the build, two types of binaries are generated. The first is a
single executable named `simd_loops`, which includes all the loop
implementations. A specific loop can be selected by passing parameters to the
program (e.g., `simd_loops -k <NNN> -n <iterations>`). The second type consists
of individual standalone binaries, each corresponding to a specific loop.
