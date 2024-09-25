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
            What is TorchScript used for in the process described above?
        answers:
            - To optimize the model’s weights and biases during training.
            - To visualize the model’s predictions on new data.
            - To save the model’s architecture and parameters in a portable format.
            - To increase the learning rate during training
        correct_answer: 3
        explanation: >
            TorchScript is used to serialize both the model’s architecture and its learned parameters, making the model portable and independent of the original class definition. This simplifies deployment and allows the model to be loaded and used in different environments without needing the original code.
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
    - questions:
        question: >
            Why do we set the model to evaluation mode during inference?
        answers:
            - To increase the learning rate.
            - To prevent changes to the model’s architecture.
            - To ensure layers like dropout and batch normalization behave correctly.
            - To load additional data for training
        correct_answer: 3
        explanation: >
            Setting the model to evaluation mode (model.eval()) ensures that certain layers, such as dropout and batch normalization, function correctly during inference. In evaluation mode, dropout is disabled, and batch normalization uses running averages instead of batch statistics, providing consistent and accurate predictions.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
