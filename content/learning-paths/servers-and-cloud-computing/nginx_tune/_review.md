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
            Linux kernel parameters can impact Nginx performance.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Kernel network stack can have a direct impact on Nginx.

    - questions:
        question: >
            Which of the following directives selects the port and protocol an Nginx file server will use?
        answers:
            - "root"
            - "worker_connections"
            - "sendfile"
            - "listen"
        correct_answer: 4                  
        explanation: >
            The listen directive can select a port and protocol like HTTP or HTTPS.
               
    - questions:
        question: >
            You should use the latest version of GCC to build Nginx from source.
        answers:
            - "True"
            - "False"
        correct_answer: 1                    
        explanation: >
            GCC is constantly updated with improvements for Arm. It's important to use the latest available version of GCC.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
