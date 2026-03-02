---
title: Wrap-up
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Wrap-up
You’ve walked through how an SME2-optimized KleidiAI matmul microkernel:
- Converts weights into a kernel-friendly packed RHS layout
- Quantizes and packs activations into a packed LHS layout
- Uses SME2 INT8 MOPA instructions (`smopa`) plus LUT-based dequantization (`luti4`) to compute a 1VL×4VL output tile efficiently
- Dequantizes back to FP32 so the result matches the surrounding FP32 computation (within expected quantization error)

If you completed the optional hands-on checks, you also confirmed where the key SME2 instructions appear in the microkernel source.

To go further, apply the same approach to a real workload:
- Use [the llama.cpp performance Learning Path](/learning-paths/mobile-graphics-and-gaming/performance_llama_cpp_sme2/) to build and profile llama.cpp with KleidiAI on an SME2-capable device
- Use [the ONNX Runtime performance Learning Path](/learning-paths/mobile-graphics-and-gaming/performance_onnxruntime_kleidiai_sme2/) to see how similar ideas apply in ONNX Runtime