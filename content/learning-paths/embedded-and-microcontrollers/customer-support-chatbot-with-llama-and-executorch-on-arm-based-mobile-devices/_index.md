---
title: Customer Support Chatbot with Llama and ExecuTorch on Arm-Based Mobile Devices (with Agentic AI Capabilities)

draft: true
cascade:
    draft: true
    
minutes_to_complete: 60

who_is_this_for: This learning plan is designed for developers with basic knowledge of Python, Mobile development, and machine learning concepts.It guides you through creating an on-device customer support chatbot using Meta's Llama models deployed via PyTorch's ExecuTorch runtime.The focus is on Arm-based Android devices.The chatbot will handle common customer queries (e.g., product info, troubleshooting) with low latency, privacy (no cloud dependency), and optimized performance.Incorporates agentic AI capabilities, transforming the chatbot from reactive (simple Q&A) to proactive and autonomous. Agentic AI enables the bot to plan multi-step actions, use external tools,reason over user intent, and adapt responses dynamically. This is achieved by extending the core LLM with tool-calling mechanisms and multi-agent orchestration.

learning_objectives: 
    - Explain the architecture and capabilities of Llama models (e.g., Llama 3.2 1B/3B) for mobile use.
    - Master the process of quantizing LLMs (e.g., 4-bit PTQ) to reduce model size and enable efficient inference on resource-constrained mobile devices.
    - Gain proficiency in using ExecuTorch to export PyTorch models to .pte format for on-device deployment.
    - Learn to leverage Arm-specific optimizations (e.g., XNNPACK, KleidiAI) to achieve 2-3x faster inference on Arm-based Android devices.
    - Implement real-time inference with Llama models, enabling seamless customer support interactions (e.g., handling FAQs, troubleshooting).

prerequisites:
    - Basic Understanding of Machine Learning & Deep Learning (Familiarity with concepts like supervised learning, neural networks, transfer learning and Understanding of model training, validation, & overfitting concepts).
    - Familiarity with Deep Learning Frameworks (Experience with PyTorch for building, training neural networks and Knowledge of Hugging Face Transformers for working with pre-trained LLMs.
    - An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
    - A USB cable to connect your smartphone to your development machine.
    - An AWS Graviton4 r8g.16xlarge instance to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server or Arm based laptop.
    - Android Debug Bridge (adb) installed on your device. Follow the steps in [adb](https://developer.android.com/tools/adb) to install Android SDK Platform Tools. The adb tool is included in this package.
    - Java 17 JDK. Follow the steps in [Java 17 JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) to download and install JDK for host.
    - Android Studio. Follow the steps in [Android Studio](https://developer.android.com/studio) to download and install Android Studio for host.
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
