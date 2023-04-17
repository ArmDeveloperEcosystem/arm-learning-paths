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
            Does SIMD Everywhere work to port AVX512 to Arm Neon?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
            Yes, SIMD Everywhere can port AVX512 to Neon. However sse2neon cannot.

    - questions:
        question: >
            When porting code to Arm Neon, SSE intrinsics must be re-written to use NEON intrinsics
        answers:
            - "True"
            - "False"
        correct_answer: 2                    
        explanation: >
            False. With the use of sse2neon or SIMDe, there is no need to re-write intrinsics.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
