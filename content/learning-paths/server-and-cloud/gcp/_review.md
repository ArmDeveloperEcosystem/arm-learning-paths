---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explination:      A short (1-3 sentence) explination of why the correct answer is correct. Can add additional context if desired

review:
    - questions:
        question: >
            If I accidentally delete my instance, I can retrieve it.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Instances that have been deleted cannot be retrieved. However, if an instance is simply stopped, you can start it again.

    - questions:
        question: >
            Terraform is an Infrastructure as Code (IaC) solution created by AWS.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Terraform is not specific to AWS and was created by HashiCorp.

    - questions:
        question: >
            We can connect to a VM that does not have an external IP address using a bastion host.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            When we use a bastion host, we log into the bastion host first, and then into the target private VM.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
