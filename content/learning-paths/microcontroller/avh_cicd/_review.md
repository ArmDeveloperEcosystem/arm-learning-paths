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
            Arm Virtual Hardware can be used in CI/CD workflows.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            CI/CD automated workflows are the primary use case for Arm Virtual Hardware.

    - questions:
        question: >
            How is Arm Virtual Hardware accessed?
        answers:
            - "As a tarball to be installed locally"
            - "Arm Virtual Hardware must be directly licensed from Arm"
            - "As an AWS Machine Instance (AMI)"
        correct_answer: 3
        explanation: >
            Arm Virtual Hardware is provided as an AMI on AWS Marketplace.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
