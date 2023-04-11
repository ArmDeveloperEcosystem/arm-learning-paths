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
            Can the lscpu command can be used to check if a system supports atomics?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                   
        explanation: >
            Check the Flags output and look for atomics to be listed.

    - questions:
        question: >
            All processors implementing the Armv8-A architecture support Large System Extensions
        answers:
            - "True"
            - "False"
        correct_answer: 2                    
        explanation: >
            Some Armv8-A processors such as the Cortex-A72 do not support LSE.
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
