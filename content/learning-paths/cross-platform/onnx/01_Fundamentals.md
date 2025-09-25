---
# User change
title: "ONNX Fundamentals"

weight: 2

layout: "learningpathall"
---
The goal of this tutorial is to provide developers with a practical, end-to-end pathway for working with Open Neural Network Exchange (ONNX) in real-world scenarios. Starting from the fundamentals, we will build a simple neural network model in Python, export it to the ONNX format, and demonstrate how it can be used for both inference and training on Arm64 platforms. Along the way, we will cover model optimization techniques such as layer fusion, and conclude by deploying the optimized model into a fully functional Android application. By following this series, you will gain not only a solid understanding of ONNX’s philosophy and ecosystem but also the hands-on skills required to integrate ONNX into your own projects—from prototyping to deployment.

In this first step, we will introduce the ONNX standard and explain why it has become a cornerstone of modern machine learning workflows. You will learn what ONNX is, how it represents models in a framework-agnostic format, and why this matters for developers targeting different platforms such as desktops, Arm64 devices, or mobile environments. We will also discuss the role of ONNX Runtime as the high-performance engine that brings these models to life, enabling efficient inference and even training across CPUs, GPUs, and specialized accelerators. Finally, we will outline the typical ONNX workflow—from training in frameworks like PyTorch or TensorFlow, through export and optimization, to deployment on edge and Android devices—which we will gradually demonstrate throughout the tutorial.

## What is ONNX
The ONNX is an open standard for representing machine learning models in a framework-independent format. Instead of being tied to the internal model representation of a specific framework—such as PyTorch, TensorFlow, or scikit-learn—ONNX provides a universal way to describe models using a common set of operators, data types, and computational graphs.

At its core, an ONNX model is a directed acyclic graph (DAG) where nodes represent mathematical operations (e.g., convolution, matrix multiplication, activation functions) and edges represent tensors flowing between these operations. This standardized representation allows models trained in one framework to be exported once and executed anywhere, without requiring the original framework at runtime.

ONNX was originally developed by Microsoft and Facebook to address a growing need in the machine learning community: the ability to move models seamlessly between training environments and deployment targets. Today, it is supported by a wide ecosystem of contributors and hardware vendors, making it the de facto choice for interoperability and cross-platform deployment.

For developers, this means flexibility: you can train your model in PyTorch, export it to ONNX, run it with ONNX Runtime on an Arm64 device such as a Raspberry Pi, and later deploy it inside an Android application without rewriting the model. This portability is the main reason ONNX has become a central building block in modern AI workflows.

A useful way to think of ONNX is to compare it to a PDF for machine learning models. Just as a PDF file ensures that a document looks the same regardless of whether you open it in Adobe Reader, Preview on macOS, or a web browser, ONNX ensures that a machine learning model behaves consistently whether you run it on a server GPU, a Raspberry Pi, or an Android phone. It is this “write once, run anywhere” principle that makes ONNX especially powerful for developers working across diverse hardware platforms.

At the same time, ONNX is not a closed box. Developers can extend the format with custom operators or layers when standard ones are not sufficient. This flexibility makes it possible to inject novel research ideas, proprietary operations, or hardware-accelerated kernels into an ONNX model while still benefiting from the portability of the core standard. In other words, ONNX gives you both consistency across platforms and extensibility for innovation.

## Why ONNX Matters
Machine learning today is not limited to one framework or one device. A model might be trained in PyTorch on a GPU workstation, tested in TensorFlow on a cloud server, and then finally deployed on an Arm64-based edge device or Android phone. Without a common standard, moving models between these environments would be complex, error-prone, and often impossible. ONNX solves this problem by acting as a universal exchange format, ensuring that models can flow smoothly across the entire development and deployment pipeline.

