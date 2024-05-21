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
            Are Windows Arm64 self-hosted runners supported by GitHub Actions?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1               
        explanation: >
            GitHub Actions supports self-hosted Windows Arm runners which provides developers the capability to deploy their workflows in a Windows Arm64 environment.

    - questions:
        question: >
            Can you use Windows Sandbox as a self-hosted runner with GitHub Actions?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Windows Sandbox provides a lightweight desktop environment to safely run applications in isolation. You can configure Windows Sandbox as a self-hosted Windows Arm64 runner with GitHub Actions.

    - questions:
        question: >
            Does .NET 6 framework for Arm include support for WPF applications?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                     
        explanation: >
            Starting with .NET 6 framework support was added for WPF on Arm. It has also been ported to .NET 5.0.8.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
