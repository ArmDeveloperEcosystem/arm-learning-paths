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
            Arm Trusted Firmware is
        answers:
            - "A framework to create custom Linux-based systems"
            - "A web-based platform to explore Arm IP"
            - "A reference implementation of Platform Security Architecture (PSA)"
        correct_answer: 3                 
        explanation: >
            You can run Arm Trusted Firmware on a number of platforms, including the Corstone-1000 Fixed Virtual Platform (FVP) and the MPS3 FPGA prototyping board.

    - questions:
        question: >
            How can you Arm Trusted Firmware on the Corstone-1000 FVP?
        answers:
            - "Through Arm Virtual Hardware or the Arm Ecosystem FVP page"
            - "Through Arm Virtual Hardware and the MPS3 FPGA prototyping board"
        correct_answer: 1                  
        explanation: >
            The Corstone-1000 FVP is a reference implementation which is available with no license control and direct download. You can review this in the "Corstone-1000 FVP or MPS3 image" section.
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
