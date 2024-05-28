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
            Is it possible to start multiple services in a container?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                   
        explanation: >
            You can use Supervisor, a process control system, to start multiple services in a container.

    - questions:
        question: >
            You must open a port to be able to reach a running container using SSH.
        answers:
            - "True"
            - "False"
        correct_answer: 2                    
        explanation: >
            You can reach a local container using docker exec and a remote container using Remote.It. There are other services to each containers but Remote.It is a good example of how to do it. 
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