The main reasons ONNX matters are:
1. Interoperability – ONNX eliminates framework lock-in. You can train in PyTorch, validate in TensorFlow, and deploy with ONNX Runtime on almost any device, from servers to IoT boards.
2. Performance – ONNX Runtime includes highly optimized execution backends, supporting hardware acceleration through Arm NEON, CUDA, DirectML, and Android NNAPI. This means the same model can run efficiently across a wide spectrum of hardware.
3. Portability – Once exported to ONNX, the model can be deployed to Arm64 devices (like Raspberry Pi or AWS Graviton servers) or even embedded in an Android app, without rewriting the code.
4. Ecosystem – The ONNX Model Zoo provides ready-to-use, pre-trained models for vision, NLP, and speech tasks, making it easy to start from state-of-the-art baselines.
5. Extensibility – Developers can inject their own layers or custom operators when the built-in operator set is not sufficient, enabling innovation while preserving compatibility.

In short, ONNX matters because it turns the fragmented ML ecosystem into a cohesive workflow, empowering developers to focus on building applications rather than wrestling with conversion scripts or hardware-specific code.

## ONNX Model Structure
An ONNX model is more than just a collection of weights—it is a complete description of the computation graph that defines how data flows through the network. Understanding this structure is key to seeing why ONNX is both portable and extensible.

At a high level, an ONNX model consists of three main parts:
1. Graph, which is the heart of the model, represented as a directed acyclic graph (DAG). In this graph nodes correspond to operations (e.g., Conv, Relu, MatMul), edges represent tensors flowing between nodes, carrying input and output data.
2. Opset (Operator Set), which is a versioned collection of supported operations. Opsets guarantee that models exported with one framework will behave consistently when loaded by another, as long as the same opset version is supported.
3. Metadata, which contains information about inputs, outputs, tensor shapes, and data types. Metadata can also include custom annotations such as the model author, domain, or framework version.

This design allows ONNX to describe anything from a simple logistic regression to a deep convolutional neural network. For example, a single ONNX graph might define:
* An input tensor representing a camera image.
* A sequence of convolution and pooling layers.
* Fully connected layers leading to classification probabilities.
* An output tensor with predicted labels.

Because the ONNX format is based on a standardized graph representation, it is both human-readable (with tools like Netron for visualization) and machine-executable (parsed directly by ONNX Runtime or other backends).

Importantly, ONNX models are not static. Developers can insert, remove, or replace nodes in the graph, making it possible to add new layers, prune unnecessary ones, or fuse operations for optimization. This graph-level flexibility is what enables many of the performance improvements we’ll explore later in this tutorial, such as layer fusion and quantization.

## ONNX Runtime
While ONNX provides a standard way to represent models, it still needs a high-performance engine to actually execute them. This is where ONNX Runtime (ORT) comes in. ONNX Runtime is the official, open-source inference engine for ONNX models, designed to run them quickly and efficiently across a wide variety of hardware.

At its core, ONNX Runtime is optimized for speed, portability, and extensibility:
1. Cross-platform support. ORT runs on Windows, Linux, macOS, and mobile operating systems like Android and iOS. It has first-class support for both x86 and Arm64 architectures, making it ideal for deployment on devices ranging from cloud servers to Raspberry Pi boards and smartphones.

2. Hardware acceleration. ORT integrates with a wide range of execution providers (EPs) that tap into hardware capabilities:
* Arm NEON / Arm Compute Library for efficient CPU execution on Arm64.
* CUDA for NVIDIA GPUs.
* DirectML for Windows.
* NNAPI on Android, enabling direct access to mobile accelerators (DSPs, NPUs).

3. Inference and training. ONNX Runtime also supports training and fine-tuning, making it possible to use the same runtime across the entire ML lifecycle.

4. Optimization built in. ORT can automatically apply graph optimizations such as constant folding, operator fusion, or memory layout changes to squeeze more performance out of your model.

For developers, this means you can take a model trained in PyTorch, export it to ONNX, and then run it with ONNX Runtime on virtually any device—without worrying about the underlying hardware differences. The runtime abstracts away the complexity, choosing the best available execution provider for your environment.

This flexibility makes ONNX Runtime a powerful bridge between training frameworks and deployment targets, and it is the key technology that allows ONNX models to run effectively on Arm64 platforms and Android devices.

