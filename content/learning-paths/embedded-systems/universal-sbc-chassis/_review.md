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
            If the single board computer isn't supported you are out of luck
        answers:
            - "true"
            - "false"
        correct_answer: 2
        explanation: >
            The GitHub repository contains the Fusion 360 project files, so you are free to modify the design as needed

    - questions:
        question: >
            What filament is optimal for this design?
        answers:
            - "ABS"
            - "PLA"
            - "PETG"
        correct_answer: 3
        explanation: >
            PETG has the ability to flex without breaking, which is needed for the thumb tabs on the card plate

    - questions:
        question: >
            What slicing software do you need to use
        answers:
            - "Cura"
            - "PrusaSlicer"
            - "OctoPrint"
            - "Whatever works best with your printer"
        correct_answer: 4
        explanation: >
            The STL files are software agnostic. Use whichever you are most comfortable with, and that works with your printer
    
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
