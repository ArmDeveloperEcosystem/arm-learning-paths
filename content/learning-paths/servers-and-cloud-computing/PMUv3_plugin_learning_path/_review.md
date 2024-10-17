---
review:
    - questions:
        question: >
           To permanently enable userspace access for performance monitoring, you need to add kernel.perf_user_access = 1 to the /etc/sysctl.conf file. 
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >        
            You need to edit the sysctl configuration file to make the change permanent. 

    - questions:
        question: >
            The PMUv3 plugin can be used to analyze performance of Python applications.
        answers:
            - "True"
            - "False"
        correct_answer: 2                   
        explanation: >
            The PMUv3 plugin collects performance information for C/C++ applications.
               
    - questions:
        question: >
            What are the advantages of using the PMUv3 plugin?
        answers:
            - Avoids context switches
            - Ability to easily collect the PMU events and metrics 
            - More precise and accurate compared to generic instrumentation methods due to direct counter access
            - All the above
        correct_answer: 4         
        explanation: >
            All of the advantages listed are correct for the PMUv3 plugin.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
