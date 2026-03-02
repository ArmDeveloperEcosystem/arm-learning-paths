---
title: Quantize and pack LHS activations
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Quantize and pack LHS activations
Next, the FP32 LHS (activation) needs to be quantized and packed when the llama.cpp graph runner computes the matmul nodes/operators. 

### Quantize and pack the LHS

Because the LHS (activations) changes for each matmul invocation, it must be quantized and packed dynamically. In this example, the FP32 LHS is quantized to signed INT8 and packed into the `qsi8d32p1vlx4` format using the *kai_run_lhs_quant_pack_qsi8d32p_f32_neon* microkernel.

The function call stack for this process in llama.cpp is as follows:
```text
llama_context::decode
   llama_context::process_ubatch
      llama_context::graph_compute
	     ggml_backend_sched_compute_splits
		    ggml_backend_cpu_graph_compute
			   ggml_graph_compute             //tick off the compute thread
			      ggml_graph_compute_thread   //the compute thread
				     ggml_compute_forward
					     ggml_cpu_extra_compute_forward
						    ggml::cpu::kleidiai::tensor_traits::compute_forward
							    ggml::cpu::kleidiai::tensor_traits::compute_forward_q4_0
								    kai_run_lhs_quant_pack_qsi8d32p_f32_neon
```
The diagram below illustrates how the LHS is quantized and packed by *kai_run_lhs_quant_pack_qsi8d32p_f32_neon*:
![Figure showing Quantization and Packing of the LHS alt-text#center](images/kai_run_lhs_quant_pack_qsi8d32p_f32_neon_for_sme2.jpg "Quantization and Packing of the LHS")

The values of mr, nr, and kr can be obtained in the same way as described above.
The values of `mr`, `nr`, and `kr`, together with the matrix dimensions `m` and `k`, are passed as parameters to *kai_run_lhs_quant_pack_qsi8d32p_f32_neon*.

This microkernel:
- Quantizes FP32 LHS values to signed INT8
- Stores the per-block scales
- Packs the quantized values into a contiguous layout based on `mr × kr` tiles (16 × 4 in this example)

This packing ensures the SME2 matmul microkernel can load a full input slice from contiguous memory, which improves cache locality.

### Hands-on: locate the LHS quant-pack microkernel in KleidiAI (optional)

If you cloned the KleidiAI repository earlier, locate the LHS quantization + packing microkernel:

```bash
grep -R "kai_run_lhs_quant_pack_qsi8d32p_f32_neon" -n kai | head
```
