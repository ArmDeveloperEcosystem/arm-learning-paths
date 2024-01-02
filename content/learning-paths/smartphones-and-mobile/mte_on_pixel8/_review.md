---
review:
    - questions:
        question: >
            Can MTE be enabled on my Google Pixel 8?
        answers:
            - Yes
            - No
        correct_answer: 1                    
        explanation: >
            MTE option is part of Developer options. Developer options need to be enabled first on your Google Pixel 8 phone to access MTE.

    - questions:
        question: >
            Which of the statements below is false?
        answers:
            - MTE working principle is based on a Lock and Key model.
            - Tagging memory implements the lock.
            - Pointers are modified to contain the key.
            - At runtime the CPU checks that the pointer and the metadata tags match. If so, the application crashes in any device.
        correct_answer: 4                   
        explanation: >
            At runtime the CPU checks that the pointer and the metadata tags match, on each load and store. Android apps that incorrectly store information in the top byte of the pointer are guaranteed to break on an MTE-enabled device.
               
    - questions:
        question: >
            Which of the statements below is true?
        answers:
            - The bug report is automatically generated for us everytime the application crashes.
            - We need to trigger the creation of the bug report using Bug report option in Developer options.
            - The bug report is a single file we can visualize directly in our phone.            
        correct_answer: 2          
        explanation: >
           We have to tap Bug report option in Developer options to capture the bug report.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
