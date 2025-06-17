---
# User change
title: "Vectorized bitmap scanning with NEON and SVE"

weight: 5

layout: "learningpathall"


---
Modern Arm CPUs like Neoverse V2 support SIMD (Single Instruction, Multiple Data) extensions that allow processing multiple bytes in parallel. In this section, you'll explore how NEON and SVE vector instructions can dramatically accelerate bitmap scanning by skipping over large regions of unset data and reducing per-bit processing overhead.

## NEON implementation

This implementation uses NEON SIMD (Single Instruction, Multiple Data) instructions to process 16 bytes (128 bits) at a time, significantly accelerating the scanning process. 

Copy the NEON implementation shown below into the same file:

```c
// NEON implementation of bit vector scanning
size_t scan_bitvector_neon(bitvector_t* bv, uint32_t* result_positions) {
    size_t result_count = 0;

    // Process 16 bytes at a time using NEON
    size_t i = 0;
    for (; i + 16 <= bv->size_bytes; i += 16) {
        uint8x16_t data = vld1q_u8(&bv->data[i]);

        // Quick check if all bytes are zero
        uint8x16_t zero = vdupq_n_u8(0);
        uint8x16_t cmp = vceqq_u8(data, zero);
        uint64x2_t cmp64 = vreinterpretq_u64_u8(cmp);

        // If all bytes are zero (all comparisons are true/0xFF), skip this chunk
        if (vgetq_lane_u64(cmp64, 0) == UINT64_MAX &&
            vgetq_lane_u64(cmp64, 1) == UINT64_MAX) {
            continue;
        }

        // Process each byte
        uint8_t bytes[16];
        vst1q_u8(bytes, data);

        for (int j = 0; j < 16; j++) {
	    uint8_t byte = bytes[j];

            // Skip empty bytes
            if (byte == 0) {
                continue;
            }

            // Process each bit in the byte
            for (int bit_pos = 0; bit_pos < 8; bit_pos++) {
                if (byte & (1 << bit_pos)) {
                    size_t global_pos = (i + j) * 8 + bit_pos;
                    if (global_pos < bv->size_bits) {
                        result_positions[result_count++] = global_pos;
                    }
                }
            }
        }
    }

    // Handle remaining bytes with scalar code
    for (; i < bv->size_bytes; i++) {
        uint8_t byte = bv->data[i];

        // Skip empty bytes
        if (byte == 0) {
            continue;
        }

        // Process each bit in the byte
    for (int bit_pos = 0; bit_pos < 8; bit_pos++) {
            if (byte & (1 << bit_pos)) {
                size_t global_pos = i * 8 + bit_pos;
                if (global_pos < bv->size_bits) {
                    result_positions[result_count++] = global_pos;
                }
            }
        }
    }

    return result_count;
}
```
This NEON implementation processes 16 bytes at a time with vector instructions. For sparse bitmaps, entire 16-byte chunks can be skipped at once, providing a significant speedup over byte-level skipping. After vector processing, it falls back to scalar code for any remaining bytes that don't fill a complete 16-byte chunk.

## SVE implementation

This implementation uses SVE instructions which are available in the Arm Neoverse V2 based AWS Graviton 4 processor. 

Copy this SVE implementation into the same file:

```c
// SVE implementation using svcmp_u8, PNEXT, and LASTB
size_t scan_bitvector_sve2_pnext(bitvector_t* bv, uint32_t* result_positions) {
    size_t result_count = 0;
    size_t sve_len = svcntb();
    svuint8_t zero = svdup_n_u8(0);

    // Process the bitvector to find all set bits	
    for (size_t offset = 0; offset < bv->size_bytes; offset += sve_len) {
        svbool_t pg = svwhilelt_b8((uint64_t)offset, (uint64_t)bv->size_bytes);
        svuint8_t data = svld1_u8(pg, bv->data + offset);
        
        // Prefetch next chunk
        if (offset + sve_len < bv->size_bytes) {
            __builtin_prefetch(bv->data + offset + sve_len, 0, 0);
        }
        
        // Find non-zero bytes
        svbool_t non_zero = svcmpne_u8(pg, data, zero);
        
        // Skip if all bytes are zero
        if (!svptest_any(pg, non_zero)) {
            continue;
        }
        
        // Create an index vector for byte positions
        svuint8_t indexes = svindex_u8(0, 1); // 0, 1, 2, 3, ...
        
        // Initialize next with false predicate
        svbool_t next = svpfalse_b();
        
        // Find the first non-zero byte
        next = svpnext_b8(non_zero, next);
        
        // Process each non-zero byte using PNEXT
        while (svptest_any(pg, next)) {
            // Get the index of this byte
            uint8_t byte_idx = svlastb_u8(next, indexes);
            
            // Get the actual byte value
            uint8_t byte_value = svlastb_u8(next, data);

            // Calculate the global byte position
            size_t global_byte_pos = offset + byte_idx;
            
            // Process each bit in the byte using scalar code
            for (int bit_pos = 0; bit_pos < 8; bit_pos++) {
                if (byte_value & (1 << bit_pos)) {
                    size_t global_bit_pos = global_byte_pos * 8 + bit_pos;
                    if (global_bit_pos < bv->size_bits) {
                        result_positions[result_count++] = global_bit_pos;
                    }
                }
            }
            
            // Find the next non-zero byte
            next = svpnext_b8(non_zero, next);
        }
    }
    
    return result_count;
}
```
The SVE implementation efficiently scans bitmaps by using `svcmpne_u8` to identify non-zero bytes and `svpnext_b8` to iterate through them sequentially. It extracts byte indices and values with `svlastb_u8`, then processes individual bits using scalar code. This hybrid vector-scalar approach maintains great performance across various bitmap densities. On Graviton4, SVE vectors are 128 bits (16 bytes), allowing processing of 16 bytes at once. 

## Next up: apply vectorized scanning to database workloads

With both NEON and SVE implementations in place, you’ve now unlocked the full power of Arm’s vector processing capabilities for bitmap scanning. These SIMD techniques allow you to process large bitvectors more efficiently—especially when filtering sparse datasets or skipping over large blocks of empty rows.

In the next section, you’ll learn how to apply these optimizations in the context of real database operations like bitmap index scans, Bloom filter probes, and column filtering. You’ll also explore best practices for selecting the right implementation based on bit density, and tuning for maximum performance on AWS Graviton4.