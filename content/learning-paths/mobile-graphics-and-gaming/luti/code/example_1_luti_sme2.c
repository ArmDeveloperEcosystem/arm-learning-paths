/*
 * SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * Learning Path exercise: from shifts and masks to SME2 LUTI2.
 *
 * Every implementation computes the same matrix multiplication:
 *   DST[M, N] = LHS[M, K] x RHS[K, N]
 *
 * The LHS contains signed 8-bit values. The RHS uses the prepared format expected
 * by this example: each byte contains four 2-bit lookup table indices.
 * Creating the prepared RHS format is outside the scope of the example.
 *
 * The example starts with the packed indices and compares how plain C and SME2 decode
 * them for matrix multiplication.
 *
 * The implementations progress from explicit operations to LUTI2:
 *   1. plain C: shift, mask, scalar lookup, then matmul.
 *   2. SME2: LUTI2 written with inline assembly.
 *
 * M and N depend on the streaming vector length (SVL). K is fixed at 4 so
 * that four signed 8-bit products accumulate into one signed 32-bit result.
 *
 * SVL is the streaming vector length in bits.
 * svcntb() returns the number of bytes in one streaming vector.
 * svcntw() returns the number of 32-bit words in one streaming vector.
 *
 *
 * The code is not restricted to 512-bit SVL. It derives these dimensions from
 * svcntw() at runtime and uses the same relationships for other valid SVLs.
 *
 * Vector terminology used below:
 * lane:    one element position in a vector. At 512-bit SVL, z0.b has 64
 *          byte lanes, z0.h has 32 halfword lanes, and z0.s has 16 word
 *          lanes. A lane number identifies one of those element positions.
 *
 * segment: a region of a packed LUTI source register containing enough
 *          indices to fill the requested destination vector group. A
 *          segment contains many indices and is not the same as one lane.
 */

// Arm SME intrinsics
#include <arm_sme.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#if !defined(__ARM_FEATURE_SME2)
#error "Compile with SME2 enabled, for example -march=armv9.2-a+sme2+nosve2+nosve"
#endif

enum {
    K = 4,
    LUT_INDICES_PER_BYTE = 4,
};

// Lookup table that expands 2-bit indices into signed 8-bit values.
// A 2-bit index selects only entries 0-3. The remaining entries are zero.
static const int8_t lut_i8_i2[16] = {
    -3, -1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
};

// Physical image for the fixed 64-byte ZT0 register. LUTI2 selects entries
// 0-3 and returns the low byte of each selected 32-bit entry.
static const int32_t zt0_table[16] __attribute__((aligned(64))) = {
    -3, -1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
};

// Return the number of 32-bit lanes in the current streaming vector.
// An SVL of 512 bits contains 16 32-bit lanes.
__arm_locally_streaming static size_t streaming_vector_words(void) {
    return svcntw();
}

// Use a fixed seed to keep the test repeatable.
static uint32_t next_random(uint32_t* state) {
    *state = *state * 1664525U + 1013904223U;
    return *state;
}

// Fill LHS (-8 to 7) and RHS_PACKED (0-255) with random data.
// Every uint8_t value is valid because it contains four 2-bit codes.
static void fill_random(int8_t* lhs, uint8_t* rhs_packed, size_t m, size_t n) {
    uint32_t random_state = 1;

    // Fill LHS with signed 8-bit values.
    for (size_t row = 0; row < m; ++row) {
        for (size_t k = 0; k < K; ++k) {
            const uint32_t random_value = next_random(&random_state);
            const uint8_t high_nibble = (uint8_t)((random_value >> 28) & 0xFU);
            lhs[row * K + k] = (int8_t)high_nibble - 8;
        }
    }

    // Fill each RHS column with four random 2-bit lookup table indices.
    for (size_t col = 0; col < n; ++col) {
        const uint32_t random_value = next_random(&random_state);
        rhs_packed[col] = (uint8_t)(random_value >> 24);
    }
}

/* --------------------------------------------------------------------------- */
/* 1. Plain C: Decode packed RHS indices with shifts and masks, then multiply. */
/* --------------------------------------------------------------------------- */

/*
 * Each packed RHS byte contains four 2-bit lookup table indices and represents one
 * output column:
 *
 *   bits [1:0]  bits [3:2]  bits [5:4]  bits [7:6]
 *    lut_idx 0   lut_idx 1   lut_idx 2   lut_idx 3
 *       k=0         k=1         k=2          k=3
 *
 * For example: 0xE4 = binary 11_10_01_00
 *
 * Reading from the least-significant bits gives lookup indices {0, 1, 2, 3}.
 * The lookup table converts these to {-3, -1, 1, 3}.
 *
 * Therefore: rhs_packed[col]
 *                 |
 *                 +-- bits [1:0] --> RHS[0, col]
 *                 +-- bits [3:2] --> RHS[1, col]
 *                 +-- bits [5:4] --> RHS[2, col]
 *                 +-- bits [7:6] --> RHS[3, col]
 *
 * For each output element, the function computes:
 *
 *   dst[row, col] = sum(k=0..3) LHS[row, k] * RHS[k, col]
 *
 * The function decodes each RHS value from rhs_packed[col] inside the K=4 dot
 * product.
 */

