---
title: Understand llama.cpp
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand llama.cpp

llama.cpp is an open-source LLM framework implemented in C++ that supports both training and inference.

This Learning Path focuses on inference on Arm CPUs.  

The `llama-cli` tool provides a command-line interface to run LLMs with the llama.cpp inference engine. 
It supports text generation, chat mode, and grammar-constrained output directly from the terminal.  

![text#center](images/llama_structure.png "Figure 1. llama-cli Flow")

### What does the Llama CLI do? 

Here are the steps performed by `llama-cli`:

1. Load and interpret LLMs in GGUF format  

2. Build a compute graph based on the model structure  

   The graph can be divided into subgraphs, each assigned to the most suitable backend device, but in this Learning Path all operations are executed on the Arm CPU backend. 

3. Allocate memory for tensor nodes using the graph planner  

4. Execute tensor nodes in the graph during the `graph_compute` stage, which traverses nodes and forwards work to backend devices  

Steps 2 to 4 are wrapped inside the function `llama_decode`.
During Prefill and Decode, `llama-cli` repeatedly calls `llama_decode` to generate tokens.  

The parameter `llama_batch` passed to `llama_decode` differs between stages, containing input tokens, their count, and their positions.  

### What are the components of llama.cpp?

The components of llama.cpp include: 

![text#center](images/llama_components.jpg "Figure 2. llama.cpp components")

llama.cpp supports various backends such as `CPU`, `GPU`, `CUDA`, and `OpenCL`.

For the CPU backend, it provides an optimized `ggml-cpu` library, mainly utilizing CPU vector instructions. 

For Arm CPUs, the `ggml-cpu` library also offers an `aarch64` trait that leverages 8-bit integer multiply (i8mm) instructions for acceleration. 

The `ggml-cpu` library also integrates the Arm [KleidiAI](https://github.com/ARM-software/kleidiai) library as an additional trait.

### Prefill and Decode in autoregressive LLMs

An autoregressive LLM is a type of Large Language Model that generates text by predicting the next token (word or word piece) in a sequence based on all the previously generated tokens. 

The term "autoregressive" means the model uses its own previous outputs as inputs for generating subsequent outputs, creating a sequential generation process.

For example, when generating the sentence "The cat sat on the", an autoregressive LLM:
1. Takes the input prompt as context
2. Predicts the next most likely token (e.g., "mat")  
3. Uses the entire sequence including "mat" to predict the following token
4. Continues this process token by token until completion

This sequential nature is why autoregressive LLMs have two distinct computational phases: Prefill (processing the initial prompt) and Decode (generating tokens one by one).

Most autoregressive LLMs are Decoder-only models. This refers to the transformer architecture they use, which consists only of decoder blocks from the original Transformer paper. The alternatives to decoder-only models include encoder-only models used for tasks like classification and encoder-decoder models used for tasks like translation. 

Decoder-only models like LLaMA have become dominant for text generation because they are simpler to train at scale, can handle both understanding and generation tasks, and are more efficient for text generation. 

Here is a brief introduction to Prefill and Decode stages of autoregressive LLMs.
![text#center](images/llm_prefill_decode.jpg "Figure 3. Prefill and Decode stages")

At the Prefill stage, multiple input tokens of the prompt are processed.

It mainly performs GEMM (a matrix is multiplied by another matrix) operations to generate the first output token. 

![text#center](images/transformer_prefill.jpg "Figure 4. Prefill stage")

At the Decode stage, by utilizing the [KV cache](https://huggingface.co/blog/not-lain/kv-caching), it mainly performs GEMV (a vector is multiplied by a matrix) operations to generate subsequent output tokens one by one.

![text#center](images/transformer_decode.jpg "Figure 5. Decode stage")

In summary, Prefill is compute-bound, dominated by large GEMM operations and Decode is memory-bound, dominated by KV cache access and GEMV operations. 

You will see this highlighted during the Streamline performance analysis.