---
title: Code example
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To illustrate the structure and design principles of SIMD Loops, consider loop 202 as an example

Use a text editor to open `loops/loop_202.c`

The function `inner_loop_202()` is defined around lines 60–70 in `loops/loop_202.c` and calls the `matmul_fp32` routine defined in `loops/matmul_fp32.c`

Open `loops/matmul_fp32.c` in your editor

This loop implements single-precision floating-point matrix multiplication of the form:

`C[M × N] = A[M × K] × B[K × N]`

You can view matrix multiplication in two equivalent ways:
- As the dot product between each row of `A` and each column of `B`
- As the sum of outer products between the columns of `A` and the rows of `B`

## Data structure

The loop begins by defining a data structure that captures the matrix
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
- Matrix `a` is stored in column-major order
- Matrix `b` is stored in row-major order
- The memory regions referenced by `a`, `b`, and `c` do not alias, as indicated by the `restrict` keyword

This layout helps optimize memory access patterns across the targeted SIMD architectures

## Loop attributes

Loop attributes are specified per target architecture:
- **SME targets** — `inner_loop_202` is invoked with the `__arm_streaming` attribute and uses a shared `ZA` register context (`__arm_inout("za")`). These attributes are wrapped in the `LOOP_ATTR` macro
- **SVE or NEON targets** — no additional attributes are required

This design enables portability across SIMD extensions

## Function implementation

`loops/matmul_fp32.c` provides several optimizations of matrix multiplication, including ACLE intrinsics and hand-optimized assembly

### Scalar code

A scalar C implementation appears around lines 40–52. It follows the dot-product formulation and serves as both a functional reference and an auto-vectorization baseline:

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

### SVE-optimized code

The SVE version uses indexed floating-point multiply–accumulate (`fmla`) to optimize the matrix multiplication operation. The outer product is decomposed into indexed multiply steps, and results accumulate directly in `Z` registers

In the intrinsics version (lines 167–210), the innermost loop is structured as follows:

```C { line_numbers="true", line_start="167" }
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

At the beginning of the loop, the accumulators (`Z` registers) are zeroed using `svdup` (or `dup` in assembly), encapsulated in the `ZERO_PAIR` macro

Within each iteration over the `K` dimension:
- 128 bits (four consecutive floating-point values) are loaded from `A` using replicate loads `svld1rq` (or `ld1rqw`), via `LOADA_PAIR`
- Two vectors are loaded from `B` using SVE vector loads, using `LOADB_PAIR`
- Indexed `fmla` operations compute element–vector products and accumulate into 16 `Z` register accumulators
- Partial sums build up the output tile

After all `K` iterations, results in the `Z` registers are stored to `C` using the `STORE_PAIR` macro

The equivalent SVE hand-optimized assembly appears around lines 478–598

This loop shows how SVE registers and indexed `fmla` enable efficient decomposition of the outer-product formulation into parallel, vectorized accumulation

For SVE/SVE2 semantics and optimization guidance, see the [Scalable Vector Extensions resources](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions)

### SME2-optimized code

The SME2 implementation leverages the outer-product formulation of the matrix
multiplication function, utilizing the `fmopa` SME instruction to perform the
outer-product and accumulate partial results in `ZA` tiles.

A snippet of the loop is shown below:

```C { line_numbers="true", line_start="78" }
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

Within the SME2 intrinsics code (lines 91–106), the innermost loop iterates across
the `K` dimension—columns of `A` and rows of `B`

In each iteration:
- Two consecutive vectors are loaded from `A` and two from `B` (`vec_a*`, `vec_b*`) using multi-vector load intrinsics
- `fmopa`, wrapped by `MOPA_TILE`, computes the outer product
- Partial results accumulate in four 32-bit `ZA` tiles

After all `K` iterations, results are written back in a store loop (lines 111–124)

During this phase, rows of `ZA` tiles are read into `Z` vectors using `svread_hor_za8_u8_vg4` (or `svreadz_hor_za8_u8_vg4` on SME2.1). Vectors are then stored to the output buffer using SME multi-vector `st1w` stores using `STORE_PAIR`

The equivalent SME2 hand-optimized assembly appears around lines 229–340

For instruction semantics and SME/SME2 optimization guidance, see the [SME Programmer's Guide](https://developer.arm.com/documentation/109246/latest/)

## Other optimizations

Beyond the SME2 and SVE implementations, this loop also includes additional
optimized versions that leverage architecture-specific features

### NEON

The NEON version (lines 612–710) uses structure load/store combined with indexed `fmla` to vectorize the computation

### SVE2.1

The SVE2.1 version (lines 355–462) extends the base SVE approach using multi-vector loads and stores

### SME2.1

The SME2.1 version uses `movaz` / `svreadz_hor_za8_u8_vg4` to reinitialize `ZA` tile accumulators while moving data out to registers
