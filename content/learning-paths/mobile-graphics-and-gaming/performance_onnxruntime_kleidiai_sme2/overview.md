---
title: ONNX Runtime overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## ONNX Runtime overview
With the rise of on-device AI, squeezing performance from CPUs has become critical. Arm's Scalable Matrix Extension 2 (SME2) represents a leap forward, offering significant speedups for matrix-heavy workloads like Transformers and CNNs.
This Learning Path walks you through the technical steps to integrate KleidiAI—Arm's specialized micro-kernel library with SME2 support—into ONNX Runtime (ORT) and profile its performance using onnxruntime_perf_test on Android devices.

### Understanding the ONNX Runtime software stack
ONNX Runtime's internal architecture consists of four main components that work together to execute AI models efficiently:
![Diagram showing the four main components of ONNX Runtime: In-Memory Graph at the top, followed by Graph Partitioner, Graph Runner, and Execution Provider at the bottom, with data flow indicated between layers alt-txt#center](images/ort_overview.jpg "The ONNX Runtime overview")

#### 1. In-Memory Graph
When loading an ONNX model, ORT parses the protobuf file and creates an In-Memory Graph. This is a live representation of the model’s structure, consisting of:
-	Nodes: Representing operations (e.g., MatMul, Conv, Add).
-	Edges: Representing the flow of data (tensors) between those operations.

During this stage, ORT performs Graph Optimizations like constant folding and node fusion.
#### 2. Graph Partitioner
The Graph Partitioner decides which part of the model runs on which hardware. It analyzes the computational graph and matches nodes to the registered Execution Providers.
It clusters adjacent nodes assigned to the same EP into "Subgraphs".
#### 3. Graph Runner 
Once the graph is partitioned, the Graph Runner executes the operators in the correct order. It manages the flow of data (Tensors) between nodes.
In ORT, parallelism splits into two distinct levels to maximize hardware utilization: Intra-op (inside an operator/node, splitting a single heavy operation/node into smaller chunks) and Inter-op (between different operators, running multiple independent operators at the same time).

#### 4. Execution Provider (EP)
An Execution Provider is the abstraction layer that interfaces with specific hardware or libraries. 
Each EP provides a set of "Kernels" (optimized math functions) for specific operators.
Examples: 
-	CPU: Default CPU, Intel DNNL, XNNPACK etc.
-	GPU: NVIDIA CUDA/TensorRT, AMD MIGraphX, DirectML etc.
-	Others: NPU, Qualcomm QNN etc.

If a specialized EP doesn't support a specific operator, ORT automatically falls back to the CPU provider.

The default CPU provider uses Microsoft Linear Algebra Subprograms (MLAS). MLAS is a minimal version of BLAS library that implements an optimized version of linear algebra operations such as general matrix multiply (GEMM) in low-level languages with various processor support. For aarch64, MLAS already uses dotprod, i8mm, fp16, and bf16 vector instructions for acceleration. 

The KleidiAI-optimized MLAS can delegate high-performance matrix operations to KleidiAI micro kernels. KleidiAI provides micro-kernels specifically tuned for SME2, allowing ORT to leverage the latest hardware features.

This Learning Path focuses on Arm CPU Execution Provider.

## What you've accomplished and what's next

You now understand how ONNX Runtime processes models through its layered architecture—from the in-memory graph to execution providers. You've learned how the Graph Partitioner assigns operations to hardware, how the Graph Runner orchestrates execution, and how Execution Providers like the CPU provider use optimized kernels. You also know that MLAS serves as the default CPU backend and that KleidiAI can optimize it with SME2-specific kernels.

Next, you'll explore how KleidiAI integrates into MLAS and which specific operators benefit from SME2 acceleration.



