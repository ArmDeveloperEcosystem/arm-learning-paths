---
# User change
title: "Set up a RAG based LLM Chatbot"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

This learning path demonstrates how to build and deploy a Retrieval Augmented Generation (RAG) enabled chatbot using open-source Large Language Models (LLMs) optimized for Arm architecture. The chatbot processes documents, stores them in a vector database, and generates contextually-relevant responses by combining the LLM's capabilities with retrieved information. The instructions in this Learning Path have been designed for Arm servers running Ubuntu 22.04 LTS. You need an Arm server instance with at least 16 cores, 8GB of RAM, and a 32GB disk to run this example. The instructions have been tested on a GCP c4a-standard-64 instance.

## Overview

In this Learning Path, you learn how to build a RAG chatbot using llama-cpp-python, a Python binding for llama.cpp that enables efficient LLM inference on Arm CPUs.

The tutorial demonstrates how to integrate the FAISS vector database with the Llama-3.1-8B model for document retrieval, while leveraging llama-cpp-python's optimized C++ backend for high-performance inference.

This architecture enables the chatbot to combine the model's generative capabilities with contextual information retrieved from your documents, all optimized for Arm-based systems.

## Install dependencies

Install the following packages on your Arm based server instance:

```bash
sudo apt update
sudo apt install python3-pip python3-venv cmake -y
```

## Create a requirements file

```bash
vim requirements.txt
```

Add the following dependencies to your `requirements.txt` file:

```python
# Core LLM & RAG Components
langchain==0.1.16
langchain_community==0.0.38
langchainhub==0.1.20

# Vector Database & Embeddings
faiss-cpu
sentence-transformers

# Document Processing
pypdf
PyPDF2
lxml

# API and Web Interface
flask
requests
flask_cors
streamlit

# Environment and Utils
argparse
python-dotenv==1.0.1
```

## Install Python Dependencies

Create a virtual environment:
```bash
    python3 -m venv rag-env
```

Activate the virtual environment:
```bash
    source rag-env/bin/activate
```

Install the required libraries using pip:
```bash
    pip install -r requirements.txt
```
## Install llama-cpp-python

Install the `llama-cpp-python` package, which includes the Kleidi AI optimized llama.cpp backend, using the following command:

```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```

## Download the Model

Create a directory called models, and navigate to it:
```bash
    mkdir models
    cd models
```

Download the Hugging Face model:
```bash
    wget https://huggingface.co/chatpdflocal/llama3.1-8b-gguf/resolve/main/ggml-model-Q4_K_M.gguf
```

## Build llama.cpp & Quantize the Model

Navigate to your home directory:

```bash
cd ~
```

Clone the source repository for llama.cpp:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

By default, `llama.cpp` builds for CPU only on Linux and Windows. You do not need to provide any extra switches to build it for the Arm CPU that you run it on.

Run `cmake` to build it:

```bash
cd llama.cpp
mkdir build
cd build
cmake .. -DCMAKE_CXX_FLAGS="-mcpu=native" -DCMAKE_C_FLAGS="-mcpu=native"
cmake --build . -v --config Release -j `nproc`
```

`llama.cpp` is now built in the `bin` directory.

Run the following command to quantize the model:

```bash
cd bin
./llama-quantize --allow-requantize ../../../models/ggml-model-Q4_K_M.gguf ../../../models/llama3.1-8b-instruct.Q4_0_arm.gguf Q4_0
```