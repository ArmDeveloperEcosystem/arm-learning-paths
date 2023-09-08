---
review:
    - questions:
        question: >
           To allow connections to the web server, all you need to do is open the OCI firewall (security list) for http(s) ? 
        answers:
            - "True"
            - "False"
        correct_answer: 2                    
        explanation: >
            You must also open connections in the local firewall of the compute instance.

    - questions:
        question: >
            Is a web server required to use WordPress?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
           A web server is required to interpret PHP scripts included in WordPress. In this
           Learning Path, you used Apache, but other web servers, such as Nginx, can be used.
           
    - questions:
        question: >
            Is a database required to use WordPress?
        answers:
            - "Yes"
            - "No"
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
