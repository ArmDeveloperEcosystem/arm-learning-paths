---
title: Set up the Environment to Run an AI Application Locally
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

This Learning Path demonstrates how to build an AI Agent Application using open-source Large Language Models (LLMs) optimized for Arm architecture. The AI Agent can use Large Language Models (LLMs) to perform actions by accessing tools and knowledge. The instructions in this Learning Path have been designed for Arm servers running Ubuntu 22.04 LTS. You need an Arm server instance with at least 4 cores and 16GB of memory to run this example. The instructions have been tested on an AWS EC2 `m7g.xlarge instance`.

## Overview

In this Learning Path, you learn how to build an AI Agent application using llama-cpp-python and llama-cpp-agent. llama-cpp-python is a Python binding from llama.cpp that enables efficient LLM inference on Arm CPUs and llama-cpp-agent provides an interface for processing text using agentic chains with tools.

## Installation

Install the `llama-cpp-python` package using pip:

```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```

Install the `llama-cpp-agent` and `pydantic` packages using pip:

```bash
pip install llama-cpp-agent pydantic
```



## Model Download

1. Create and navigate to a models directory:

```bash
mkdir models
cd models
```
2. Download the Hugging Face model:

```bash
wget https://huggingface.co/chatpdflocal/llama3.1-8b-gguf/resolve/main/ggml-model-Q4_K_M.gguf
```

## Building llama.cpp

1. Navigate to your home directory:

```bash
cd ~
```

2. Clone the llama.cpp repository:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

3. Build llama.cpp:
   > Note: By default, `llama.cpp` builds for CPU only on Linux and Windows. No extra switches are needed for Arm CPU builds.

```bash
cd llama.cpp
mkdir build
cd build
cmake .. -DCMAKE_CXX_FLAGS="-mcpu=native" -DCMAKE_C_FLAGS="-mcpu=native"
cmake --build . -v --config Release -j `nproc`
```

## Model Quantization

After building, quantize the model using the following command:

```bash
cd bin
./llama-quantize --allow-requantize ../../../models/ggml-model-Q4_K_M.gguf ../../../models/llama3.1-8b-instruct.Q4_0_arm.gguf Q4_0
```

This process will create a quantized version of the model optimized for your system.