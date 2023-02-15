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
            Is pointer authentication available on all Arm Cortex-A CPUs?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                    
        explanation: >
            The answer is no: Pointer Authentication and Branch Target Identification is available only on Arm CPUs using ARMv8.3-A architecture and later extensions. It was also introduced in Armv8.1-M acrchitecture CPUs.

    - questions:
        question: >
            When using pointer authentication, the signature of the address is stored in the lowest bits of the 64-bit address.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            The signature is stored in the upper bits of the 64-bit virtual address.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
