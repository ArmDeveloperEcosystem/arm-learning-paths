---
# User change
title: "Build ONNX Runtime and set up the Phi-3.5 Vision Model"

weight: 2

# Do not modify these elements
layout: "learningpathall"
---
## Overview

In this Learning Path, you'll run quantized Phi models with ONNX Runtime on Microsoft Azure Cobalt 100 servers. Specifically, you'll deploy the Phi-3.5 vision model on Arm-based servers running Ubuntu 24.04 LTS. These instructions have been tested on a 32-core Azure `Dpls_v6` instance.



You will learn how to build and configure ONNX Runtime to enable efficient LLM inference on Arm CPUs.

This Learning Path walks you through the following tasks:
- Build ONNX Runtime.
- Quantize and convert the Phi-3.5 vision model to ONNX format.
- Run the model using a Python script with ONNX Runtime for CPU-based LLM inference.
- Analyze performance on Arm CPUs.

## Install dependencies

On your Arm-based server, install the following packages:

```bash
    sudo apt update
    sudo apt install python3-pip python3-venv cmake -y
```

## Create a requirements file

Use a file editor of your choice and create a `requirements.txt` file with the Python packages shown below:

```python
    requests
    torch
    transformers
    accelerate
    huggingface-hub
    pyreadline3
```
{{% notice optional_title %}}
`pyreadline3` is typically used on Windows systems. You can safely omit it on Linux.
{{% /notice %}}


## Install Python dependencies

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
{{% notice optional_title %}}
Ensure you're using Python 3.12 to match the cp312 wheel format.
{{% /notice %}}

This build includes optimizations from Kleidi AI for efficient inference on Arm CPUs.

## Download and Quantize the Model

Navigate to your home directory. Now download the quantized model using `huggingface-cli`:
```bash
    cd ~
    huggingface-cli download microsoft/Phi-3.5-vision-instruct-onnx --include cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4/* --local-dir .
```

The Phi-3.5 vision model is now downloaded in ONNX format with INT4 quantization and is ready to run with ONNX Runtime.
