---
title: Agentic AI Chatbot with Llama, ExecuTorch, and KleidiAI on Arm-Based Android Devices
minutes_to_complete: 90

who_is_this_for: This learning plan is designed for developers with basic knowledge of Python, Android development (Kotlin), and machine learning concepts. It guides you through creating an on-device agentic AI chatbot using Meta's Llama models deployed via PyTorch's ExecuTorch runtime with Arm-optimized KleidiAI acceleration. The focus is on Arm-based Android devices. This chatbot goes beyond simple Q&A—it incorporates agentic AI capabilities, enabling it to plan multi-step actions, invoke Android system tools (Battery Manager, mock databases), reason over user intent, and adapt responses dynamically. You'll achieve low-latency inference, complete privacy (no cloud dependency), and optimized performance through quantization and Arm-specific optimizations (XNNPACK, KleidiAI). The agentic architecture uses prompt engineering for structured outputs and tool-calling mechanisms to create a truly autonomous mobile AI assistant.

learning_objectives: 
    - Explain the architecture and capabilities of Llama models (e.g., Llama 3.2 1B/3B) for mobile use.
    - Master the process of quantizing LLMs (e.g., 4-bit PTQ) to reduce model size and enable efficient inference on resource-constrained mobile devices.
    - Gain proficiency in using ExecuTorch to export PyTorch models to .pte format for on-device deployment.
    - Learn to leverage Arm-specific optimizations including XNNPACK and **KleidiAI** to achieve 2-3x faster inference on Arm-based Android devices.
    - Understand how KleidiAI provides optimized kernels for matrix multiplication and quantized operations on Arm CPUs.
    - **Design and Implement an Agentic Loop in Kotlin**: Create a system where the LLM can "reason" and "act" by invoking Android system tools (e.g., Battery Manager, Mock Database).
    - **Master Prompt Engineering for Agents**: Craft system prompts that enforce structured outputs (e.g., JSON or specific Action tags) for reliable tool calling on mobile.

prerequisites:
    - **Android Development Basics**: Familiarity with Kotlin, Android Studio, and the Android Lifecycle.
    - Basic Understanding of Machine Learning & Deep Learning (Familiarity with concepts like supervised learning, neural networks, transfer learning).             
    - Familiarity with Deep Learning Frameworks (PyTorch, Hugging Face Transformers).
    - An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
    - A USB cable to connect your smartphone to your development machine.
    - An AWS Graviton4 r8g.16xlarge instance (or similar Arm-based environment) for model export and optimization.
    - Android Debug Bridge (adb) installed.
    - Java 17 JDK.
    - Android Studio (latest version).
    - Python 3.10.

author: Parichay Das

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse

tools_software_languages:
    - LLM
    - GenAI
    - Python
    - PyTorch
    - ExecuTorch
    - KleidiAI
    - Kotlin
operatingsystems:
    - Linux
    - Windows
    - Android  


further_reading:
     - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
     - resource:
        title: PyTorch Documentation
        link: https://pytorch.org/docs/stable/index.html
        type: documentation
     - resource:
        title: Android 
        link: https://www.android.com/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
