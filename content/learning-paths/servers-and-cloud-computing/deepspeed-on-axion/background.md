---
title: Understand DeepSpeed and Google Axion C4A for AI training
weight: 2

layout: "learningpathall"
---

## Google Axion C4A Arm instances for AI and machine learning

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for AI, machine learning, data analytics, and modern cloud-native workloads.

The C4A series provides a cost-effective alternative to x86 virtual machines while offering the scalability and efficiency advantages of the Arm architecture in Google Cloud. For AI and machine learning workloads, Axion processors provide high multi-core CPU throughput, efficient tensor computation performance, improved performance-per-watt, and scalable CPU execution for training and inference workloads.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## DeepSpeed for scalable AI training on Arm

DeepSpeed is an open-source deep learning optimization framework developed by Microsoft for efficient and scalable training of large AI models. It is widely used for distributed deep learning, memory optimization, large language model (LLM) training, efficient inference execution, and high-performance AI workloads. Its core capabilities include Zero Redundancy Optimizer (ZeRO) memory optimization, distributed training acceleration, mixed precision training, pipeline and tensor parallelism, and optimized inference execution.

By running DeepSpeed on Google Axion C4A Arm-based infrastructure, you can perform efficient CPU-based AI training and benchmarking with multi-core Arm processors and optimized memory performance. This improves performance-per-watt and reduces infrastructure costs.

On SUSE Linux Enterprise Server Arm64 environments, some DeepSpeed native CPU communication extensions require GCC 9 or later to compile. Because the default SUSE image ships with GCC 7.5.0., you'll install DeepSpeed in compatibility mode alongside PyTorch CPU execution. This provides a stable and reproducible AI training and benchmarking environment.

Common use cases of DeepSpeed include neural network training, AI benchmarking, scalable experimentation pipelines, and CPU-based inference validation.

To learn more, see the [DeepSpeed documentation](https://www.deepspeed.ai/) and the [DeepSpeed GitHub repository](https://github.com/microsoft/DeepSpeed).

## What you've learned and what's next

You've now learned about Google Axion C4A Arm-based virtual machines and DeepSpeed as a scalable AI training framework suited to Arm processors. 

Next, you'll provision a C4A virtual machine, then install PyTorch and DeepSpeed to run training and benchmarking workloads.
