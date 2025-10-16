---
title: ONNX Installation
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## ONNX Installation on Azure Ubuntu Pro 24.04 LTS
To work with ONNX models on Azure, you will need a clean Python environment with the required packages. The following steps show you how to install Python, set up a virtual environment, and prepare for ONNX model execution using ONNX Runtime.


## Install Python and virtual environment

To get started, update your package list and install Python 3 along with the tools needed to create a virtual environment:

```console
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

Create and activate a virtual environment:

```console
python3 -m venv onnx-env
source onnx-env/bin/activate
```
{{% notice Note %}}Using a virtual environment isolates ONNX and its dependencies to avoid system conflicts.{{% /notice %}}

Once your environment is active, you're ready to install the required libraries.


## Install ONNX and required libraries

Upgrade pip and install ONNX with its runtime and supporting libraries:
```console
pip install --upgrade pip
pip install onnx onnxruntime fastapi uvicorn numpy
```
This installs ONNX libraries, FastAPI (for web serving, if you want to deploy models as an API), Uvicorn (ASGI server for FastAPI), and NumPy (for input tensor generation).

If you encounter errors during installation, check your internet connection and ensure you are using the activated virtual environment. For missing dependencies, try updating pip or installing system packages as needed.

After installation, you're ready to validate your setup.


## Validate ONNX and ONNX Runtime
Once the libraries are installed, verify that both ONNX and ONNX Runtime are correctly set up on your VM.

Create a file named `version.py` with the following code:
```python
import onnx  
import onnxruntime 

print("ONNX version:", onnx.__version__)
print("ONNX Runtime version:", onnxruntime.__version__)
```
Run the script:
```console
python3 version.py
```
You should see output similar to:
```output
ONNX version: 1.19.0
ONNX Runtime version: 1.23.0
```
If you see version numbers for both ONNX and ONNX Runtime, your environment is ready. If you get an ImportError, double-check that your virtual environment is activated and the libraries are installed.

Great job! You have confirmed that ONNX and ONNX Runtime are installed and ready on your Azure Cobalt 100 VM. This is the foundation for running inference workloads and serving ONNX models.


## Download and validate ONNX model: SqueezeNet
SqueezeNet is a lightweight convolutional neural network (CNN) architecture designed to provide accuracy close to AlexNet while using 50x fewer parameters and a much smaller model size. This makes it well-suited for benchmarking ONNX Runtime.

Now that your environment is set up and validated, you're ready to download and test the SqueezeNet model in the next step.
Download the quantized model:
```console
wget https://github.com/onnx/models/raw/main/validated/vision/classification/squeezenet/model/squeezenet1.0-12-int8.onnx -O squeezenet-int8.onnx
```
## Validate the model: 

After downloading the SqueezeNet ONNX model, the next step is to confirm that it is structurally valid and compliant with the ONNX specification. ONNX provides a built-in checker utility that verifies the graph, operators, and metadata.
Create a file named `validation.py` with the following code:

```python
import onnx

model = onnx.load("squeezenet-int8.onnx")
onnx.checker.check_model(model)
print("✅ Model is valid!")
```
Run the script:

```bash
python3 validation.py
```

You should see output similar to:
```output
✅ Model is valid!
```
With this validation, you have confirmed that the quantized SqueezeNet model is valid and ONNX-compliant. The next step is to run inference with ONNX Runtime and to benchmark performance.

ONNX installation and model validation are complete. You can now proceed with the baseline testing.
