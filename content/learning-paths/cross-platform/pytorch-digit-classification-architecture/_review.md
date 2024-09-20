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
            Does the input layer of the model flatten the 28x28 pixel image into a 1D array of 784 elements?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes, the model uses nn.Flatten() to reshape the 28x28 pixel image into a 1D array of 784 elements for processing by the fully connected layers.
    - questions:
        question: >
            Does the model use dropout layers with a 20% dropout rate after each hidden layer?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes, the model applies dropout layers after each hidden layer, randomly setting 20% of the neurons to 0 during training to prevent overfitting. 
    - questions:
        question: >
            Will the model make random predictions if it’s run before training?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes, however in such the case the model will produce random outputs, as the network has not been trained to recognize any patterns from the data. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
