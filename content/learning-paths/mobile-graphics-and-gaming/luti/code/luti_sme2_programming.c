/*
 * SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <arm_sme.h>
#include <assert.h>
#include <stddef.h>
#include <stdint.h>

// These examples assume that they run on an SME2-compatible system. They
// deliberately perform no runtime capability checks.
#if !defined(__ARM_FEATURE_SME2)
#error "Compile with SME2 enabled, for example -march=armv9.2-a+sme2+nosve2+nosve"
#endif

__arm_new("za", "zt0") __arm_locally_streaming void arm_lp_gemm_luti4(
    const float16_t* lhs, const uint8_t* rhs_indices, float32_t* out, const uint32_t* zt0_lut) {
    const uint32_t m = svcntw();  // Number of FP32 rows/columns in one ZA tile.

    assert(lhs != NULL);
    assert(rhs_indices != NULL);
    assert(out != NULL);
    assert(zt0_lut != NULL);

    /*                         LUTI4 decode
     * +------+---------------------------+----------------------------------------+
     * | Step | Decision                  | Choice                                 |
     * +------+---------------------------+----------------------------------------+
     * | 1    | Index and table width     | 4-bit index                            |
     * |      |                           | Low 16 bits of a 32-bit ZT0 register   |
     * |      |                           | entry                                  |
     * | 2    | Destination element type  | .H, because FMOPA consumes FP16        |
     * | 3    | Destination group         | x1 for rhs_0/rhs_1, then x2 for rhs_23 |
     * +------+---------------------------+----------------------------------------+
     */

    // Derive the source segments from the size of the source register.

    // Load the LUT.
    svldr_zt(0, zt0_lut);
    svzero_za();

    // Load the LHS.
    svbool_t pg = svptrue_b16();
    svfloat16_t lhs_ip = svld1_f16(pg, lhs);

    // Load one source register of packed indices. Each packed code is a
    // lookup-table index.
    svuint8_t s4_indices = svld1_u8(svptrue_b8(), rhs_indices);

    // Case 1: a single-register destination group uses one of four segments.

    //  Step 4 : Number of input segments for x1
    // --------------------------------------------
    //   One byte of indices produces two halfwords after the lookup.
    //   VL_b bytes of indices from a source register produce 2 * VL_h halfword
    //   elements, or 4 * VL_b bytes. Filling VL_b destination bytes therefore
    //   consumes VL_b / 4 source bytes: segments 0, 1, 2, and 3.

    //
    //                source Z register: packed indices
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
    //   VL_b bytes of indices from a source register produce 2 * VL_h halfword
    //   elements, or 4 * VL_b bytes. Filling 2 * VL_b destination bytes
    //   therefore consumes VL_b / 2 source bytes: segments 0 and 1.
    //
    //               source Z register: packed indices
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
    svfloat16x2_t rhs_23 = svluti4_lane_zt_f16_x2(0, s4_indices, /* segment */ 1);

    svmopa_za32_f16_m(0, pg, pg, lhs_ip, rhs_0);
    svmopa_za32_f16_m(1, pg, pg, lhs_ip, rhs_1);
    svmopa_za32_f16_m(2, pg, pg, lhs_ip, svget2_f16(rhs_23, 0));
    svmopa_za32_f16_m(3, pg, pg, lhs_ip, svget2_f16(rhs_23, 1));

    // Extract the data from the ZA tiles and store it.
    for (uint32_t i_m = 0; i_m < m; i_m += 1) {
        svfloat32x4_t out_row = svread_hor_za32_f32_vg4(0, 4 * i_m);
        svst1_f32_x4(svptrue_c32(), out + ((size_t)4 * i_m * m), out_row);
    }
}

// This example shows two-stage decoding of vector-quantized weights.
__arm_new("za", "zt0") __arm_locally_streaming void arm_lp_gemv_luti2_luti4(
    const int8_t* lhs, const uint8_t* rhs_indices, int32_t* out, const uint32_t* zt0_luti4, const uint32_t* zt0_luti2) {
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
    for (size_t i_k = 0; i_k < lhs_blocks; ++i_k) {
        // For SVL = 512 bits: VL_b = 64 bytes and VL_s = 16 words.

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

        // Two source registers provide the four packed 2-bit index vectors needed for the second stage.
        svuint8x2_t rhs_packed = svld1_u8_x2(pn8, rhs_indices);
        rhs_indices += 2 * vl_b;

        // Load LUT 1.
        svldr_zt(0, zt0_luti4);

        //  Step 4 : Number of input segments for x2
        // --------------------------------------------
        //   One packed byte contains two 4-bit indices and produces two bytes
        //   after the lookup. VL_b source bytes therefore produce 2 * VL_b
        //   destination bytes, filling the x2 destination group. This uses
        //   source segment 0.

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

        // Load LUT 2.
        svldr_zt(0, zt0_luti2);

        //  Step 4 : Number of input segments for x4
        // --------------------------------------------
        //   One packed byte contains four 2-bit indices and produces four bytes
        //   after the lookup. VL_b source bytes therefore produce 4 * VL_b
        //   destination bytes, filling the x4 destination group. This uses
        //   source segment 0.

        svint8x4_t rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_01, 0), 0));

        // Process K values 0 to 3 for the first VL_s N values.
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* lane */ 0);

        rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_01, 1), 0));

        // Process K values 4 to 7 for the next VL_s N values.
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* lane */ 1);

        rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_23, 0), 0));

        // Process K values 8 to 11 for the next VL_s N values.
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* lane */ 2);

        rhs_unpacked = svreinterpret_s8_u8_x4(svluti2_lane_zt_u8_x4(0, svget2_u8(patterns_23, 1), 0));

        // Process K values 12 to 15 for the final VL_s N values.
        svdot_lane_za32_s8_vg1x4(0, rhs_unpacked, lhs_ip, /* lane */ 3);

        // Total processed: 16 K values and 4 * VL_s N values.
    }

    svint32x4_t result = svread_za32_s32_vg1x4(0);
    svst1_s32_x4(svptrue_c32(), out, result);
}