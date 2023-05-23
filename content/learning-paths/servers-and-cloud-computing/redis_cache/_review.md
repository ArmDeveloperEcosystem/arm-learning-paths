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
            Data replication is supported in Redis.
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explanation: >        
            Redis uses by default asynchronous replication.
    - questions:
        question: >
            Redis-cli is used to interact with Redis.
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explanation: >
            Redis-cli allows sending commands to Redis and read the replies sent by the server directly from the terminal.
               
    - questions:
        question: >
            Redis is a multi-threaded architecture.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Redis is a single-threaded architecture.
            
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
