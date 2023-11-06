---
review:
    - questions:
        question: >
            Taints and tolerations ensure that pods are scheduled on correct nodes.
        answers:
            - "True"
            - "False"
        correct_answer: 1                    
        explanation: >
            Taints and tolerations work together to make sure that application pods are not scheduled on wrong architecture nodes.

    - questions:
        question: >
            You can't create an Amazon EKS cluster with both x86/amd64 and arm64 nodes.
        answers:
            - "True"
            - "False"
        correct_answer: 2                   
        explanation: >
            Amazon EKS supports hybrid clusters with both x86/amd64 and arm64 nodes.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