static void plain_c_matmul(
    const int8_t* lhs,
    const uint8_t* rhs_packed,
    int32_t* dst,
    size_t m,
    size_t n) {

    // Iterate over the output rows and columns.
    for (size_t row = 0; row < m; ++row) {
        for (size_t col = 0; col < n; ++col) {

            // Read the packed byte for this output column.
            const uint8_t packed_byte = rhs_packed[col];

            // Initialize the accumulator for this output element.
            int32_t acc_sum = 0;

            for (size_t k_idx = 0; k_idx < K; ++k_idx) {
                // Extract the 2-bit lookup table index for this k position.
                const unsigned bit_shift = 2U * (unsigned)k_idx;
                const uint8_t lut_idx = (uint8_t)((packed_byte >> bit_shift) & 0x3U);
                const int8_t expanded_byte = lut_i8_i2[lut_idx];

                // Widen the LHS and RHS values before multiplication.
                const int32_t lhs_value = (int32_t)lhs[row * K + k_idx];
                const int32_t expanded_rhs_value = (int32_t)expanded_byte;

                acc_sum += lhs_value * expanded_rhs_value;
            }

            // Store the accumulator in the corresponding output element.
            dst[row * n + col] = acc_sum;
        }
    }
}

/* ------------------------------------------------------------------------- */
/* 2. SME2: LUTI2 and SMOPA written with inline assembly.                    */
/* ------------------------------------------------------------------------- */

/*
 * LUTI2 expands one streaming vector of packed RHS indices into four vectors
 * of signed 8-bit values. Each SMOPA combines the LHS vector with one expanded
 * RHS vector and accumulates an M-by-M output panel in a ZA.S tile.
 *
 *   z0.b: M rows of LHS values, with K=4 values per row.
 *   z4.b: M columns of expanded RHS values for output panel 0.
 *   z5.b: M columns of expanded RHS values for output panel 1.
 *   z6.b: M columns of expanded RHS values for output panel 2.
 *   z7.b: M columns of expanded RHS values for output panel 3.
 */

__arm_new("za", "zt0") __arm_locally_streaming
static void luti2_sme2_asm_matmul(const int8_t *lhs,
                                  const uint8_t *rhs_packed,
                                  int32_t *dst, size_t m, size_t n) {
    __asm__ volatile(
        "ptrue p0.b\n"
        "ldr zt0, [%[table]]\n"     // Load the lookup table into ZT0
        "zero {za}\n"               // Clear all ZA accumulator state

        // Load one streaming vector from each input.
        "ld1b {z0.b}, p0/z, [%[lhs]]\n"
        "ld1b {z1.b}, p0/z, [%[rhs]]\n"

        // Expand one packed source vector into four signed 8-bit vectors.
        "luti2 {z4.b-z7.b}, zt0, z1[0]\n"

        // Accumulate four adjacent M-by-M output panels in ZA0-ZA3.
        "smopa za0.s, p0/m, p0/m, z0.b, z4.b\n"
        "smopa za1.s, p0/m, p0/m, z0.b, z5.b\n"
        "smopa za2.s, p0/m, p0/m, z0.b, z6.b\n"
        "smopa za3.s, p0/m, p0/m, z0.b, z7.b\n"
        :
        : [lhs] "r"(lhs),
          [rhs] "r"(rhs_packed),
          [table] "r"(zt0_table)
        : "p0", "z0", "z1", "z4", "z5", "z6", "z7",
          "za", "zt0", "memory");

    // Read four vectors from ZA and store them.
    for (uint32_t row = 0; row < m; ++row) {
        svint8x4_t read_tiles = svread_hor_za8_s8_vg4(0, 4 * row);
        svint32x4_t output_tiles = svreinterpret_s32_s8_x4(read_tiles);
        svst1_s32_x4(
            svptrue_c32(),
            dst + (size_t)row * n,
            output_tiles);
    }
}

/* ------------------------------------------------------------------------- */
/* Validation and output.                                                    */
/* ------------------------------------------------------------------------- */

static void require_matrices_equal(
    const char* name, const int32_t* expected, const int32_t* actual, size_t m, size_t n) {
    for (size_t row = 0; row < m; ++row) {
        for (size_t col = 0; col < n; ++col) {
            const size_t idx = row * n + col;

            if (actual[idx] != expected[idx]) {
                fprintf(
                    stderr, "FAIL: %s C[%zu, %zu]: expected %d, obtained %d\n", name, row, col, expected[idx],
                    actual[idx]);
                exit(EXIT_FAILURE);
            }
        }
    }
}

