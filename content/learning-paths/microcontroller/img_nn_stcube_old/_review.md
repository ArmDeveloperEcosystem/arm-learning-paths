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
            Do the number of color channels in yor dataset impact the input shape of the convolution layer?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
            The number of color channels also referred to as depth is one of the array inputs to the CNN.
    - questions:
        question: >
            Does model training time vary based on number of epochs used?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
            As the number of epochs increases, the same number of times weights are changed in the neural network and hence it takes longer.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
