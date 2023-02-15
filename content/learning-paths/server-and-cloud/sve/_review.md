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
            What is SVE vector register length?
        answers:
            - "128 bits"
            - "Any vector length from 128 to 2048 bits"
        correct_answer: 2                   
        explanation: >
            SVE and SVE2 do not define the size of the vector registers, but constrains it to a range of possible values, from a minimum of 128 bits up to a maximum of 2048 in 128-bit wide units.
    - questions:
        question: >
            Complete the sentence: the size of the predicate register is...
        answers:
            - "1/8th the size of SVE registers"
            - "the same as the vector register"
            - "128 bits"
        correct_answer: 1                    
        explanation: >
            SVE is vector-length agnostic and a predicate-centric architecture with vector registers and predicate registers. Predicate registers are 1/8th the size of SVE registers (1 bit/byte). 
    - questions:
        question: >
            Is SVE supported on all Arm v8-A and Arm v9-A processors?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                
        explanation: >
            Not all Arm v8-A processors support SVE instructions. However, they can still run SVE applications using the Arm Instruction Emulator. Armv9-A builds on SVE with the SVE2 extension.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
