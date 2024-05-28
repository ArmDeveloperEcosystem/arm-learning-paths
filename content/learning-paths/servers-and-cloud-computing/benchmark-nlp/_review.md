---
review:
    - questions:
        question: >
            Do all Arm Neoverse CPUs include support for BFloat16 instructions?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            Recent Arm CPUs such as Arm Neoverse V1 and Neoverse N2 include support for BFloat16 instructions.

    - questions:
        question: >
            Can you run Hugging Face PyTorch models on an Arm AArch64 CPU?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            You can easily run and deploy models from Hugging Face on Arm CPUs using the Transformers library.

    - questions:
        question: >
            Does enabling support for BFloat16 fast math kernels in PyTorch improve the performance of NLP models?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes. A performance boost of up to 1.9x is observed on Arm Neoverse-based AWS Graviton3 instances by enabling support for BFloat16 fast math kernels in PyTorch.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
