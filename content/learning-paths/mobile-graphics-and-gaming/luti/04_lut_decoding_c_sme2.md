---
title: Compare plain C decoding with SME2 LUTI2
description: Compare low-bit matrix multiplication in plain C with an SME2 implementation that uses LUTI2 and SMOPA.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare plain C and SME2

In this section, you compare two ways to expand packed 2-bit right-hand side
(RHS) values for signed 8-bit matrix multiplication.

The plain C reference extracts each index with a shift and mask. It then uses
the index to select a signed 8-bit value from the lookup table. The SME2
implementation uses `LUTI2` to expand one packed vector and `SMOPA` to
accumulate four adjacent output panels in `ZA0`-`ZA3`.

Both implementations use the same matrix dimensions, packed RHS bytes, and
lookup table. The program compares their output matrices element by element.

## Set up the example

Open `code/example_1_luti_sme2.c`. The file contains both implementations and
the validation code. The following snippets highlight the sections to inspect
before you build the complete example.

### Inspect the matrix shape

The example derives its matrix dimensions from the streaming vector length (SVL).
SVL is the number of bits in one streaming vector.

Use these relationships when reasoning about the dimensions:

- `svcntb()` returns the number of bytes in one streaming vector.
- `svcntw()` returns the number of 32-bit words in one streaming vector.
- One 32-bit word contains four bytes, so `svcntb() = 4 * svcntw()`

The example uses those values to define the matrix shape:

```c
const size_t m = streaming_vector_words();  // svcntw()
const size_t n = 4 * m;                     // svcntb()
```

Both implementations calculate:

```text
DST[M, N] = LHS[M, K] x RHS[K, N]
```

`M` is the number of 32-bit words for one streaming vector: `M = svcntw()`.
`N` is the number of bytes in one streaming vector: `N = svcntb()`, which is equivalent to `N = 4 * M`. 

The example fixes `K = 4` for two related reasons. First, LUTI2 uses 2-bit lookup indices, so one packed RHS byte contains four 2-bit groups.
Those four groups provide the four RHS values along the K dimension for one output column.
Second, with `M = svcntw()`, setting `K = 4` makes the `M * K` signed 8-bit LHS block occupy exactly one streaming vector.

For an SVL of 512 bits:

- M = svcntw() = 512 / 32 = 16
- N = svcntb() = 512 / 8 = 64
- K = 4

| Block | Calculation | Size |
|---|---|---|
| LHS | `M * K = 16 * 4` | 64 signed 8-bit values |
| Logical RHS | `K * N = 4 * 64` | 256 2-bit codes |
| Packed RHS | `256 * 2 bits = 512 bits` | 64 bytes |
| DST | `M * N = 16 * 64` | 1024 signed 32-bit values |

The complete LHS block and packed RHS block each fit in one streaming Z register.

### Low-bit packed format

For each output column, the packed RHS stores the four `K` dimension RHS values in one byte: rhs_packed[col].
LUTI2 uses 2-bit indices, so the byte is split into four 2-bit groups.
Each group selects the lookup-table value for one RHS element, RHS[k, col]. 

```text
rhs_packed[col]
bits         [7:6] |    [5:4] |    [3:2] |    [1:0]
RHS:      [k3,col] | [k2,col] | [k1,col] | [0k,col]
```

The example reads the 2-bit groups from the least-significant bits first. For example:

```text
packed byte:  0xE4 = 11_10_01_00
                      |  |  |  |
                      k3 k2 k1 k0

lookup indices read in k order: 0, 1, 2, 3
```

The example uses these constants in both implementations:

```c
enum {
    K = 4,
    LUT_INDICES_PER_BYTE = 4,
};
```

### Inspect the lookup table

The example uses this mapping:

```text
2-bit code  index  signed 8-bit value  raw byte
    00         0            -3          0xFD
    01         1            -1          0xFF
    10         2             1          0x01
    11         3             3          0x03
```

```c
static const int8_t lut_i8_i2[16] = {
    -3, -1, 1, 3,
     0,  0, 0, 0,
     0,  0, 0, 0,
     0,  0, 0, 0,
};
```

The 2-bit indices select only entries 0-3. Entries 4-15 remain zero.

## Inspect the plain C reference

The plain C reference calculates one output element at a time. It reads one
packed RHS byte for each column. For each `k` position, the inner loop shifts
the corresponding 2-bit field into bits `[1:0]`, applies the `0x03` mask,
and uses the result to index `lut_i8_i2`.

```c
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
```

