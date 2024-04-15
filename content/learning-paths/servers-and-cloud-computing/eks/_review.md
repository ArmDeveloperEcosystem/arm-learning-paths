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
            You can use Amazon EKS to create a Kubernetes cluster with Arm-based Graviton processors.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            You can run Kubernetes applications in EKS using Graviton processors.

    - questions:
        question: >
            What is the name of the command line tool for working with Kubernetes clusters?
        answers:
            - "helm"
            - "eksctl"
            - "kubectl"
        correct_answer: 3
        explanation: >
            kubectl is the command line tool you can use to communicate with a Kubernetes API server. It can be used for any implementation of Kubernetes. 

    -  questions:
        question: >
            EKS clusters can be updated to a new version of Kubernetes software without stopping the cluster.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Amazon EKS performs managed and in-place cluster upgrades for both Kubernetes and Amazon EKS platform software.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
