---
title: Install ONNX, Validate Model, and Measure Performance
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Platform Overview
Whether you're using an Azure Linux 3.0 Docker container or a VM created from a custom Azure Linux 3.0 image, the deployment and benchmarking steps remain the same.

### Working inside Azure Linux 3.0 Docker container
The Azure Linux Container Host is an operating system image that's optimized for running container workloads on Azure Kubernetes Service (AKS). Microsoft maintains the Azure Linux Container Host and based it on CBL-Mariner, an open-source Linux 
distribution created by Microsoft. 
To know more about Azure Linux 3.0, kindly refer [What is Azure Linux Container Host for AKS](https://learn.microsoft.com/en-us/azure/azure-linux/intro-azure-linux). Azure Linux 3.0 offers support for Aarch64. However, the standalone VM image for Azure Linux 3.0 or CBL Mariner 3.0 is not available for Arm.

Hence, to use the default software stack provided by the Microsoft team, this guide will focus on creating a docker container with Azure Linux 3.0 as a base image and will build 
and run the onnx based application inside the container. 

### Create Azure Linux 3.0 Docker Container 
The [Microsoft Artifact Registry](https://mcr.microsoft.com/en-us/artifact/mar/azurelinux/base/core/about) offers updated docker image for the Azure Linux 3.0.  

To create a docker container, install docker, and then follow the below instructions: 

```console
$ sudo docker run -it --rm mcr.microsoft.com/azurelinux/base/core:3.0
``` 

The default container startup command is bash. tdnf and dnf are the default package managers.

### Install Python and Virtual Environment:

```console
$ tdnf update
$ tdnf install -y python3 python3-pip python3-virtualenv
```
Create and activate a virtual environment:

```console
$ python3 -m venv onnx-env
$ source onnx-env/bin/activate
```
{{% notice Note %}}Using a virtual environment isolates ONNX and its dependencies to avoid system conflicts.{{% /notice %}}

### Install ONNX and Required Libraries:

```console
$ pip install --upgrade pip
$ pip install onnx onnxruntime fastapi uvicorn numpy
```
This installs ONNX libraries along with FastAPI (web serving) and NumPy (for input tensor generation).

### Validate ONNX and ONNX Runtime:
Create **version.py** as below:

```python
import onnx  
import onnxruntime 

print("ONNX version:", onnx.version)  
print("ONNX Runtime version:", onnxruntime.__version__)  
```
Now, run version.py: 

```console
$ python3 version.py
```
Output:
```output
ONNX version: 1.18.0
ONNX Runtime version: 1.22.0
```
### Download and Validate ONNX Model - SqueezeNet:
SqueezeNet is a lightweight convolutional neural network (CNN) architecture designed to achieve comparable accuracy to AlexNet, but with fewer parameters and smaller model size. 

```console
$ wget https://github.com/onnx/models/raw/main/validated/vision/classification/squeezenet/model/squeezenet1.0-12-int8.onnx -O squeezenet-int8.onnx
```
#### Validate the model: 

Create a **vaildation.py** file with the code below for validation for ONNX model:

```python
import onnx

model = onnx.load("squeezenet-int8.onnx")
onnx.checker.check_model(model)
print("✅ Model is valid!")
```
Output:
```output
✅ Model is valid!
```
This downloads a quantized (INT8) classification model on the both VMs, and validates its structure using ONNX’s built-in checker. 

### Baseline testing using ONNX Runtime: 

This test measures the inference latency of the ONNX Runtime by timing how long it takes to process a single input using the `squeezenet-int8.onnx model`. It helps evaluate how efficiently the model runs on the target hardware.

Create a **baseline.py** file with the below code for baseline test of ONNX:

```python
import onnxruntime as ort
import numpy as np
import time

session = ort.InferenceSession("squeezenet-int8.onnx")
input_name = session.get_inputs()[0].name
data = np.random.rand(1, 3, 224, 224).astype(np.float32)

start = time.time()
outputs = session.run(None, {input_name: data})
end = time.time()

print("Inference time:", end - start)
```

Run the baseline test:

```console
$ python3 baseline.py
```
Output:
```output
Inference time: 0.02060103416442871
```
{{% notice Note %}}Inference time is the amount of time it takes for a trained machine learning model to make a prediction (i.e., produce output) after receiving input data. 
input tensor of shape (1, 3, 224, 224): 
- 1: batch size 
- 3: color channels (RGB) 
- 224 x 224: image resolution (common for models like SqueezeNet)
{{% /notice %}}

#### Output of ONNX baseline testing on the Arm VM: 

- Single inference latency: ~2.60 milliseconds (0.00260 sec) 
- This shows the initial (cold-start) inference performance of ONNX Runtime on CPU using an optimized int8 quantized model. 
- This demonstrates that the setup is fully working, and ONNX Runtime efficiently executes quantized models on Arm64. 
