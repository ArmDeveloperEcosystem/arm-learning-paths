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
            How is the PyTorch model loaded in the Android app?
        answers:
            - Using Module.load(assetManager.open("model.pth")).
            - By directly passing the model file path to Tensor.load().
            - Using Module.load(assetFilePath("model.pth")).
            - By copying the model file to the app’s external storage.
        correct_answer: 3
        explanation: >
            The PyTorch model is loaded in the Android app using the Module.load() method, which takes the absolute file path of the model. The assetFilePath("model.pth") function copies the model from the assets directory to the internal storage and returns its path, which is required by Module.load().
    - questions:
        question: >
            How is the data prepared before running inference on the PyTorch model?
        answers:
            - The bitmap image is converted to a tensor with a shape of [1, 3, 224, 224].
            - The bitmap is resized and normalized to a tensor of shape [1, 1, 28, 28].
            - The image is converted to grayscale and then reshaped to [1, 28, 28].
            - The image is flattened into a one-dimensional array.
        correct_answer: 2
        explanation: >
            Before running inference, the bitmap is converted to a float array and then to a tensor with a shape of [1, 1, 28, 28]. The 1 in the first dimension represents the batch size, the second 1 is the number of channels (grayscale), and 28, 28 are the height and width of the image.
    - questions:
        question: >
            Which transformation is applied to the MNIST test images during data preparation in the app?
        answers:
            - Rotation and scaling.
            - Conversion to a tensor with RGB normalization.
            - Conversion to a tensor with normalization specific to grayscale images.
            - Random cropping and flipping.

        correct_answer: 3
        explanation: >
            During data preparation, the MNIST images are converted to tensors and normalized for grayscale images. This involves scaling the pixel values to a range of [-1, 1], which matches the input expectations of the pre-trained PyTorch model used in the app.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
