---
review:
    - questions:
        question: >
            What is ExecuTorch?
        answers:
            - ExecuTorch is an end-to-end solution for enabling on-device inference capabilities across mobile and edge devices.
            - It is a Pytorch method to quantize LLMs.
            - It is a program to execute pytorch models.
        correct_answer: 1                    
        explanation: >
            ExecuTorch is part of the PyTorch Edge ecosystem and enables efficient deployment of PyTorch models to edge devices.

    - questions:
        question: >
            What is Llama?
        answers:
            - A domesticated South American camelid.
            - A proprietary Large Language Model.
            - Llama is a family of large language models that uses publicly-available data for training.
        correct_answer: 3                   
        explanation: >
            LLaMA is a state-of-the-art foundational large language model designed to enable researchers to advance their work in this subfield of AI.
               
    - questions:
        question: >
            Which quantization scheme did you use for an Android app?
        answers:
            - 8-bit groupwise per token dynamic quantization of all the linear layers.
            - 4-bit groupwise per token dynamic quantization of all the linear layers.
            - 16-bit groupwise per token dynamic quantization of all the linear layers.
            - No quantization.
        correct_answer: 2          
        explanation: >
            Dynamic quantization refers to quantizing activations dynamically, such that quantization parameters for activations are calculated, from min/max range, at runtime.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
