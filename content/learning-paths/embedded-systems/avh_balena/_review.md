---
review:
    - questions:
        question: >
            The Balena OS image files downloaded from Balena Cloud can be uploaded directly to AVH
        answers:
            - "True"
            - "False"
        correct_answer: 2                    
        explanation: >
            AVH requires custom firmware be packaged in a specifically defined format. You must use the supplied script to convert the Balena OS images you download into AVH custom firmware images.

    - questions:
        question: >
            What does Balena OS use to install and run applications on a device?
        answers:
            - Raw binaries
            - Tarballs
            - Linux Packages
            - Docker Containers
        correct_answer: 4                   
        explanation: >
            The Balena Engine is a Docker engine for managing apps in containers on your IoT Devices.
               
    - questions:
        question: >
            Applications deployed to devices using Balena are accessible on the public internet
        answers:
            - "True"
            - "False"
        correct_answer: 2          
        explanation: >
            By default your Balena OS device is not accessible from the public internet, you must ask Balena Cloud to make a publicly accessible URL in order to view apps on your device from your browser.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
