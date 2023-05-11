---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add additional context if desired

review:
    - questions:
        question: >
            Amazon EKS work with AWS Fargate.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            You can run Kubernetes applications as serverless containers using AWS Fargate and Amazon EKS.

    - questions:
        question: >
            Terraform is an Infrastructure as Code (IaC) solution created by AWS.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Terraform is not specific to AWS and was created by HashiCorp.

    -  questions:
        question: >
            Kubernetes cluster can be updated to a new version.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Amazon EKS performs managed, in-place cluster upgrades for both Kubernetes and Amazon EKS platform versions.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
