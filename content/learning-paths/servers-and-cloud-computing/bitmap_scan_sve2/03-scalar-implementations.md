---
# User change
title: "Implement Scalar Bitmap Scanning in C"

weight: 4

layout: "learningpathall"


---
## Bitmap scanning implementations

Bitmap scanning is a fundamental operation in performance-critical systems such as databases, search engines, and filtering pipelines. It involves identifying the positions of set bits (`1`s) in a bit vector, which is often used to represent filtered rows, bitmap indexes, or membership flags. 

In this section, you'll implement multiple scalar approaches to bitmap scanning in C, starting with a simple per-bit baseline, followed by an optimized version that reduces overhead for sparse data.

Now, let’s walk through the scalar versions of this operation that locate all set bit positions.

### Generic scalar implementation

This is the most straightforward implementation, checking each bit individually. It serves as the baseline for comparison against the other implementations to follow. 

Copy the code below into the same file:

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

You might notice that this generic C implementation processes every bit, even when most bits are not set. It has high per-bit function call overhead and does not take advantage of any vector instructions.

In the following implementations, you can address these inefficiencies with more optimized techniques.

### Optimized scalar implementation

This implementation adds byte-level skipping to avoid processing empty bytes. 

Copy this optimized C scalar implementation code into the same file:

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
Instead of iterating through each bit individually, this implementation processes one byte (8 bits) at a time. The main optimization over the previous scalar implementation is checking if an entire byte is zero and skipping it entirely. For sparse bitmaps, this can dramatically reduce the number of bit checks.

## Next up: accelerate bitmap scanning with NEON and SVE

You’ve now implemented two scalar scanning routines:

* A generic per-bit loop for correctness and simplicity

* An optimized scalar version that improves performance using byte-level skipping

These provide a solid foundation and performance baseline—but scalar methods can only take you so far. To unlock real throughput gains, it’s time to leverage SIMD (Single Instruction, Multiple Data) execution.

In the next section, you’ll explore how to use Arm NEON and SVE vector instructions to accelerate bitmap scanning. These approaches will process multiple bytes at once and significantly outperform scalar loops—especially on modern Arm-based CPUs like AWS Graviton4.
