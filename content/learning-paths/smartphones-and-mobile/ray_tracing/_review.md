---
review:
    - questions:
        question: >
            Which of these is the recommended way to do ray traversal on Arm GPUs?
        answers:
            - Ray query
            - Ray tracing pipeline
        correct_answer: 1
        explanation: >
            Ray query is the most efficient way to implement ray traversal on Arm GPUs.

    - questions:
        question: >
            When designing acceleration structure, which of the following statements is true?
        answers:
            - Empty space does not matter, reduce BLAS overlap.
            - Minimize empty space and minimize overlap.
            - BLAS overlap does not matter, reduce empty space.
            - On Arm GPUs, neither empty space nor BLAS overlap matters.
        correct_answer: 2
        explanation: >
            On ray tracing, the quality of your acceleration structure can have a huge performance impact. Try to reduce overlap across BLASes and reduce empty space inside a BLAS as much as possible.
    - questions:
        question: >
            Can reflections handle objects outside the screen?
        answers:
            - Ray tracing reflections can reflect objects not on the screen but Screen Space Reflections can only reflect objects on the screen.
            - Both Screen Space Reflections and ray tracing reflections can reflect objects not on the screen.
            - Neither Screen Space Reflections nor ray tracing reflections can reflect objects on the screen.
            - Ray tracing reflections can only reflect objects on the screen but Screen Space Reflections can reflect objects not on the screen.
        correct_answer: 1
        explanation: >
             Screen Space Reflections obtains the information from the G-buffer so it can only reflect object currently on the screen. Ray tracing reflections offer better quality since they can handle any object in the acceleration structure, including objects not on the screen.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
