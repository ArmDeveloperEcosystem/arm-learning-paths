---
# User change
title: "Build ONNX Runtime and set up the Phi-4-mini Model"

weight: 2

# Do not modify these elements
layout: "learningpathall"
---
## Overview

In this Learning Path, you'll run quantized Phi models with ONNX Runtime on Microsoft Azure Cobalt 100 servers.

Specifically, you'll deploy the Phi-4-mini model on Arm-based servers running Ubuntu 24.04 LTS.

{{% notice Note %}}
These instructions have been tested on a 32-core Azure `Dpls_v6` instance with 32 cores, 64GB of RAM, and 32GB of disk space.
{{% /notice %}}

You will learn how to build and configure ONNX Runtime to enable efficient LLM inference on Arm CPUs.

This Learning Path walks you through the following tasks:
- Build ONNX Runtime.
- Quantize and convert the Phi-4-mini model to ONNX format.
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
    pandas
    numpy
    psutil
    packaging
    setuptools
    requests
```

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

Clone, build, and install the `onnxruntime` repository using the following commands:

```bash
git clone --recursive https://github.com/microsoft/onnxruntime.git
cd onnxruntime
./build.sh --config Release --build_shared_lib --parallel --build_wheel --skip_tests --update --build
cd build/Linux/Release
cmake --install . --prefix install
cd dist
pip install onnxruntime-*.whl
```

This process builds and installs ONNX Runtime with optimizations for efficient inference on Arm CPUs.

## Clone and build ONNX Runtime genai

Clone and build the `onnxruntime-genai` repository:

```bash
cd ~
cp ./onnxruntime/build/Linux/Release/install/include/onnxruntime/onnxruntime_float16.h ./onnxruntime/build/Linux/Release/install/include/onnxruntime_float16.h
cp ./onnxruntime/build/Linux/Release/install/include/onnxruntime/onnxruntime_c_api.h ./onnxruntime/build/Linux/Release/install/include/onnxruntime_c_api.h
git clone https://github.com/microsoft/onnxruntime-genai.git
cd onnxruntime-genai
python3 build.py --config Release --update --ort_home ../onnxruntime/build/Linux/Release/install
python3 build.py --config Release --build --skip_tests --ort_home ../onnxruntime/build/Linux/Release/install
cd build/Linux/Release/wheel
pip install onnxruntime_genai-*.whl
```

{{% notice Note %}}
Ensure you're using Python 3.12 to match the cp312 wheel format.
{{% /notice %}}

This build includes optimizations from KleidiAI for efficient inference on Arm CPUs.

## Download and quantize the model

Navigate to your home directory. Now download the quantized model using `huggingface-cli`:
```bash
    cd ~
    huggingface-cli download microsoft/Phi-4-mini-instruct-onnx --include cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4/* --local-dir .
```

The Phi-4-mini model is now downloaded in ONNX format with INT4 quantization and is ready to run with ONNX Runtime.
