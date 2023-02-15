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
            The Azure CLI can be used to find virtual machine images to deploy on Arm instances.
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explanation: >
            The "vm image" command is a good way to find virtual machine images.

    - questions:
        question: >
            Which command implements changes in a Terraform configuration?
        answers:
            - tf apply
            - tf init
            - tf plan
        correct_answer: 1                     
        explanation: >
            Terraform apply is used to apply changes to the configuration.
               



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
