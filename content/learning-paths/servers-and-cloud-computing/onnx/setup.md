---
# User change
title: "Build ONNX Runtime and setup Phi-3.5 vision model"

weight: 2

# Do not modify these elements
layout: "learningpathall"
---

In this Learning Path you will learn how to run quantized Phi models using ONNX Runtime on Microsoft Azure Cobalt 100 servers using ONNX Runtime. Specifically, you will deploy the Phi 3.5 vision model on Arm-based servers running Ubuntu 24.04 LTS. The instructions have been tested on an Azure `Dpls_v6` 32 core instance.

## Overview

You will learn how to build and configure ONNX Runtime to enable efficient LLM inference on Arm CPUs.

The tutorial covers the following steps:
- Building ONNX Runtime, quantizing and converting the Phi 3.5 vision model to the ONNX format.
- Running the model using a Python script with ONNX Runtime to perform LLM inference on the CPU.
- Analyzing the performance.

## Install dependencies

Install the following packages on your Arm-based server instance:

```bash
    sudo apt update
    sudo apt install python3-pip python3-venv cmake -y
```

## Create a requirements file

Use a file editor of your choice and create a `requirements.txt` file will the python packages shown below:

```python
    requests
    torch
    transformers
    accelerate
    huggingface-hub
    pyreadline3
```

## Install Python Dependencies

Create a virtual environment:
```bash
    python3 -m venv onnx-env
```

Activate the virtual environment:
```bash
    source onnx-env/bin/activate
```

Install the required libraries using pip:
```bash
    pip install -r requirements.txt
```
## Clone and build ONNX Runtime

Clone and build the `onnxruntime-genai` repository, which includes the Kleidi AI optimized ONNX Runtime, using the following commands:

```bash
    git clone https://github.com/microsoft/onnxruntime-genai.git
    cd onnxruntime-genai/
    python3 build.py --config Release
    cd build/Linux/Release/wheel/
    pip install onnxruntime_genai-0.9.0.dev0-cp312-cp312-linux_aarch64.whl
```

## Download and Quantize the Model

Navigate to the home directory, download the quantized model using `huggingface-cli`:
```bash
    cd ~
    huggingface-cli download microsoft/Phi-3.5-vision-instruct-onnx --include cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4/* --local-dir .
```

The Phi 3.5 vision model has now been successfully quantized into the ONNX format. The next step is to run the model using ONNX Runtime.
