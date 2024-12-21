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
            A secure boundary is sufficient for confidential computing.
        answers:
            - "True."
            - "False."
        correct_answer: 2                
        explanation: >
            A secure boundary is necessary for confidential computing, but it is not sufficient. There must also be a way to establish trust with the target compute environment that the boundary is protecting (the TEE). Trust needs to be built by a process that is both explicit and transparent. This process is known as attestation.
    - questions:
        question: >
            The CCA attestation token is divided at the top level into two sub-tokens. 
        answers:
            - "True."
            - "False."
        correct_answer: 1
        explanation: >
            The CCA attestation token is divided at the top-level into the platform token and the realm token.
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
