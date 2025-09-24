---
title: Understand the llama.cpp
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the llama.cpp

**llama.cpp** is an open-source LLM framework implemented in C++ that supports both training and inference.
This learning path focuses only on **inference on the CPU**.  

The **llama-cli** tool provides a command-line interface to run LLMs with the llama.cpp inference engine. 
It supports text generation, chat mode, and grammar-constrained output directly from the terminal.  

![text#center](images/llama_structure.png "Figure 1. llama-cli Flow")

### What llama-cli does
- Load and interpret LLMs in **.gguf** format  
- Build a **compute graph** based on the model structure  
  - The graph can be divided into subgraphs, each assigned to the most suitable backend device  
  - In this guide, all operators are executed on the **CPU backend**  
- Allocate memory for tensor nodes using the **graph planner**  
- Execute tensor nodes in the graph during the **graph_compute** stage, which traverses nodes and forwards work to backend devices  

Step2 to Step4 are wrapped inside the function **`llama_decode`**.
During **Prefill** and **Decode**, `llama-cli` repeatedly calls `llama_decode` to generate tokens.  
The parameter **`llama_batch`** passed to `llama_decode` differs between stages, containing input tokens, their count, and their positions.  

### Components of llama.cpp
The components of llama.cpp include: 
![text#center](images/llama_componetns.jpg "Figure 2. llmama.cpp components")

llama.cpp supports various backends such as `CPU`, `GPU`, `CUDA`, `OpenCL` etc.

For the CPU backend, it provides an optimized `ggml-cpu` library (mainly utilizing CPU vector instructions). 
For Arm CPUs, the `ggml-cpu` library also offers an `aarch64` trait that leverages the new **I8MM** instructions for acceleration. 
The `ggml-cpu` library also integrates the Arm [KleidiAI](https://github.com/ARM-software/kleidiai) library as an additional trait.

### Prefill and Decode in autoregressive LLMs
Most autoregressive LLMs are Decoder-only model.
Here is a brief introduction to Prefill and Decode stage of autoregressive LLMs.
![text#center](images/llm_prefill_decode.jpg "Figure 3. Prefill and Decode stage")

At the Prefill stage, multiple input tokens of the prompt are processed.
It mainly performs GEMM (A matrix is multiplied by another matrix) operations to generate the first output token. 
![text#center](images/transformer_prefill.jpg "Figure 4. Prefill stage")

At the Decode stage, by utilizing the [KV cache](https://huggingface.co/blog/not-lain/kv-caching), it mainly performs GEMV (A vector is multiplied by a matrix) operations to generate subsequent output tokens one by one.
![text#center](images/transformer_decode.jpg "Figure 5. Decode stage")

Therefore, 
- **Prefill** is **compute-bound**, dominated by large GEMM operations  
- **Decode** is **memory-bound**, dominated by KV cache access and GEMV operations 

This can be seen in the subsequent analysis with Streamline.