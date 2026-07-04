---
title: Understand how SME2 and KleidiAI accelerate LLM inference in llama.cpp
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## How SME2 and KleidiAI accelerate LLM inference in llama.cpp

In this Learning Path, you'll optimize llama.cpp inference on an Arm CPU by enabling SME2 acceleration through Arm KleidiAI microkernels.

You will measure the performance difference between the default CPU path and the SME2-optimized path using a 3 billion parameter LLM. By the end, you will understand:

- What SME2 changes in the matrix execution path
- How KleidiAI integrates into llama.cpp’s CPU backend
- How to verify that SME2 microkernels are active
- What measurable improvement you should expect

Scalable Matrix Extension 2 (SME2) is an Arm architectural feature designed to accelerate matrix-heavy workloads. Large language model (LLM) inference relies heavily on matrix multiplication, especially in transformer layers. When SME2 is available on the CPU, KleidiAI provides optimized microkernels that replace generic implementations inside llama.cpp.

llama.cpp is a CPU-focused LLM inference engine. On Arm systems, it integrates with KleidiAI by default. If SME2 is supported and enabled at runtime, llama.cpp dispatches SME2-optimized matrix kernels for supported operations.

This Learning Path uses the `Llama-3.2-3B-Instruct-Q4_0.gguf` model (3 billion parameters) as a reproducible test case.

In the next section, you'll examine how KleidiAI microkernels integrate into the llama.cpp backend and where SME2 is activated in the execution path.




