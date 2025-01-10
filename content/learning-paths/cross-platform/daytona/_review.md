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
            Can Daytona be used to manage local dev container based environments?
        answers:
            - "Yes."
            - "No."
        correct_answer: 1                 
        explanation: >
            Daytona can manage local development environments.

    - questions:
        question: >
            Which abstraction manages the details of the connection to your source code projects?
        answers:
            - "Provider."
            - "Target."
            - "Git provider."
        correct_answer: 3                  
        explanation: >
            Git providers connect your source code to your workspaces.

    - questions:
        question: >
            Can Daytona manage remote development environments in machines provided by cloud service providers?
        answers:
            - "Yes."
            - "No."
        correct_answer: 1                  
        explanation: >
            Daytona can manage development environments in AWS, Azure, and GCP. All offer Arm-based virtual machines.
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
