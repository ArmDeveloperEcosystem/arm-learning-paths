---
review:
    - questions:
        question: >
            Does CMSIS v6 support assembly startup files?
        answers:
            - Yes
            - No
        correct_answer: 2                    
        explanation: >
            CMSIS v6 only support C startup files for better code portability and less issues when switching between compilers.

    - questions:
        question: >
            What does a scatter file/linker script do?
        answers:
            - It helps the compiler to understand the code structure.
            - It helps you to understand the code structure.
            - It enables you to specify the memory map of an image to the linker.
        correct_answer: 3                   
        explanation: >
            The scatter-loading mechanism enables you to specify the memory map of an image to the linker using a description in a text file. Scatter-loading gives you complete control over the grouping and placement of image components.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
