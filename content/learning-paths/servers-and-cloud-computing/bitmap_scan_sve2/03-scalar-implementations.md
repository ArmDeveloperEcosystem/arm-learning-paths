---
# User change
title: "Scalar Implementations of Bitmap Scanning"

weight: 4

layout: "learningpathall"


---
## Bitmap scanning implementations

Now, let's implement four versions of a bitmap scanning operation that finds all positions where a bit is set:

### 1. Generic Scalar Implementation

This is the most straightforward implementation, checking each bit individually. It serves as our baseline for comparison against the other implementations to follow. Copy the code below into the same file:

```c
// Generic scalar implementation of bit vector scanning (bit-by-bit)
size_t scan_bitvector_scalar_generic(bitvector_t* bv, uint32_t* result_positions) {
    size_t result_count = 0;

    for (size_t i = 0; i < bv->size_bits; i++) {
        if (bitvector_get_bit(bv, i)) {
            result_positions[result_count++] = i;
        }
    }

    return result_count;
}
```

You will notice this generic C implementation processes every bit, even when most bits are not set. It has high function call overhead and does not advantage of vector instructions.

In the following implementations, you will address these inefficiencies with more optimized techniques.

### 2. Optimized Scalar Implementation

This implementation adds byte-level skipping to avoid processing empty bytes. Copy this optimized C scalar implementation code into the same file:

```c
// Optimized scalar implementation of bit vector scanning (byte-level)
size_t scan_bitvector_scalar(bitvector_t* bv, uint32_t* result_positions) {
size_t result_count = 0;

    for (size_t byte_idx = 0; byte_idx < bv->size_bytes; byte_idx++) {
        uint8_t byte = bv->data[byte_idx];

        // Skip empty bytes
        if (byte == 0) {
            continue;
        }

        // Process each bit in the byte
        for (int bit_pos = 0; bit_pos < 8; bit_pos++) {
            if (byte & (1 << bit_pos)) {
                size_t global_pos = byte_idx * 8 + bit_pos;
                if (global_pos < bv->size_bits) {
                    result_positions[result_count++] = global_pos;
                }
            }
        }
    }

    return result_count;
}
```
Instead of iterating through each bit, this implementation processes one byte(8 bits) at a time. The main optimization over the previous scalar implementation is checking if an entire byte is zero and skipping it entirely, For sparse bitmaps, this can dramatically reduce the number of bit checks.

