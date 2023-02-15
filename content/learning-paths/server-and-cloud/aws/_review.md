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
            Private key files used with SSH must be accessible to others (read permission).
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Private key files must not be readable for others, use chmod 400 to set the permission

    - questions:
        question: >
            Terraform is an Infrastructure as Code (IaC) solution created by AWS.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Terraform is not specific to AWS and was created by HashiCorp.
               



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
