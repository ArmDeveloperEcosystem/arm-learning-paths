/*
 * SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <arm_sme.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// This example assumes it runs on an SME2-compatible system. It deliberately
// performs no runtime capability check.
#if !defined(__ARM_FEATURE_SME2)
#error "Compile with SME2 enabled, for example -march=armv9.2-a+sme2+nosve2+nosve"
#endif

__arm_new("za", "zt0") __arm_locally_streaming void arm_lp_gemm_luti4(
    const float16_t* lhs, const uint8_t* rhs_indices, float32_t* out, const uint32_t* zt0_lut);

__arm_new("za", "zt0") __arm_locally_streaming void arm_lp_gemv_luti2_luti4(
    const int8_t* lhs, const uint8_t* rhs_indices, int32_t* out, const uint32_t* zt0_luti4, const uint32_t* zt0_luti2);

int ex1_luti_test(void);

__arm_locally_streaming static size_t get_streaming_vector_bytes(void) {
    return svcntb();
}

__arm_locally_streaming static uint32_t get_streaming_vl_words(void) {
    return svcntw();
}

static int compare_outputs_i32(
    const int32_t* actual, const int32_t* expected, size_t rows, size_t columns, const char* test_name) {
    for (size_t row = 0; row < rows; ++row)
        for (size_t column = 0; column < columns; ++column) {
            size_t index = row * columns + column;
            if (actual[index] != expected[index]) {
                fprintf(
                    stderr, "%s: FAIL at row %zu, column %zu: got %d, expected %d\n", test_name, row, column,
                    actual[index], expected[index]);
                return 1;
            }
        }
    return 0;
}

/* -------------------------------------------------------------------------- */
/* Reference matrix multiplication                                            */
/* -------------------------------------------------------------------------- */

// Fixed GEMV shape: M = 1 and K = N = VL_b. The RHS is packed as
// (VL_b / 4) rows of 4 * VL_b bytes, one row for each four-element K group.
static void arm_lp_gemv_luti2_luti4_ref(const int8_t* lhs, const int8_t* rhs, int32_t* out) {
    const size_t vl_b = get_streaming_vector_bytes();

    for (size_t n = 0; n < vl_b; ++n) {
        int32_t sum = 0;
        for (size_t k = 0; k < vl_b; ++k) sum += (int32_t)lhs[k] * (int32_t)rhs[k * vl_b + n];
        out[n] = sum;
    }
}

// SME2 SDOT reference implementation using already-unpacked RHS weights.
__arm_new("za") __arm_locally_streaming static void arm_lp_matmul_s8_s8_dotprod(
    const int8_t* lhs, const int8_t* rhs_packed, int32_t* out) {
    const size_t vl_b = svcntb();
    const size_t lhs_blocks = vl_b / 16;  // 16 bytes in a 128-bit LHS block.
    const svbool_t pg8 = svptrue_b8();
    const svcount_t pn8 = svptrue_c8();

    svzero_za();
    for (size_t i_k = 0; i_k < lhs_blocks; ++i_k) {
        svint8_t lhs_vec = svld1rq_s8(pg8, lhs);
        lhs += 16;

        svint8x4_t rhs_vec = svld1_s8_x4(pn8, rhs_packed);
        rhs_packed += 4 * vl_b;
        svdot_lane_za32_s8_vg1x4(0, rhs_vec, lhs_vec, 0);

        rhs_vec = svld1_s8_x4(pn8, rhs_packed);
        rhs_packed += 4 * vl_b;
        svdot_lane_za32_s8_vg1x4(0, rhs_vec, lhs_vec, 1);

        rhs_vec = svld1_s8_x4(pn8, rhs_packed);
        rhs_packed += 4 * vl_b;
        svdot_lane_za32_s8_vg1x4(0, rhs_vec, lhs_vec, 2);

        rhs_vec = svld1_s8_x4(pn8, rhs_packed);
        rhs_packed += 4 * vl_b;
        svdot_lane_za32_s8_vg1x4(0, rhs_vec, lhs_vec, 3);
    }

    svint32x4_t result = svread_za32_s32_vg1x4(0);
    svst1_s32_x4(svptrue_c32(), out, result);
}

/* -------------------------------------------------------------------------- */
/* Reference packing                                                          */
/* -------------------------------------------------------------------------- */

// Pack dense int8 RHS weights for the SME2 SDOT reference implementation.
__arm_locally_streaming static void arm_lp_matmul_s8_s8_dotprod_rhs_pack_ref(const int8_t* rhs, int8_t* rhs_packed) {
    const size_t kr = 4;
    const size_t vl_b = get_streaming_vector_bytes();
    const size_t columns_per_vector = svcntw();

    for (size_t k_group = 0; k_group < vl_b / kr; ++k_group)
        for (size_t vector = 0; vector < 4; ++vector) {
            int8_t* packed_vector = rhs_packed + (k_group * 4 + vector) * vl_b;

            for (size_t column = 0; column < columns_per_vector; ++column)
                for (size_t k_lane = 0; k_lane < kr; ++k_lane)
                    packed_vector[column * kr + k_lane] =
                        rhs[(k_group * kr + k_lane) * vl_b + vector * columns_per_vector + column];
        }
}

