---
title: SME2 intrinsics matrix multiplication
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this chapter, you will write an SME2 optimized matrix multiplication in C
using the intrinsics provided by the compiler.

## Matrix multiplication with SME2 intrinsics

*Intrinsics*, also know known as *compiler intrinsics* or *intrinsic functions*
are functions available to application developers that the compiler has an
intimate knowledge of. This enables the compiler to either translate that
function to a very specific instruction and/or to perform specific
optimizations.

You can lean more about intrinsics in this [wikipedia
article](https://en.wikipedia.org/wiki/Intrinsic_function).

Using intrinsics allows the programmer to use the very specific instructions
needed to achieve the required performance while writing in C all the mundane
code (loops, ...). This gives performance close to what can be reached with hand
written assembly whilst being significantly more maintainable and portable !

All Arm specific intrinsics are specified in the
[ACLE](https://github.com/ARM-software/acle) --- Arm C language extension. ACLE
is supported by the main compilers, most notably [GCC](https://gcc.gnu.org/) and
[clang](https://clang.llvm.org).

## Streaming mode

In the previous page, the assembly language gave the programmer full access to
the processor features. However, this comes at a cost in complexity and
maintenance especially when one has to manage large code bases with deeply
nested function calls. The assembly version is very low level, and does not deal
properly with the SME state. In real world large scale software, the program
will move back and forth from streaming mode, and some streaming mode routines
will call other streaming mode routines, which means that some state (including
the ZA storage) needs to be saved and restored. This is defined in the ACLE and
supported by the compiler: the programmer *just* has to annotate the function
with some keywords and set up some registers (see function ``setup_sme`` in
``misc.c`` for an example). See
[Introduction to streaming and non-streaming mode](https://arm-software.github.io/acle/main/acle.html#controlling-the-use-of-streaming-mode)
for further details. The rest of this section quotes parts from the ACLE as there is no better way to
restate the same.

The AArch64 architecture defines a concept called “streaming mode”, controlled
by a processor state bit called ``PSTATE.SM``. At any given point in time, the
processor is either in streaming mode (``PSTATE.SM==1``) or in non-streaming mode
(``PSTATE.SM==0``). There is an instruction called ``SMSTART`` to enter streaming mode
and an instruction called ``SMSTOP`` to return to non-streaming mode.

Streaming mode has three main effects on C and C++ code:

- It can change the length of SVE vectors and predicates: the length of an SVE
  vector in streaming mode is called the “streaming vector length” (SVL), which
  might be different from the normal non-streaming vector length. See
  [Effect of streaming mode on VL](https://arm-software.github.io/acle/main/acle.html#effect-of-streaming-mode-on-vl)
  for more details.
- Some instructions can only be executed in streaming mode, which means that
  their associated ACLE intrinsics can only be used in streaming mode. These
  intrinsics are called “streaming intrinsics”.
- Some other instructions can only be executed in non-streaming mode, which
  means that their associated ACLE intrinsics can only be used in non-streaming
  mode. These intrinsics are called “non-streaming intrinsics”.

The C and C++ standards define the behavior of programs in terms of an “abstract
machine”. As an extension, the ACLE specification applies the distinction
between streaming mode and non-streaming mode to this abstract machine: at any
given point in time, the abstract machine is either in streaming mode or in
non-streaming mode.

This distinction between processor mode and abstract machine mode is mostly just
a dry specification detail. However, the usual “as if” rule applies: the
processor's actual mode at runtime can be different from the abstract machine's
mode, provided that this does not alter the behavior of the program. One
practical consequence of this is that C and C++ code does not specify the exact
placement of ``SMSTART`` and ``SMSTOP`` instructions; the source code simply places
limits on where such instructions go. For example, when stepping through a
program in a debugger, the processor mode might sometimes be different from the
one implied by the source code.

ACLE provides attributes that specify whether the abstract machine executes statements:

- in non-streaming mode, in which case they are called “non-streaming statements”
- in streaming mode, in which case they are called “streaming statements”
- in either mode, in which case they are called “streaming-compatible statements”

SME provides an area of storage called ZA, of size ``SVL.B`` x ``SVL.B`` bytes. It
also provides a processor state bit called ``PSTATE.ZA`` to control whether ZA
is enabled.

In C and C++ code, access to ZA is controlled at function granularity: a
function either uses ZA or it does not. Another way to say this is that a
function either “has ZA state” or it does not.

If a function does have ZA state, the function can either share that ZA state
with the function's caller or create new ZA state “from scratch”. In the latter
case, it is the compiler's responsibility to free up ZA so that the function can
use it; see the description of the lazy saving scheme in
[AAPCS64](https://arm-software.github.io/acle/main/acle.html#AAPCS64) for details
about how the compiler does this.

## Implementation

Here again, a top level function named ``matmul_intr`` in ``matmul_intr.c``
will be used to stitch together the preprocessing and the multiplication:

```C  "{ line_numbers = true }"
__arm_new("za") __arm_locally_streaming void matmul_intr(
    uint64_t M, uint64_t K, uint64_t N, const float *restrict matLeft,
    const float *restrict matRight, float *restrict matLeft_mod,
    float *restrict matResult) {
    uint64_t SVL = svcntsw();
    preprocess_l_intr(M, K, SVL, matLeft, matLeft_mod);
    matmul_intr_impl(M, K, N, SVL, matLeft_mod, matRight, matResult);
}
```

Note the ``__arm_new("za")`` and ``__arm_locally_streaming`` at line 1 that will
make the compiler save the ZA storage so we can use it without destroying its
content if it was still in use by one of the callers.

``SVL``, the dimension of the ZA storage, is requested from the underlying
hardware with the ``svcntsw()`` function call at line 5, and passed down to the
``preprocess_l_intr`` and ``matmul_intr_impl`` functions. ``svcntsw()`` is a
function provided be the ACLE library.

### Matrix preprocessing

```C "{ line_numbers = true }"
void preprocess_l_intr(
    uint64_t M, uint64_t K, uint64_t SVL, const float *restrict a,
    float *restrict a_mod) __arm_streaming __arm_inout("za") {
    const uint64_t M_mod = SVL * (M / SVL + (M % SVL != 0 ? 1 : 0));

    // The outer loop, iterating over rows (M dimension)
    for (uint64_t row = 0; row < M; row += SVL) {

        svbool_t pMDim = svwhilelt_b32(row, M);

        // The inner loop, iterating on columns (K dimension).
        for (uint64_t col = 0; col < K; col += 2 * SVL) {

            svcount_t pKDim = svwhilelt_c32(col, K, 2);

            // Load-as-rows
            for (uint64_t trow = 0; trow < SVL; trow += 4) {
                svcount_t p0 = svpsel_lane_c32(pKDim, pMDim, trow + 0);
                svcount_t p1 = svpsel_lane_c32(pKDim, pMDim, trow + 1);
                svcount_t p2 = svpsel_lane_c32(pKDim, pMDim, trow + 2);
                svcount_t p3 = svpsel_lane_c32(pKDim, pMDim, trow + 3);

                const uint64_t tile_UL_corner = (row + trow) * K + col;
                svfloat32x2_t zp0 = svld1_x2(p0, &a[tile_UL_corner + 0 * K]);
                svfloat32x2_t zp1 = svld1_x2(p1, &a[tile_UL_corner + 1 * K]);
                svfloat32x2_t zp2 = svld1_x2(p2, &a[tile_UL_corner + 2 * K]);
                svfloat32x2_t zp3 = svld1_x2(p3, &a[tile_UL_corner + 3 * K]);

                svfloat32x4_t zq0 = svcreate4(svget2(zp0, 0), svget2(zp1, 0),
                                              svget2(zp2, 0), svget2(zp3, 0));
                svfloat32x4_t zq1 = svcreate4(svget2(zp0, 1), svget2(zp1, 1),
                                              svget2(zp2, 1), svget2(zp3, 1));
                svwrite_hor_za32_f32_vg4(
                    /* tile: */ 0, /* slice: */ trow, zq0);
                svwrite_hor_za32_f32_vg4(
                    /* tile: */ 1, /* slice: */ trow, zq1);
            }

            // Read-as-columns and store
            const uint64_t dest_0 = row * K + col * SVL;
            const uint64_t dest_1 = dest_0 + SVL * SVL;
            for (uint64_t tcol = 0; tcol < SVL; tcol += 4) {
                svcount_t p0 = svwhilelt_c32(dest_0 + tcol * SVL, K * M_mod, 4);
                svcount_t p1 = svwhilelt_c32(dest_1 + tcol * SVL, K * M_mod, 4);
                svfloat32x4_t zq0 =
                    svread_ver_za32_f32_vg4(/* tile: */ 0, /* slice: */ tcol);
                svfloat32x4_t zq1 =
                    svread_ver_za32_f32_vg4(/* tile: */ 1, /* slice: */ tcol);
                svst1(p0, &a_mod[dest_0 + tcol * SVL], zq0);
                svst1(p1, &a_mod[dest_1 + tcol * SVL], zq1);
            }
        }
    }
}
```

Note that ``preprocess_l_intr`` has been annotated at line 3 with:

- ``__arm_streaming``, because this function is using streaming instructions,

- ``__arm_inout("za")``, because ``preprocess_l_intr`` reuses the ZA storage
  from its caller.

The matrix preprocessing is performed in a double nested loop, over the ``M``
(line 7) and ``K`` (line 12) dimensions of the input matrix ``a``. Both loops
have an ``SVL`` step increment, which corresponds to the horizontal and vertical
dimensions of the ZA storage that will be used. The dimensions of ``a`` may not
be perfect multiples of ``SVL`` though... which is why the predicates ``pMDim``
(line 9) and ``pKDim`` (line 14) are computed in order to know which rows (resp.
columns) are valid.

The core of ``preprocess_l_intr`` is made of two parts:

- lines 17 - 37: load matrix tile as rows. In this part, loop unrolling has been
  used at 2 different levels. At the lowest level, 4 rows are loaded at a time
  (lines 24-27). But this goes much further because as SME2 has multi-vectors
  operations (hence the ``svld1_x2`` intrinsic to load 2 rows in 2 vector
  registers), this allows the function to load the consecutive row, which
  happens to be the row from the neighbouring tile on the right : this means 2
  tiles are processed at once. At line 29-32, the pairs of vector registers are
  rearranged on quads of vector registers so they can be stored horizontally in
  the 2 tiles' ZA storage at lines 33-36 with the ``svwrite_hor_za32_f32_vg4``
  intrinsic. Of course, as the input matrix may not have dimensions that are
  perfect multiples of ``SVL``, the ``p0``, ``p1``, ``p2`` and ``p3`` predicates
  are computed with the ``svpsel_lane_c32`` intrinsic (lines 18-21) so that
  elements outside of the input matrix are set to 0 when they are loaded at
  lines 24-27.

- lines 39 - 51: read the matrix tile as columns and store them. Now that the 2
  tiles have been loaded *horizontally*, they will be read *vertically* with the
  ``svread_ver_za32_f32_vg4`` intrinsic to quad-registers of vectors (``zq0``
  and ``zq1``) at lines 45-48 and then stored with the ``svst1`` intrinsic to
  the relevant location in the destination matrix ``a_mod`` (lines 49-50). Note
  again the usage of predicates ``p0`` and ``p1`` (computed at lines 43-44) to
  ``svst1`` to prevent writing out of the matrix bounds.

As you can see, the usage of intrinsics greatly simplifies the writing of a
function once one has a good understanding of the available instructions in the
SME2 instruction set. The usage of predicates, which are at the core of SVE and
SME and allows to express an algorithm almost naturally and deal elegantly with
the corner cases (you will note that there is no explicit testing in the loops
for the cases where the rows or columns are outside of the matrix bounds).

### Outer-product multiplication

```C "{ line_numbers = true }"
void matmul_intr_impl(
    uint64_t M, uint64_t K, uint64_t N, uint64_t SVL,
    const float *restrict matLeft_mod, const float *restrict matRight,
    float *restrict matResult) __arm_streaming __arm_inout("za") {

    // Build the result matrix tile by tile.
    for (uint64_t row = 0; row < M; row += SVL) {

        svbool_t pMDim = svwhilelt_b32(row, M);

        for (uint64_t col = 0; col < N; col += SVL) {

            svbool_t pNDim = svwhilelt_b32(col, N);

            // Outer product + accumulation
            svzero_za();
            const uint64_t matLeft_pos = row * K;
            const uint64_t matRight_UL_corner = col;
            for (uint64_t k = 0; k < K; k++) {
                svfloat32_t zL =
                    svld1(pMDim, &matLeft_mod[matLeft_pos + k * SVL]);
                svfloat32_t zR =
                    svld1(pNDim, &matRight[matRight_UL_corner + k * N]);
                svmopa_za32_m(0, pMDim, pNDim, zL, zR);
            }

            // Store ZA to matResult.
            const uint64_t result_tile_UL_corner = row * N + col;
            for (uint64_t trow = 0; trow < SVL && row + trow < M; trow += 4) {
                svbool_t p0 = svpsel_lane_b32(pNDim, pMDim, row + trow + 0);
                svbool_t p1 = svpsel_lane_b32(pNDim, pMDim, row + trow + 1);
                svbool_t p2 = svpsel_lane_b32(pNDim, pMDim, row + trow + 2);
                svbool_t p3 = svpsel_lane_b32(pNDim, pMDim, row + trow + 3);

                svst1_hor_za32(
                    /* tile: */ 0, /* slice: */ trow + 0, p0,
                    &matResult[result_tile_UL_corner + (trow + 0) * N]);
                svst1_hor_za32(
                    /* tile: */ 0, /* slice: */ trow + 1, p1,
                    &matResult[result_tile_UL_corner + (trow + 1) * N]);
                svst1_hor_za32(
                    /* tile: */ 0, /* slice: */ trow + 2, p2,
                    &matResult[result_tile_UL_corner + (trow + 2) * N]);
                svst1_hor_za32(
                    /* tile: */ 0, /* slice: */ trow + 3, p3,
                    &matResult[result_tile_UL_corner + (trow + 3) * N]);
            }
        }
    }
}
```

Note again that ``matmul_intr_impl`` function has been annotated at line 4 with:

- ``__arm_streaming``, because the function is using streaming instructions,

- ``__arm_inout("za")``, because the function reuses the ZA storage from its caller.

The multiplication with the outer product is performed in a double nested loop,
over the ``M`` (line 7) and ``N`` (line 11) dimensions of the input matrices
``matLeft_mod`` and ``matRight``. Both loops have an ``SVL`` step increment,
which corresponds to the horizontal and vertical dimensions of the ZA storage
that will be used as one tile at a time will be processed. The ``M`` and ``N``
dimensions of the inputs may not be perfect multiples of ``SVL`` so the
predicates ``pMDim`` (line 9) (resp. ``pNDim`` at line 13) are computed in order
to know which rows (resp. columns) are valid.

The core of the multiplication is done in 2 parts:

- outer-product and accumulation at lines 15-25. As ``matLeft`` has been
  laid-out perfectly in memory with ``preprocess_l_intr``, this part becomes
  straightforward. First, the tile is zeroed with the ``svzero_za`` intrinsics
  at line 16 so the outer products can be accumulated in the tile. The outer
  products are computed and accumulation over the ``K`` common dimension with
  the loop at line 19: the column of ``matleft_mod`` and the row of ``matRight``
  are loaded with the ``svld1`` intrinsics at line 20-23 to vector registers
  ``zL`` and ``zR``, which are then used at line 24 with the ``svmopa_za32_m``
  intrinsic to perform the outer product and accumulation (to tile 0). This
  corresponds exactly to what you saw in figure 2 earlier in the learning path.
  Note again the usage of the ``pMDim`` and ``pNDim`` predicates to deal
  correctly with the rows and columns respectively which are out of bounds.

- storing of the result matrix at lines 27-46. The previous part has computed
  the result of the matrix multiplication for the current tile, which now needs
  to be written back to memory. This is done with the loop at line 29 which will
  iterate over all rows of the tile: the ``svst1_hor_za32`` intrinsic at lines
  35-46 stores directly from the tile to memory. Note that the loop has been
  unrolled by a factor of 4 (thus the ``trow += 4`` increment, line 29) and the
  4 ``svst1_hor_za32``. Again, the ``pMDim`` and ``pNDim`` predicates deal
  gracefully with the parts of the tile which are out-of-bound for the
  destination matrix ``matResult``.

Once again you will note that the usage of the intrinsics made it easy to take
advantage of the full power of SME2 --- once there is a good undestanding of the
available SME2 instructions. The predicates deal elegantly with the corner
cases. And most importanly, our code will deal with different SVL from different
hardware implementations without having to be recompiled. It's the important
concept of *compile-once* / *run-everywhere*, plus the implementations that have
larger SVL will perform the computation faster (for the same binary).

### Compile and run

The main function is exactly the same that was used for the assembly version,
with the ``IMPL`` macro defined to be ``intr`` in the ``Makefile``.

First, make sure that the ``sme2_matmul_intr`` executable is up to date:

```BASH
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 make sme2_matmul_intr
```

Then execute ``sme2_matmul_intr`` on the FVP:

```BASH
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 ./run-fvp.sh sme2_matmul_intr
```

which should output something similar to:

```TXT
SME2 Matrix Multiply fp32 *intr* example with args 125 35 70
Matrix preprocessing: PASS !
Matrix multiplication: PASS !

Info: /OSCI/SystemC: Simulation stopped by user.
```
