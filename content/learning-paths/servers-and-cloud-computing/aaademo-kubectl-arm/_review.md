---
review:
    - questions:
        question: >
            Can you run LLMs on Arm CPUs?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes. The advancements made in the Generative AI space with new model formats like GGUF and smaller parameter models make LLM inference on CPUs very efficient.

    - questions:
        question: >
            Can llama.cpp be built and run on CPU only?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes. By default llama.cpp is built for CPU only on Linux and Windows. 

    - questions:
        question: >
            Can you profile the time taken by the model to generate the output until the end of text?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            llama.cpp prints a few timing parameters at the end of the execution of the LLM. One of these timing parameters is the eval time which is the time taken by the model to generate the output.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
