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
            Redis runs at port 6000 by default.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >        
            Redis runs at port 6379 by default.

    - questions:
        question: >
            Redis is written in Java.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Redis is written in ANSI C.
               
    - questions:
        question: >
            There are 6000 hash slots in Redis Cluster.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            There are 16384 hash slots in Redis Cluster.
            
    - questions:
        question: >
            Redis Cluster requires minimum 6 primary nodes to work properly. 
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Redis Cluster requires minimum 3 primary nodes to work properly.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

