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

## Objective
In this hands-on learning path, you will explore the practical aspects of running inference on an ONNX-formatted model for an image classification task. Specifically, the demonstration uses the widely used Modified National Institute of Standards and Technology (MNIST) dataset, illustrating how ONNX can be applied to accurately recognize handwritten digits, showcasing both the flexibility and simplicity offered by this standardized format.

## Before you begin
You need the following to complete the tutorial:  
### Python
At the time of this writing Python 3.13.3 was available. Use the installer for ARM64, which is available [here](https://www.python.org/ftp/python/3.13.3/python-3.13.3-arm64.exe). After running the installer, select "Add python.exe to PATH", and click Install Now:

[img1]

### A virtual environment with all the required packages

### A code editor 
 
The companion code is available for download [here](). 
