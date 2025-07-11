---
title: Example
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To illustrate the structure and design principles of simd-loops, consider loop
202 as an example. `inner_loop_202` is defined at lines 69-79 in file
`loops/loops_202.c` and calls the `matmul_fp32` routine defined in
`matmul_fp32.c`.

Open `loops/matmul_fp32.c`.

This loop implements a single precision floating point matrix multiplication of
the form:

`C[M x N] = A[M x K] x B[K x N]`

A matrix multiplication can be understood in two equivalent ways:
- As the dot product between each row of matrix `A` and each column of matrix `B`.
- As the sum of outer products between the columns of `A` and the rows of `B`.

## Data structure

The loop begins by defining the data structure, which captures the matrix
dimensions (`M`, `K`, `N`) along with input and output buffers:

```C
struct loop_202_data {
  uint64_t m;
  uint64_t n;
  uint64_t k;
  float *restrict a;
  float *restrict b;
  float *restrict c;
};
```

For this loop:
- The first input matrix (A) is stored in column-major format in memory.
- The second input matrix (b) is stored in row-major format in memory.
- None of the memory area designated by `a`, `b` anf `c` alias (i.e. they
  overlap in some way) --- as indicated by the `restrict` keyword.

This layout choice helps optimize memory access patterns for all the targeted
SIMD architectures.

## Loop attributes

Next, the loop attributes are specified depending on the target architecture:
- For SME targets, the function `inner_loop_202` must be invoked with the
  `__arm_streaming` attribute, using a shared `ZA` register context
  (`__arm_inout("za")`). There attributes are wrapped in the LOOP_ATTR macro.
- For SVE or NEON targets, no additional attributes are required.

This design enables portability across different SIMD extensions.

## Function implementation

The `matmul_fp32` function from file `loops/matmul_fp32.c` provides several
optimizations of the single-precision floating-point matrix multiplication,
including the ACLE intrinsics-based code, and the assembly hand-optimized code.

### Scalar code

A scalar C implementation is provided at lines 40-52. This version follows the
dot-product formulation of matrix multiplication, serving both as a functional
reference and a baseline for auto-vectorization:

```C { line_numbers="true", line_start="40" }
   for (uint64_t x = 0; x < m; x++) {
     for (uint64_t y = 0; y < n; y++) {
       c[x * n + y] = 0.0f;
     }
   }

   // Loops ordered for contiguous memory access in inner loop
   for (uint64_t z = 0; z < k; z++)
     for (uint64_t x = 0; x < m; x++) {
       for (uint64_t y = 0; y < n; y++) {
         c[x * n + y] += a[z * m + x] * b[z * n + y];
       }
     }
```

### SVE optimized code

The SVE implementation uses the indexed floating-point multiply-accumulate
(`fmla`) instruction to optimize the matrix multiplication operation. In this
formulation, the outer-product is decomposed into multiple indexed
multiplication steps, with results accumulated directly into `Z` registers.

In the intrinsic version (lines 167-210), the innermost loop is structured as follows:

```C { line_numbers = "true", line_start="167"}
  for (m_idx = 0; m_idx < m; m_idx += 8) {
    for (n_idx = 0; n_idx < n; n_idx += svcntw() * 2) {
      ZERO_PAIR(0);
      ZERO_PAIR(1);
      ZERO_PAIR(2);
      ZERO_PAIR(3);
      ZERO_PAIR(4);
      ZERO_PAIR(5);
      ZERO_PAIR(6);
      ZERO_PAIR(7);

      ptr_a = &a[m_idx];
      ptr_b = &b[n_idx];
      while (ptr_a < cnd_k) {
        lda_0 = LOADA_PAIR(0);
        lda_1 = LOADA_PAIR(1);
        ldb_0 = LOADB_PAIR(0);
        ldb_1 = LOADB_PAIR(1);

        MLA_GROUP(0);
        MLA_GROUP(1);
        MLA_GROUP(2);
        MLA_GROUP(3);
        MLA_GROUP(4);
        MLA_GROUP(5);
        MLA_GROUP(6);
        MLA_GROUP(7);

        ptr_a += m * 2;
        ptr_b += n * 2;
      }

      ptr_c = &c[n_idx];
      STORE_PAIR(0);
      STORE_PAIR(1);
      STORE_PAIR(2);
      STORE_PAIR(3);
      STORE_PAIR(4);
      STORE_PAIR(5);
      STORE_PAIR(6);
      STORE_PAIR(7);
    }
    c += n * 8;
  }
```

At the beginning of the loop, the accumulators (`Z` registers) are explicitly
initialized to zero. This is achieved using `svdup` intrinsic (or its equivalent
`dup` assembly instruction), encapsulated in the `ZERO_PAIR` macro.

Within each iteration over the `K` dimension:
- 128 bits (four consecutive floating point values) are loaded from the matrix
  `A`, using the load replicate `svld1rq` intrinsics (or `ld1rqw` in assembly)
  in `LOADA_PAIR` macro.
- Two consecutive vectors are loaded from matrix `B`, using the SVE load
  instructions, called by the `LOADB_PAIR` macro.
