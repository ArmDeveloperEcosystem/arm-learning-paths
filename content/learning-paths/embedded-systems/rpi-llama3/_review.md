---
review:
    - questions:
        question: >
            What is the benefit of quantization?
        answers:
            - "It reduces the size of the model."
            - "It improves the accuracy of the model."
            - "It reduces the number of weights in the model."
        correct_answer: 1
        explanation: >
            By converting FP32 tensors to INT4, the number of bits needed to represent the tensor decreases dramatically, with a smaller memory footprint as a result.
    - questions:
        question: >
            What quantization scheme does Llama require to run on an embedded device such as the Raspberry Pi 5?
        answers:
            - "8-bit groupwise per token dynamic quantization of all the linear layers."
            - "4-bit groupwise per token dynamic quantization of all the linear layers."
            - "No quantization is needed."
        correct_answer: 2
        explanation: >
            The 4-bit quantization scheme yields the smallest memory footprint for Llama 3 in this case.
    - questions:
        question: >
            Dynamic quantization happens at runtime.
        answers:
            - "False"
            - "True"
        correct_answer: 2
        explanation: >
            Dynamic quantization refers to quantizing activations at runtime.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
