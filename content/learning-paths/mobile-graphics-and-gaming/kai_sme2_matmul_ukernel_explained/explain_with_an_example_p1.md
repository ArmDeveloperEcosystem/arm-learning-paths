---
title: Repack RHS weights (GGML Q4_0)
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Repack RHS weights (GGML Q4_0)
When you [integrate SME2-optimized KleidiAI kernels into llama.cpp](/learning/mobile-graphics-and-gaming/performance_llama_cpp_sme2/), the heavy matrix-multiplication work in attention (K/Q/V projections) and feed-forward network (FFN) layers can run through the SME2 matmul microkernel.

In these operators, the LHS (activations) is FP32 and the RHS (weights) uses the GGML Q4_0 quantized type.

To keep the example readable, this Learning Path uses a simplified matmul shape:
- LHS `[m, k] = [16, 64]`
- RHS `[n, k] = [64, 64]`

It also assumes an SME2 SVL of 512 bits.

### Pack the RHS
Although the original Q4_0 RHS (weights) uses INT4 quantization, it is signed INT4 and uses a GGML-specific layout and scale encoding. The SME2 matmul microkernel expects a different packed RHS representation (including an unsigned INT4 form and per-block metadata arranged for efficient loads).

Because the RHS (weights) stays constant during inference, you only need to convert and pack it once when loading the model.


Start by reviewing GGML Q4_0 quantization so you can see why the original RHS layout doesn’t match what the SME2 microkernel expects.
In the Q4_0 model, the Q4_0 weights are stored in layout of [n, k].
GGML Q4_0 quantizes weights in blocks of 32 floats. For each block, it calculates a scale for the block and then converts each value into a signed 4-bit integer. The scale is stored as FP16. 
Then GGML Q4_0 packs the values in a way of,
- the low nibble (bits 0–3) holds the first value (even index)
- and the high nibble (bits 4–7) holds the second value (odd index)
Thus, each byte contains a low/high pair. 
The following diagram shows how GGML Q4_0 quantizes and packs the original [n, k] FP32 matrix into Q4_0 type with layout of [n, k].
![Figure showing GGML Q4_0 quantization alt-text#center](images/q4_0_format.jpg "GGML Q4_0 quantization")

Unfortunately, the Q4_0 format does not meet the requirements of the SME2 matmul microkernel. It needs to be converted to an unsigned INT4 quantization format and repacked using the *kai_run_rhs_pack_nxk_qsi4c32ps1s0scalef16_qsu4c32s16s0_neon* function. 

This example uses m=16 and k=64.
- The required mr value for the SME2 matmul kernel is obtained using *kai_get_mr_matmul_clamp_f32_qai8dxp1vlx4_qsi8cxp4vlx4_1vlx4vl_sme2_mopa*. Here, mr=16.
- The required nr value for the SME2 matmul kernel is obtained using *kai_get_nr_matmul_clamp_f32_qai8dxp1vlx4_qsi8cxp4vlx4_1vlx4vl_sme2_mopa*. Here, nr=64.
- The required kr value for the SME2 matmul kernel is obtained using *kai_get_kr_matmul_clamp_f32_qai8dxp1vlx4_qsi8cxp4vlx4_1vlx4vl_sme2_mopa*. Here, kr=4.
- The required sr value for the SME2 matmul kernel is obtained using *kai_get_sr_matmul_clamp_f32_qai8dxp1vlx4_qsi8cxp4vlx4_1vlx4vl_sme2_mopa*. Here, sr=2 (two INT4 elements in a byte).

The function call stack for this process in llama.cpp when loading the model is as follows:
```text
llama_model_load  
  llama_model::load_tensors  
     llama_model_loader::load_all_data					 
			ggml_backend_tensor_set		 
				ggml_backend_cpu_kleidiai_buffer_set_tensor 
                        ggml::cpu::kleidiai::tensor_traits::repack
						    kai_run_rhs_pack_nxk_qsi4c32ps1s0scalef16_qsu4c32s16s0_neon
```
This process can be illustrated with the diagram below.
![Figure showing RHS packing with KleidiAI alt-text#center](images/kai_kernel_packed_rhs.jpg "RHS packing with KleidiAI")

The numerical label of an element in the diagram is used to indicate its row and column number in the original matrix. For example , 
![Figure showing row/column label for tracking elements alt-text#center](images/row_col_lable.png "Row/column label used for tracking")
This indicates the element is at row 01, column 02 in the original matrix. This row/column label stays consistent through quantization and packing so you can track elements across layouts.

After this step, the RHS is converted and packed into a format the SME2 matmul microkernel can consume efficiently. This allows the kernel to load packed RHS data into SME2 Z registers using sequential memory access, which improves cache locality.

### Hands-on: find the RHS repack microkernel in KleidiAI (optional)

If you cloned the KleidiAI repository earlier, you can locate the repack function used for RHS conversion.

From the KleidiAI repo root:

```bash
grep -R "kai_run_rhs_pack_nxk_qsi4c32ps1s0scalef16_qsu4c32s16s0_neon" -n kai | head
```

You can also search for the `qsu4` (unsigned INT4) string to find related packers:

```bash
grep -R "qsu4" -n kai | head
```