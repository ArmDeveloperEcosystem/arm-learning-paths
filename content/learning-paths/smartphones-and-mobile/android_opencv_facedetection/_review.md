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
            What is Haar XML file?
        answers:
            - "It contains device description."
            - "It is used to record images from the camera."
            - "It contains pre-trained data for detecting specific objects, such as faces, eyes, and cars."
        correct_answer: 3
        explanation: >
            A Haar cascade file is an XML file used in computer vision, specifically within the OpenCV library, to perform object detection. It contains pre-trained data for detecting specific objects, such as faces, eyes, and cars. The file is created using the Haar cascade classifier algorithm, which is based on machine learning.
            
    - questions:
        question: >
            What you can do to accelerate face detection?
        answers:
        answers:
            - "Upscale the image."
            - "Downscale the image."                        
        correct_answer: 2
        explanation: >
            Downscaling the image accelerates face detection.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
