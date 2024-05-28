---
review:
    - questions:
        question: >
            Is it possible to run LLMs on edge devices such as a Raspberry Pi? 
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes. The advancements made in the Generative AI space with new model formats like GGUF and smaller parameter models make LLM inference on CPUs very efficient.

    - questions:
        question: >
            Does llama.cpp require skills to build and run C++ applications?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            No. You can use Python bindings for llama.cpp and control everything from Python.

    - questions:
        question: >
            Can you estimate memory usage without loading an LLM? 
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes. Memory estimation tools are available on the Hugging Face website and using the accelerate CLI. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
