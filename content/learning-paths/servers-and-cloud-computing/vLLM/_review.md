
---
review:
    - questions:
        question: >
            What is the primary purpose of vLLM?
        answers:
            - "Operating System Development."
            - "Large Language Model Inference and Serving."
            - "Database Management."
        correct_answer: 2
        explanation: >
            vLLM is designed for fast and efficient Large Language Model inference and serving.

    - questions:
        question: >
           In addition to Python, which extra programming languages are required by the vLLM build system?
        answers:
            - "Java."
            - "Rust."
            - "C++."
            - "Rust and C++."
        correct_answer: 4
        explanation: >
            The vLLM build system requires the Rust toolchain and GCC for its compilation.

    - questions:
         question: >
            What is the VLLM_TARGET_DEVICE environment variable set to for building vLLM for Arm CPUs?
         answers:
             - "cuda."
             - "gpu."
             - "cpu."
         correct_answer: 3
         explanation: >
            The VLLM_TARGET_DEVICE environment variable needs to be set to cpu to target the Arm processor.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
