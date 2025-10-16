---
title: "Overview"

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor


Azure’s Cobalt 100 is built on Microsoft's first-generation, in-house Arm-based processor, the Cobalt 100. Designed entirely by Microsoft and based on Arm’s Neoverse N2 architecture, it is a 64-bit CPU that delivers improved performance and energy efficiency across a broad spectrum of cloud-native, scale-out Linux workloads. 

You can use Cobalt 100 for:

- Web and application servers
- Data analytics
- Open-source databases
- Caching systems
- Many other scale-out workloads

Running at 3.4 GHz, the Cobalt 100 processor allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance. You can learn more about Cobalt 100 in the Microsoft blog [Announcing the preview of new Azure virtual machine based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## ONNX  

ONNX (Open Neural Network Exchange) is an open-source format designed for representing machine learning models. 

You can use ONNX to:

- Move models between different deep learning frameworks, such as PyTorch and TensorFlow
- Deploy models trained in one framework to run in another
- Build flexible, portable, and production-ready AI workflows

ONNX models are serialized into a standardized format that you can execute with ONNX Runtime - a high-performance inference engine optimized for CPU, GPU, and specialized hardware accelerators. This separation of model training and inference lets you deploy models efficiently across cloud, edge, and mobile environments.

To learn more, see the [ONNX official website](https://onnx.ai/) and the [ONNX Runtime documentation](https://onnxruntime.ai/docs/).

## Next steps for ONNX on Azure Cobalt 100

Now that you understand the basics of Azure Cobalt 100 and ONNX Runtime, you are ready to deploy and benchmark ONNX models on Arm-based Azure virtual machines. This Learning Path will guide you step by step through setting up an Azure Cobalt 100 VM, installing ONNX Runtime, and running machine learning inference on Arm64 infrastructure.
