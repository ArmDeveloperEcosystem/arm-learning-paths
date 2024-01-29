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
            What is XAML for?
        answers:
            - "To declare views in various UI frameworks (WPF, WinUI 3, Xamarin Forms)"
            - "To accelerate applications"
            - "To implement logic of the application"
        correct_answer: 1
        explanation: >
            XAML, which stands for Extensible Application Markup Language, is a declarative XML-based language used primarily for defining graphical user interfaces in various Microsoft frameworks and technologies, including WPF (Windows Presentation Foundation), UWP (Universal Windows Platform), Xamarin.Forms, and WinUI.

    - questions:
        question: >
            Can you use C++ to implement WinUI apps?
        answers:
            - "Yes"
            - "No"            
        correct_answer: 1
        explanation: >
            Yes, you can use C++ to implement WinUI 3 apps. WinUI 3, being a part of the Windows App SDK, supports development in both C++ and C#
            

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
