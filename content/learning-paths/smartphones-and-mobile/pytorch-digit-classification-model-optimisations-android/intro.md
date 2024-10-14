---
# User change
title: "Optimising neural network models in PyTorch"

weight: 2

layout: "learningpathall"
---

In the realm of machine learning (ML) for edge and mobile inference, optimizing models is crucial to achieving efficient performance while minimizing resource consumption. As mobile and edge devices often have limited computational power, memory, and energy availability, various strategies are employed to ensure that ML models can run effectively in these constrained environments. 

**Quantization** is one of the most widely used techniques, which reduces the precision of the model's weights and activations from floating-point to lower-bit representations, such as int8 or float16. This not only reduces the model size but also accelerates inference speed on hardware that supports lower precision arithmetic. 

Another key optimization strategy is **layer fusion**, where multiple operations, such as combining linear layers with their subsequent activation functions (like ReLU), into a single layer. This reduces the number of operations that need to be executed during inference, minimizing latency and improving throughput. 

In addition to these techniques, **pruning**, which involves removing less important weights or neurons from the model, can help in creating a leaner model that requires fewer resources without significantly affecting accuracy. 

Finally, leveraging hardware-specific optimizations, such as **using the Android Neural Networks API (NNAPI)**  allows developers to take full advantage of the underlying hardware acceleration available on edge devices. By employing these strategies, developers can significantly enhance the efficiency of ML models for deployment on mobile and edge platforms, ensuring a balance between performance and resource utilization.

PyTorch offers robust support for various optimization techniques that enhance the performance of machine learning models for edge and mobile inference. One of the key features is its quantization toolkit, which provides a streamlined workflow for applying quantization to models. PyTorch supports both static and dynamic quantization, allowing developers to reduce model size and improve inference speed without sacrificing accuracy. Additionally, PyTorch enables layer fusion through its torch.quantization module, enabling seamless integration of operations like fusing linear layers with their activation functions, thus optimizing execution by minimizing computational overhead. Furthermore, the TorchScript functionality allows for the creation of serializable and optimizable models that can be efficiently deployed on mobile devices. PyTorch’s integration with hardware acceleration libraries, such as NNAPI for Android, enables developers to leverage specific hardware capabilities, ensuring optimal model performance tailored to the device’s architecture. Overall, PyTorch provides a comprehensive ecosystem that empowers developers to implement effective optimizations for mobile and edge deployment, enhancing both speed and efficiency.

In this Learning Path, we will delve into the techniques of **quantization** and **fusion** using our previously created neural network model for [digit classification](/learning-paths/cross-platform/pytorch-digit-classification-arch-training/). By applying quantization, we will reduce the model's weight precision, transitioning from floating-point representations to lower-bit formats, which not only minimizes the model size but also enhances inference speed. This process is crucial for optimizing our model for deployment on resource-constrained devices. 

Additionally, we will explore layer fusion, which combines multiple operations within the model—such as fusing linear layers with their subsequent activation functions—into a single operation. This reduction in operational complexity further streamlines the model, leading to improved performance during inference. By implementing these optimizations, we aim to enhance the efficiency of our digit classification model, making it well-suited for deployment in mobile and edge environments.

First, we will modify our previous Python scripts for [both training and inference](/learning-paths/cross-platform/pytorch-digit-classification-arch-training/)to incorporate model optimizations like quantization and fusion. After adjusting the training pipeline to produce an optimized version of the model, we will also update our inference script to handle both the original and optimized models. Once these changes are made, we will modify the [Android app](pytorch-digit-classification-inference-android-app) to load either the original or optimized model based on user input, allowing us to switch between them dynamically. This setup will enable us to directly compare the inference speed of both models on the device, providing valuable insights into the performance benefits of model optimization techniques in real-world scenarios.