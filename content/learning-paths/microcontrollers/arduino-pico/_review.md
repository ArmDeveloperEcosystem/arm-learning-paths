---
review:
    - questions:
        question: >
            What makes embedded programming different from application programming?
        answers:
            - Embedded software requires the use of assembly language
            - Embedded software doesn't use language constructs like classes and functions
            - Embedded software typically runs on resource-limited hardware
        correct_answer: 3                    
        explanation: >
            Fundamentally, there is no difference between embedded programming and application programming. The biggest difference is the hardware resources available to your program.

    - questions:
        question: >
            You can only write Arduino code for Arduino brand devices.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            The Arduino core software works with board support packages that cover a number of boards, not all of these are Arduino branded. For example, the Raspberry Pi branded Pico board is not from Arduino.
               
    - questions:
        question: >
            Which function of your sketch does Arduino core call when your board first starts up?
        answers:
            - main()
            - setup()
            - loop()
            - delay()
        correct_answer: 2          
        explanation: >
            Arduino sketches don't have a main() function, instead Arduino core calls the setup() function at start.

    - questions:
        question: >
            Which function of your sketch does Arduino core call continuously after it has started?
        answers:
            - main()
            - setup()
            - loop()
            - delay()
        correct_answer: 3          
        explanation: >
            After startup, Arduino core calls loop() continuously.

    - questions:
        question: >
            What happens when your loop() function completes?
        answers:
            - Your setup() function will be called again
            - Your loop() function will be called again
            - Your Sketch will stop running
            - Your board will turn off
        correct_answer: 2          
        explanation: >
            Arduino core continuously calls loop() until you call exit() or the board loses power.

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
            Variables can be changed during an interrupt but both delay() and Serial.println() depend on background timing updates that won't happen until after the interrupt handling has finished and returned execution back to normal.
               
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
