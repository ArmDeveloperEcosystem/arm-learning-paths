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
            To get enough memory, the Arm Automotive Solutions Software Reference Stack must be built on an Arm cloud instance.
        answers:
            - "True"
            - "False"
        correct_answer: 2               
        explanation: >
            You can build the automotive software stack on a local machine using the System76 Thelio Astra Linux desktop.

    - questions:
        question: >
            Which things below are benefits of Parsec?
        answers:
            - "Platform Agnostic API"
            - "Secure boot and attestation"
            - "Key management and cryptography"
            - "All of the above"
        correct_answer: 4                     
        explanation: >
            All of these help Parsec provide unified access to hardware security.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
