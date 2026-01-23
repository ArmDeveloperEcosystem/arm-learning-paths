---
# User change
title: "Environment Setup"

weight: 3

layout: "learningpathall"
---

## Objective
This step gets you ready to build, export, run, and optimize ONNX models on Arm64. You’ll set up Python, install ONNX & ONNX Runtime, confirm hardware-backed execution providers.

## Choosing the hardware
You can choose a variety of hardware, including:
* Edge boards (Linux/Arm64) - Raspberry Pi 4/5 (64-bit OS), Jetson (Arm64 CPU; GPU via CUDA if using NVIDIA stack), Arm servers (e.g., AWS Graviton).
* Apple Silicon (macOS/Arm64) - Great for development, deploy to Arm64 Linux later.
* Windows on Arm - Dev/test on WoA, deploy to Linux Arm64 for production if desired.

The nice thing about ONNX is that the **same model file** can run across all of these, so your setup is flexible.

## Install Python
Depending on the hardware you use you follow different installation paths

1. Linux (Arm64). In the console type:
```console
sudo apt update
sudo apt install -y python3 python3-venv python3-pip build-essential libopenblas-dev libgl1 libglib2.0-0
```

2. macOS (Apple Sillicon):
```console
brew install python
```

3. Windows on Arm:
* Install Python 3.10+ from python.org (Arm64 build).
* Ensure pip is on PATH.

After installing Python, open a terminal or console, create a clean virtual environment, and update pip and wheel:

```console
python3 -m venv .venv
source .venv/bin/activate                   # on Windows use: .venv\Scripts\activate
python -m pip install --upgrade pip wheel
```

Using a virtual environment keeps dependencies isolated and avoids conflicts with system-wide Python packages.

## Install Core Packages
Start by installing the minimal stack:
```console
pip install onnx onnxruntime onnxscript netron numpy
```
The above will install the following:
* onnx – core library for loading/saving ONNX models.
* onnxruntime – high-performance runtime to execute models.
* onnxscript – required for the new Dynamo-based exporter.
* netron – tool for visualizing ONNX models.
* numpy – used for tensor manipulation.

Now, install PyTorch (we’ll use it later to build and export a sample model):

```console
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

## Verify the installation
Let’s verify everything works end-to-end by training a toy network and exporting it to ONNX.

Create a new file 01_Init.py and add the following code

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

Then, run it as follows

```console
python3 01_Init.py
```

You should see the following output:
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

The 01_Init.py script serves as a quick end-to-end validation of your ONNX environment. It defines a very small convolutional neural network (SmallNet) in PyTorch, which consists of a convolution layer, activation function, pooling, flattening, and a final linear layer that outputs 10 logits. Instead of training the model, we simply run it in evaluation mode on a random input tensor to make sure the graph structure works. This model is then exported to the ONNX format using PyTorch’s new Dynamo-based exporter, producing a portable smallnet.onnx file.

After export, the script immediately loads the ONNX model with ONNX Runtime and executes a forward pass using the CPU execution provider. This verifies that the installation of ONNX, ONNX Runtime, and PyTorch is correct and that models can flow seamlessly from definition to inference. By printing the output tensor’s shape and the active execution provider, the script demonstrates that the toolchain is fully functional on your Arm64 device, giving you a solid baseline before moving on to more advanced models and optimizations.

## Summary
You now have a fully functional ONNX development environment on Arm64. Python and all required packages are installed, and you successfully exported a small PyTorch model to ONNX using the new Dynamo exporter, ensuring forward compatibility. Running the model with ONNX Runtime confirmed that inference works end-to-end with the CPU execution provider, proving that your toolchain is correctly configured. With this foundation in place, the next step is to build and export a more complete model and run it on Arm64 hardware to establish baseline performance before applying optimizations.
