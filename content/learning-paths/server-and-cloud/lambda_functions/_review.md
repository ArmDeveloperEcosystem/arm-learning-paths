---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            AWS Lambda is a serverless computing
        answers:
            - "True"
            - "False"
        correct_answer: 1                    
        explanation: >
            Yes, AWS Lambda is a serverless computing service.

    - questions:
        question: >
            Does AWS Lambda support environment variables
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explanation: >
             Yes, You can easily create and modify environment variables from the AWS Lambda Console, CLI, or SDKs.
               



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
