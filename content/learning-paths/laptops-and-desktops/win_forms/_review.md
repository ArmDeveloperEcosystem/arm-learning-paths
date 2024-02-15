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
            What is the NumericUpDown control for?
        answers:
            - "It enables the user to provide a numeric input of a given range in specific steps"
            - "For creating a dropdown list"
            - "For creating a text box with scrollable input"
        correct_answer: 1
        explanation: >
            NumericUpDown control enables the user to provide a numeric input

    - questions:
        question: >
            Can you use Windows Forms on .NET or do you need .NET Framework?
        answers:
            - "Yes, Windows Forms is available on .NET"
            - "No, Windows Forms is available in .NET Framework only"            
        correct_answer: 1
        explanation: >
            Microsoft provides a port of Windows Forms for .NET
            

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
