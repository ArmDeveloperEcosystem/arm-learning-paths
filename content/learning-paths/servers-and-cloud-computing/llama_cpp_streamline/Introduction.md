---
title: PLACEHOLDER STEP TITLE 1
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Introduction 
Large Language Model (LLM) models run very smoothly on Arm CPUs. The framework for running LLM models is usually complex. To analyze the execution of LLM and utilize profiling information for potential code optimization, a good understanding of various LLMs based on transformers and appropriate analysis tools are required.
This article provides a guide of using llama-cli application built from llama.cpp and Arm’s Streamline tool to analyze the efficiency of LLM running on the CPU. The guide includes,
* How to profile token generation on LLM Prefill and Decode stage
* How to profile individual tensor OP
* How to profile LLM execution on multi-thread and multi-core

Understanding this article requires prerequisite knowledge of transformer, llama.cpp, and Streamline.

In this guide, we run Qwen1_5-0_5b-chat-q4_0.gguf model with llama-cli on Arm64 Linux and use Streamline for analysis. This guide should also work on Arm64 Android platform. 

