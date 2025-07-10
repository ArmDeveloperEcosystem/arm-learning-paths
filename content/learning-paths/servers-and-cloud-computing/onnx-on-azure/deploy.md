---
title: ONNX Installation and Model Validation
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## ONNX Installation on Azure Linux 3.0
Install Python, create a virtual environment, and use pip to install ONNX, ONNX Runtime, and dependencies. Verify the setup and validate a sample ONNX model like SqueezeNet.

### Install Python and Virtual Environment:

```console
tdnf update
tdnf install -y python3 python3-pip python3-virtualenv
```
Create and activate a virtual environment:

```console
python3 -m venv onnx-env
source onnx-env/bin/activate
```
{{% notice Note %}}Using a virtual environment isolates ONNX and its dependencies to avoid system conflicts.{{% /notice %}}

### Install ONNX and Required Libraries:

```console
pip install --upgrade pip
pip install onnx onnxruntime fastapi uvicorn numpy
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
python3 version.py
```
You should see an output similar to:
```output
ONNX version: 1.18.0
ONNX Runtime version: 1.22.0
```
### Download and Validate ONNX Model - SqueezeNet:
SqueezeNet is a lightweight convolutional neural network (CNN) architecture designed to achieve comparable accuracy to AlexNet, but with fewer parameters and smaller model size. 

```console
wget https://github.com/onnx/models/raw/main/validated/vision/classification/squeezenet/model/squeezenet1.0-12-int8.onnx -O squeezenet-int8.onnx
```
#### Validate the model: 

Create a **vaildation.py** file with the code below for validation for ONNX model:

```python
import onnx

model = onnx.load("squeezenet-int8.onnx")
onnx.checker.check_model(model)
print("✅ Model is valid!")
```
You should see an output similar to:
```output
✅ Model is valid!
```
This downloads a quantized (INT8) classification model, and validates its structure using ONNX’s built-in checker. 

ONNX installation and model validation are complete. You can now proceed with the baseline testing.
