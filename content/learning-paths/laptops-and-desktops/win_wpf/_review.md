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
            What is the **ObservableCollection**?
        answers:
            - "A dynamic data collection that provides notifications when items are added, removed, or when the whole list is refreshed"
            - "A dynamic data collection that can be used to observe hardware signals (i.e., when the USB stick is inserted or removed)"            
        correct_answer: 1
        explanation: >
            **ObservableCollection** is a dynamic data collection that provides notifications when items are added, removed or when the whole list is refreshed

    - questions:
        question: >
            Can you use Windows Presentation Foundation (WPF) on .NET 8?
        answers:
            - "Yes"
            - "No"            
        correct_answer: 1
        explanation: >
            Yes, WPF is available on .NET 8

    - questions:
        question: >
            What is the average percentage performance uplift on Arm64 compared to x86_64?
        answers:
            - "10%"
            - "30%"
            - "25%"
        correct_answer: 2
        explanation: > 
            There is on average a 30% reduction in computation times when the application ran on the Arm64 architecture compared to the x86_64 architecture
            

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
