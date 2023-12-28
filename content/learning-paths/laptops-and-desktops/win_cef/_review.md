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
            Do you need to rebuild CEF application, if you modify the page to be rendered?
        answers:
            - "Yes"
            - "No"            
        correct_answer: 2
        explanation: >
            CEF application will render an updated page without the need of rebuilding the CEF application

    - questions:
        question: >
            What is the CefBrowserProcessHandler? 
        answers:
            - "It is an interface exclusive to the browser process"
            - "It is an interface for downloading Chrome Web Browser"
            - "It is a class to download CEF"
        correct_answer: 1
        explanation: >
            

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
