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
            Ansible is a pull-based configuration management tool
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Ansible works on the Push mechanism.
    - questions:
        question: >
            We can keep secret data in the playbook
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explanation: >
             Yes, it is possible to keep secret data in your Ansible content with the use of Vault in playbooks.
               
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
