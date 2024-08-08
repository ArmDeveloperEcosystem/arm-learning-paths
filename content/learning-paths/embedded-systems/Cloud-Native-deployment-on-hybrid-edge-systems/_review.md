---
review:
    - questions:
        question: >
            The firmware is deployed as a container running on Linux on a Cortex-A.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            The firmware runs on a Cortex-M, from `containerd`'s perspective it appears to runs as a normal Linux container.

    - questions:
        question: >
            Can you run multiple hybrid containers on the same Cortex-M?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            Each embedded core can only run a single container at once.
            
    - questions:
        question: >
            Which command is used to interact with the hybrid-runtime from `containerd`?
        answers:
            - ctr run --runtime io.containerd.hybrid hybrid_app_imx8mp:latest test-container
            - ctr run --runtime runc hybrid_app_imx8mp:latest test-container
            - ctr run hybrid_app_imx8mp:latest test-container
        correct_answer: 1
        explanation: >
            --runtime io.containerd.hybrid is needed to interact with the hybrid runtime.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
