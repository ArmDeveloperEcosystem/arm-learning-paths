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
            Does .NET MAUI project contains sub-platform-specific projects?
        answers:
            - "Yes"
            - "No"            
        correct_answer: 2
        explanation: >
            .NET MAUI, contrary to Xamarin.Forms, contains a single project. The platform-specific code is included in the Platforms sub-folder

    - questions:
        question: >
            What is the MauiProgram.cs file for?
        answers:
            - "It serves the purpose of the application's entry point"
            - "It enables you to specify platforms on which the application can run"
        correct_answer: 1
        explanation: >
            MauiProgram.cs contains the entry point for .NET MAUI application. It's where you configure and set up the app, including services, dependencies, and the main app configuration. It typically contains the CreateMauiApp method, which builds and returns an instance of MauiApp class

    - questions:
        question: >
            What is the MVVM pattern for?
        answers:
            - "To build a single page applications"
            - "To accelerate applications"
            - "To separate concerns, e.g., separate the logic from the view"
        correct_answer: 3
        explanation: >
            The Model-View-ViewModel (MVVM) architectural pattern is designed to separate an application's business and presentation logic from its user interface
            

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
