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
            Which project template do you use to create the ASP.NET Core Web API project?
        answers:
            - "webapi"
            - "api"
            - "web-api"
            - "webapiproject"
        correct_answer: 1               
        explanation: >
            webapi is the name of the project template you use for the ASP.NET Core Web API projects.

    - questions:
        question: >
            Is Swagger a part of a default ASP.NET Core project template?
        answers:
            - "No"
            - "Yes"
        correct_answer: 2                     
        explanation: >
            Swagger is automatically included in the ASP.NET Core project (starting from version 6)

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
