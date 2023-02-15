---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            Performance Analyzer is used to extract actionable information from Streamline captures.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Streamline captures can be complicated for a new user. With Performance Analyzer you can generate an easy to understand report highlighting key areas to focus on.

    - questions:
        question: >
            Performance Analyzer can generate its report in JSON format?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            True. JSON is particularly beneficial for use within a CI/CD workflow.
               
    - questions:
        question: >
            Mali Offline Compiler can only analyze OpenGL ES shaders.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            You can compile OpenGL ES and Vulkan shader programs.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
