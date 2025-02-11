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
            What is the purpose of the `ImageProcessor` class?
        answers:
            - "To handle user interactions for the application."
            - "To apply a selected image processing operation to a Mat object."
            - "To manage and display performance metrics for image processing."
        correct_answer: 2
        explanation: >
            The `ImageProcessor` class is responsible for applying a specified image processing operation from the `ImageOperation` enum to a Mat object.

    - questions:
        question: >
            How does the `PerformanceMetrics` class compute the standard deviation of operation durations?
        answers:
            - "By finding the difference between the maximum and minimum durations."
            - "By calculating the square root of the average of squared differences from the mean."
            - "By dividing the total duration by the number of repetitions."
        correct_answer: 2
        explanation: >
            The `PerformanceMetrics` class computes the standard deviation by finding the mean of durations, calculating the squared differences from the mean, averaging these values, and taking the square root of the result.

    - questions:
        question: >
            What is the purpose of the `REPETITIONS` constant in `MainActivity`?
        answers:
            - "To set the number of times the user can retry loading an image."
            - "To determine how many times an image operation is repeated for performance measurement."
            - "To limit the maximum number of image processing operations the app supports."
        correct_answer: 2
        explanation: >
            The `REPETITIONS` constant specifies how many times an image operation is repeated to measure performance and gather statistical data.

    - questions:
        question: >
            What does the `convertBitmapToMat` method in `MainActivity` achieve?
        answers:
            - "It initializes OpenCV with the provided bitmap."
            - "It converts a Bitmap object into a Mat object and prepares it for processing by changing its color space."
            - "It displays the bitmap on the screen."
        correct_answer: 2
        explanation: >
            The `convertBitmapToMat` method converts a Bitmap to a Mat object using OpenCV utilities and changes its color space from RGBA to BGR, making it ready for further image processing.
            
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
