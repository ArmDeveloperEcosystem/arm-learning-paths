---
title: Accelerate ExecuTorch operators with KleidiAI micro-kernels
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Understand how KleidiAI micro-kernels integrate with ExecuTorch

ExecuTorch uses XNNPACK as its main CPU backend to run and optimize operators like convolutions, matrix multiplications, and fully connected layers.

KleidiAI SME (Scalable Matrix Extension) micro-kernels are integrated into XNNPACK to boost performance on supported Arm platforms. These micro-kernels accelerate operators that use specific data types and quantization settings in ExecuTorch models.

When an operator matches a supported configuration, ExecuTorch automatically uses the KleidiAI-optimized path for faster execution. If an operator is not supported by KleidiAI, ExecuTorch falls back to the standard XNNPACK implementation. This ensures your models always run correctly, even if they do not use KleidiAI acceleration.

## Understand how KleidiAI micro-kernels integrate with ExecuTorch

In ExecuTorch v1.0.0, the following operator types are implemented through the XNNPACK backend and can potentially benefit from KleidiAI acceleration:
- XNNFullyConnected – Fully connected (dense) layers
- XNNConv2d – Standard 2D convolution layers
- XNNBatchMatrixMultiply – Batched matrix multiplication operations

However, not all instances of these operators are accelerated by KleidiAI.

Acceleration eligibility depends on several operator attributes and backend support, including:
- Data types (for example, float32, int8, int4)
- Quantization schemes (for example, symmetric/asymmetric, per-tensor/per-channel)
- Tensor memory layout and alignment
- Kernel dimensions and stride settings
    
The following section provides detailed information on which operator configurations can benefit from KleidiAI acceleration, along with their corresponding data type and quantization support.


## XNNFullyConnected 

| XNNPACK GEMM Variant | Activations DataType| Weights DataType | Output DataType                      |
| ------------------  | ---------------------------- | --------------------------------------- | ---------------------------- |
| pf16_gemm    | FP16                         | FP16                                    | FP16                         |
| pf32_gemm    | FP32                         | FP32                                    | FP32                         |
| qp8_f32_qc8w_gemm | Asymmetric INT8 per-row quantization | Per-channel symmetric INT8 quantization | FP32                         |
| pqs8_qc8w_gemm    | Asymmetric INT8 quantization | Per-channel symmetric INT8 quantization | Asymmetric INT8 quantization |
| qp8_f32_qb4w_gemm | Asymmetric INT8 per-row quantization | INT4 (signed), shared blockwise quantization | FP32                         |


## XNNConv2d
| XNNPACK GEMM Variant | Input DataType| Filter DataType | Output DataType                      |
| ------------------  | ---------------------------- | --------------------------------------- | ---------------------------- |
| pf32_gemm    | FP32                         | FP32, pointwise (1×1)                   | FP32                         |
| pqs8_qc8w_gemm | Asymmetric INT8 quantization (NHWC) | Per-channel or per-tensor symmetric INT8 quantization | Asymmetric INT8 quantization(NHWC) |


## XNNBatchMatrixMultiply
| XNNPACK GEMM Variant | Input A DataType| Input B DataType |Output DataType |
| ------------------  | ---------------------------- | --------------------------------------- |--------------------------------------- |
| pf32_gemm    | FP32                         | FP32                         | FP32 | 
| pf16_gemm    | FP16                         | FP16                         | FP16 |



