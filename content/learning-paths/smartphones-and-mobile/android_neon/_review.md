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
            Dot Product instructions were added in the Arm v7-A architecture.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Dot product instructions were added in the Arm v8.4-A architecture. 
    - questions:
        question: >
            Neon intrinsics provide a performance improvement to dot product implementation.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Using Neon intrinsics can provide over 30 percent performance improvement to dot product implementation on 64-bit Arm powered phones running Android. 


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
