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
            The Arm RAN Acceleration library supports:
        answers:
            - "Neon"
            - "SVE"
            - "SVE2"
            - "All the above"
        correct_answer: 4
        explanation: >
            The library can be built to support all these vectorizing technologies, selected with ARMRAL_ARCH macro at build time.
    - questions:
        question: >
            All vectorizing technologies are available on all platforms
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
             The capabilities of platforms will vary. You will see run time errors if you build for features that are not available for that platform.
               
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
