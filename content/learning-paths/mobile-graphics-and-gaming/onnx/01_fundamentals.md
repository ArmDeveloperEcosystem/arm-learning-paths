---
# User change
title: "ONNX Fundamentals"

weight: 2

layout: "learningpathall"
---
The goal of this tutorial is to provide a practical, end-to-end introduction to working with Open Neural Network Exchange (ONNX) in real-world scenarios. You will build a simple neural network model in Python, export it to the ONNX format, and run inference on Arm64 platforms using ONNX Runtime. Along the way, you will learn about model optimization techniques such as layer fusion, and conclude by deploying the optimized model into a fully functional Android application. By the end of this learning path, you will understand both the conceptual foundations of ONNX and the practical steps required to move a model from training to efficient deployment on Arm-based systems.

## What is ONNX
ONNX (Open Neural Network Exchange) is an open standard for representing machine learning models as a framework-independent intermediate representation (IR). Instead of relying on the internal model format of a specific framework—such as PyTorch or TensorFlow, ONNX defines a common computational graph structure, standardized operators, and well-specified data types.
At its core, an ONNX model is a directed acyclic graph (DAG). Nodes represent mathematical operations (such as Conv, MatMul, or Relu), while edges represent tensors flowing between these operations. The model file stores both the graph structure and the trained parameters (weights), making it self-contained and executable without the original training framework.

In practice, portability depends on operator support and opset compatibility within the chosen runtime. However, ONNX reduces the friction of moving models across frameworks and hardware targets by standardizing operator semantics and graph representation.

ONNX was originally developed by Microsoft and Facebook to address a growing need in the machine learning community: the ability to move models seamlessly between training environments and deployment targets. Today, it is supported by a wide ecosystem of contributors and hardware vendors, making it a widely adopted standard for model exchange and deployment.

For developers, this means flexibility. You can train your model in PyTorch, export it to ONNX, run it with ONNX Runtime on an Arm64 device such as a Raspberry Pi, and later deploy it inside an Android application without rewriting the model. This portability is the main reason ONNX has become a central building block in modern AI workflows.

A helpful analogy is to think of ONNX as a “PDF for machine learning models.” Just as a PDF preserves the structure of a document across operating systems and viewers, ONNX preserves the structure and semantics of a trained model across frameworks and hardware platforms.

Importantly, ONNX is also extensible. Developers and hardware vendors can define custom operators or operator domains when the standard operator set is not sufficient. This allows innovation and hardware-specific acceleration while maintaining compatibility with the broader ONNX ecosystem.

## Why ONNX Matters
Modern machine learning workflows span multiple frameworks and deployment targets. A model might be trained in PyTorch on a GPU workstation, validated in the cloud, and ultimately deployed on an Arm64-based edge device or Android smartphone. Without a common representation, moving models between these environments would require complex and error-prone conversions.
ONNX addresses this challenge by acting as a universal exchange format that separates model development from deployment.

The key reasons ONNX matters are:
1. Interoperability – ONNX decouples training from inference. Models trained in PyTorch or TensorFlow can be exported into a common format and executed in a different runtime environment without embedding the original framework.
2. Performance – ONNX Runtime includes highly optimized execution backends, supporting hardware acceleration through Arm NEON, CUDA, DirectML, and Android NNAPI. This means the same model can run efficiently across a wide spectrum of hardware.
3. Portability – A single `.onnx` model file can be deployed across Arm-based cloud servers, embedded Arm devices, and mobile applications, provided the required operators are supported by the target runtime.
4. Ecosystem – The ONNX Model Zoo and broad industry adoption make it easier to reuse validated architectures across platforms.
5. Extensibility – Custom operators and execution providers allow researchers and hardware vendors to extend ONNX without breaking compatibility with the broader ecosystem.

## ONNX Model Structure
An ONNX model is a complete description of a computation graph, not just a collection of weights. Understanding its structure clarifies why it is both portable and extensible.
At a high level, an ONNX model consists of:
1. Graph - The core directed acyclic graph (DAG). Nodes correspond to operations (such as Conv, Relu, or MatMul), and edges represent tensors flowing between nodes.
2. Initializers – These store learned parameters such as weights and biases. Initializers are embedded directly in the model file.
3. Opset (Operator Set) - A versioned collection of operator definitions. Opsets define the exact semantics of each operator and ensure compatibility between model exporters and runtimes. Selecting an appropriate opset version during export is critical for deployment compatibility.
4. Metadata - These describe tensor shapes, data types, input/output signatures, and optional annotations such as author information or framework version.
5. Operator Domains – Namespaces that allow standard and custom operators to coexist without conflict.

This design allows ONNX to describe anything from a simple logistic regression to a deep convolutional neural network. For example, a single ONNX graph might define:
* An input tensor representing a camera image.
* A sequence of convolution and pooling layers.
* Fully connected layers leading to classification probabilities.
* An output tensor with predicted labels.

