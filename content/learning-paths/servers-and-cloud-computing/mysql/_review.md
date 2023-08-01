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
            The MySQL serve default configuration (or out of box configuration) works without issue.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            The default configuration of MySQL works. However, the Learn how to Tune MySQL learning path should be completed to learn how to tune a MySQL server that is running on Arm.
    - questions:
        question: >
            There are numerous options for deploying MySQL on Arm.
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explanation: >
            From bare metal, to cloud VMs, to cloud provider database services. There are many ways to get access to different Arm based hardware for deploying MySQL server.
               
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
