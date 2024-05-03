---
review:
    - questions:
        question: >
            What is the purpose of symbol files?
        answers:
            - "They provide a mapping between the binary code and the human-readable identifiers in the source code."
            - "They are used to store the graphical symbols used in the user interface of the program."
            - "They contain the compiled machine code that is directly executable by the computer."
            - "All of the above."
        correct_answer: 1
        explanation: >
            Symbol files enable debuggers to identify program locations, function names, and display source files during code execution.

    - questions:
        question: >
            When debugging Trusted Firmware-A, how should the symbol files be loaded considering the offsets for the different Exception Levels that the BLs run at?
        answers:
            - "Load the files at the offset values specified in the source code."
            - "Load the files at 0x0 because ATF uses absolute addresses for its symbols."
            - "Load the files at the base address of the memory region."
            - "The loading offset does not matter."
        correct_answer: 2
        explanation: >
            ATF uses absolute addresses for its symbols so we ensure an offset of 0.
               
    - questions:
        question: >
            You've successfully added the symbol files, but the code does not stop at the breakpoints. What could the reason be?
        answers:
            - "The symbol files are loaded into the incorrect virtual address space and memory offset."
            - "You have forgotten to check the Execute debugger commands."
            - "All of the above."
        correct_answer: 3
        explanation: >
            There could be multiple reasons. It's important to load the symbol files into the correct virtual address space and memory offset. If incorrect, the debugger won't be able to properly map the symbols to the correct locations in the code. The Execute debugger command ensures that the add-symbol-file command is actually being executed. 



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

