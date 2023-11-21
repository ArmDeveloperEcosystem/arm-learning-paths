---
review:
    - questions:
        question: >
            Do TensorFlow, PyTorch and JAX run on Arm servers?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Even though these dependencies aren't pure Python, the respective
            authors compile the software packages and make them available for the Arm architecture.

    - questions:
        question: >
            Do you need to perform Arm specific steps when using Keras? 
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            Using Keras doesn't require anything specific for Arm. The 
            software stack used is fully supported on 64-bit Arm Linux.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
