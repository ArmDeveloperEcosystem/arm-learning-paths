---
title: Matrix multiplication using SME2 intrinsics in C
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will write an SME2-optimized matrix multiplication routine in C using the intrinsics that the compiler provides.

## What are instrinsics?

*Intrinsics*, also known as *compiler intrinsics* or *intrinsic functions*, are the functions available to application developers that the compiler has intimate knowledge of. This enables the compiler to either translate the function to a specific instruction or to perform specific optimizations, or both.

You can learn more about intrinsics in this [Wikipedia
Article on Intrinsic Function](https://en.wikipedia.org/wiki/Intrinsic_function).

Using intrinsics allows you to write performance-critical code in C while still using standard constructs like loops. This produces performance close to what can be reached with hand-written assembly whilst being significantly more maintainable and portable.

All Arm-specific intrinsics are specified in the
[ACLE](https://github.com/ARM-software/acle), which is the Arm C Language Extension. ACLE
is supported by the main compilers, most notably [GCC](https://gcc.gnu.org/) and
[Clang](https://clang.llvm.org).

## Implementation

In this example, a top-level function named `matmul_intr`, defined in `matmul_intr.c`, brings together the preprocessing and matrix multiplication steps:

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

Note the use of `__arm_new("za")` and `__arm_locally_streaming` at line 1. These attributes ensure that the compiler saves the ZA storage, allowing your function to use it safely without destroying its content if it was still in use by one of the callers.

`SVL`, the dimension of the ZA storage, is requested from the underlying hardware with the `svcntsw()` function call at line 5, and passed down to the `preprocess_l_intr` and `matmul_intr_impl` functions. `svcntsw()` is a function provided by the ACLE library.

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

Note that `preprocess_l_intr` has been annotated at line 3 with:

- `__arm_streaming` - because this function is using streaming instructions

- `__arm_inout("za")` - because `preprocess_l_intr` reuses the ZA storage
  from its caller

The matrix preprocessing is performed in a double-nested loop, over the `M` (line 7) and `K` (line 12) dimensions of the input matrix `a`. Both loops have an `SVL` step increment, which corresponds to the horizontal and vertical dimensions of the ZA storage that will be used. The dimensions of `a` might not be perfect multiples of `SVL` however, which is why the predicates `pMDim`
(line 9) and `pKDim` (line 14) are computed in order to know which rows (respectively columns) are valid.

The core of `preprocess_l_intr` is made of two parts:

- Lines 17 - 37: load matrix tile as rows. In this part, loop unrolling has been used at two different levels. At the lowest level, 4 rows are loaded at a time  (lines 24-27). But this goes much further because as SME2 has multi-vectors operations (hence the `svld1_x2` intrinsic to load 2 rows in 2 vector registers), this allows the function to load the consecutive row, which happens to be the row from the neighboring tile on the right: this means two tiles are processed at once. At lines 29-32, the pairs of vector registers are rearranged on quads of vector registers so they can be stored horizontally in the two tiles' ZA storage at lines 33-36 with the`svwrite_hor_za32_f32_vg4` intrinsic. Of course, as the input matrix might not have dimensions that are perfect multiples of `SVL`, the `p0`, `p1`, `p2` and `p3` predicates are computed with the `svpsel_lane_c32` intrinsic (lines 18-21) so that elements outside of the input matrix are set to 0 when they are loaded at lines 24-27.

- Lines 39 - 51: read the matrix tile as columns and store them. Now that the two tiles have been loaded *horizontally*, they will be read *vertically* with the `svread_ver_za32_f32_vg4` intrinsic to quad-registers of vectors (`zq0` and `zq1`) at lines 45-48 and then stored with the `svst1` intrinsic to the relevant location in the destination matrix `a_mod` (lines 49-50). Note again the usage of predicates `p0` and `p1` (computed at lines 43-44) to `svst1` to prevent writing out of the matrix bounds.

Using intrinsics simplifies function development, provided you have a good understanding of the SME2 instruction set. Predicates, which are fundamental to both SVE and SME, allow you to express  algorithms cleanly while handling corner cases efficiently. Notably, the loops for include no explicit condition checks for rows or columns that extend beyond matrix bounds.

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

Note again that `matmul_intr_impl` function has been annotated at line 4 with:

- `__arm_streaming`, because the function is using streaming instructions

- `__arm_inout("za")`, because the function reuses the ZA storage from its caller

The multiplication with the outer product is performed in a double-nested loop, over the `M` (line 7) and `N` (line 11) dimensions of the input matrices `matLeft_mod` and `matRight`. Both loops have an `SVL` step increment, which corresponds to the horizontal and vertical dimensions of the ZA storage that will be used as one tile at a time will be processed.

The `M` and `N` dimensions of the inputs might not be perfect multiples of `SVL` so the predicates `pMDim` (line 9) (respectively `pNDim` at line 13) are computed in order to know which rows (respectively columns) are valid.

The core of the multiplication is done in two parts:

- Outer-product and accumulation at lines 15-25. As `matLeft` has been laid out perfectly in memory with `preprocess_l_intr`, this part becomes straightforward. First, the tile is zeroed with the `svzero_za` intrinsics at line 16 so the outer products can be accumulated in the tile. The outer
products are computed and accumulation over the `K` common dimension with the loop at line 19: the column of `matleft_mod` and the row of `matRight` are loaded with the `svld1` intrinsics at line 20-23 to vector registers `zL` and `zR`, which are then used at line 24 with the `svmopa_za32_m` intrinsic to perform the outer product and accumulation (to tile 0). This
is exactly what was shown in Figure 2 earlier in the Learning Path. Note again the usage of the `pMDim` and `pNDim` predicates to deal correctly with the rows and columns respectively which are out of bounds.

- Storing of the result matrix at lines 27-46. The previous section computed the
  matrix multiplication result for the current tile, which now needs to be
  written back to memory. This is done with the loop at line 29 which will
  iterate over all rows of the tile: the `svst1_hor_za32` intrinsic at lines
  35-46 stores directly from the tile to memory. Note that the loop has been
  unrolled by a factor of 4 (thus the `trow += 4` increment, line 29) and the
  4 `svst1_hor_za32`. Again, the `pMDim` and `pNDim` predicates deal
  gracefully with the parts of the tile which are out-of-bound for the
  destination matrix `matResult`.

Once again, intrinsics makes it easy to fully leverage SME2, provided you have a
solid understanding of its available instructions. The compiler is automatically
handling many low-level aspects (saving / restoring of the different contexts),
as well as not using registers that are reserved on specific platforms (like
`x18`). Predicates handle corner cases elegantly, ensuring robust execution.
Most importantly, the code adapts to different SVL values across various
hardware implementations without requiring recompilation. This follows the key
principle of compile-once, run-everywhere, allowing systems with larger SVL to
execute computations more efficiently while using the same binary.

### Compile and run

The main function is exactly the same that was used for the assembly version,
with the `IMPL` macro defined to be `intr` in the `Makefile`.

First, make sure that the `sme2_matmul_intr` executable is up-to-date:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-3">}}
ninja -C build-native/ sme2_matmul_intr
ninja: Entering directory `build-native/'
ninja: no work to do.
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2-3">}}
ninja -C build-android/ sme2_matmul_intr
ninja: Entering directory `build-android/'
ninja: no work to do.
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-3">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ninja -C build-baremetal/ sme2_matmul_intr
ninja: Entering directory `build-baremetal/'
ninja: no work to do.
{{< /tab >}}

{{< /tabpane >}}

Then execute `sme2_matmul_intr` either natively or on the FVP:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-4">}}
./build-native/sme2_matmul_intr
SME2 Matrix Multiply fp32 *intr* [verification mode] with M=125, K=70, N=35
Matrix preprocessing: PASS !
Matrix multiplication: PASS !
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2,5-7">}}
adb push build-android/sme2_matmul_intr /data/local/tmp
build-android/sme2_matmul_intr: 1 file pushed, 0 skipped. 29.7 MB/s (19456 bytes in 0.001s)
adb shell chmod 755 /data/local/tmp/sme2_matmul_intr
adb shell /data/local/tmp/sme2_matmul_intr
SME2 Matrix Multiply fp32 *intr* [verification mode] with M=125, K=70, N=35
Matrix preprocessing: PASS !
Matrix multiplication: PASS !
{{< /tab >}}

{{< tab header="Emulated SME2 support" language="bash" output_lines="2-6">}}
docker run --rm -v "$PWD:/work" armswdev/sme2-learning-path:sme2-environment-v3 ./run-fvp.sh build-baremetal/sme2_matmul_intr
SME2 Matrix Multiply fp32 *intr* [verification mode] with M=125, K=70, N=35
Matrix preprocessing: PASS !
Matrix multiplication: PASS !

Info: /OSCI/SystemC: Simulation stopped by user.
{{< /tab >}}

{{< /tabpane >}}

{{% notice Tip %}}
As with the `sme2_matmul_asm` program, you can provide the `M`, `K`and `N`
parameters on the command line to `sme2_matmul_intr`.
{{% /notice %}}