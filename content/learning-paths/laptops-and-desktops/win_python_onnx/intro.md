---
# User change
title: "Introduction"

weight: 2

layout: "learningpathall"
---

## What is ONNX?
Open Neural Network Exchange (ONNX) provides a portable, interoperable standard for machine learning (ML). It is an open-source format that enables representation of ML models through a common set of operators and a standardized file format. These operators serve as fundamental building blocks in machine learning and deep learning models, facilitating compatibility and ease of integration across various platforms.

Machine learning practitioners frequently create ML models using diverse frameworks such as PyTorch, TensorFlow, scikit-learn, Core ML, and Azure AI Custom Vision. However, each framework has its own unique methods for creating, storing, and utilizing models. This diversity poses significant challenges when deploying trained models across different environments or executing inference tasks using hardware-accelerated tools or alternate programming languages. For example, deploying models on edge devices or Arm64-powered hardware often necessitates using programming languages other than Python to fully exploit specialized hardware features, such as dedicated neural network accelerators.

By defining a unified and standardized format, ONNX effectively addresses these interoperability challenges. With ONNX, you can easily develop models using your preferred framework and export these models to the ONNX format. Additionally, the ONNX ecosystem includes robust runtime environments (such as ONNX Runtime), enabling efficient inference across multiple hardware platforms and diverse programming languages, including C++, C#, and Java, beyond Python alone.

ONNX Runtime, in particular, provides optimized inference capabilities, supporting execution on CPUs, GPUs, and specialized accelerators, thus significantly improving performance and efficiency for deployment in production environments and edge devices.

Several major ML frameworks currently support exporting models directly to the ONNX format, including Azure AI Custom Vision, Core ML, PyTorch, TensorFlow, and scikit-learn, streamlining the workflow from model development to deployment.

The [companion code](https://github.com/dawidborycki/ONNX.WoA/tree/main) is available on GitHub.

## Objective
In this hands-on learning path, you will explore the practical aspects of running inference on an ONNX-formatted model for an image classification task. Specifically, the demonstration uses the widely used Modified National Institute of Standards and Technology (MNIST) dataset, illustrating how ONNX can be applied to accurately recognize handwritten digits, showcasing both the flexibility and simplicity offered by this standardized format.

## Before you Begin
Ensure you have the following prerequisites installed to complete this tutorial:

### Python
At the time of writing, Python 3.13.3 is available. You can download it using the links below
1. [Windows x64 (64-bit)](https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe)
2. [Windows ARM64](https://www.python.org/ftp/python/3.13.3/python-3.13.3-arm64.exe)

Install both Python versions as required. After installation, confirm both are available by running the following command in your console

```console
py --list
```

The output should look like this:

```output
py --list       
 -V:3.13 *        Python 3.13 (64-bit)
 -V:3.13-arm64    Python 3.13 (ARM64)
```

### Creating a Virtual Environment
Create a virtual environment tailored to your Python installation's architecture. For the 64-bit Python environment, use:
```console
py -V:3.13 -m venv venv-x64 
```

For arm64 use the following command:
```console
py -V:3.13-arm64 -m venv venv-arm64
```

By using different virtual environments, you can compare the performance of the same code across different architectures. However, at the time of writing, ONNX Runtime is unavailable as a Python wheel for Windows ARM64. Therefore, the subsequent instructions apply only to Windows x64.

### A Code Editor 
For this demonstration we use Visual Studio Code. [Download Visual Studio Code](https://code.visualstudio.com/download).

## Pre-trained Models
Many pre-trained models are available in the ONNX format ([ONNX Model Zoo](https://github.com/onnx/models)). There are models for image classification, image recognition, machine translation, language modeling, speech, audio processing, and more. 
 
In this tutorial, you will use the pre-trained model for [handwritten digit recognition](https://github.com/onnx/models/tree/main/validated/vision/classification/mnist) — the deep learning convolutional neural model trained on the popular MNIST dataset
