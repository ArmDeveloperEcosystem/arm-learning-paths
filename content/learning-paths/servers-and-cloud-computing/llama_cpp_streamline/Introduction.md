---
title: Introduction
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Introduction 
Large Language Models (LLM) run very smoothly on Arm CPUs. The framework that runs LLM models is usually complex. To analyze the execution of LLM and utilize profiling information for potential code optimization, a good understanding of transformer architecture and an appropriate analysis tool is required.
This guide uses llama-cli application from llama.cpp and Arm’s Streamline tool to analyze the efficiency of LLM running on arm CPU. 

The guide includes,
* How to profile LLM token generation at Prefill and Decode stage
* How to profile execution of individual tensor node/operator
* How to profile LLM execution with multi-thread/multi-core

Understanding this guide requires prerequisite knowledge of transformer architecture, llama.cpp and Streamline.

We run Qwen1_5-0_5b-chat-q4_0.gguf model with llama-cli on Arm64 Linux and use Streamline for analysis. This guide should also work on Arm64 Android platform. 

