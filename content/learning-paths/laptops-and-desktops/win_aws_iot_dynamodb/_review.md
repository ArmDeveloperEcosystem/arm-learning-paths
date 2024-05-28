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
            What is the Rules Engine?
        answers:
            - "A part of the AWS IoT Core to process and route data between IoT devices and other AWS services."
            - "An engine to create security rules."
            - "An engine for accelerating database access."            
        correct_answer: 1               
        explanation: >
            The Rules Engine in AWS IoT Core is a powerful feature designed to process and route data between IoT devices and other AWS services or external endpoints.

    - questions:
        question: >
            Does Amazon DynamoDB require you to set up the database server?
        answers:
            - "No"
            - "Yes"
        correct_answer: 1
        explanation: >
            Amazon DynamoDB is a fully-managed NoSQL database service, so you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.
            
    - questions:
        question: >
            What is partitioning used for?
        answers:
        answers:
            - "To format database elements."
            - "To filter database elements."            
            - "To allow the database to scale horizontally."
            - "To allow the database to scale vertically."            
        correct_answer: 3
        explanation: >
            Amazon DynamoDB uses partitioning, which is a mechanism that allows the database to scale horizontally, and distribute large amounts of data across multiple servers while ensuring quick data access and high availability.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
