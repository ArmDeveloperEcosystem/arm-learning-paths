---
# User change
title: "Prepare a PyTorch development environment"

weight: 2

layout: "learningpathall"
---

## Introduction to PyTorch

PyTorch is an open-source deep learning framework that is developed by Meta AI and is now part of the Linux Foundation.

PyTorch is designed to provide a flexible and efficient platform for building and training neural networks. It is widely used due to its dynamic computational graph, which allows users to modify the architecture during runtime, making debugging and experimentation easier. 

PyTorch's objective is to provide a more flexible, user-friendly deep learning framework that addresses the limitations of static computational graphs found in earlier tools like TensorFlow. 

Prior to PyTorch, many frameworks used static computation graphs that require the entire model structure to be defined before training, making experimentation and debugging cumbersome. PyTorch introduced dynamic computational graphs, also known as “define-by-run”, that allow the graph to be constructed dynamically as operations are executed. This flexibility significantly improves ease of use for researchers and developers, enabling faster prototyping, easier debugging, and more intuitive code.


Additionally, PyTorch seamlessly integrates with Python, encouraging a native coding experience. Its deep integration with GPU acceleration also makes it a powerful tool for both research and production environments. This combination of flexibility, usability, and performance has contributed to PyTorch’s rapid adoption, especially in academic research, where experimentation and iteration are crucial.

A typical process for creating a feedforward neural network in PyTorch involves defining a sequential stack of fully-connected layers, which are also known as linear layers. Each layer transforms the input by applying a set of weights and biases, followed by an activation function like ReLU. PyTorch supports this process using the torch.nn module, where layers are easily defined and composed.

To create a model, users subclass the torch.nn.Module class, defining the network architecture in the __init__ method, and implement the forward pass in the forward method. PyTorch’s intuitive API and support for GPU acceleration make it ideal for building efficient feedforward networks, particularly in tasks such as image classification and digit recognition.

In this Learning Path, you will explore how to use PyTorch to create and train a model for digit recognition.

## Before you begin

Before you begin make sure Python3 is installed on your system. You can check this by running:

```console
python3 --version
```

The expected output is the Python version, for example:

```output
Python 3.11.2
```

If Python3 is not installed, download and install it from [python.org](https://www.python.org/downloads/). 

Alternatively, you can also install Python3 using package managers such as Homebrew or APT. 

If you are using Windows on Arm you can refer to the [Python install guide](https://learn.arm.com/install-guides/py-woa/).

Next, download and install [Visual Studio Code](https://code.visualstudio.com/download).

## Install PyTorch and additional Python packages

To prepare a virtual Python environment, install PyTorch, and the additional tools you will need for this Learning Path:

1. Open a terminal or command prompt and navigate to your project directory. 

2. Create a virtual environment by running:

```console
python -m venv pytorch-env
```

This will create a virtual environment named pytorch-env. 

3. Activate the virtual environment:

* On Windows:
```console
pytorch-env\Scripts\activate
```

* On macOS or Linux: 
```console
source pytorch-env/bin/activate
```

Once activated, you see the virtual environment name `(pytorch-env)` before your terminal prompt.

3. Install PyTorch using Pip:

```console
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

4. Install torchsummary, Jupyter and IPython Kernel:

```console
pip install torchsummary
pip install jupyter
pip install ipykernel
```

5. Register your virtual environment as a new kernel:

```console
python3 -m ipykernel install --user --name=pytorch-env
```

6. Install the Jupyter Extension in VS Code:

* Open VS Code and go to the Extensions view (click on the Extensions icon or press Ctrl+Shift+X).

* Search for “Jupyter” and install the official Jupyter extension.

* Optionally, also install the Python extension if you haven’t already, as it improves Python language support in VS Code.

To ensure everything is set up correctly:

1. Open Visual Studio Code. 
2. Click New file, and select `Jupyter Notebook .ipynb Support`.
3. Save the file as `pytorch-digits.ipynb`.
4. Select the Python kernel you created earlier (pytorch-env). To do so, click Kernels in the top right corner. Then, click Jupyter Kernel..., and you will see the Python kernel as shown below:

![img1](Figures/1.png)

5. In your Jupyter notebook, run the following code to verify PyTorch is working correctly:

```console
import torch
print(torch.__version__)
```

It will look as follows:
![img2](Figures/2.png)

With your development environment created, you can proceed to creating a PyTorch model.
