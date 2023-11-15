---
review:
    - questions:
        question: >
            Do TensorFlow, PyTorch and JAX runt on Arm servers?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Even though these dependencies aren't pure Python, the respective
            authors compile these software and make them available for aarch64.
            For the end user it just works.

    - questions:
        question: >
            Do you need to perform Arm specific steps during the learning path? 
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            The learning path doesn't contain steps specific for Arm as all the
            software stack used is fully supporte on 64-bit Arm servers running Linux.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
