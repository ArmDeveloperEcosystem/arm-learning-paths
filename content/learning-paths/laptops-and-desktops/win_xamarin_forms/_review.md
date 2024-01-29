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
            What is the MVVM pattern for?
        answers:
            - "To build a single page applications"
            - "To accelerate applications"
            - "To separate concerns, e.g. separate the logic from the view"
        correct_answer: 3
        explanation: >
            The Model-View-ViewModel (MVVM) architectural pattern is designed to separate an application's business and presentation logic from its user interface

    - questions:
        question: >
            Can you use Xamarin.Forms to build iOS apps?
        answers:
            - "Yes"
            - "No"            
        correct_answer: 1
        explanation: >
            Yes, Xamarin.Forms enables you to build cross-platform applications using the single codebase
            

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
