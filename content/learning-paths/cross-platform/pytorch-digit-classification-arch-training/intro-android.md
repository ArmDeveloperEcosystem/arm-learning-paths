---
# User change
title: "Learn about Inference on Android"

weight: 7

layout: "learningpathall"
---

Running pre-trained machine learning models on mobile and edge devices has become increasingly common as it enables these devices to gain intelligence and perform complex tasks directly on-device. This capability allows smartphones, IoT devices, and embedded systems to execute advanced functions such as image recognition, natural language processing, and real-time decision-making without relying on cloud-based services. 

By leveraging on-device inference, applications can offer faster responses, reduced latency, enhanced privacy, and offline functionality, making them more efficient and capable of handling sophisticated tasks in various environments.

Arm provides a wide range of hardware and software accelerators designed to optimize the performance of machine learning (ML) models on edge devices. These include specialized processors like Arm's Neural Processing Units (NPUs) and Graphics Processing Units (GPUs), as well as software frameworks like the Arm Compute Library and Arm NN, which are tailored to leverage these hardware capabilities. 

Running a machine learning model on Android involves a few key steps. 

* You train and save the model in a mobile-friendly format, such as TensorFlow Lite, ONNX, or TorchScript, depending on the framework you are using. 

* You add the model file to your Android project's assets directory. In your application's code, use the corresponding framework's Android library, such as TensorFlow Lite or PyTorch Mobile, to load the model. 

* You prepare the input data, ensuring it is formatted and preprocessed in the same way as during model training. The input data is passed through the model, and the output predictions are retrieved and interpreted accordingly.

For improved performance, you can leverage hardware acceleration using Android’s Neural Networks API (NNAPI) or use GPU support if available. This process enables the Android app to make real-time predictions and execute complex machine learning tasks directly on the device.

In this Learning Path, you will learn how to perform inference in an Android application using the pre-trained digit classifier from the previous sections. 

## Before you begin

Before you begin make [Android Studio](https://developer.android.com/studio/install) is installed on your system.

## Project Source Code

The following steps explain how to build an Android application for MNIST inference. The application can be constructed from scratch, but there are two GitHub repositories available if you need to copy any files from them as you learn how to create the Android application. 

The complete source code for the [Android application](https://github.com/dawidborycki/Arm.PyTorch.MNIST.Inference.git) is available on GitHub. 

The [Python scripts](https://github.com/dawidborycki/Arm.PyTorch.MNIST.Inference.Python.git) used in the previous steps are also available on GitHub.
