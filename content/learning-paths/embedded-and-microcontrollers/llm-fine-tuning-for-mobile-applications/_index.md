---
title: LLM Fine-Tuning for Mobile Applications

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This learning path provides an introduction for developers and data scientists new to fine-tuning large language models (LLMs) and looking to develop a fine-tuned LLM for mobile applications. Fine-tuning involves adapting a pre-trained LLM to specific tasks or domains by training it on domain-specific data and optimizing its responses for accuracy and relevance. For mobile applications, fine-tuning enables personalized interactions, enhanced query handling, and improved contextual understanding, making AI-driven features more effective. This session will cover key concepts, techniques, tools, and best practices, ensuring a structured approach to building a fine-tuned LLM that aligns with real-world mobile application requirements.Mobile application with Llama, KleidiAI, ExecuTorch, and XNNPACK.

learning_objectives: 
    - Learn the basics of large language models (LLMs) and how fine-tuning enhances model performance for specific use cases focusing on mobile applications. 
    - Understand full fine-tuning, parameter-efficient fine-tuning (e.g., LoRA, QLoRA, PEFT), and instruction-tuning.
    - Learn when to use different fine-tuning approaches based on model size, task complexity, and computational constraints.
    - Learn how to curate, clean, and preprocess domain-specific datasets for optimal fine-tuning.
    - Understand dataset formats, tokenization, and annotation techniques for improving model learning.
    - Implementing Fine-Tuning with Popular Frameworks like Hugging Face Transformers and PyTorch for LLM fine-tuning.
    - Learn how to deploy and fine-tune the model in the mobile device.
    - Compile a Large Language Model (LLM) using ExecuTorch.
    - Describe techniques for running large language models in an mobile environment.

prerequisites:
    - Basic Understanding of Machine Learning & Deep Learning (Familiarity with concepts like supervised learning, neural networks, transfer learning and Understanding of model training, validation, & overfitting concepts).
    - Familiarity with Deep Learning Frameworks (Experience with PyTorch for building, training neural networks and Knowledge of Hugging Face Transformers for working with pre-trained LLMs.
    - An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
    - A USB cable to connect your smartphone to your development machine.
    - An AWS Graviton4 r8g.16xlarge instance to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server or Arm based laptop.
    - Python 3.10.

author: Parichay Das

### Tags
skilllevels: Introductory
subjects: GenAI
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
