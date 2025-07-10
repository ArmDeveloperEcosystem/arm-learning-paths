---
title: "About Cobalt 100 Arm-based processor and ONNX"

weight: 2

layout: "learningpathall"
---

## What is Cobalt 100 Arm-based processor? 

Azure’s Cobalt 100 is built on Microsoft's first-generation, in-house Arm-based processor: the Cobalt 100. Designed entirely by Microsoft and based on Arm’s Neoverse N2 architecture, this 64-bit CPU delivers improved performance and energy efficiency across a broad spectrum of cloud-native, scale-out Linux workloads. These include web and application servers, data analytics, open-source databases, caching systems, and more. Running at 3.4 GHz, the Cobalt 100 processor allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance. 

To learn more about Cobalt 100, refer to the blog [Announcing the preview of new Azure virtual machine based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Introduction to Azure Linux 3.0

Azure Linux 3.0 is Microsoft's in-house, lightweight Linux distribution optimized for running cloud-native workloads on Azure. Designed with performance, security, and reliability in mind, it is fully supported by Microsoft and tailored for containers, microservices, and Kubernetes. With native support for Arm64 (AArch64) architecture, Azure Linux 3.0 enables efficient execution of workloads on energy-efficient Arm-based infrastructure, making it a powerful choice for scalable and cost-effective cloud deployments.

## Introduction to ONNX

ONNX (Open Neural Network Exchange) is an open standard for representing machine learning models, enabling interoperability between different AI frameworks. It allows you to train a model in one framework (like PyTorch or TensorFlow) and run it using ONNX Runtime for optimized inference.

In this Learning Path, we deploy ONNX on Azure Linux 3.0 (Arm64) and benchmark its performance using the[ onnxruntime_perf_test tool](https://onnxruntime.ai/docs/performance/tune-performance/profiling-tools.html#in-code-performance-profiling).