This structured design enables ONNX to represent models ranging from simple linear regression to complex deep neural networks. Tools such as Netron allow developers to visualize the graph, while runtimes such as ONNX Runtime parse and execute it efficiently.

Because the model is graph-based, developers can modify it programmatically - adding, removing, or replacing nodes. This graph-level flexibility enables optimization techniques such as operator fusion, constant folding, and quantization, which you will explore later.

## ONNX Runtime
While ONNX defines how a model is represented, ONNX Runtime (ORT) is responsible for executing that model efficiently. ORT is the official open-source runtime for ONNX models and is optimized for performance, portability, and modular hardware acceleration.
Key characteristics of ONNX Runtime include:
1. Cross-platform support: ORT runs on Windows, Linux, and macOS, as well as mobile platforms like Android and iOS. It supports both x86 and Arm64 architectures, making it suitable for deployment from cloud servers to edge devices such as Raspberry Pi boards and smartphones.

2. Hardware acceleration: ORT integrates with a wide range of execution providers (EPs) that tap into hardware capabilities:
* Arm Kleidi kernels accelerated with Arm NEON, SVE2, and SME2 instructions for efficient CPU execution on Arm64.
* CUDA for NVIDIA GPUs.
* DirectML for Windows.
* NNAPI on Android, enabling direct access to mobile accelerators (DSPs, NPUs).

3. Primarily inference-focused: ONNX Runtime includes optional training capabilities, but it is most widely used for high-performance inference in production and edge deployments.

4. Built-in Optimizations: ORT can automatically apply graph optimizations such as constant folding, operator fusion, or memory layout changes to squeeze more performance out of your model.

By abstracting hardware differences behind execution providers, ONNX Runtime enables a single ONNX model to run across heterogeneous systems while still leveraging platform-specific optimizations.

## How ONNX Fits into the Workflow
One of ONNX’s greatest strengths is how naturally it integrates into a modern ML workflow. Instead of locking developers into a single framework from training to deployment, ONNX acts as a bridge between stages.
A typical ONNX workflow looks like this:
1. Train the model: You first use your preferred framework (e.g., PyTorch, TensorFlow, or scikit-learn) to design and train a model. At this stage, you benefit from the flexibility and ecosystem of the framework of your choice.
2. Export to ONNX: Once trained, the model is exported into the ONNX format using built-in converters (such as torch.onnx.export for PyTorch). This produces a portable .onnx file describing the network architecture, weights, and metadata.
3. Run inference with ONNX Runtime: The ONNX model can now be executed on different devices using ONNX Runtime. On Arm64 hardware, ONNX Runtime can take advantage of Arm Kleidi kernels accelerated with NEON, SVE2, and SME2 instructions, while on Android devices it can leverage NNAPI to access mobile accelerators (where available).
4. Optimize the model: Apply graph optimizations like layer fusion, constant folding, or quantization to improve performance and reduce memory usage, making the model more suitable for edge and mobile deployments.
5. Deploy: Finally, the optimized ONNX model is packaged into its target environment. This could be an Arm64-based embedded system (e.g., Raspberry Pi), a server powered by Arm CPUs (e.g., AWS Graviton), or an Android application distributed via the Play Store.

This modularity means developers are free to mix and match the best tools for each stage: train in PyTorch, optimize with ONNX Runtime, and deploy to Android—all without rewriting the model. By decoupling training from inference, ONNX enables efficient workflows that span from research experiments to production-grade applications.

## Example Use Cases
ONNX is already widely adopted in real-world applications where portability and performance are critical. A few common examples include:
1. Computer Vision at the Edge – Running an object detection model (e.g., YOLOv5 exported to ONNX) on a Raspberry Pi 4 or NVIDIA Jetson, enabling low-cost cameras to detect people, vehicles, or defects in real time.
2. Mobile Applications – Deploying face recognition or image classification models inside an Android app using ONNX Runtime Mobile, with NNAPI acceleration for efficient on-device inference.
3. Natural Language Processing (NLP) – Running BERT-based models on Arm64 cloud servers (like AWS Graviton) to provide fast, low-cost inference for chatbots and translation services.
4. Healthcare Devices – Using ONNX to integrate ML models into portable diagnostic tools or wearable sensors, where Arm64 processors dominate due to their low power consumption.
5. Cross-platform Research to Production – Training experimental architectures in PyTorch, exporting them to ONNX, and validating them across different backends to ensure consistent performance.
6. AI Accelerator Integration – ONNX is especially useful for hardware vendors building custom AI accelerators. Since accelerators often cannot support the full range of ML operators, ONNX’s extensible operator model allows manufacturers to plug in custom kernels where hardware acceleration is available, while gracefully falling back to the standard runtime for unsupported ops. This makes it easier to adopt new hardware without rewriting entire models.

This section introduces ONNX and ONNX Runtime for portable, high-performance inference on Arm64 and Android, and prepares you to set up Python, install the required tools, and verify hardware-backed execution providers before building and optimizing models.
