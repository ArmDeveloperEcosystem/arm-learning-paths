---
title: Identify additional LUTI features
description: Compare ZT0 and Z-register lookup tables, SME2.1 destination forms, and their compile-time feature macros.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The earlier examples use the original SME2 lookup path: a table in `ZT0`,
packed indices in Z registers, and one or more Z-register results. Other
architectural features use a different table source or add specialized forms.

## Compare the feature paths

| Feature path | Table source | Execution state | Distinguishing capability |
|---|---|---|---|
| `FEAT_SME2` | Fixed 512-bit `ZT0` | Streaming mode with ZA enabled | `LUTI2` and `LUTI4` can produce one, two, or four Z-register results, subject to the element-width encoding |
| `FEAT_SME2p1` | Fixed 512-bit `ZT0` | Streaming mode with ZA enabled | Extends the SME2 forms with strided destination pairs and quads |
| `FEAT_LUT` with `FEAT_SVE2` or `FEAT_SME2` | One or two scalable Z registers | Non-streaming SVE or Streaming SVE, respectively | Add Z-register table forms of `LUTI2` and `LUTI4` which produce one Z-register result without using `ZT0` |

## Use Z-register tables with FEAT_LUT

`FEAT_LUT` expand the functionality of `FEAT_SME2` allowing to use scalable Z registers as the lookup-table source. This provide an alternative to using the `ZT0` register. 

```text
table Z register(s) + packed-index Z register
                    |
                 LUTI2/LUTI4
                    |
             one result Z register
```

Use this form for vector kernels that do not need  `ZT0` register and where multiple LUT are
required by the algorithm.

For example, the two-stage vector decode loop in section 5 reloads `ZT0` for its LUTI4 and
LUTI2 tables. With `FEAT_LUT`, load separate Z-register tables once before
the loop with the appropriate predicate. For the byte forms shown here, the
LUTI4 load needs 16 active lanes and the LUTI2 load needs 4.

```c
const svuint8_t luti4_table_z = svld1_u8(pg_1, luti4_table_storage);
const svuint8_t luti2_table_z = svld1_u8(pg_2, luti2_table_storage);

for (size_t i_k = 0; i_k < lhs_blocks; ++i_k) {
    svuint8_t packed_indices = svld1_u8(pg8, rhs_indices);
    rhs_indices += vl_b;
```
<del><code>    svldr_zt(0, zt0_luti4);</code></del>
```c
    svuint8_t codewords =
        svluti4_lane_u8(luti4_table_z, packed_indices, /* segment */ 0);
    ..
```
<del><code>    svldr_zt(0, zt0_luti2);</code></del>
```c
    svint8_t values = svreinterpret_s8_u8(
        svluti2_lane_u8(luti2_table_z, codewords, /* segment */ 0));
    // Consume values, then continue with the next input block.
    ..
}
```

Each Z-register-table LUTI instruction produces one destination Z register.
The table entries are the one or two SVL-sized Z register. The logical LUT is still the four entries for LUTI2
or sixteen entries for LUTI4.

## Place results with FEAT_SME2p1

The SME2 examples use consecutive destination registers. `FEAT_SME2p1` extends the `ZT0` SME2 forms with strided destination pairs and quads:

```text
Consecutive pair: { z0, z1 }
Strided pair:     { z0, z8 }

Consecutive quad: { z0, z1, z2, z3 }
Strided quad:     { z0, z4, z8, z12 }
```

For example, the following LUTI2 instruction writes a strided destination quad:
```asm
luti2 {z0.b, z4.b, z8.b, z12.b}, zt0, z1[0]
```

This form gives the register allocator more placement options. It does not change
the index width, table contents, or number of results produced by the
instruction.

## Check compiler feature macros

Use ACLE macros to guard the currently standardized intrinsic families:

```c
#if defined(__ARM_FEATURE_SME2)
// Original ZT0-based LUTI2 and LUTI4 forms.
#endif

#if defined(__ARM_FEATURE_LUT) && \
    (defined(__ARM_FEATURE_SVE2) || defined(__ARM_FEATURE_SME2))
// Z-register table forms.
#endif

#if defined(__ARM_FEATURE_SME2p1)
// SME2.1 forms, including strided destination groups.
#endif
```

These macros describe the compiler target. Runtime dispatch separately checks
that the operating system exposes the required feature on the current processor.

## What you've learned

You've identified the table source, execution state, output shape, and feature macro for the main LUTI variants. Use these distinctions when selecting an instruction form and when adding compile-time and runtime feature checks to production code.
