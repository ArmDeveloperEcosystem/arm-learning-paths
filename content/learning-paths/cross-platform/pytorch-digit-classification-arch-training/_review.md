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
            Will the model make random predictions if it’s run before training?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Yes, however in such the case the model will produce random outputs, as the network has not been trained to recognize any patterns from the data. 
    - questions:
        question: >
            Which loss function was used to train the PyTorch model on the MNIST dataset?
        answers:
            - Mean Squared Error Loss
            - CrossEntropyLoss
            - Hinge Loss
            - Binary Cross-Entropy Loss
        correct_answer: 2
        explanation: >
            The CrossEntropyLoss function was used to train the model because it is suitable for multi-class classification tasks like digit classification. It measures the difference between the predicted probabilities and the true class labels, helping the model learn to make accurate predictions. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
