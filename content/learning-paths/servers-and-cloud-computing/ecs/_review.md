---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentance question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explination:      A short (1-3 sentance) explination of why the correct answer is correct. Can add aditional context if desired

review:
    - questions:
        question: >
            If you accidentally delete your ECS cluster, can it be restored?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            No, deleted clusters cannot be restored.

    - questions:
        question: >
            Does Amazon ECS support AWS Graviton processors?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes, both Fargate and EC2 instances can be used with ECS and AWS Graviton processors.

    - questions:
        question: >
            Does Amazon ECS support dynamic port mapping?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes, it is possible to associate a service on Amazon ECS to an Application Load Balancer (ALB) and provide dynamic port mapping.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
