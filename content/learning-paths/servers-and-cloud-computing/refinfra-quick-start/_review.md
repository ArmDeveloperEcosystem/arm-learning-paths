---
review:
    - questions:
        question: >
            Why do we use the repo tool?
        answers:
            - repo allows for the initialization of multiple repositories with specific revisions for the multiple components (scp-firmware, tfa, edk2, ...)
            - repo enables the use of a manifest file, which can simplify the management of multiple repositories
            - repo provides a mechanism to group multiple repositories into a single directory
            - All of the above
        correct_answer: 4                    
        explanation: >
            repo is a tool over git for managing complex projects with multiple git repositories as it allows the simultaneous initialization of these repositories with specific revisions and simplifies the management through a manifest file.

    - questions:
        question: >
            You cannot provide specific compilation parameters for individual software projects.
        answers:
            - "True"
            - "False"
        correct_answer: 2                   
        explanation: >
            To provide specific compilation parameters for individual software projects, modify the configuration files. They are located in `build-scripts/config/<platform>/<platform>`. 
               
    - questions:
        question: >
            You can use any recent FVP version to run the software stack.
        answers:
            - "True"
            - "False"
        correct_answer: 2          
        explanation: >
            You can only use the supported FVP version found in the supported platform's release tags. This can be found in the Neoverse Reference Design Platform Software documentation.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
