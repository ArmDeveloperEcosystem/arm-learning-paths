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
            How do you style the Electron application?
        answers:
            - "Using CSS"
            - "Using a style package"
            - "Using an npm"            
        correct_answer: 1               
        explanation: >
            CSS is the common approach to style Electron applications

    - questions:
        question: >
            What is the JSONPlaceholder?
        answers:
            - "A library for JSON serialization"
            - "A mock API for testing web apps"
        correct_answer: 2
        explanation: >
            JSONPlaceholder is a free online REST API service that serves as a mock server for testing and prototyping web applications

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