// Pack a dense M=1, K=N=VL_b RHS matrix for the LUTI4 -> LUTI2 SDOT kernel.
// Return zero on success, or nonzero when a weight or four-weight pattern is
// not representable by the supplied table register contents.
__arm_locally_streaming static int arm_lp_gemv_luti2_luti4_rhs_pack_ref(
    const int8_t* rhs, uint8_t* rhs_indices, const uint32_t* zt0_luti4, const uint32_t* zt0_luti2) {
    const size_t vl_b = svcntb();
    const size_t packed_bytes = vl_b * vl_b / 8;

    if (rhs == NULL || rhs_indices == NULL || zt0_luti4 == NULL || zt0_luti2 == NULL || vl_b % 16 != 0) return 1;

    for (size_t offset = 0; offset < packed_bytes; offset += vl_b)
        svst1_u8(svptrue_b8(), rhs_indices + offset, svdup_n_u8(0));
    for (size_t k_group = 0; k_group < vl_b / 4; ++k_group) {
        const size_t block = k_group / 4;
        const size_t lane = k_group % 4;
        const size_t source_vector = 2 * block + lane / 2;
        const size_t source_segment = lane % 2;
        const size_t packed_base = source_vector * vl_b + source_segment * (vl_b / 2);

        for (size_t column = 0; column < vl_b; ++column) {
            uint8_t packed_levels = 0;
            for (size_t k_lane = 0; k_lane < 4; ++k_lane) {
                const int8_t weight = rhs[(4 * k_group + k_lane) * vl_b + column];
                size_t level_code;

                for (level_code = 0; level_code < 4; ++level_code)
                    if (weight == (int8_t)zt0_luti2[level_code]) break;
                if (level_code == 4) return 1;

                packed_levels |= (uint8_t)(level_code << (2 * k_lane));
            }

            size_t pattern_id;
            for (pattern_id = 0; pattern_id < 16; ++pattern_id)
                if (packed_levels == (uint8_t)zt0_luti4[pattern_id]) break;
            if (pattern_id == 16) return 1;

            rhs_indices[packed_base + column / 2] |= (uint8_t)(pattern_id << (4 * (column & 1)));
        }
    }

    return 0;
}

static int run_arm_lp_gemm_luti4_test(void) {
    enum { K = 2 };
    uint32_t lut[16];
    uint32_t m = get_streaming_vl_words();
    uint32_t n = 4 * m;
    size_t vl_bytes = (size_t)4 * m;
    float16_t* lhs = malloc((size_t)K * m * sizeof(*lhs));
    uint8_t* rhs_indices = calloc(vl_bytes, sizeof(*rhs_indices));
    float32_t* actual = malloc((size_t)m * n * sizeof(*actual));
    int result = 1;

    if (lhs == NULL || rhs_indices == NULL || actual == NULL) {
        fputs("failed to allocate FP16 LUTI4 test data\n", stderr);
        goto cleanup;
    }

    // LUTI4 .H reads the low 16 bits of each 32-bit ZT0 entry. 0x3c00 is 1.0
    // in the IEEE 754 binary16 format.
    for (uint32_t entry = 0; entry < 16; ++entry) lut[entry] = 0x00003c00U;
    for (uint32_t element = 0; element < K * m; ++element) lhs[element] = (float16_t)1.0F;

    arm_lp_gemm_luti4(lhs, rhs_indices, actual, lut);
    puts("FP16 LUTI4 + FMOPA test (M = VL_s, K = 2, N = 4 * VL_s)");

    result = 0;
    for (uint32_t row = 0; row < m; ++row)
        for (uint32_t column = 0; column < n; ++column) {
            size_t index = (size_t)row * n + column;
            if (actual[index] != (float32_t)K) {
                fprintf(
                    stderr, "FAIL: row %u, column %u: got %g, expected %d\n", row, column, (double)actual[index], K);
                result = 1;
                goto cleanup;
            }
        }
    puts("PASS");

cleanup:
    free(lhs);
    free(rhs_indices);
    free(actual);
    return result;
}

