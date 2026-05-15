---
title: Learn about DeepSpeed and Google Axion C4A for AI training
weight: 2

layout: "learningpathall"
---

## Google Axion C4A Arm instances for AI and machine learning

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for AI, machine learning, data analytics, and modern cloud-native workloads.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and efficiency advantages of the Arm architecture in Google Cloud.

For AI and machine learning workloads, Axion processors provide high multi-core CPU throughput, efficient tensor computation performance, improved performance-per-watt, and scalable CPU execution for training and inference workloads. These capabilities make Axion Arm-based systems suitable for neural network training, benchmarking, experiment validation, and scalable AI development pipelines.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## DeepSpeed for scalable AI training on Arm

DeepSpeed is an open-source deep learning optimization framework developed by Microsoft to enable efficient and scalable training of large AI models. It is widely used for distributed deep learning, memory optimization, large language model (LLM) training, efficient inference execution, and high-performance AI workloads.

DeepSpeed provides a unified optimization platform with capabilities such as:

* ZeRO (Zero Redundancy Optimizer) memory optimization  
* Distributed training acceleration  
* Mixed precision training  
* Pipeline and tensor parallelism  
* Optimized inference execution  
* Scalable AI workload management  

Running DeepSpeed on Google Axion C4A Arm-based infrastructure enables efficient CPU-based AI training and benchmarking workflows by utilizing multi-core Arm processors and optimized memory performance. This results in improved performance-per-watt, reduced infrastructure costs, and scalable execution for AI experimentation and model training workloads.

On SUSE Linux Enterprise Server Arm64 environments, some DeepSpeed native CPU communication extensions require newer GCC toolchains for compilation. For this reason, this Learning Path uses DeepSpeed compatibility-mode installation together with PyTorch CPU execution to provide stable AI workload validation and benchmarking on GCP Axion Arm64 processors.

Common use cases include neural network training, AI benchmarking, scalable experimentation pipelines, distributed AI research environments, and CPU-based inference validation workflows.

To learn more, see the [DeepSpeed documentation](https://www.deepspeed.ai/) and the [DeepSpeed GitHub repository](https://github.com/microsoft/DeepSpeed).

## What you've learned and what's next

You've now learned about Google Axion C4A Arm-based virtual machines and their performance advantages for AI and machine learning workloads. You were also introduced to core DeepSpeed capabilities including distributed training optimization, ZeRO memory optimization, scalable AI execution, and CPU-based AI benchmarking workflows.

Next, you'll set up PyTorch and DeepSpeed on a GCP Axion Arm64 virtual machine, configure a Python AI/ML environment, and begin running AI training and benchmarking workloads on Arm processors.
