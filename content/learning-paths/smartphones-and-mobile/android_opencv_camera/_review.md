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
            What is OpenCVLoader used for?
        answers:
            - "To compile OpenCV on Android."
            - "To load the OpenCV library."                        
        correct_answer: 2               
        explanation: >
            OpenCVLoader is used to load the OpenCV library.

    - questions:
        question: >
            What do you do to prepare the image acquired with OpenCV before display?
        answers:
            - "Detect the device’s current orientation and apply the necessary rotation to ensure the camera preview appears correctly oriented."
            - "Configure the app manifest."
            - "Configure the device."
        correct_answer: 1
        explanation: >
            To properly display the image from the camera, you need to detect the device’s current orientation and apply the necessary rotation to ensure the camera preview appears correctly oriented.
            
    - questions:
        question: >
            Can the thresholding of OpenCV be applied to RGB images?
        answers:
        answers:
            - "Yes."
            - "No."                        
        correct_answer: 2
        explanation: >
            Before you can apply thresholding, you need to convert the color image to grayscale using the Imgproc.cvtColor OpenCV function.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
