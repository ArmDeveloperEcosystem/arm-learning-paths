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
            What is the Amazon S3?
        answers:
            - "A part of the AWS IoT Core to process and route data between IoT devices and other AWS services."
            - "A scalable, high-speed, web-based cloud storage service designed for online backup and archiving of data."
            - "An engine for accelerating database access."            
        correct_answer: 2               
        explanation: >
            Amazon S3 (Simple Storage Service) is a scalable, high-speed, web-based cloud storage service designed for online backup and archiving of data and applications on Amazon Web Services (AWS).

    - questions:
        question: >
            Does Amazon S3 require you to set up the archive server?
        answers:
            - "No"
            - "Yes"
        correct_answer: 1
        explanation: >
            Amazon S3 is a managed service, so you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.
            
    - questions:
        question: >
            Can you use Amazon S3 for static website hosting?        
        answers:
            - "Yes"
            - "No"                        
        correct_answer: 1
        explanation: >
            Amazon S3 can also be used for static website hosting. This feature allows users to host static web pages directly from an S3 bucket, making it a cost-effective and simple solution for serving static content such as HTML, CSS, JavaScript, and images.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
