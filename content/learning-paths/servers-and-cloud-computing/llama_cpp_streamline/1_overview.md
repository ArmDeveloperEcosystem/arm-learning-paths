---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profile LLMs on Arm CPUs with Streamline

Deploying Large Language Models (LLMs) on Arm CPUs provides a power-efficient and flexible solution for many applications. While larger models can benefit from GPU acceleration, techniques like quantization enable a wide range of LLMs to perform effectively on CPUs alone by reducing model precision to save memory.

Frameworks such as [llama.cpp](https://github.com/ggml-org/llama.cpp) provide a convenient way to run LLMs. However, understanding their performance characteristics requires specialized analysis tools. To optimize LLM execution on Arm platforms, you need both a basic understanding of transformer architectures and the right profiling tools to identify bottlenecks.

This Learning Path demonstrates how to use `llama-cli` from the command line together with Arm Streamline to analyze the efficiency of LLM inference on Arm CPUs. You'll gain insights into token generation performance at both the Prefill and Decode stages. You'll also understand how individual tensor operations contribute to overall execution time, and evaluate multi-threaded performance across multiple CPU cores.

You will run the Qwen1_5-0_5b-chat-q4_0.gguf model using `llama-cli` on Arm Linux and use Streamline for detailed performance analysis. The same methodology can also be applied on Android systems.

By the end of this Learning Path, you'll understand how to profile LLM inference, identify performance bottlenecks, and analyze multi-threaded execution patterns on Arm CPUs.
