---
title: KleidiAI basics
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Intro

This tutorial overviews KleidiAI from Arm. KleidiAI is a set of micro-kernels that integrates into various machine learning frameworks with one goal: Accellerating your AI inference on Arm-based platforms. KleidiAI's micro-kernels are hand-optimized in Arm assembly code to leverage modern architecture instructions that greatly speed up AI inference on Arm CPUs. 

Best of all is you don't need to do anything to get the benefits of KleidiAI; it will automatically apply if two conditions are met:
1. Your ML Framework integrates KleidiAI, and
2. Your hardware platform supports *i8mm* Arm instructions.

At launch, KleidiAI is being leveraged by Google's MediaPipe framework and XNNPack backend, with more support upcoming. For a tutorial of using KleidiAI to accelerate ?????? whatever Mediapipe/XNNPack tutorial is doing ?????? view [this learning path](https://google.com). To find out if your platform supports KleidiAI, view a list of supported platforms [further down on this page](#what-arm-cpus-support-kleidiai).

![KleidiAI#center](Arm_KleidiAI_square_color.png "Optimized micro-kernels for AI workloads on Arm CPUs")


### Why is KleidiAI valuable?
KleidiAI speeds up Generative AI performance with no end-developer work required. The first integrations of KleidiAI have provided ?????? 30x ?????? speedup in ????? MediaPipe LLM performance ???. You can read more about this speedup in [this blog ?????????](https://google.com). This drastic speedup will bring more AI use-cases to CPUs in servers and at the edge. 

This value comes at no cost to developers - the range of GenAI applications possible to run on Arm CPUs is now larger.

The rest of this tutorial will explain how KlediAI works. To understand how KleidiAI accelerates workloads so effectively, an overview of how AI works is needed. 

## Generative AI = Lots of Matrix Multiplication

{{% notice Quote %}}
“Any sufficiently advanced technology is indistinguishable from magic” - Arthur C. Clarke
{{% /notice %}}

In the case of Generative AI models today, the math behind the precieved magic is **matrix multiplication**. To understand this, and better understand KleidiAI itself, this section offers a high-level explination of neural network architecture.

Neural networks consist of layers of neurons. Each neuron in a layer is connected to all neurons in the previous layer. Each of these connections has a unique connection strength, learned through training. This is called a connection's *weight*. 

During inference (such as trying to generate the next token/word with a given input), each neuron performs a weighted sum of inputs and then decides its value via an activation function. The weighted sum is the dot product of each connected neruon's input (*x*) and its connection weight (*w*). A layer of neuron's calculations can be efficiently calculated via matrix multiplication, where the input matrix is multiplied by the weight matrix. 

For example, in the image below, *z1* is calculated as a dot product of connected *x*'s and *w*'s from the previous layer. All *z* values in Layer 0 can therefore be effeciently calculated with a matrix multiplication operation.

![Neural Network example#center](neural-node-pic.jpg "Figure 1. Zoomed in on neural network node")


Sidebar:  In addition to *weights*, each neuron in a neural network is assigned a *bias*. These weights and biases are learned during training and make up a model's parameters. For example, in the Llama 3 model with 8 billion parameters, the model has around 8 billion individual weights and biases that embody what it learned during training. Generally speaking, the more parameters a model has, the more information it can retain from its training, leading to more capable models.

### Matrix Multiplication speedup is critical
What does this all mean? An 8 billion parameter model generating one token requires billions of dot product calculations, with at least hundreds of millions of matrix multiplication operations. Therefore speeding up matrix multiplication is a critical piece to accelerating AI workloads. 

This is where KleidiAI comes in, taking advantage of the modern Arm CPU instructions dedicated to accelerating matrix multiplication.

## What Arm CPUs support KlediAI?
KlediAI leverages the *i8mm* architecture feature, which stands for *Int8 Matrix Multiplication*. The feature is included in all Arm CPUs following Armv8.6-A architectures and beyond that include Advanced SIMD (it could be optionally enabled from Armv8.2-A as well). The specific instruction in the *i8mm* feature is *SMMLA*, which stands for *Signed 8-bit integer matrix multiply-accumulate*. For more information view the *SMMLA* and *i8mm* documentation [here](https://developer.arm.com/documentation/ddi0602/latest/SIMD-FP-Instructions/SMMLA--vector---Signed-8-bit-integer-matrix-multiply-accumulate--vector--).

Today, Arm-powered hardware containing this instruction exists in cloud servers and smartphones. Below are some examples of the first products from popular vendors that support *i8mm*:

| Area        |  Product            | Arm-based SoC      | Arm Architecture  |
| ---------   | -----------------   | ----------------   | ----------- |
| Server      |  C7g, M7g, R7g      | AWS Graviton 3     | Armv8.4  |
| Server      |  c8y                | Alibaba Yitian 710 | Armv9.0  |
| Server      |  GB200 NVL72        | NVIDIA Grace       | Armv9.0  |
| Smartphone  |  Google Pixel 8 Pro | Google Tensor G3   | Armv9.0  |
| Smartphone  |  Samsung Galexy S22 | Snapdragon 8 Gen 1 | Armv9.0  |
| Smartphone  |  OPPO Find X5 Pro   | Snapdragon 8 Gen 1 | Armv9.0  |
| Smartphone  |  Xiaomi 12T         | Mediatek Dimensity 9000 | Armv9.0  |


To view a range of devices and what Arm instructinos they support (including this i8mm), visit [this website](https://gpages.juszkiewicz.com.pl/arm-socs-table/arm-socs.html) and find your platform. 


## What's next?
The remaineder of this Learning Path will answer the following questions while stepping through a C++ example:
* How does KleidAI 'just work' with ML Frameworks?
* What do the micro-kernels in KleidiAI functionally do?
* How are the KleidiAI micro-kernels actually speeding up matrix multiplication?
