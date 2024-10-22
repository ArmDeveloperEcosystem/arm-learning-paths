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
            What is the purpose of layer fusion in neural network optimization?
        answers:
            - To increase the size of the model
            - To combine multiple layers into one to reduce computational overhead            
            - To add dropout to the model
            - To improve the training process
        correct_answer: 2
        explanation: >
            Layer fusion combines multiple operations, such as linear layers and activation functions, into one, reducing the computational overhead and improving inference performance.
    - questions:
        question: >
            How does quantization improve the performance of models on mobile devices?
        answers:
            - By increasing the precision of the model’s weights
            - By reducing the size and precision of weights and activations
            - By enabling the model to use more layers
            - By increasing the batch size
        correct_answer: 2
        explanation: >
            Quantization reduces the precision of the model’s weights and activations (e.g., from float32 to int8), making the model smaller and faster without significant loss in accuracy. 
    - questions:
        question: >
            Why are dropout layers typically removed during inference?
        answers:
            - Dropout layers are only useful for improving memory usage
            - Dropout layers are not compatible with mobile devices
            - Dropout layers are used during training to prevent overfitting and are unnecessary during inference
            - Dropout layers increase the inference time
        correct_answer: 3
        explanation: >
            Dropout layers are used during training to prevent overfitting by randomly deactivating neurons, but they are not necessary during inference, where the entire model is used for prediction. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