- A sequence of indexed multiply-accumulate operations is performed, computing
  the product of each element from `A` with the vectors from `B`.
- The results are accumulated across the 16 `Z` register accumulators,
  progressively building the partial results of the matrix multiplication.

After completing all iterations across the `K` dimension, the accumulated
results in the `Z` registers are stored back to memory. The `STORE_PAIR` macro
writes the values into the corresponding locations of the output matrix `C`.

The equivalent SVE hand-optimized assembly code is written at lines 478-598.

This loop showcases how SVE registers and indexed `fmla` instructions enable
efficient decomposition of the outer-product formulation into parallel,
vectorized accumulation steps.

For more details on SVE/SVE2 instruction semantics, optimization guidelines and
other documents refer to the [Scalable Vector Extensions
resources](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions).

### SME2 optimized code

The SME2 implementation leverages the outer-product formulation of the matrix
multiplication function, utilizing the `fmopa` SME instruction to perform the
outer-product and accumulate partial results in `ZA` tiles.

A snippet of the loop is shown below:

```C { line_numbers = "true", line_start="78"}
#if defined(__ARM_FEATURE_SME2p1)
  svzero_za();
#endif

  for (m_idx = 0; m_idx < m; m_idx += svl_s * 2) {
    for (n_idx = 0; n_idx < n; n_idx += svl_s * 2) {
#if !defined(__ARM_FEATURE_SME2p1)
      svzero_za();
#endif

      ptr_a = &a[m_idx];
      ptr_b = &b[n_idx];
      while (ptr_a < cnd_k) {
        vec_a0 = svld1_x2(c_all, &ptr_a[0]);
        vec_b0 = svld1_x2(c_all, &ptr_b[0]);
        vec_a1 = svld1_x2(c_all, &ptr_a[m]);
        vec_b1 = svld1_x2(c_all, &ptr_b[n]);

        MOPA_TILE(0, 0, 0, 0);
        MOPA_TILE(1, 0, 0, 1);
        MOPA_TILE(2, 0, 1, 0);
        MOPA_TILE(3, 0, 1, 1);
        MOPA_TILE(0, 1, 0, 0);
        MOPA_TILE(1, 1, 0, 1);
        MOPA_TILE(2, 1, 1, 0);
        MOPA_TILE(3, 1, 1, 1);

        ptr_a += m * 2;
        ptr_b += n * 2;
      }

      ptr_c = &c[n_idx];
      for (l_idx = 0; l_idx < l_cnd; l_idx += 8) {
#if defined(__ARM_FEATURE_SME2p1)
        vec_c0 = svreadz_hor_za8_u8_vg4(0, l_idx + 0);
        vec_c1 = svreadz_hor_za8_u8_vg4(0, l_idx + 4);
#else
        vec_c0 = svread_hor_za8_u8_vg4(0, l_idx + 0);
        vec_c1 = svread_hor_za8_u8_vg4(0, l_idx + 4);
#endif

        STORE_PAIR(0, 0, 1, 0);
        STORE_PAIR(1, 0, 1, n);
        STORE_PAIR(0, 2, 3, c_blk);
        STORE_PAIR(1, 2, 3, c_off);

        ptr_c += n * 2;
      }
    }
    c += c_blk * 2;
  }
```

Within the SME2 intrinsics code (lines 91-106), the innermost loop iterates across
the `K` dimension - corresponding to the columns of matrix `A` and the rows of
matrix `B`.

In each iteration:
- Two consecutive vectors are loaded from `A` and two consecutive vectors are
  loaded from `B` (`vec_a`, and `vec_b`), using the multi-vector load
  instructions.
- The `fmopa` instruction, encapsulated within the `MOPA_TILE` macro, computes
  the outer product of the input vectors.
- The results are accumulated into the four 32-bit `ZA` tiles.

After all iterations over K dimension, the accumulated results are stored back
to memory through a store loop at lines 111-124:

During this phase, four rows of `ZA` tiles are read out into four `Z` vectors
using the `svread_hor_za8_u8_vg4` intrinsic (or the equivalent `mova` assembly
instruction). The vectors are then stored into the output buffer with SME
multi-vector `st1w` store instructions, wrapped in the `STORE_PAIR` macro.

The equivalent SME2 hand-optimized code is at lines 229-340.

For more details on instruction semantics, and SME/SME2 optimization guidelines,
refer to the official [SME Programmer's
Guide](https://developer.arm.com/documentation/109246/latest/).

## Other optimizations

Beyond the SME2 and SVE2 implementations shown above, this loop also includes several
alternative optimized versions, each leveraging architecture-specific features.

### Neon

The neon version (lines 612-710) relies on multiple structure load/store
combined with indexed `fmla` instructions to vectorize the matrix multiplication
operation.

### SVE2.1

The SVE2.1 implementation (lines 355-462) extends the base SVE approach by
utilizing multi-vector load and store instructions.

### SME2.1

The SME2.1 leverages the `movaz` instruction / `svreadz_hor_za8_u8_vg4`
intrinsic to simultaneously reinitialize `ZA` tile accumulators while moving
data out to registers.
