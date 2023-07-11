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
            If I accidentally delete my cluser, I can retrieve it.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            No, Cluster that have been deleted cannot be retrieved.

    - questions:
        question: >
            Does Amazon ECS support any other container types?
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            No, docker is the only container platform supported by Amazon ECS at this time.

    - questions:
        question: >
            Does Amazon ECS support dynamic port mapping?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, it is possible to associate a service on Amazon ECS to an Application Load Balancer (ALB) for the ELB service.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
