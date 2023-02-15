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
            WSL is a way to run Linux binaries for different architectures using instruction translation.
        answers:
            - "True"
            - "False"
        correct_answer: 2               
        explanation: >
            WSL is the Windows Subsystem for Linux and provides a way to run the Linux kernel and applications on computers running Windows.

    - questions:
        question: >
            Does WSL require VNC to run graphical Linux applications?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                     
        explanation: >
            Graphical Linux applications running in WSL automatically show up on the Windows desktop with Windows 11.
               
    - questions:
        question: >
            What is the best way to back up your work in WSL?
        answers:
            - "Create a tar file of your home directory and scp it to another machine"
            - "Use the wsl --export command"
            - "Copy important files to a tape or CD-ROM"
        correct_answer: 2                     
        explanation: >
            The wsl export command will save the entire filesystem as a tar file which can easily be restored with the wsl import command.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