## How ONNX Fits into the Workflow

One of the biggest advantages of ONNX is how naturally it integrates into a developer’s machine learning workflow. Instead of locking you into a single framework from training to deployment, ONNX provides a bridge that connects different stages of the ML lifecycle.

A typical ONNX workflow looks like this:
1. Train the model. You first use your preferred framework (e.g., PyTorch, TensorFlow, or scikit-learn) to design and train a model. At this stage, you benefit from the flexibility and ecosystem of the framework of your choice.
2. Export to ONNX. Once trained, the model is exported into the ONNX format using built-in converters (such as torch.onnx.export for PyTorch). This produces a portable .onnx file describing the network architecture, weights, and metadata.
3. Run inference with ONNX Runtime. The ONNX model can now be executed on different devices using ONNX Runtime. On Arm64 hardware, ONNX Runtime takes advantage of the Arm Compute Library and NEON instructions, while on Android devices it can leverage NNAPI for mobile accelerators.
4. Optimize the model. Apply graph optimizations like layer fusion, constant folding, or quantization to improve performance and reduce memory usage, making the model more suitable for edge and mobile deployments.
5. Deploy. Finally, the optimized ONNX model is packaged into its target environment. This could be an Arm64-based embedded system (e.g., Raspberry Pi), a server powered by Arm CPUs (e.g., AWS Graviton), or an Android application distributed via the Play Store.

This modularity means developers are free to mix and match the best tools for each stage: train in PyTorch, optimize with ONNX Runtime, and deploy to Android—all without rewriting the model. By decoupling training from inference, ONNX enables efficient workflows that span from research experiments to production-grade applications.

## Example Use Cases
ONNX is already widely adopted in real-world applications where portability and performance are critical. A few common examples include:
1. Computer Vision at the Edge – Running an object detection model (e.g., YOLOv5 exported to ONNX) on a Raspberry Pi 4 or NVIDIA Jetson, enabling low-cost cameras to detect people, vehicles, or defects in real time.
2. Mobile Applications – Deploying face recognition or image classification models inside an Android app using ONNX Runtime Mobile, with NNAPI acceleration for efficient on-device inference.
3. Natural Language Processing (NLP) – Running BERT-based models on Arm64 cloud servers (like AWS Graviton) to provide fast, low-cost inference for chatbots and translation services.
4. Healthcare Devices – Using ONNX to integrate ML models into portable diagnostic tools or wearable sensors, where Arm64 processors dominate due to their low power consumption.
5. Cross-platform Research to Production – Training experimental architectures in PyTorch, exporting them to ONNX, and validating them across different backends to ensure consistent performance.
6. AI Accelerator Integration – ONNX is especially useful for hardware vendors building custom AI accelerators. Since accelerators often cannot support the full range of ML operators, ONNX’s extensible operator model allows manufacturers to plug in custom kernels where hardware acceleration is available, while gracefully falling back to the standard runtime for unsupported ops. This makes it easier to adopt new hardware without rewriting entire models.

## Summary
In this section, we introduced ONNX as an open standard for representing machine learning models across frameworks and platforms. We explored its model structure—graphs, opsets, and metadata—and explained the role of ONNX Runtime as the high-performance execution engine. We also showed how ONNX fits naturally into the ML workflow: from training in PyTorch or TensorFlow, to exporting and optimizing the model, and finally deploying it on Arm64 or Android devices.

A useful way to think of ONNX is as the PDF of machine learning models—a universal, consistent format that looks the same no matter where you open it, but with the added flexibility to inject your own layers and optimizations.

Beyond portability for developers, ONNX is also valuable for hardware and AI-accelerator builders. Because accelerators often cannot support every possible ML operator, ONNX’s extensible operator model allows manufacturers to seamlessly integrate custom kernels where acceleration is available, while relying on the runtime for unsupported operations. This combination of consistency, flexibility, and extensibility makes ONNX a cornerstone technology for both AI application developers and hardware vendors.