For each output element, the loop implements:

```text
DST[row, col] = sum(k=0..3) LHS[row, k] * RHS[k, col]
```

The program uses this implementation as the correctness reference. The
innermost loop shifts, masks, looks up, and multiplies each value.

## Inspect the SME2 LUTI2 implementation

### Step 1: Store the same lookup values in `ZT0`

The SME2 path uses the same logical lookup values. `ZT0` has a fixed physical
layout of sixteen 32-bit entries (64 bytes).

```c
static const int32_t zt0_table[16] __attribute__((aligned(64))) = {
    -3, -1, 1, 3,
     0,  0, 0, 0,
     0,  0, 0, 0,
     0,  0, 0, 0,
};
```

`LUTI2 .B` selects entries 0-3 and copies the low byte of each selected
32-bit entry. The low bytes of `ZT0` entries 0-3 therefore match the bit
patterns in the plain C table for the four signed 8-bit values.

### Step 2: Declare a locally streaming SME function

```c
__arm_new("za", "zt0") __arm_locally_streaming
```

These attributes tell the compiler to run the function body in streaming
mode and provide new `ZA` and `ZT0` state for the function.

### Step 3: Follow the SME2 compute path

Review the SME2 implementation below. Inline assembly loads `ZT0`, expands
the packed RHS, and accumulates four output panels. ACLE intrinsics read `ZA`
and store the output matrix.

```c
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
```

The inline assembly loads the lookup table into `ZT0` and loads one vector
from each input. `LUTI2` expands the packed RHS into four vectors. Four
`SMOPA` instructions accumulate those vectors into `ZA0`-`ZA3`.

The output loop reads one horizontal row across `ZA0`-`ZA3`. It
reinterprets the returned bytes as four vectors of `int32_t` accumulators and
stores them as one contiguous output row.

`LUTI2` does not perform the multiplication. The packed RHS stays compact
until the matrix kernel needs it. The expanded values then pass directly from
Z registers to SME2 matrix instructions.

To see the same instruction pattern in production code, inspect the
[`qai8dxp_qsu2csp` Arm® KleidiAI™ micro-kernel source](https://gitlab.arm.com/kleidi/kleidiai/-/blob/v1.30.0/kai/ukernels/matmul/matmul_clamp_f32_qai8dxp_qsu2cxp/kai_matmul_clamp_f32_qai8dxp1vlx4_qsu2cxp4vlx4_1vlx4vl_sme2_mopa_asm.S).

## Build and validate the example

From the `code` directory, compile `example_1_luti_sme2.c` with SME2 enabled:

```bash
/opt/homebrew/opt/llvm/bin/clang \
  -O2 -Wall -Wextra -Werror \
  -march=native+sme2 \
  -isysroot "$(xcrun --show-sdk-path)" \
  example_1_luti_sme2.c \
  -o example_1_luti_sme2
```

Run the example:

```bash
./example_1_luti_sme2
```

The program first prints the logical lookup table:

```text
bits  idx  signed  raw byte
 00   0      -3    0xFD
 01   1      -1    0xFF
 10   2       1    0x01
 11   3       3    0x03
```

It then prints sample packed bytes, their indices in `k0` to `k3` order, and
the signed and hexadecimal decoded values.

After showing a preview of the result matrix, the program reports:

```text
PASS: LUTI2 SME2 matches plain C matmul.
```

The program produces this message only after comparing every SME2 result
against the corresponding plain C result.

## Inspect the generated SME2 instructions

Disassemble the executable and confirm that the SME2 function contains
`LUTI2` followed by four `SMOPA` instructions.

```bash
/opt/homebrew/opt/llvm/bin/llvm-objdump -d example_1_luti_sme2 | \
  grep -E "luti2|smopa"
```

## Check your understanding

Before continuing, make sure you can explain:

- Why one packed byte represents four values along the `K` dimension.
- Why the plain C shift counts are 0, 2, 4, and 6.
- Why the mask is `0x03`.
- How one `LUTI2` produces four decoded Z registers.
- Why four `SMOPA` instructions produce four adjacent output panels in
  `ZA0`-`ZA3`.
- How the element-by-element comparison validates the SME2 result.

## What you can do now and what's next

You can now decode the same packed 2-bit RHS data in plain C or expand it with
SME2 `LUTI2`. You can also pass the expanded Z-register values directly to
`SMOPA` and accumulate signed 32-bit results in `ZA`.

Next, develop intuition for programming LUTI instructions through practical
SME2 examples.