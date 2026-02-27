---
title: Decode the SME2 matmul microkernel
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Decode the SME2 matmul microkernel

This Learning Path uses one concrete KleidiAI microkernel to explain SME2 matmul microkernels in detail:

*kai_matmul_clamp_f32_qsi8d32p1vlx4_qsi4c32p4vlx4_1vlx4vl_sme2_mopa*

In the rest of this Learning Path, this is referred to as *the SME2 matmul microkernel* (unless noted otherwise).

### Decode `1vlx4vl`

`_1vlx4vl` indicates that, in a single inner-loop iteration, the kernel computes an intermediate result for a 1VL × 4VL submatrix (one SME2 streaming vector length × four SME2 streaming vector lengths) of the output matrix.

If you assume an SME2 SVL of 512 bits, the FP32 shape is 16 × 64:
- 1VL rows: `512 / 8 / 4 = 16` FP32 elements
- 4VL columns: `4 × 16 = 64` FP32 elements

### See the pipelined MOPA pattern

To improve throughput, the kernel pipelines four MOPA instructions so it can accumulate into four ZA tiles in parallel (one ZA tile per MOPA).

The same pattern applies here as shown by the video in the [SME2 INT8 MOPA section](/learning-paths/mobile-graphics-and-gaming/kai_sme2_matmul_ukernel_explained/sme2_mpoa_matmul/). 

![Figure showing Matrix Multiplication with 1VLx4VL SME2 MOPA alt-text#center](videos/1vlx4vl_sme2_mopa.gif "Matrix Multiplication with 1VLx4VL SME2 MOPA")

The animation demonstrates how four pipelined MOPA instructions multiply one 16×4 submatrix (1VL) from matrix A by four 4×16 submatrices (4VL) from matrix B in a single iteration.

The intermediate result of 4x16x16 output submatrix is held in four ZA.S tiles.

### Decode the input formats

The table below decodes the input and output format tags in the microkernel name.

| Format tag | Meaning | Why it matters |
| --- | --- | --- |
| `qsi8d32p1vlx4` | LHS layout is [M, K], symmetrically quantized to signed INT8 in blocks of 32; packed into 1VL × 4 submatrices (16 × 4 for a 512-bit SVL). | Row-wise packing makes LHS loads contiguous, which improves cache locality. |
| `qsi4c32p4vlx4` | RHS layout is [N, K], symmetrically quantized to signed INT4 in blocks of 32; packed into 4VL × 4 submatrices (4 × 16 × 4 for a 512-bit SVL). | INT4 packs two values per byte, and SME2 LUTI expands them to INT8 for MOPA. |
| `_f32_` | Output matrix is FP32; the INT32 accumulation from MOPA is dequantized to FP32. | Preserves FP32 results while using INT8/INT4 arithmetic in the inner loop. |

Sometimes, the original LHS or RHS doesn’t match the quantization and packing requirements of the SME2 matmul microkernel. In that case, your software needs to quantize and pack the LHS and RHS first.

### Hands-on: compute the FP32 tile shape for your assumed SVL (optional)

If you want to sanity-check the `1VL` size used in the diagrams, calculate how many FP32 values fit in one SVL.

For an assumed 512-bit SVL:

```bash
SVL_BITS=512
FP32_PER_VL=$((SVL_BITS / 8 / 4))
echo "FP32 per VL: ${FP32_PER_VL}"
echo "1VLx4VL tile: ${FP32_PER_VL}x$((4 * FP32_PER_VL))"
```

If your target device uses a different SVL, the same formulas still apply.