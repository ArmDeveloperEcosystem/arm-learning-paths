---
review:
    - questions:
        question: >
            Are at least four cores, 16GB of RAM, and 32GB of disk storage required to run the LLM chatbot using rtp-llm on an Arm-based server?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes. Depends on the LLM model parameters size, bigger the model parameters, more CPU, RAM and disk space is required.

    - questions:
        question: >
            Does the rtp-llm project use the --config=arm option to optimize LLM inference for Arm CPUs?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes. rtp-llm uses GPU for inference by default, rtp-llm optimizes LLM inference on Arm architecture by providing a configuration option --config=arm during the build process.

    - questions:
        question: >
            Is the given Python script the only way to run the LLM chatbot on an Arm AArch64 CPU and output a response from the model?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            No. rtp-llm can also be deployed as a API server, user can use curl or other client to get LLM chatbot response.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
