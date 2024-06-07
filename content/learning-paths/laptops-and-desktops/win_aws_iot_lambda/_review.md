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
            What is AWS Lambda?
        answers:
            - "A part of the AWS IoT Core to process and route data between IoT devices and other AWS services."
            - "A software design architecture."
            - "A serverless compute service provided by AWS."            
        correct_answer: 3              
        explanation: >
             AWS Lambda is a serverless compute service that AWS provides that allows you to run code without provisioning or managing servers.

    - questions:
        question: >
            Does Amazon SNS require you to set up the notification server?
        answers:
            - "No"
            - "Yes"
        correct_answer: 1
        explanation: >
            Amazon SNS uses a publish/subscribe (pub/sub) messaging model, and does not require you to set up the notification server. Instead, you create topics, to which you push messages. Interested subscribers read messages from these topics.
            
    - questions:
        question: >
            What are policies for?
        answers:
        answers:
            - "To format database elements."
            - "To filter IoT messaages."            
            - "To define who should receive a notification."
            - "To define permissions."            
        correct_answer: 4
        explanation: >
            Policies are JSON documents that define permissions. They specify who can access resources and the actions that they can perform. Policies can be attached to users, groups, or roles.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
