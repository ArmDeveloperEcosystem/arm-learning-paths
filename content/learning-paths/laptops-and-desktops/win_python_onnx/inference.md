---
# User change
title: "Running Inference"

weight: 4

layout: "learningpathall"
---

## Objective
You will now use the implemented code to run inference.

## Packages
Start by activating the virtual environment and installing the necessary Python packages. Activate the virtual environment:

```console
venv-x64\Scripts\activate.bat
```

Then install required packages:
```console
py -V:3.13 -m pip install onnxruntime numpy matplotlib wget torchvision torch
```

## Running Inference
To perform inference, run the following command:

```console
py -V:3.13 .\main.py  
```

The code will display a sample inference result similar to the image below:
![fig1](figures/01.webp)
Upon closing the displayed image, the script will output the computation time:
```output
PS C:\Users\db\onnx> py -V:3.13 .\main.py  
Computation time: 95.854 ms
PS C:\Users\db\onnx> py -V:3.13 .\main.py
Computation time: 111.230 ms
```


To compare results with Windows Arm 64, repeat the steps below using the Arm-64 Python architecture. Activate the Arm64 virtual environment and install packages:
```console
venv-arm64\Scripts\activate.bat
py -V:3.13-arm64 -m pip install onnxruntime numpy matplotlib wget torchvision torch
```

Run inference using Arm64:
```console
py -V:3.13-arm64 main.py
```

Note: The above Arm64 commands will function properly once ONNX Runtime becomes available for Windows Arm 64.

## Summary
In this learning path, you’ve learned how to use ONNX Runtime to perform inference on the MNIST dataset. You prepared your environment, implemented the necessary Python code, and measured the performance of your inference tasks.
