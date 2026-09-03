---
title: Program SME2 LUTI examples
description: Select LUTI destination groups and source segments for FP16 FMOPA and two-stage SDOT kernels.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The examples in `luti_sme2_programming.c` show a recipe-based approach to programming
with LUTI instructions.

The examples cover the following combinations and have their base
in KleidiAI's matrix multiplication micro-kernels:

| Example | Decode | Arithmetic | Main concept |
|---|---|---|---|
| One | LUTI4 to `float16` | GEMM using FMOPA | Use LUTI and source segments |
| Two | LUTI4, then LUTI2 to `int8` | GEMV using SDOT | Use multiple LUTs and source segments |

## Run the learning tests

From the `code` directory, run:

```bash
./sme2_luti --learning
```

In the output, `SVL` is the streaming vector length in bits. `VL_b` is the
number of byte elements (`SVL / 8`), `VL_h` is the number of half-word
elements (`SVL / 16`), and `VL_s` is the number of 32-bit word elements
(`SVL / 32`).

With a 512-bit SVL, the expected output is:
```output
FP16 LUTI4 + FMOPA test (M = VL_s, K = 2, N = 4 * VL_s)
PASS
LUTI4 -> LUTI2 -> SDOT test (M = 1, K = N = VL_b)
PASS
```

Each `PASS` confirms that the kernel matches the reference result.

## The four-step LUTI recipe

For every LUTI call, answer these questions.

| Step | Decision | Result |
|---|---|---|
| 1 | What are the packed-index and table-element widths? | Choose the LUTI form and ZT0 register table-entry width. |
| 2 | What element type does the destination Z register require? | Select `.B`, `.H`, or `.S`. |
| 3 | How many destination Z registers do you need the lookup to fill? | Choose x1, x2, or x4 to match the target operation. |
| 4 | How much of the source Z register fills the destination register group? | Source-register segment |

A *source segment* is the portion of one packed source Z register that fills the chosen destination group.</br>
Its selector is relative to the destination-group size.</br>
The examples use several source-segment cases to help you develop intuition for selecting the correct segment.


## Example 1: LUTI4 for FP16 GEMM using FMOPA

