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
            Which flag do you use to specify the processor architecture for the dotnet run command
        answers:
            - "-a"
            - "--arch"
            - "--a"
            - "-processor"
        correct_answer: 1               
        explanation: >
            -a is the flag you use to specify the processor architecture, e.g., dotnet run -a x64.

    - questions:
        question: >
            Which library do you use to benchmark .NET applications?
        answers:
            - "PerformanceDotNet"
            - "BenchmarkDotNet"
        correct_answer: 2                     
        explanation: >
            BenchmarkDotNet is the commonly used library for benchmarking .NET applications

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
