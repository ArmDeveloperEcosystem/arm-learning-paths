---
title: Set Up Your Local Environment to Run an AI Application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

This Learning Path demonstrates how to build an AI Agent Application using open-source LLMs optimized for the Arm architecture. The AI Agent can use Large Language Models (LLMs) to perform actions by accessing tools and knowledge. 

The instructions in this Learning Path have been designed for Arm servers running Ubuntu 22.04 LTS. You will need an Arm server instance with at least 4 cores and 16GB of memory. Configure disk storage for 32 GB or more. The instructions have been tested on an AWS EC2 Graviton3 `m7g.xlarge` instance.

## Overview

In this Learning Path, you will learn how to build an AI agent application using `llama-cpp-python` and `llama-cpp-agent`. `llama-cpp-python` is a Python binding for `llama.cpp` that enables efficient LLM inference on Arm CPUs and `llama-cpp-agent` provides an interface for processing text using agentic chains with tools.

## Install Dependencies

Install the following packages on your Arm-based server instance:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-pip python3-venv cmake -y
```

Create and activate a Python virtual environment:
```bash
python3 -m venv ai-agent
source ai-agent/bin/activate
```

Install the `llama-cpp-python` package using pip:

```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```

Install the `llama-cpp-agent` and `pydantic` packages using pip:

```bash
pip install llama-cpp-agent pydantic
```


## Download the Pre-quantized Llama-3.1-8B LLM Model from Hugging Face

You are now ready to download the LLM.

Create and navigate to the models directory:

```bash
mkdir models
cd models
```
Install the `huggingface_hub` Python library using `pip`:

```bash
pip install huggingface_hub
```
You can now download the [pre-quantized Llama3.1 8B model](https://huggingface.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf) using the `huggingface-cli`:

```bash
huggingface-cli download cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf dolphin-2.9.4-llama3.1-8b-Q4_0.gguf --local-dir . --local-dir-use-symlinks False
```

`Q4_0` in the model name refers to the quantization method the model uses. Quantization aims to reduce the model's size (decreasing memory requirements) and increase execution speed (reducing memory bandwidth bottlenecks when transferring large amounts of data from memory to the processor). The primary trade-off when reducing a model’s size is balancing speed and size improvements against maintaining the quality of performance. Ideally, a model is quantized to meet size and speed requirements while not having a negative impact on performance.

The key aspect of quantization format is the number of bits per parameter, denoted as ‘Q4’ in this case, which represents 4-bit integers. 

## Build llama.cpp

As of [llama.cpp commit 0f1a39f3](https://github.com/ggerganov/llama.cpp/commit/0f1a39f3), Arm has contributed code for performance optimization with KleidiAI kernels. 

You can leverage these kernels to enhance model performance when running your model using the `llama.cpp` framework. 

Navigate to your home directory:

```bash
cd ~
```

Clone the `llama.cpp` repository:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

Build llama.cpp:

```bash
cd llama.cpp
mkdir build
cd build
cmake .. -DCMAKE_CXX_FLAGS="-mcpu=native" -DCMAKE_C_FLAGS="-mcpu=native"
cmake --build . -v --config Release -j `nproc`
```
The build outputs binaries to the `bin` directory, and you will see that `llama.cpp` is now built there.

Check that `llama.cpp` has built correctly by running the help command:

```bash
cd bin
./llama-cli -h
```

If `llama.cpp` has built correctly, you will see the help options displayed. 

A snippet of the output is shown below:

```output
usage: ./llama-cli [options]

general:

  -h,    --help, --usage          print usage and exit
         --version                show version and build info
  -v,    --verbose                print verbose information
         --verbosity N            set specific verbosity level (default: 0)
         --verbose-prompt         print a verbose prompt before generation (default: false)
         --no-display-prompt      don't print prompt at generation (default: false)
  -co,   --color                  colorise output to distinguish prompt and user input from generations (default: false)
  -s,    --seed SEED              RNG seed (default: -1, use random seed for < 0)
  -t,    --threads N              number of threads to use during generation (default: 4)
  -tb,   --threads-batch N        number of threads to use during batch and prompt processing (default: same as --threads)
  -td,   --threads-draft N        number of threads to use during generation (default: same as --threads)
  -tbd,  --threads-batch-draft N  number of threads to use during batch and prompt processing (default: same as --threads-draft)
         --draft N                number of tokens to draft for speculative decoding (default: 5)
  -ps,   --p-split N              speculative decoding split probability (default: 0.1)
  -lcs,  --lookup-cache-static FNAME
                                  path to static lookup cache to use for lookup decoding (not updated by generation)
  -lcd,  --lookup-cache-dynamic FNAME
                                  path to dynamic lookup cache to use for lookup decoding (updated by generation)
  -c,    --ctx-size N             size of the prompt context (default: 0, 0 = loaded from model)
  -n,    --predict N              number of tokens to predict (default: -1, -1 = infinity, -2 = until context filled)
  -b,    --batch-size N           logical maximum batch size (default: 2048)
```
In the next section, you will create a Python script to execute an AI agent powered by the downloaded model.
