---
review:
    - questions:
        question: >
            Google Axion supports self-hosted runners on GitLab
        answers:
            - "True"
            - "False"
        correct_answer: 1                    
        explanation: >
            Google Axion based VMs can be used as self-hosted GitLab runners

    - questions:
        question: >
            You can't execute parallel jobs on separate GitLab runners 
        answers:
            - "True"
            - "False"
        correct_answer: 2                   
        explanation: >
            GitLab allows executing jobs parallely on two different self-hosted runners with tags

    - questions:
        question: >
            What is the primary role of a GitLab Runner in GitLab CI/CD?
        answers:
            - To manage the GitLab repository.
            - To execute jobs defined in the GitLab CI/CD configuration.
            - To provide multi-architecture support for different processors.
            - To create virtual machines in Google Cloud.
        correct_answer: 2
        explanation: >
            To execute jobs defined in the GitLab CI/CD configuration.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