static int run_arm_lp_gemv_luti2_luti4_test(void) {
    const size_t vl_b = get_streaming_vector_bytes();
    const size_t matrix_bytes = vl_b * vl_b;
    const size_t luti_packed_bytes = matrix_bytes / 8;
    uint32_t luti4_table[16];
    uint32_t luti2_table[16] = {0};
    int8_t levels[4] = {-3, -1, 1, 3};
    uint8_t codewords[16] = {
        0x00, 0x01, 0x12, 0x23, 0x34, 0x45, 0x56, 0x67, 0x78, 0x89, 0x9a, 0xab, 0xbc, 0xcd, 0xde, 0xe7,
    };
    int8_t* lhs = malloc(vl_b * sizeof(*lhs));
    int8_t* rhs = malloc(matrix_bytes * sizeof(*rhs));
    int8_t* rhs_sdot_packed = malloc(matrix_bytes * sizeof(*rhs_sdot_packed));
    uint8_t* rhs_luti_packed = calloc(luti_packed_bytes, sizeof(*rhs_luti_packed));
    int32_t* reference = malloc(vl_b * sizeof(*reference));
    int32_t* sdot_actual = malloc(vl_b * sizeof(*sdot_actual));
    int32_t* luti_actual = malloc(vl_b * sizeof(*luti_actual));
    int result = 1;

    if (lhs == NULL || rhs == NULL || rhs_sdot_packed == NULL || rhs_luti_packed == NULL || reference == NULL ||
        sdot_actual == NULL || luti_actual == NULL) {
        fputs("failed to allocate LUTI4 -> LUTI2 -> SDOT test data\n", stderr);
        goto cleanup;
    }
    if (vl_b % 16 != 0) {
        fputs("LUTI4 -> LUTI2 -> SDOT requires VL_b divisible by 16\n", stderr);
        goto cleanup;
    }

    for (uint32_t entry = 0; entry < 16; ++entry) luti4_table[entry] = (uint8_t)codewords[entry] * 0x01010101U;
    for (uint32_t entry = 0; entry < 4; ++entry) luti2_table[entry] = (uint8_t)levels[entry] * 0x01010101U;

    for (size_t k = 0; k < vl_b; ++k) lhs[k] = (int8_t)(((5 * k + 3) % 9) - 4);
    for (size_t k_group = 0; k_group < vl_b / 4; ++k_group)
        for (size_t column = 0; column < vl_b; ++column) {
            uint8_t id = (uint8_t)((5 * k_group + 3 * column + 1) & 0xf);
            uint8_t packed_levels = codewords[id];
            for (size_t k_lane = 0; k_lane < 4; ++k_lane) {
                uint8_t level_code = (packed_levels >> (2 * k_lane)) & 0x3;
                rhs[(4 * k_group + k_lane) * vl_b + column] = levels[level_code];
            }
        }

    arm_lp_matmul_s8_s8_dotprod_rhs_pack_ref(rhs, rhs_sdot_packed);
    if (arm_lp_gemv_luti2_luti4_rhs_pack_ref(rhs, rhs_luti_packed, luti4_table, luti2_table) != 0) {
        fputs("failed to pack representable RHS for LUTI4 -> LUTI2 -> SDOT\n", stderr);
        goto cleanup;
    }

    arm_lp_gemv_luti2_luti4_ref(lhs, rhs, reference);
    arm_lp_matmul_s8_s8_dotprod(lhs, rhs_sdot_packed, sdot_actual);
    arm_lp_gemv_luti2_luti4(lhs, rhs_luti_packed, luti_actual, luti4_table, luti2_table);
    if (compare_outputs_i32(sdot_actual, reference, 1, vl_b, "arm_lp_matmul_s8_s8_dotprod") != 0 ||
        compare_outputs_i32(luti_actual, reference, 1, vl_b, "arm_lp_gemv_luti2_luti4") != 0)
        goto cleanup;

    const int8_t saved_weight = rhs[0];
    rhs[0] = 99;
    if (arm_lp_gemv_luti2_luti4_rhs_pack_ref(rhs, rhs_luti_packed, luti4_table, luti2_table) == 0) {
        fputs("LUTI packer accepted an unsupported scalar level\n", stderr);
        goto cleanup;
    }
    rhs[0] = saved_weight;

    for (size_t k_lane = 0; k_lane < 4; ++k_lane) rhs[k_lane * vl_b] = levels[3];
    if (arm_lp_gemv_luti2_luti4_rhs_pack_ref(rhs, rhs_luti_packed, luti4_table, luti2_table) == 0) {
        fputs("LUTI packer accepted an unsupported four-weight pattern\n", stderr);
        goto cleanup;
    }

    puts("LUTI4 -> LUTI2 -> SDOT test (M = 1, K = N = VL_b)");
    puts("PASS");
    result = 0;

cleanup:
    free(lhs);
    free(rhs);
    free(rhs_sdot_packed);
    free(rhs_luti_packed);
    free(reference);
    free(sdot_actual);
    free(luti_actual);
    return result;
}

int main(int argc, char** argv) {
    if (argc == 1) return ex1_luti_test();

    if (argc != 2 || strcmp(argv[1], "--learning") != 0) {
        fprintf(stderr, "Usage: %s [--learning]\n", argv[0]);
        return 2;
    }

    if (run_arm_lp_gemm_luti4_test() != 0) return 1;
    if (run_arm_lp_gemv_luti2_luti4_test() != 0) return 1;
    return 0;
}