static void print_matrix_preview(const int32_t* matrix, size_t m, size_t n) {
    const size_t rows_to_print = m < 4 ? m : 4;
    const size_t cols_to_print = n < 8 ? n : 8;

    printf("\nC matrix preview (%zux%zu of %zux%zu):\n", rows_to_print, cols_to_print, m, n);

    for (size_t row = 0; row < rows_to_print; ++row) {
        for (size_t col = 0; col < cols_to_print; ++col) {
            printf("%6d", matrix[row * n + col]);
        }
        putchar('\n');
    }
}

static void print_binary_byte(uint8_t value) {
    for (int bit = 7; bit >= 0; --bit) {
        putchar(((value >> (unsigned)bit) & 1U) != 0U ? '1' : '0');
        if (bit == 6 || bit == 4 || bit == 2) {
            putchar(' ');
        }
    }
}

/* Print the logical 2-bit lookup table independently of any packed RHS byte. */
static void print_lookup_table(void) {
    puts("2-bit LUT mapping:");
    puts("bits  idx  signed  raw byte");

    for (uint8_t index = 0; index < LUT_INDICES_PER_BYTE; ++index) {
        const int8_t value = lut_i8_i2[index];

        printf(
            " %u%u   %u    %4d    0x%02X\n", (unsigned)((index >> 1) & 1U), (unsigned)(index & 1U),
            (unsigned)index, (int)value, (unsigned)(uint8_t)value);
    }
}

/* Show how the first packed RHS bytes become indices and signed 8-bit values. */
static void print_rhs_decoding_preview(const uint8_t* rhs_packed, size_t n) {
    const size_t cols_to_print = n < 8 ? n : 8;

    printf("\nRHS decoding preview (%zu of %zu columns):\n", cols_to_print, n);
    puts("  col byte   2-bit[k3k2k1k0]  lut_idx[k0k1k2k3]  signed values    raw bytes");

    for (size_t col = 0; col < cols_to_print; ++col) {
        const uint8_t packed_byte = rhs_packed[col];
        uint8_t lut_indices[K];
        int8_t s8_values[K];

        // Decode the four 2-bit indices once.
        for (size_t k = 0; k < K; ++k) {
            const unsigned shift = 2U * (unsigned)k;
            lut_indices[k] = (uint8_t)((packed_byte >> shift) & 0x3U);
            s8_values[k] = lut_i8_i2[lut_indices[k]];
        }

        printf("%4zu  0x%02X   ", col, (unsigned)packed_byte);
        print_binary_byte(packed_byte);

        printf("        [");
        for (size_t k = 0; k < K; ++k) {
            printf("%u%s", (unsigned)lut_indices[k], k + 1 == K ? "" : " ");
        }
        printf("]        [");

        for (size_t k = 0; k < K; ++k) {
            printf("%2d%s", (int)s8_values[k], k + 1 == K ? "" : " ");
        }
        printf("]    [");

        for (size_t k = 0; k < K; ++k) {
            printf("0x%02X%s", (unsigned)(uint8_t)s8_values[k], k + 1 == K ? "" : " ");
        }
        puts("]");
    }
}

int main(void) {
    const size_t m = streaming_vector_words();
    const size_t n = 4 * m;

    // Calculate storage sizes and allocate one result for each implementation.
    const size_t lhs_bytes = m * K * sizeof(int8_t);
    const size_t rhs_packed_bytes = n * sizeof(uint8_t);
    const size_t dst_bytes = m * n * sizeof(int32_t);

    // Allocate memory.
    int8_t* lhs = malloc(lhs_bytes);
    uint8_t* rhs_packed = malloc(rhs_packed_bytes);
    int32_t* plain_c_result = malloc(dst_bytes);
    int32_t* sme2_result = malloc(dst_bytes);

    // Fill the LHS and packed RHS with random values.
    fill_random(lhs, rhs_packed, m, n);

    // Use plain C as the reference result.
    plain_c_matmul(lhs, rhs_packed, plain_c_result, m, n);

    // Run the SME2 LUTI2 implementation.
    luti2_sme2_asm_matmul(lhs, rhs_packed, sme2_result, m, n);
    require_matrices_equal("LUTI2 + SMOPA", plain_c_result, sme2_result, m, n);

    // Print a small part of the matrix rather than the complete scalable result.
    printf("SVL = %zu bits; matrix shape M=%zu, K=%d, N=%zu\n", m * 32, m, K, n);
    print_lookup_table();
    print_rhs_decoding_preview(rhs_packed, n);
    print_matrix_preview(plain_c_result, m, n);

    puts("PASS: LUTI2 SME2 matches plain C matmul.");

    // Free memory.
    free(lhs);
    free(rhs_packed);
    free(plain_c_result);
    free(sme2_result);
    return EXIT_SUCCESS;
}
