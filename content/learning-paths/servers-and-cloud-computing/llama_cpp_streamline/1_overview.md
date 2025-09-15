---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview: Profiling LLMs on Arm CPUs with Streamline

Large Language Models (LLMs) run efficiently on Arm CPUs.  
Frameworks that run LLMs, such as [**llama.cpp**](https://github.com/ggml-org/llama.cpp), provides a convenient framework for running LLMs, it also comes with a certain level of complexity. 

To analyze their execution and use profiling insights for optimization, you need both a basic understanding of transformer architectures and the right analysis tools.

This learning path demonstrates how to use the **llama-cli** application from llama.cpp together with **Arm Streamline** to analyze the efficiency of LLM inference on Arm CPUs.  

In this guide you will learn how to:
- Profile token generation at the **Prefill** and **Decode** stages
- Profile execution of individual tensor nodes and operators
- Profile LLM execution across **multiple threads and cores**

You will run the **Qwen1_5-0_5b-chat-q4_0.gguf** model with llama-cli on **Arm64 Linux** and use Streamline for analysis.  
The same method can also be applied to **Arm64 Android** platforms.  

## Prerequisites
Before starting this guide, you should be familiar with:
- Transformer architectures
- llama.cpp
- Arm Streamline
