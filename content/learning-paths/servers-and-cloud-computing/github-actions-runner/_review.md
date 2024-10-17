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
            With RunsOn, any AWS EC2 instance with Graviton processors can be used for GitHub Actions.
        answers:
            - "True"
            - "False"
        correct_answer: 1                   
        explanation: >
            You can select any instance type and use job labels to configure details such as number of vCPU and RAM size.

    - questions:
        question: >
            Is RunsOn free for non-commercial projects?
        answers:
            - "No"
            - "Yes"
        correct_answer: 2                   
        explanation: >
            RunsOn is free for non-commerical projects. You pay the cost of the EC2 instances that are used and a small free for the  AWS App Runner service. 

    - questions:
        question: >
            Which Neoverse processor is not available for GitHub Actions when using RunsOn in AWS?
        answers:
            - "Neoverse N1"
            - "Neoverse N2"
            - "Neoverse V1"
            - "Neoverse V2"
        correct_answer: 2                    
        explanation: >
            Neoverse N2 is not available in AWS. Graviton2 is Neoverse N1, Graviton3 is Neoverse V1, and Graviton4 is Neoverse V2.
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
