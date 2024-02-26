---
review:
    - questions:
        question: >
            What does a hardware interrupt do?
        answers:
            - Pauses the normal execution of a program for the execution of a different piece of code
            - Turns your device off until you turn it back on again
            - Starts talking over you while you're talking
        correct_answer: 1                    
        explanation: >
            A hardware interrupt will cause the device to pause the application code that is currently running so that the interrupt handler code can be run immediately.

    - questions:
        question: >
            Which of the following can be called from inside an interrupt handler?
        answers:
            - delay(500)
            - event_happened = true
            - Serial.println("Hello world")
        correct_answer: 2                   
        explanation: >
            Variables can be changed during an interrupt, but both delay() and Serial.println() depend on background timing updates that won't happen until after the interrupt handling has finished and returned execution back to normal.
               
    - questions:
        question: >
            Which of the following is not a condition for an interrupt?
        answers:
            - RISING
            - FALLING
            - CHANGE
            - IS_NULL
        correct_answer: 4          
        explanation: >
            Hardware interrupts can be triggered by a change in an input pin, either rising, falling, or both.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
