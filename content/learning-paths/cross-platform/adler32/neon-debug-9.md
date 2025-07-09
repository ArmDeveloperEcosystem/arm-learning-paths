---
title: Debug the NEON version to match the standard C version
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Can I Debug the NEON Version Adler32 and Compare Performance?

In the previous step, GitHub Copilot revealed that the NEON implementation did not produce the same checksum results as the standard C version.

Use the prompt below to instruct GitHub Copilot to try to debug and fix the issue.

```console
Can you modify adler32-neon.c to produce the correct checksum results for the adler32 algorithm? The test program is adler32-test.c and the simple version is adler32-simple.c 
The NEON version should produce the same checksum as adler32-simple.c but run faster. 
```

If the LLM you’re using cannot resolve the NEON functional issues, consider trying another model, such as Gemini 2.5 Pro.

The output is:

```output
GitHub Copilot: Okay, I can help with that. The issue seems to be in how the `a` and `b` accumulators are updated within the NEON processing loop. The update to `b` needs to correctly incorporate the value of `a` *before* it was updated in the current block, along with the weighted sum of the data bytes.

I will modify the `adler32_neon` function in adler32-neon.c to correctly calculate the sums `s1` (sum of bytes) and `s2` (weighted sum of bytes) for each block using NEON intrinsics, and then update the scalar `a` and `b` values according to the Adler-32 definition: `a = (a_old + s1) % MOD_ADLER` and `b = (b_old + BLOCK_SIZE * a_old + s2) % MOD_ADLER`.

uint32_t adler32_neon(const unsigned char *data, size_t length, uint32_t initial)
{
    uint32_t a = initial & 0xffff;
    uint32_t b = (initial >> 16) & 0xffff;
    
    /* For small inputs, use the standard implementation */
    if (length < BLOCK_SIZE) {
        return adler32_standard(data, length, initial);
    }

    /* Preload weights */
    static const uint16_t weights[16] = {16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
    uint16x8_t vweights_low = vld1q_u16(weights);
    uint16x8_t vweights_high = vld1q_u16(weights + 8);

    /* Process blocks of BLOCK_SIZE bytes */
    while (length >= BLOCK_SIZE) {
        /* Store old 'a' before processing the block */
        uint32_t a_old = a;

        /* Load 16 bytes */
        uint8x16_t vdata = vld1q_u8(data);
        
        /* Widen bytes to 16 bits */
        uint16x8_t vdata_low = vmovl_u8(vget_low_u8(vdata));
        uint16x8_t vdata_high = vmovl_u8(vget_high_u8(vdata));
        
        /* Calculate S1 = sum(data[i]) for the block */
        uint16x8_t vs1_sum = vaddq_u16(vdata_low, vdata_high);
        /* Horizontal sum for S1 */
        uint32x4_t vs1_pairs = vpaddlq_u16(vs1_sum);
        uint64x2_t vs1_quads = vpaddlq_u32(vs1_pairs);
        uint32_t block_s1 = (uint32_t)(vgetq_lane_u64(vs1_quads, 0) + vgetq_lane_u64(vs1_quads, 1));

        /* Calculate S2 = sum((BLOCK_SIZE-i) * data[i]) for the block */
        uint16x8_t weighted_low = vmulq_u16(vdata_low, vweights_low);
        uint16x8_t weighted_high = vmulq_u16(vdata_high, vweights_high);
        uint16x8_t vs2_sum = vaddq_u16(weighted_low, weighted_high);
        /* Horizontal sum for S2 */
        uint32x4_t vs2_pairs = vpaddlq_u16(vs2_sum);
        uint64x2_t vs2_quads = vpaddlq_u32(vs2_pairs);
        uint32_t block_s2 = (uint32_t)(vgetq_lane_u64(vs2_quads, 0) + vgetq_lane_u64(vs2_quads, 1));
        
        /* Update scalar a and b */
        a = (a_old + block_s1) % MOD_ADLER;
        b = (b + (BLOCK_SIZE * a_old) + block_s2) % MOD_ADLER;
        
        /* Move to next block */
        data += BLOCK_SIZE;
        length -= BLOCK_SIZE;
    }
    
    /* Process remaining bytes using standard implementation */
    if (length > 0) {
// ...existing code...


Made changes.

I've modified the `adler32_neon` function in adler32-neon.c to correctly calculate the checksum using NEON intrinsics.

Now, I'll check for any compilation errors and then rebuild and run the test program to verify the results.I have modified the `adler32_neon` function in adler32-neon.c to correctly calculate the block sums and update the `a` and `b` accumulators according to the Adler-32 algorithm definition, using NEON intrinsics for the block processing.

I then checked for errors in the modified file and rebuilt the project using `make`. The build completed successfully, although there's a minor compiler warning in adler32-test.c about comparing signed and unsigned integers, which is unrelated to the changes made.

You can now run the test program adler32-test to verify that the NEON implementation produces the same results as the simple implementation.
```

GitHub Copilot successfully modified the NEON version to produce correct checksum results matching the standard C implementation.

Continue to the next section to summarize the project, highlight the performance improvements, and generate a full project description.