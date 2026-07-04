---
title: "Set up your development environment"

weight: 3

layout: "learningpathall"
---

## Objective

Prepare your development environment to build, export, run, and optimize ONNX models on Arm64 platforms. You will install Python, ONNX, and ONNX Runtime, and verify that your system correctly detects and uses available execution providers.

## Choose your hardware
You can use a variety of Arm64 platforms for this Learning Path:
* Edge boards (Linux/Arm64) - Raspberry Pi 4/5 (64-bit OS), Jetson (Arm64 CPU; GPU via CUDA if using NVIDIA stack), Arm-based servers.
* Apple Silicon (macOS/Arm64) - Great for development, deploy to Arm64 Linux later.
* Windows on Arm - Suitable for development and testing; deployment to Linux Arm64 systems is also possible.

One of ONNX's key advantages is that the same `.onnx` model file can run across all of these platforms, provided the required operators are supported by the runtime and execution providers available on the target system.

## Install Python on your platform

{{% notice Note %}}
ONNX Runtime provides prebuilt wheels only for specific Python versions. At the time of writing, Python 3.12 is not yet supported by ONNX Runtime on macOS or Arm platforms. If you see an error like:

```output
ERROR: No matching distribution found for onnxruntime
```

it usually means your Python version is too new. Python 3.10 is tested and recommended for this Learning Path.
{{% /notice %}}

Depending on your platform, follow different installation paths:

### Linux (Arm64)
```console
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-dev python3-pip build-essential libopenblas-dev libgl1 libglib2.0-0
```

If Python 3.10 is not available in your default repositories, you can use the deadsnakes PPA:
```console
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-dev
```

### macOS (Apple Silicon)

Install Python 3.10 using Homebrew:
```console
brew install python@3.10
```

After installation, use `python3.10` explicitly when creating virtual environments.

### Windows on Arm

Download and install Python 3.10 from [python.org](https://www.python.org/downloads/):

1. Select the ARM64 build for Windows
2. Run the installer
3. Check **Add Python to PATH** during installation
4. Verify the installation by opening Command Prompt and running `python --version`


## Create a Virtual Environment
After installing Python 3.10, create a clean virtual environment:

```console
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
```

On macOS, if `python3.10` is not found, use the full Homebrew path:
```console
/opt/homebrew/bin/python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
```

Using a virtual environment ensures dependency isolation and prevents conflicts with system-wide Python packages.

## Install Core Packages
Install the minimal ONNX toolchain:
```console
pip install onnx onnxruntime onnxscript netron numpy
```
This installs:
* onnx – core library for loading/saving ONNX models.
* onnxruntime – high-performance runtime to execute models.
* onnxscript – required for the new Dynamo-based exporter.
* netron – tool for visualizing ONNX models.
* numpy – used for tensor manipulation.

Now, install PyTorch(CPU build):

```console
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```
On Arm64 systems without discrete GPUs, the CPU build is sufficient. ONNX Runtime will later handle optimized inference execution.

## Verify the installation

You'll now validate the entire toolchain by defining a small PyTorch model, exporting it to ONNX, and running inference using ONNX Runtime.

Create a file named `01_Init.py`:

```python
import torch, torch.nn as nn
import onnx, onnxruntime as ort
import numpy as np

class SmallNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.seq = nn.Sequential(
            nn.Conv2d(1, 8, 3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1,1)),
            nn.Flatten(),
            nn.Linear(8, 10)
        )
    def forward(self, x): return self.seq(x)

m = SmallNet().eval()
dummy = torch.randn(1, 1, 28, 28)

torch.onnx.export(
    m, dummy, "smallnet.onnx",
    input_names=["input"], output_names=["logits"],
    opset_version=19,
    do_constant_folding=True,
    keep_initializers_as_inputs=False,
    dynamo=True       
)

# Quick sanity run
sess = ort.InferenceSession("smallnet.onnx", providers=["CPUExecutionProvider"])
out = sess.run(["logits"], {"input": dummy.numpy()})[0]
print("Output shape:", out.shape, "Providers:", sess.get_providers())
```

Run the script:

```console
python3 01_Init.py
```

You should see output similar to:
```output
python3 01_Init.py
[torch.onnx] Obtain model graph for `SmallNet([...]` with `torch.export.export(..., strict=False)`...
[torch.onnx] Obtain model graph for `SmallNet([...]` with `torch.export.export(..., strict=False)`... ✅
[torch.onnx] Run decomposition...
[torch.onnx] Run decomposition... ✅
[torch.onnx] Translate the graph into ONNX...
[torch.onnx] Translate the graph into ONNX... ✅
Output shape: (1, 10) Providers: ['CPUExecutionProvider']
```

The `01_Init.py` script serves as a quick end-to-end validation of your ONNX environment. It defines a very small convolutional neural network (SmallNet) in PyTorch, which consists of a convolution layer, activation function, pooling, flattening, and a final linear layer that outputs 10 logits. Instead of training the model, we simply run it in evaluation mode on a random input tensor to make sure the graph structure works. This model is then exported to the ONNX format using PyTorch’s new Dynamo-based exporter, producing a portable smallnet.onnx file.

After export, the script immediately loads the ONNX model with ONNX Runtime and executes a forward pass using the CPU execution provider. This verifies that the installation of ONNX, ONNX Runtime, and PyTorch is correct and that models can flow seamlessly from definition to inference. By printing the output tensor’s shape and the active execution provider, the script demonstrates that the toolchain is fully functional on your Arm64 device, giving you a solid baseline before moving on to more advanced models and optimizations.

## What you've learned and what's next

In this section, you installed Python 3.10 and the core ONNX toolchain on your Arm64 platform, created an isolated virtual environment, and verified the entire setup by exporting a small PyTorch model to ONNX and running inference with ONNX Runtime. Your development environment is now ready for model development and optimization.

Next, you'll build a complete neural network model, export it to ONNX format, and run it on Arm64 hardware to establish baseline performance metrics before applying optimization techniques.