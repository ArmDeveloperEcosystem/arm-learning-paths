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
            Do you need to setup SSH keys to access running containers created by Copilot? 
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                   
        explanation: >
            Copilot takes care of everything you need to connect a shell or execute commands on a running container. You do not need to worry about SSH keys or security groups.

    - questions:
        question: >
            AWS Fargate is a serverless compute engine that lets you run containers and works with AWS Graviton processors. 
        answers:
            - "True"
            - "False"
        correct_answer: 1                    
        explanation: >
            Fargate is a great way to take advantage of the improved price performance of Graviton processors and avoid managing servers. 
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
