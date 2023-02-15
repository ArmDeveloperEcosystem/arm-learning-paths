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
            Does Hyperscan run on Arm servers?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                    
        explanation: >
            The answer is yes: Vectorscan is a fork of Intel's Hyperscan regex library that is fully supported on 64-bit Arm servers

    - questions:
        question: >
            Can you run Snort3 with hyperscan as the search engine on an Arm machine?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                     
        explanation: >
            You can build and run Snort3 with hyperscan for Arm


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
