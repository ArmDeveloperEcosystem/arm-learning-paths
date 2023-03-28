---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            The Azure command line interface (CLI) commands start with:
        answers:
            - "ms"
            - "az"
            - "az-cli"
            - "tf"
        correct_answer: 2                     
        explanation: >
            The Azure CLI commands start with az
    - questions:
        question: >
            The WordPress tutorial from the Kubernetes documentation works without any changes in AKS with Arm-based instances. 
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            This Learning Path includes a modified WordPress example which works on AKS with Arm-based instances.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
