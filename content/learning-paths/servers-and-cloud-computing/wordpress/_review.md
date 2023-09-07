---
review:
    - questions:
        question: >
           To allow connections to the Webserver, it's only required to open the OCI firewall (security list) for http(s) ? 
        answers:
            - "True"
            - "False"
        correct_answer: 2                    
        explanation: >
            It's also required to allow connections in the local firewall of the compute instance.

    - questions:
        question: >
            Is a Webserver required to use WordPress ?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
           Indeed, a Webserver is required to interpret PHP scripts included in WordPress. In this
           learning path, we used Apache, but any other webserver, ngix for example, could have
           been used.
    - questions:
        question: >
            Is a database required to use WordPress ?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, WordPress requires a RDBMS. The preferred database to use with WordPress is MySQL.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
