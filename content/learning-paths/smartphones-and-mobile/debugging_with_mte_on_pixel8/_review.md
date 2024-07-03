---
review:
    - questions:
        question: >
             Which of the below statements is true?
        answers:
            - Memory safety bugs are errors in handling memory by the hardware. Although important, they are not very common in the Android codebase.
            - Memory safety bugs are errors in handling memory by the software. Although important, they are not very common in the Android codebase.
            - Memory safety bugs are errors in handling memory by the software. They are important and very common in the Android codebase.
            
        correct_answer: 3                    
        explanation: >
            Memory safety bugs are errors in handling memory by software. Memory safety bugs are the most common issue in the Android codebases. They account for over 70% of high severity security vulnerabilities and for millions of user-visible crashes.

    - questions:
        question: >
           Which statement is false?
        answers:
            - The MTE Test application implements common memory safety bugs.
            - The MTE Test application implements four common memory safety bugs.
            - The MTE Test application implements four function that trigger memory safety bugs.
            - The MTE Test application implements four functions which are common in the Android codebase.
        correct_answer: 4                   
        explanation: >
            The MTE Test application implements common memory safety bugs. It implements four common memory safety bugs using four functions. Each function triggers a memory safety bug.
               
    - questions:
        question: >
            Which of the below statements is true?
        answers:
            - To debug an application in Android Studio with MTE, you only need to enable MTE in the phone settings.
            - To debug an application in Android Studio with MTE, you only need to enable MTE in the Android manifest.
            - To debug an application in Android Studio with MTE, you need to enable MTE in the Android settings and in the Android manifest.
            - To debug an application in Android Studio with MTE, you only need to launch Android Studio with the device connected.
        correct_answer: 3          
        explanation: >
            To debug an application in Android Studio with MTE, you need to enable MTE in the Android manifest by assigning to the *memTagMode* attribute any of the values: *sync*, *async*, or *asymm*. However, this is not enough. MTE also must be enabled in *System-> Developer options-> Memory tagging Extension*.

    - questions:
        question: >
            Which of these statements is false?
        answers:
            - Memory safety bugs always make applications crash.
            - If MTE is enabled in the application manifest and in the phone settings, a memory safety bug always makes the application crash.
            - A memory safety bug can be detected by debugging the application in Android Studio with MTE enabled in the application manifest and in the phone settings.
            - To debug an application in Android Studio with MTE enabled requires you to have the device connected and recognized by Android Studio.
        correct_answer: 1          
        explanation: >
            To debug an application in Android Studio with MTE, you need to enable MTE in the phone settings and in the Android manifest by assigning to *memTagMode* attribute any of the values: *sync*, *async*, or *asymm*. If we connect a device to Android Studio and it is recognized, an application running in debug mode with a memory safety bug crashes and Android Studio shows the line of code that triggers the memory bug. 




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
