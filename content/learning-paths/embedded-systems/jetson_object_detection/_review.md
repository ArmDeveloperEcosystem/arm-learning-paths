---
review:
    - questions:
        question: >
            True or False? You must use a MIPI CSI-2 Camera for object detection. 
        answers:
            - "True"
            - "False"
        correct_answer: 1                
        explanation: >
            Object detection can be done with still images, a USB camera, as well as other sources.

    - questions:
        question: >
            What program did you use for object detection?
        answers:
            - ImageNet
            - Skynet
            - DetectNet
            - TensorFlow
        correct_answer: 2                   
        explanation: >
            DetectNet is the program the Docker image provides for object detection and labeling.
               
    - questions:
        question: >
            True or False? The Jetson Orin Nano is underpowered for this use case.
        answers:
            - "True"
            - "False"
        correct_answer: 2          
        explanation: >
            The Jetson Orin Nano excels at this kind of task.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
