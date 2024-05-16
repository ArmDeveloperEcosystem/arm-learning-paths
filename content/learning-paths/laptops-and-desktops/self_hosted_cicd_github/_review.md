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
            When setting up a self-hosted runner do you need to manage software components?
        answers:
            - "True"
            - "False"
        correct_answer: 1               
        explanation: >
            When using self-hosted runners, you are responsible for patching the operating system and installing all the software required to build the application.

    - questions:
        question: >
            Which YAML section do you use to configure job dependency?
        answers:
            - "depends-on"
            - "needs"
            - "child"
        correct_answer: 2
        explanation: >
            Use jobs.<job_id>.needs to identify any jobs that must complete successfully before this job will run.

    - questions:
        question: >
            How do you store Docker credentials?
        answers:
            - "Directly in the YAML file"
            - "In GitHub secrets"            
        correct_answer: 2
        explanation: >
            You use GitHub secrets to securely store sensitive information like credentials

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
