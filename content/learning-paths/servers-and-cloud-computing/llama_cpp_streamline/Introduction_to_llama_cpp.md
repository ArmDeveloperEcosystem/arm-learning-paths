---
title: Introduction to llama.cpp
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Introduction to llama.cpp
llama.cpp is a LLM framework implemented in C++ that can be used for both training and inference. This guide only covers inference on the CPU.
llama-cli is a terminal interface to interact with LLM using the llama.cpp inference engine. It enables running inference, chat mode, grammar-constrained generation directly from the command line.
    <p align="center">
      <img src="images/llama_structure.png" alt="Alt text" width="60%"/>
    </p>
llama-cli does work below,
* Load and interpret LLMs in .gguf format.
* Build a compute graph according to the model structure. The compute graph can be divided into subgraphs suitable for different backends. The subgraphs are assigned to the most suitable backend devices. At this step, the model structure are converted into a compute graph with many tensor nodes and operators (such as ADD, MAT_MUL, NORM, SOFTMAX) that can be actually computed. 
Since this guide only focuses on running LLM on CPU, all operators are set to CPU backend. 
* Allocate memory for tensors nodes in the compute graph by the graph planner.
* Compute tensor nodes at the graph compute stage, where the ‘graph_compute’ function forwards the compute subgraphs to the backend devices. The compute graph is a tree of nodes. The computation is performed by traversing the nodes in the graph.

Those steps above are wrapped in the function ‘llama_decode’. At LLM Prefill and Decode stage, llama-cli calls ‘llama_decode’ repeatedly to generate tokens. However, the parameter ‘llama_batch’ passed to ‘llama_decode' is different at Prefill and Decode stage. ‘llama_batch’ includes information such as input tokens, number of input tokens, the position of input tokens.

The components of llama.cpp include
    <p align="center">
      <img src="images/llama_componetns.png" alt="Alt text" width="50%"/>
    </p>

llama.cpp supports various backends such as CPU, GPU, CUDA, OpenCL etc. 
For the CPU backend, it provides an optimized ggml-cpu library (mainly utilizing CPU vector instructions). For Arm CPUs, the ggml-cpu library also offers an aarch64 trait that can leverage the new I8MM instructions for acceleration. The ggml-cpu library also integrates the Arm KleidiAI library as an additional trait.

Most of autoregressive LLMs are Decoder-only model. Let us have a brief introduction to Prefill and Decode stage of autoregressive LLMs.
    <p align="center">
      <img src="images/llm_prefill_decode.jpg" alt="Alt text" width="70%"/>
    </p>

At the Prefill stage, multiple input tokens of the prompt are processed. It mainly performs GEMM (A matrix is multiplied by another matrix) operations to generate the first output token. 
    <p align="center">
      <img src="images/transformer_prefill.jpg" alt="Alt text" width="100%"/>
    </p>

At the Decode stage, by utilizing the KV cache, it mainly performs GEMV (A vector is multiplied by a matrix) operations to generate subsequent output tokens one by one.
    <p align="center">
      <img src="images/transformer_decode.jpg" alt="Alt text" width="100%"/>
    </p>

Therefore, the prefill stage is compute-bound, while the decode stage has relatively less computation and is more memory-bound due to KV cache memory access. This can be seen in the subsequent analysis with Streamline.