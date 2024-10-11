---
# User change
title: "Background"

weight: 2

layout: "learningpathall"
---

Running pre-trained machine learning models on mobile and edge devices has become increasingly common as it enables these devices to gain intelligence and perform complex tasks directly on-device. This capability allows smartphones, IoT devices, and embedded systems to execute advanced functions such as image recognition, natural language processing, and real-time decision-making without relying on cloud-based services. By leveraging on-device inference, applications can offer faster responses, reduced latency, enhanced privacy, and offline functionality, making them more efficient and capable of handling sophisticated tasks in various environments.

Arm provides a wide range of hardware and software accelerators designed to optimize the performance of machine learning (ML) models on edge devices. These include specialized processors like Arm's Neural Processing Units (NPUs) and Graphics Processing Units (GPUs), as well as software frameworks like the Arm Compute Library and Arm NN, which are tailored to leverage these hardware capabilities. Arm's technology is ubiquitous, powering a vast array of devices from smartphones and tablets to IoT gadgets and embedded systems. With Arm chips being the core of many Android-based smartphones and other devices, running ML models efficiently on this hardware is crucial for enabling advanced applications such as image recognition, voice assistance, and real-time analytics. By utilizing Arm’s accelerators, developers can achieve lower latency, reduced power consumption, and enhanced performance, making on-device AI both practical and powerful for a wide range of applications.

Running a machine learning model on Android involves a few key steps. First, you need to train and save the model in a mobile-friendly format, such as TensorFlow Lite, ONNX, or TorchScript, depending on the framework you are using. Next, you add the model file to your Android project’s assets directory. In your app’s code, use the corresponding framework’s Android library, such as TensorFlow Lite or PyTorch Mobile, to load the model. You then prepare the input data, ensuring it is formatted and preprocessed in the same way as during model training. The input data is passed through the model, and the output predictions are retrieved and interpreted accordingly. For improved performance, you can leverage hardware acceleration using Android’s Neural Networks API (NNAPI) or use GPU support if available. This process enables the Android app to make real-time predictions and execute complex machine learning tasks directly on the device.

In this Learning Path, you will learn how to perform such inference in the Android app using a pre-trained digit classifier, created [here](learning-paths/cross-platform/pytorch-digit-classification-training).

## Before you begin
Before you begin make sure Python3, [Visual Studio Code](https://code.visualstudio.com/download) and [Android Studio](https://developer.android.com/studio/install) are installed on your system.

## Source code
The complete source code is available [here](https://github.com/dawidborycki/Arm.PyTorch.MNIST.Inference.git). 

The Python scripts are available [here](https://github.com/dawidborycki/Arm.PyTorch.MNIST.Inference.Python.git)
