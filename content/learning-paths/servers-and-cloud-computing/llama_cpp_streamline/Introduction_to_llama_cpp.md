---
title: Introduction to llama.cpp
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Introduction to llama.cpp
llama.cpp is a LLM framework implemented in C++ that can be used for both training and inference. This guide only covers inference on the CPU.
llama-cli provides a terminal interface to interact with LLM using the llama.cpp inference engine. It enables LLM inference, chat mode, grammar-constrained generation directly from the command line.
![text#center](images/llama_structure.png "Figure 1. Annotation String")

llama-cli does the following things,
* Load and interpret LLMs in .gguf format.
* Build a compute graph according to the model structure. The compute graph can be divided into subgraphs that are assigned to the most suitable backend devices. At this step, the model structure are converted into a compute graph with many tensor nodes/operators (such as ADD, MUL_MAT, NORM, SOFTMAX) that can be actually computed. 
Since this guide only focuses on running LLM on CPU, all operators are assigned to CPU backend. 
* Allocate memory for tensors nodes in the compute graph by the graph planner.
* Compute tensor nodes at the graph compute stage, where the ‘graph_compute’ function forwards the compute subgraphs to the backend devices. The computation is performed by traversing the tree of nodes in the compute graph.

Those steps above are wrapped in the function ‘llama_decode’. At LLM Prefill and Decode stage, llama-cli calls ‘llama_decode’ repeatedly to generate tokens. However, the parameter ‘llama_batch’ passed to ‘llama_decode' is different at Prefill and Decode stage. ‘llama_batch’ includes information such as input tokens, number of input tokens, the position of input tokens.

The components of llama.cpp include
![text#center](images/llama_componetns.jpg "Figure 2. llmama.cpp components")

llama.cpp supports various backends such as CPU, GPU, CUDA, OpenCL etc. 
For the CPU backend, it provides an optimized ggml-cpu library (mainly utilizing CPU vector instructions). For Arm CPUs, the ggml-cpu library also offers an aarch64 trait that leverages the new I8MM instructions for acceleration. The ggml-cpu library also integrates the Arm KleidiAI library as an additional trait.

Most autoregressive LLMs are Decoder-only model. Here is a brief introduction to Prefill and Decode stage of autoregressive LLMs.
![text#center](images/llm_prefill_decode.jpg "Figure 3. Prefill and Decode stage")

At the Prefill stage, multiple input tokens of the prompt are processed. It mainly performs GEMM (A matrix is multiplied by another matrix) operations to generate the first output token. 
![text#center](images/transformer_prefill.jpg "Figure 4. Prefill stage")


At the Decode stage, by utilizing the KV cache, it mainly performs GEMV (A vector is multiplied by a matrix) operations to generate subsequent output tokens one by one.
![text#center](images/transformer_decode.jpg "Figure 5. Decode stage")

Therefore, the prefill stage is compute-bound, while the decode stage has relatively less computation and is more memory-bound due to lots of KV cache memory access. This can be seen in the subsequent analysis with Streamline.