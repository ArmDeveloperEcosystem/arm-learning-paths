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
            Does AWS IoT Core use MQTT protocol?
        answers:
            - "No"
            - "Yes"
        correct_answer: 2
        explanation: >
            Yes, AWS IoT Core uses MQTT protocol for secure data transmission.

    - questions:
        question: >
            Can you use the device's certificate to manage device permissions in AWS IoT Core?
        answers:
            - "Yes"
            - "No"            
        correct_answer: 1
        explanation: >
            Yes, you attach the policy to the certificate in order to control device permissions.

    - questions:
        question: >
            What do you use to connect a device to the AWS IoT Core?
        answers:
            - "AWS Device SDK"
            - "AWS IoT Core SDK"
            - "AWS Core SDK"
        correct_answer: 1
        explanation: > 
            You use AWS Device SDK to implement applications that connect to the AWS cloud.
            

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