This example is a focused extraction from KleidiAI's
[FP16 LUTI4 FMOPA micro-kernel](https://gitlab.arm.com/kleidi/kleidiai/-/blob/v1.30.0/kai/ukernels/matmul/matmul_clamp_f32_f16p_qsi4c32p/kai_matmul_clamp_f32_f16p1vlx2_qsi4c32p4vlx2_1vlx4vl_sme2_mopa.c).
The example uses 4-bit codes as indices that map to `float16` values.
This example shows how the source-index segment is interpreted relative to the destination-group size.
This section uses generic SVL terminology to explain the example.

```c
__arm_new("za", "zt0") __arm_locally_streaming void arm_lp_gemm_luti4(
    const float16_t* lhs, const uint8_t* rhs_indices, float32_t* out, const uint32_t* zt0_lut) {
    uint32_t m = svcntw();  // Number of FP32 rows/columns in one ZA tile.

    /*                         LUTI4 decode
     * +------+---------------------------+----------------------------------------+
     * | Step | Decision                  | Choice                                 |
     * +------+---------------------------+----------------------------------------+
     * | 1    | Index and table width     | 4-bit index                            |
     * |      |                           | 16-bit ZT0 LUT register element        |
     * | 2    | Destination element type  | .H, because FMOPA consumes FP16        |
     * | 3    | Destination group         | x1 for rhs_0/rhs_1, then x2 for rhs_23 |
     * +------+---------------------------+----------------------------------------+
     */

    // There are more than one ways to reason about the number of input segment. Here, we go
    // about it from the source register as the reference point.

    // Load the LUT
    svldr_zt(0, zt0_lut);
    svzero_za();

    // Load the LHS
    svbool_t pg = svptrue_b16();
    svfloat16_t lhs_ip = svld1_f16(pg, lhs);

    // Load one source register of indices
    svuint8_t s4_indices = svld1_u8(svptrue_b8(), rhs_indices);

    // Case 1: a single-register destination group uses one of four segments.

    //  Step 4 : Number of input segments for x1
    // --------------------------------------------
    //   one byte of index produces two half words after the look up.
    //   VL_b bytes of indices from a source register produces 2 * VL_h half-word elements or
    //                                                          4 * VL_b bytes.
    //   In other words, to fill VL_b bytes of destination, VL_b / 4 bytes
    //   is needed =>  4 input segments with values 0, 1, 2 and 3

    //
    //                source z register: Packed indices
    //   +-------------+-------------+-------------+-------------+
    //   | segment [3] | segment [2] | segment [1] | segment [0] |
    //   +-------------+-------------+-------------+-------------+
    //                                                         |
    //                                                         | LUTI4 .H, segment [0]
    //                                                         v
    //                       destination z register with F16 elements
    //              +----------------------------------------------------+
    //              |                  VL_h elements                     |
    //              +----------------------------------------------------+

    // Unpredicated LUTI read.
    svfloat16_t rhs_0 = svluti4_lane_zt_f16(0, s4_indices, /* segment */ 0);
    svfloat16_t rhs_1 = svluti4_lane_zt_f16(0, s4_indices, /* segment */ 1);

    // Case 2: a two-register destination group using one of two segments.

    //  Step 4 : Number of input segments for x2
    // --------------------------------------------
    //   VL_b bytes of indices from a source register produces 2 * VL_h half-word elements or
    //                                                          4 * VL_b bytes.
    //   In other words, to fill 2 * VL_b bytes of destination, VL_b / 2 bytes
    //   is needed =>  2 segments with values 0 and 1
    //
    //               source z register: packed indices
    //   +---------------------------+---------------------------+
    //   |        segment [1]        |        segment [0]        |
    //   +---------------------------+---------------------------+
    //                      |
    //                      | LUTI4 .H, segment [1]
    //                      v
    //               two-register destination z register group
    //              +---------------------+---------------------+
    //              |  destination 1      |   destination 0     |
    //              |    VL_h elements    |   VL_h elements     |
    //              +---------------------+---------------------+
    svfloat16x2_t rhs_23 = svluti4_lane_zt_f16_x2(0, s4_indices, /* Segment */ 1);

    svmopa_za32_f16_m(0, pg, pg, lhs_ip, rhs_0);
    svmopa_za32_f16_m(1, pg, pg, lhs_ip, rhs_1);
    svmopa_za32_f16_m(2, pg, pg, lhs_ip, svget2_f16(rhs_23, 0));
    svmopa_za32_f16_m(3, pg, pg, lhs_ip, svget2_f16(rhs_23, 1));

    // Extract out the data from ZA tiles and store
    for (uint32_t i_m = 0; i_m < m; i_m += 1) {
        svfloat32x4_t out_row = svread_hor_za32_f32_vg4(0, 4 * i_m);
        svst1_f32_x4(svptrue_c32(), out + ((size_t)4 * i_m * m), out_row);
    }
}
```
## Two-stage LUTI4 and LUTI2 for GEMV using SDOT

The SDOT micro-kernel and block size are similar to the KleidiAI's
[SDOT micro-kernel](https://gitlab.arm.com/kleidi/kleidiai/-/blob/v1.30.0/kai/ukernels/matmul/matmul_clamp_f32_qai8dxp_qsi4cxp/kai_matmul_clamp_f32_qai8dxp1x4_qsi4cxp4vlx4_1x4vl_sme2_sdot.c),
with two LUTs added to implement a two-stage decode of vector-quantized
weights.

### Define the terms

In this context, vector quantization uses a 4-bit code as an index to select an 8-bit codeword that represents a four-weight pattern. The sixteen `ZT0` entries represent sixteen unique patterns.

The two-stage decode uses LUTI4 to select an 8-bit codeword, then LUTI2 to map the codeword to four 8-bit numerical values.

This encoding reduces the bytes required to store weights.
```text
                packed 4-bit pattern ID
             +-----------------------------+
             |          index[3:0]          |
             +-----------------------------+
                           |
                           | LUTI4: select one 8-bit codeword from ZT0
                           v
                packed 8-bit data with 2-bit symbols
             +--------+--------+--------+--------+
             | sym[3] | sym[2] | sym[1] | sym[0] |
             |  2 bits|  2 bits|  2 bits|  2 bits|
             +--------+--------+--------+--------+
                 |        |        |        |
                 +--------+--------+--------+
                           | LUTI2: expand each 2-bit symbol from ZT0
                           v
             +--------+--------+--------+--------+
             | weight3| weight2| weight1| weight0|
             |  int8  |  int8  |  int8  |  int8  |
             +--------+--------+--------+--------+

```

```c
__arm_new("za", "zt0") __arm_locally_streaming void arm_lp_gemv_luti2_luti4(
    const int8_t* lhs, const uint8_t* rhs_indices, int32_t* out,
    const uint32_t* zt0_luti4, const uint32_t* zt0_luti2) {
    const size_t vl_b = svcntb();
    const size_t lhs_blocks = vl_b / 16;
    const svbool_t pg8 = svptrue_b8();
    const svcount_t pn8 = svptrue_c8();

    assert(lhs != NULL);
    assert(rhs_indices != NULL);
    assert(out != NULL);
    assert(zt0_luti4 != NULL);
    assert(zt0_luti2 != NULL);
    assert(vl_b % 16 == 0);

    svzero_za();
    for (size_t i_k = 0; i_k < lhs_blocks; i_k++) {
        // For a SVL of 512 bits: SVL_b = 64 bytes and SVL_s = 16 words.

        // Replicated read of one 16-byte LHS block for SDOT lanes.
        svint8_t lhs_ip = svld1rq_s8(pg8, lhs);
        lhs += 16;

        /*                      LUTI4 decode (first stage)
         * +------+---------------------------+----------------------------------------+
         * | Step | Decision                  | Choice                                 |
         * +------+---------------------------+----------------------------------------+
         * | 1    | Index and table width     | 4-bit index                            |
         * |      |                           | 8-bit ZT0 LUT register element         |
         * | 2    | Destination element type  | NA. Second decode stage addresses this |
         * | 3    | Destination group         | x2 for patterns_01 and patterns_23     |
         * +------+---------------------------+----------------------------------------+
         */

        // Two source registers provide the four packed 2-bit vectors needed for the second stage.
        svuint8x2_t rhs_packed = svld1_u8_x2(pn8, rhs_indices);
        rhs_indices += 2 * vl_b;

        // Load LUT 1
        svldr_zt(0, zt0_luti4);

        //  Step 4 : Number of input segments for x2
        // --------------------------------------------
        //   One packed byte contains two 4-bit indices and produces two bytes
        //   after the lookup. SVL_b bytes of indices from one source register
        //   therefore produce 2 * SVL_b bytes, filling the x2 destination
        //   group. This uses one input segment with value 0.

        svuint8x2_t patterns_01 = svluti4_lane_zt_u8_x2(0, svget2_u8(rhs_packed, 0), 0);
        svuint8x2_t patterns_23 = svluti4_lane_zt_u8_x2(0, svget2_u8(rhs_packed, 1), 0);

        /*                      LUTI2 decode (second stage)
         * +------+---------------------------+----------------------------------------+
         * | Step | Decision                  | Choice                                 |
         * +------+---------------------------+----------------------------------------+
         * | 1    | Index and table width     | 2-bit index                            |
         * |      |                           | 8-bit ZT0 LUT register element         |
         * | 2    | Destination element type  | .B, SDOT consumes int8                 |
         * | 3    | Destination group         | x4 for rhs_unpacked                    |
         * +------+---------------------------+----------------------------------------+
         */

        // Load LUT 2
        svldr_zt(0, zt0_luti2);

        //  Step 4 : Number of input segments for x4
        // --------------------------------------------
        //   One packed byte contains four 2-bit indices and produces four
        //   bytes after the lookup. SVL_b bytes of indices from one source
        //   register therefore produce 4 * SVL_b bytes, filling the x4
        //   destination group. This uses one input segment with value 0.

        svint8x4_t rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_01, 0), 0));

        // Process k index of 0 to 3.
        // Process 1VL_s of N
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* Lane */ 0);

        rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_01, 1), 0));

        // Process k index of 4 to 7
        // process next 1VL_s of N
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* Lane */ 1);

        rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_23, 0), 0));

        // Process k index of 8 to 11
        // Process next 1VL_s of N
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* Lane */ 2);

        rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_23, 1), 0));

        // Process k index of 12 to 15
        // Process next 1VL_s or N
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* Lane */ 3);

        // Total processed: 16 K-values, 4VL_s N values
    }

    svint32x4_t result = svread_za32_s32_vg1x4(0);
    svst1_s32_x4(svptrue_c32(), out, result);
}
```

## What you've learned in this section

You've seen how destination-group size determines the meaning of a source
segment, and how the same four-step method applies once or repeatedly in a
multi-stage decode.