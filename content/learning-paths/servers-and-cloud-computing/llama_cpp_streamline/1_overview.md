---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profiling LLMs on Arm CPUs with Streamline

Deploying Large Language Models (LLMs) on Arm CPUs provides a power-efficient and flexible solution. While larger models may benefit from GPU acceleration, techniques like quantization enable a wide range of LLMs to perform effectively on CPUs alone.  

Frameworks such as [**llama.cpp**](https://github.com/ggml-org/llama.cpp), provide a convenient way to run LLMs, but it also comes with a certain level of complexity. 

To analyze their execution and use profiling insights for optimization, you need both a basic understanding of transformer architectures and the right analysis tools.

This Learning Path demonstrates how to use `llama-cli` from the command line together with Arm Streamline to analyze the efficiency of LLM inference on Arm CPUs.  

You will learn how to:
- Profile token generation at the Prefill and Decode stages
- Profile execution of individual tensor nodes and operators
- Profile LLM execution across multiple threads and cores

You will run the `Qwen1_5-0_5b-chat-q4_0.gguf` model using `llama-cli` on Arm Linux and use Streamline for analysis.  

The same method can also be used on Android.
