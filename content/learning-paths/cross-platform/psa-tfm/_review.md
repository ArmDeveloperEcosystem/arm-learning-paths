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
            Arm Trusted Firmware is
        answers:
            - "A framework to create custom Linux-based systems"
            - "A web-based platform to explore Arm IP"
            - "A reference implementation of the Platform Security Architecture (PSA)"
        correct_answer: 3
        explanation: >
            Arm Trusted Software forms the foundations of a Trusted Execution Environment (TEE) or Secure Processing Environment (SPE).
    - questions:
        question: >
            What is Corstone-1000?
        answers:
            - An Arm processor with secure capabilities
            - A configurable subsystem of Arm processor and security IP			
        correct_answer: 2
        explanation: >
            Corstone-1000 is pre-verified, configurable subsystem to enable designers build secure SoCs faster.
    - questions:
        question: >
            The Cortex-A ("host") processor is considered secure by the Secure Enclave
        answers:
            - True
            - False		
        correct_answer: 2
        explanation: >
            All components outside of the enclave are considered as less trustworthy. It is only after verification that the host is taken out of reset.
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
