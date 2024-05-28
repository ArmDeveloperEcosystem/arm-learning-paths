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
            What do you need to consider when using Arm intrinsics?
        answers:
            - "Ensuring that function calls adhere to the conventions of the C language to facilitate optimized code generation"
            - "Automatically convert parts of loops that do not use intrinsics into vectorized instructions to improve execution speed" 
            - "Loop unrolling"            
        correct_answer: 3
        explanation: >
            For loops that incorporate intrinsics, programmers are responsible for unrolling them, including manually writing any necessary loop tails to ensure proper execution.
    - questions:
        question: >
            Can SVE2 intrinsics provide a performance improvement?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Using SVE2 intrinsics enables significant performance improvement on 64-bit Arm powered phones running Android. 


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
