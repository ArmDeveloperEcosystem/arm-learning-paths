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
            Which solution provides higher performance for building containers?
        answers:
            - "QEMU virtualization."
            - "Arm-hosted runners."
        correct_answer: 2                 
        explanation: >
            Arm-hosted runners are faster than QEMU because there is no instruction translation. QEMU may be suitable for very small builds but is too slow for large projects. 

    - questions:
        question: >
            What is the benefit of Arm-hosted runners compared to self-hosted runners?
        answers:
            - "Self-hosted runners are slower than the Arm-hosted runners that GitHub provides."
            - "Arm-hosted runners don't require you to manage servers."
            - "GitHub-provided Arm-hosted runners are free, and self-hosted runners are not."
        correct_answer: 2                  
        explanation: >
            Arm-hosted runners are managed by GitHub so you don't need to manage hardware yourself. The cost and performance of self-hosted runners depends on the hardware you choose to use for a self-hosted runner.
               
    - questions:
        question: >
            Can Arm-hosted runners replace self-hosted runners currently on an Arm server?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
            You can use Arm-hosted runners instead of your own Arm server with a self-hosted runner installed.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
